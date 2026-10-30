"""Tests for the EPUB builder module."""

from __future__ import annotations

import logging
import xml.etree.ElementTree as ET
import zipfile
from pathlib import Path
from typing import Any
from unittest.mock import patch

import pytest

# Fixtures are imported from conftest.py automatically by pytest
# Import from parent directory (handled by conftest.py sys.path)
from build_epub import (
    EPUB_DIAGRAM_FONT,
    BuildState,
    ChapterCollector,
    EPUBConfig,
    MermaidRenderer,
    MermaidRenderError,
    ValidationError,
    create_chapter_html,
    extract_all_mermaid_blocks,
    flatten_svg_vars,
    get_chapter_order,
    setup_logging,
    validate_inputs,
)
from pele_renderer import (
    PeleDiagramError,
    PeleHelperError,
    PeleResult,
    PeleUnavailableError,
)

SVG_NS = "{http://www.w3.org/2000/svg}"

# Real Pele 1.6.0 output for `graph TD; A[ユーザー] --> B[エージェント]`.
PELE_SVG = (
    '<svg xmlns="http://www.w3.org/2000/svg" class="pele pele-flowchart" '
    'viewBox="0 0 148 160" width="148" height="160" style="max-width:100%;'
    "height:auto;--_bg:var(--pele-bg,#fff);--_fg:var(--pele-fg,#1f1f1f);"
    "--_m:var(--pele-muted,#6e6e6e);--_l:var(--pele-line,#1f1f1f);"
    "--_s:var(--pele-surface,#f3f3f3);--_a:var(--pele-surface-alt,#e6e6e6);"
    "--_b:var(--pele-border,#8a8a8a);--_c:var(--pele-accent,#5b7bd5);"
    "color:var(--_fg);--_r:var(--pele-radius,4px);"
    "--_fm:var(--pele-font-mono,monospace);font:16px sans-serif;"
    "letter-spacing:normal;word-spacing:normal;text-transform:none;"
    'direction:ltr;font-family:var(--pele-font,sans-serif)" fill="var(--_fg)" '
    'role="graphics-document document" aria-roledescription="flowchart">'
    '<g class="pele-edges" fill="none" stroke="var(--_l)" stroke-linecap="round">'
    '<g class="pele-edge" data-id="L_A_B_0"><path d="M74,56L74,97"/>'
    '<path class="pele-marker" d="M74,104L70.64,96L77.36,96Z" fill="var(--_l)" '
    'stroke="none"/></g></g><g class="pele-nodes">'
    '<g class="pele-node pele-shape-rect" data-id="A" transform="translate(74,32)">'
    '<rect x="-50" y="-24" width="100" height="48" fill="var(--_s)" '
    'stroke="var(--_b)" style="rx:var(--_r)"/><text class="pele-label" x="0" '
    'y="5.6" text-anchor="middle">ユーザー</text></g>'
    '<g class="pele-node pele-shape-rect" data-id="B" transform="translate(74,128)">'
    '<rect x="-66" y="-24" width="132" height="48" fill="var(--_s)" '
    'stroke="var(--_b)" style="rx:var(--_r)"/><text class="pele-label" x="0" '
    'y="5.6" text-anchor="middle">エージェント</text></g></g></svg>'
)

# Pele-shaped SVG with labels that look like CSS (`--model: opus`, `;`), XML
# entities, a Mermaid `style` statement after the radius, and a cluster title
# halo drawn with color-mix().
ADVERSARIAL_LABELS = [
    "claude --model: opus",
    "a; b & c",
    "x > y",
    '"quoted"',
    "--resume: x",
    "Session",
]
ADVERSARIAL_SVG = (
    '<svg xmlns="http://www.w3.org/2000/svg" class="pele pele-flowchart" '
    'viewBox="0 0 745 124" width="745" height="124" style="max-width:100%;'
    "height:auto;--_bg:var(--pele-bg,#fff);--_fg:var(--pele-fg,#1f1f1f);"
    "--_m:var(--pele-muted,#6e6e6e);--_l:var(--pele-line,#1f1f1f);"
    "--_s:var(--pele-surface,#f3f3f3);--_a:var(--pele-surface-alt,#e6e6e6);"
    "--_b:var(--pele-border,#8a8a8a);--_c:var(--pele-accent,#5b7bd5);"
    "color:var(--_fg);--_r:var(--pele-radius,4px);"
    "--_fm:var(--pele-font-mono,monospace);font:16px sans-serif;"
    'font-family:var(--pele-font,sans-serif)" fill="var(--_fg)">'
    '<g class="pele-clusters"><g class="pele-cluster" data-id="S">'
    '<rect x="8" y="8" width="466.43" height="108" fill="var(--_a)" '
    'fill-opacity="0.5" stroke="var(--_b)" style="rx:var(--_r)"/>'
    '<text fill="none" stroke="color-mix(in srgb,var(--_a) 50%,var(--_bg))" '
    'stroke-width="5" x="50.46" y="33.6">Session</text></g></g>'
    '<g class="pele-edge-labels" font-size="14"><g class="pele-edge-label">'
    '<rect x="235.89" y="61.5" width="78.78" height="21" rx="3" '
    'fill="var(--_bg)"/><text x="275.28" y="76.9">--resume: x</text></g></g>'
    '<g class="pele-nodes"><g class="pele-node" data-id="A">'
    '<rect x="-92.7" y="-24" width="185.39" height="48" fill="var(--_s)" '
    'stroke="var(--_b)" style="rx:var(--_r);fill:#e1f5fe;stroke:#333;"/>'
    '<text class="pele-label">claude --model: opus</text></g>'
    '<g class="pele-node" data-id="B"><rect fill="var(--_s)" '
    'style="rx:var(--_r)"/><text class="pele-label">a; b &amp; c</text></g>'
    '<g class="pele-node" data-id="C"><text class="pele-label">x &gt; y</text></g>'
    '<g class="pele-node" data-id="D"><text class="pele-label">&quot;quoted&quot;'
    "</text></g></g></svg>"
)

# Real Pele 1.6.0 pie output (trimmed to two slices). Series colours use
# numbered custom properties (`--pele-series-1`), as do timeline, mindmap and
# journey diagrams.
PIE_SVG = (
    '<svg xmlns="http://www.w3.org/2000/svg" class="pele pele-pie" '
    'viewBox="0 0 397 352" width="397" height="352" style="max-width:100%;'
    "height:auto;--_bg:var(--pele-bg,#fff);--_fg:var(--pele-fg,#1f1f1f);"
    "--_m:var(--pele-muted,#6e6e6e);--_l:var(--pele-line,#1f1f1f);"
    "--_s:var(--pele-surface,#f3f3f3);--_a:var(--pele-surface-alt,#e6e6e6);"
    "--_b:var(--pele-border,#8a8a8a);--_c:var(--pele-accent,#5b7bd5);"
    "color:var(--_fg);--_tw:var(--pele-title-weight,bold);"
    "--_fm:var(--pele-font-mono,monospace);font:16px sans-serif;"
    "letter-spacing:normal;word-spacing:normal;text-transform:none;"
    'direction:ltr;font-family:var(--pele-font,sans-serif)" fill="var(--_fg)" '
    'role="graphics-document document" aria-roledescription="pie">'
    '<text class="pele-title" font-weight="var(--_tw)" text-anchor="middle" '
    'xml:space="preserve"><tspan x="198.5" y="25.6">Pets</tspan></text>'
    '<g class="pele-slices" transform="translate(156,196)" stroke="var(--_bg)" '
    'stroke-width="1" stroke-linejoin="round">'
    '<path class="pele-slice" data-id="Dogs" '
    'd="M0,0L0,-120A120,120 0 1 1 -115.39,-32.93Z" '
    'fill="var(--pele-series-1,#4c78a8)"/>'
    '<path class="pele-slice" data-id="Cats" '
    'd="M0,0L-115.39,-32.93A120,120 0 0 1 0,-120Z" '
    'fill="var(--pele-series-2,#f58518)"/></g>'
    '<g class="pele-legend" font-size="14">'
    '<g class="pele-legend-item" data-id="Dogs"><rect x="336" y="164" '
    'width="12" height="12" rx="2" fill="var(--pele-series-1,#4c78a8)"/>'
    '<text x="372.34" y="174.9" text-anchor="middle">Dogs</text></g></g></svg>'
)


def _attribute_values(svg: str) -> list[str]:
    return [v for el in ET.fromstring(svg).iter() for v in el.attrib.values()]


def _texts(svg: str) -> list[str]:
    return [el.text or "" for el in ET.fromstring(svg).iter(f"{SVG_NS}text")]


# =============================================================================
# BuildState Tests
# =============================================================================


class TestBuildState:
    """Tests for BuildState dataclass."""

    def test_initial_state(self, state: BuildState) -> None:
        """Test that initial state is empty."""
        assert state.mermaid_counter == 0
        assert len(state.mermaid_cache) == 0
        assert len(state.mermaid_added_to_book) == 0
        assert len(state.path_to_chapter) == 0

    def test_state_modification(self, state: BuildState) -> None:
        """Test that state can be modified."""
        state.mermaid_counter = 5
        state.mermaid_cache["key"] = (b"data", "file.png")
        state.mermaid_added_to_book.add("file.png")
        state.path_to_chapter["README.md"] = "chap_01.xhtml"

        assert state.mermaid_counter == 5
        assert state.mermaid_cache["key"] == (b"data", "file.png")
        assert "file.png" in state.mermaid_added_to_book
        assert state.path_to_chapter["README.md"] == "chap_01.xhtml"

    def test_reset(self, state: BuildState) -> None:
        """Test that reset clears all state."""
        state.mermaid_counter = 5
        state.mermaid_cache["key"] = (b"data", "file.png")
        state.mermaid_added_to_book.add("file.png")
        state.path_to_chapter["README.md"] = "chap_01.xhtml"

        state.reset()

        assert state.mermaid_counter == 0
        assert len(state.mermaid_cache) == 0
        assert len(state.mermaid_added_to_book) == 0
        assert len(state.path_to_chapter) == 0


# =============================================================================
# EPUBConfig Tests
# =============================================================================


class TestEPUBConfig:
    """Tests for EPUBConfig dataclass."""

    def test_required_fields(self, tmp_path: Path) -> None:
        """Test that required fields must be provided."""
        config = EPUBConfig(
            root_path=tmp_path,
            output_path=tmp_path / "out.epub",
        )
        assert config.root_path == tmp_path
        assert config.output_path == tmp_path / "out.epub"

    def test_default_values(self, tmp_path: Path) -> None:
        """Test that default values are set correctly."""
        config = EPUBConfig(
            root_path=tmp_path,
            output_path=tmp_path / "out.epub",
        )
        assert config.identifier == "claude-howto-guide"
        assert config.title == "Claude Code How-To Guide"
        assert config.language == "en"
        assert config.author == "Claude Code Community"

    def test_custom_values(self, tmp_path: Path) -> None:
        """Test that custom values override defaults."""
        config = EPUBConfig(
            root_path=tmp_path,
            output_path=tmp_path / "out.epub",
            title="Custom Title",
        )
        assert config.title == "Custom Title"


# =============================================================================
# Validation Tests
# =============================================================================


class TestValidation:
    """Tests for input validation."""

    def test_valid_inputs(self, config: EPUBConfig, logger: logging.Logger) -> None:
        """Test that valid inputs pass validation."""
        # Should not raise
        validate_inputs(config, logger)

    def test_missing_root_path(self, tmp_path: Path, logger: logging.Logger) -> None:
        """Test that missing root path raises ValidationError."""
        config = EPUBConfig(
            root_path=tmp_path / "nonexistent",
            output_path=tmp_path / "out.epub",
        )
        with pytest.raises(ValidationError, match="Root path does not exist"):
            validate_inputs(config, logger)

    def test_root_path_is_file(self, tmp_path: Path, logger: logging.Logger) -> None:
        """Test that file as root path raises ValidationError."""
        file_path = tmp_path / "file.txt"
        file_path.write_text("content")
        config = EPUBConfig(
            root_path=file_path,
            output_path=tmp_path / "out.epub",
        )
        with pytest.raises(ValidationError, match="Root path is not a directory"):
            validate_inputs(config, logger)

    def test_no_markdown_files(self, tmp_path: Path, logger: logging.Logger) -> None:
        """Test that directory with no markdown files raises ValidationError."""
        empty_dir = tmp_path / "empty"
        empty_dir.mkdir()
        config = EPUBConfig(
            root_path=empty_dir,
            output_path=tmp_path / "out.epub",
        )
        with pytest.raises(ValidationError, match="No markdown files found"):
            validate_inputs(config, logger)

    def test_missing_output_directory(
        self, tmp_project: Path, logger: logging.Logger
    ) -> None:
        """Test that missing output directory raises ValidationError."""
        config = EPUBConfig(
            root_path=tmp_project,
            output_path=tmp_project / "nonexistent" / "out.epub",
        )
        with pytest.raises(ValidationError, match="Output directory does not exist"):
            validate_inputs(config, logger)


# =============================================================================
# Mermaid Processing Tests
# =============================================================================


class TestMermaidProcessing:
    """Tests for Mermaid diagram processing."""

    def test_numbered_label_passes_through_unchanged(
        self, tmp_path: Path, logger: logging.Logger
    ) -> None:
        """`[1. Load file]` reaches Pele as written (no backslash escaping).

        Pele renders `1. Load file` correctly but would draw an escape
        backslash literally, so the source must not be rewritten.
        """
        md_file = tmp_path / "steps.md"
        md_file.write_text(
            '```mermaid\ngraph TD\n    A["1. Load file"] --> B[2. Parse]\n```\n',
            encoding="utf-8",
        )

        source = 'graph TD\n    A["1. Load file"] --> B[2. Parse]'

        diagrams = extract_all_mermaid_blocks([(md_file, "Steps")], logger)
        assert diagrams == [(1, source)]

        state = BuildState()
        config = EPUBConfig(root_path=tmp_path, output_path=tmp_path / "o.epub")
        with patch(
            "build_epub.render_diagrams",
            return_value=[PeleResult(svg=PELE_SVG, diagram_type="flowchart")],
        ) as mock_render:
            MermaidRenderer(config, state, logger).render_all(diagrams)

        assert mock_render.call_args.args[0] == [source]
        assert list(state.mermaid_cache) == [source]

    def test_extract_mermaid_blocks(
        self, tmp_path: Path, logger: logging.Logger
    ) -> None:
        """Test extraction of Mermaid blocks from files."""
        # Create test file with mermaid blocks
        md_file = tmp_path / "test.md"
        md_file.write_text(
            """# Test

```mermaid
graph TD
    A --> B
```

Some text

```mermaid
graph LR
    C --> D
```
"""
        )

        diagrams = extract_all_mermaid_blocks([(md_file, "Test")], logger)

        assert len(diagrams) == 2
        assert diagrams[0][0] == 1  # First diagram index
        assert diagrams[1][0] == 2  # Second diagram index
        assert "A --> B" in diagrams[0][1]
        assert "C --> D" in diagrams[1][1]

    def test_extract_mermaid_blocks_deduplication(
        self, tmp_path: Path, logger: logging.Logger
    ) -> None:
        """Test that duplicate Mermaid blocks are deduplicated."""
        md_file1 = tmp_path / "test1.md"
        md_file2 = tmp_path / "test2.md"

        same_diagram = """```mermaid
graph TD
    A --> B
```"""

        md_file1.write_text(f"# File 1\n\n{same_diagram}")
        md_file2.write_text(f"# File 2\n\n{same_diagram}")

        diagrams = extract_all_mermaid_blocks(
            [(md_file1, "Test1"), (md_file2, "Test2")], logger
        )

        # Should only have one diagram since they're identical
        assert len(diagrams) == 1


# =============================================================================
# Chapter Collection Tests
# =============================================================================


class TestChapterCollector:
    """Tests for ChapterCollector class."""

    def test_collect_single_file(self, tmp_path: Path, state: BuildState) -> None:
        """Test collecting a single markdown file."""
        readme = tmp_path / "README.md"
        readme.write_text("# Test")

        collector = ChapterCollector(tmp_path, state)
        chapters = collector.collect_all_chapters([("README.md", "Introduction")])

        assert len(chapters) == 1
        assert chapters[0].file_path == readme
        assert chapters[0].display_name == "Introduction"
        assert chapters[0].chapter_filename == "chap_01.xhtml"
        assert state.path_to_chapter["README.md"] == "chap_01.xhtml"

    def test_collect_folder(self, tmp_project: Path, state: BuildState) -> None:
        """Test collecting a folder with multiple files."""
        collector = ChapterCollector(tmp_project, state)
        chapters = collector.collect_all_chapters([("01-test-chapter", "Test Chapter")])

        assert len(chapters) == 2  # README.md and section.md
        assert chapters[0].is_folder_overview is True
        assert chapters[0].folder_name == "Test Chapter"
        assert chapters[1].is_folder_overview is False

    def test_path_mapping(self, tmp_project: Path, state: BuildState) -> None:
        """Test that path mapping is built correctly."""
        collector = ChapterCollector(tmp_project, state)
        collector.collect_all_chapters(
            [
                ("README.md", "Introduction"),
                ("01-test-chapter", "Test Chapter"),
            ]
        )

        assert "README.md" in state.path_to_chapter
        assert "01-test-chapter" in state.path_to_chapter
        assert "01-test-chapter/README.md" in state.path_to_chapter


# =============================================================================
# HTML Generation Tests
# =============================================================================


class TestHTMLGeneration:
    """Tests for HTML generation."""

    def test_create_chapter_html_overview(self) -> None:
        """Test creating HTML for an overview chapter."""
        html = create_chapter_html(
            display_name="Introduction",
            file_title="Introduction",
            html_content="<p>Content</p>",
            is_overview=True,
        )

        assert "<!DOCTYPE html>" in html
        assert '<html xmlns="http://www.w3.org/1999/xhtml"' in html
        assert "<h1>Introduction</h1>" in html
        assert "<p>Content</p>" in html

    def test_create_chapter_html_section(self) -> None:
        """Test creating HTML for a section chapter."""
        html = create_chapter_html(
            display_name="Chapter",
            file_title="Section",
            html_content="<p>Content</p>",
            is_overview=False,
        )

        assert "<h2>Section</h2>" in html
        assert "<h1>" not in html

    def test_html_escaping(self) -> None:
        """Test that HTML special characters are escaped."""
        html = create_chapter_html(
            display_name="<script>alert('xss')</script>",
            file_title="Test & Title",
            html_content="<p>Content</p>",
            is_overview=True,
        )

        assert "&lt;script&gt;" in html
        # Note: Python's html.escape uses &#x27; for single quotes
        assert "<script>alert" not in html


# =============================================================================
# Chapter Order Tests
# =============================================================================


class TestChapterOrder:
    """Tests for chapter ordering."""

    def test_get_chapter_order(self) -> None:
        """Test that chapter order is defined correctly."""
        order = get_chapter_order()

        assert len(order) > 0
        assert order[0] == ("README.md", "Introduction")

        # Check that all expected chapters are present
        chapter_names = [name for name, _ in order]
        assert "01-slash-commands" in chapter_names
        assert "02-memory" in chapter_names
        assert "resources.md" in chapter_names

    def test_all_numbered_modules_are_in_learning_order(self) -> None:
        """The default book includes all ten modules before the resources."""
        chapter_names = [name for name, _ in get_chapter_order()]
        modules = [name for name in chapter_names if name[:2].isdigit()]

        assert [name[:2] for name in modules] == [
            f"{number:02d}" for number in range(1, 11)
        ]
        assert modules[-1] == "10-cli"
        assert chapter_names.index("10-cli") < chapter_names.index("resources.md")

    def test_default_collector_includes_cli_and_maps_links(
        self, tmp_path: Path, state: BuildState
    ) -> None:
        """CLI overview and nested examples use the normal chapter collector."""
        for folder in ("09-advanced-features", "10-cli", "10-cli/examples"):
            directory = tmp_path / folder
            directory.mkdir(parents=True, exist_ok=True)
            (directory / "README.md").write_text("# Overview\n", encoding="utf-8")
        (tmp_path / "resources.md").write_text("# Resources\n", encoding="utf-8")

        chapters = ChapterCollector(tmp_path, state).collect_all_chapters(
            get_chapter_order()
        )

        collected_paths = [
            chapter.file_path.relative_to(tmp_path).as_posix() for chapter in chapters
        ]
        assert collected_paths == [
            "09-advanced-features/README.md",
            "10-cli/README.md",
            "10-cli/examples/README.md",
            "resources.md",
        ]
        assert chapters[1].display_name == "CLI Reference"
        assert state.path_to_chapter["10-cli"] == chapters[1].chapter_filename
        for chapter in chapters:
            relative_path = str(chapter.file_path.relative_to(tmp_path))
            assert state.path_to_chapter[relative_path] == chapter.chapter_filename


# =============================================================================
# Logging Tests
# =============================================================================


class TestLogging:
    """Tests for logging setup."""

    def test_setup_logging_default(self) -> None:
        """Test default logging setup."""
        logger = setup_logging(verbose=False)
        assert logger.name == "epub_builder"

    def test_setup_logging_verbose(self) -> None:
        """Test verbose logging setup."""
        logger = setup_logging(verbose=True)
        assert logger.name == "epub_builder"


# =============================================================================
# MermaidRenderer Tests
# =============================================================================


class TestMermaidRenderer:
    """Tests for the Pele-backed MermaidRenderer (render_diagrams mocked)."""

    def _make_renderer(
        self, tmp_path: Path, state: BuildState, logger: logging.Logger
    ) -> MermaidRenderer:
        config = EPUBConfig(root_path=tmp_path, output_path=tmp_path / "out.epub")
        return MermaidRenderer(config, state, logger)

    def test_render_all_success(
        self, tmp_path: Path, state: BuildState, logger: logging.Logger
    ) -> None:
        """Pele SVG is flattened, encoded and cached as mermaid_N.svg."""
        renderer = self._make_renderer(tmp_path, state, logger)

        with patch(
            "build_epub.render_diagrams",
            return_value=[PeleResult(svg=PELE_SVG, diagram_type="flowchart")],
        ):
            results = renderer.render_all([(1, "graph TD\n  A --> B\n")])

        assert list(results) == ["graph TD\n  A --> B"]
        svg_bytes, img_name = results["graph TD\n  A --> B"]
        assert img_name == "mermaid_1.svg"
        svg = svg_bytes.decode("utf-8")
        assert "var(" not in svg
        assert "ユーザー" in svg
        assert state.mermaid_cache["graph TD\n  A --> B"] == (svg_bytes, img_name)

    def test_render_all_diagram_error(
        self, tmp_path: Path, state: BuildState, logger: logging.Logger
    ) -> None:
        """A diagram Pele rejects fails the build with its code and line."""
        renderer = self._make_renderer(tmp_path, state, logger)
        error = PeleDiagramError("syntax", "Expecting 'NODE_STRING'", 3, 1)

        with (
            patch(
                "build_epub.render_diagrams",
                return_value=[
                    PeleResult(svg=PELE_SVG, diagram_type="flowchart"),
                    PeleResult(svg=None, diagram_type=None, error=error),
                ],
            ),
            pytest.raises(
                MermaidRenderError,
                match=r"Pele failed for diagram 7: \[syntax\] .*diagram line 3",
            ),
        ):
            renderer.render_all([(1, "graph TD\n  A --> B"), (7, "graph TD\n  A -->")])

    def test_render_all_pele_unavailable(
        self, tmp_path: Path, state: BuildState, logger: logging.Logger
    ) -> None:
        """Missing Node.js surfaces as MermaidRenderError with the hint."""
        renderer = self._make_renderer(tmp_path, state, logger)

        with (
            patch(
                "build_epub.render_diagrams",
                side_effect=PeleUnavailableError("node not found on PATH"),
            ),
            pytest.raises(MermaidRenderError, match=r"Node\.js >= 20"),
        ):
            renderer.render_all([(1, "graph TD\n  A --> B")])

    def test_render_all_helper_failure(
        self, tmp_path: Path, state: BuildState, logger: logging.Logger
    ) -> None:
        """A crashed or timed-out helper raises MermaidRenderError."""
        renderer = self._make_renderer(tmp_path, state, logger)

        with (
            patch(
                "build_epub.render_diagrams",
                side_effect=PeleHelperError("Pele helper timed out after 120s"),
            ),
            pytest.raises(MermaidRenderError, match="timed out"),
        ):
            renderer.render_all([(1, "graph TD\n  A --> B")])

    def test_render_all_deduplication(
        self, tmp_path: Path, state: BuildState, logger: logging.Logger
    ) -> None:
        """Identical diagrams are rendered once, in a single Pele call."""
        renderer = self._make_renderer(tmp_path, state, logger)
        same_code = "graph TD\n  A --> B"

        with patch(
            "build_epub.render_diagrams",
            return_value=[PeleResult(svg=PELE_SVG, diagram_type="flowchart")],
        ) as mock_render:
            results = renderer.render_all([(1, same_code), (2, same_code + "\n")])

        assert mock_render.call_count == 1
        assert mock_render.call_args.args[0] == [same_code]
        assert len(results) == 1


# =============================================================================
# SVG flattening (EPUB readers lack CSS custom properties)
# =============================================================================


class TestFlattenSvgVars:
    @pytest.mark.parametrize(
        "svg", [PELE_SVG, ADVERSARIAL_SVG, PIE_SVG], ids=["real", "adv", "series"]
    )
    def test_no_css_variables_left_and_valid_xml(self, svg: str) -> None:
        out = flatten_svg_vars(svg)

        ET.fromstring(out)  # still well-formed XML
        for value in _attribute_values(out):
            assert "var(" not in value
            assert "--_" not in value
            assert "color-mix" not in value

    def test_text_nodes_are_untouched(self) -> None:
        out = flatten_svg_vars(ADVERSARIAL_SVG)

        assert _texts(out) == _texts(ADVERSARIAL_SVG)
        assert sorted(_texts(out)) == sorted(ADVERSARIAL_LABELS)

    def test_aliases_resolve_to_pele_fallbacks(self) -> None:
        root = ET.fromstring(flatten_svg_vars(ADVERSARIAL_SVG))

        assert root.get("fill") == "#1f1f1f"
        style = root.get("style", "")
        assert "color:#1f1f1f" in style
        assert "max-width:100%" in style
        halo = next(t for t in root.iter(f"{SVG_NS}text") if t.get("stroke"))
        # color-mix(in srgb, #e6e6e6 50%, #fff)
        assert halo.get("stroke") == "#f2f2f2"

    def test_numbered_series_variables_resolve(self) -> None:
        root = ET.fromstring(flatten_svg_vars(PIE_SVG))
        slices = [p for p in root.iter(f"{SVG_NS}path") if p.get("data-id")]

        assert [p.get("fill") for p in slices] == ["#4c78a8", "#f58518"]
        title = next(root.iter(f"{SVG_NS}text"))
        assert title.get("font-weight") == "bold"
        themed = ET.fromstring(
            flatten_svg_vars(PIE_SVG, {"--pele-series-1": "#123456"})
        )
        assert {
            r.get("fill") for r in themed.iter(f"{SVG_NS}rect") if r.get("rx") == "2"
        } == {"#123456"}

    def test_theme_override_applied(self) -> None:
        root = ET.fromstring(
            flatten_svg_vars(
                PELE_SVG, {"--pele-surface": "#abcdef", "--pele-bg": "#000"}
            )
        )

        node_rects = list(root.iter(f"{SVG_NS}rect"))[1:]
        assert {r.get("fill") for r in node_rects} == {"#abcdef"}
        assert root[0].get("fill") == "#000"

    def test_radius_moves_to_attribute_keeping_other_declarations(self) -> None:
        root = ET.fromstring(flatten_svg_vars(ADVERSARIAL_SVG))
        node_a = next(g for g in root.iter(f"{SVG_NS}g") if g.get("data-id") == "A")
        rect = node_a.find(f"{SVG_NS}rect")

        assert rect is not None
        assert rect.get("rx") == "4"
        assert rect.get("style") == "fill:#e1f5fe;stroke:#333;"
        node_b = next(g for g in root.iter(f"{SVG_NS}g") if g.get("data-id") == "B")
        rect_b = node_b.find(f"{SVG_NS}rect")
        assert rect_b is not None
        assert rect_b.get("rx") == "4"
        assert "style" not in rect_b.attrib

    def test_font_stack_replaces_pele_font(self) -> None:
        root = ET.fromstring(flatten_svg_vars(PELE_SVG))

        assert f"font-family:{EPUB_DIAGRAM_FONT}" in root.get("style", "")

    def test_opaque_background_rect_is_first_child(self) -> None:
        root = ET.fromstring(flatten_svg_vars(PELE_SVG))

        first = root[0]
        assert first.tag == f"{SVG_NS}rect"
        assert (first.get("x"), first.get("y")) == ("0", "0")
        assert (first.get("width"), first.get("height")) == ("148", "160")
        assert first.get("fill") == "#fff"

    def test_serialises_with_default_namespace(self) -> None:
        out = flatten_svg_vars(PELE_SVG)

        assert out.startswith('<svg xmlns="http://www.w3.org/2000/svg"')
        assert "ns0:" not in out

    @pytest.mark.parametrize(
        "svg",
        [
            "<svg xmlns='http://www.w3.org/2000/svg'><g></svg>",
            '<svg xmlns="http://www.w3.org/2000/svg" width="1"/>',
            '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 10"/>',
            '<svg xmlns="http://www.w3.org/2000/svg" viewBox="0 0 1 1" '
            'fill="var(--_zz)"/>',
        ],
        ids=["malformed-xml", "no-viewbox", "short-viewbox", "unknown-alias"],
    )
    def test_unflattenable_svg_raises(self, svg: str) -> None:
        with pytest.raises(MermaidRenderError):
            flatten_svg_vars(svg)


# =============================================================================
# Integration Tests
# =============================================================================


class TestIntegration:
    """Integration tests for the full build process."""

    def test_default_build_contains_cli_in_spine_navigation_and_links(
        self, tmp_project: Path, logger: logging.Logger
    ) -> None:
        """Build with the real chapter order so an omitted module cannot pass."""
        from build_epub import build_epub_async

        (tmp_project / "README.md").write_text(
            "# Guide\n\n[CLI reference](10-cli/README.md)\n", encoding="utf-8"
        )
        cli = tmp_project / "10-cli"
        cli.mkdir()
        (cli / "README.md").write_text(
            "# CLI Reference\n\nCLI chapter regression marker.\n", encoding="utf-8"
        )
        (tmp_project / "resources.md").write_text("# Resources\n", encoding="utf-8")
        config = EPUBConfig(root_path=tmp_project, output_path=tmp_project / "cli.epub")

        build_epub_async(config, logger)

        with zipfile.ZipFile(config.output_path) as archive:
            opf = ET.fromstring(archive.read("EPUB/content.opf"))
            nav = archive.read("EPUB/nav.xhtml").decode("utf-8")
            introduction = archive.read("EPUB/chap_01.xhtml").decode("utf-8")
            chapter = archive.read("EPUB/chap_02_00.xhtml").decode("utf-8")

        namespaces = {"opf": "http://www.idpf.org/2007/opf"}
        items = {
            item.attrib["id"]: item.attrib["href"]
            for item in opf.findall("opf:manifest/opf:item", namespaces)
        }
        spine = [
            items[item.attrib["idref"]]
            for item in opf.findall("opf:spine/opf:itemref", namespaces)
        ]
        assert spine == ["nav.xhtml", "chap_01.xhtml", "chap_02_00.xhtml", "chap_03.xhtml"]
        assert "CLI chapter regression marker." in chapter
        assert 'href="chap_02_00.xhtml"' in nav
        assert 'href="chap_02_00.xhtml"' in introduction
        assert "10-cli/README.md" not in introduction

    def test_build_without_mermaid(
        self, tmp_project: Path, logger: logging.Logger
    ) -> None:
        """Test building an EPUB without Mermaid diagrams."""
        from build_epub import build_epub_async

        config = EPUBConfig(
            root_path=tmp_project,
            output_path=tmp_project / "test.epub",
        )

        # Override chapter order for minimal test
        with patch("build_epub.get_chapter_order") as mock_order:
            mock_order.return_value = [("README.md", "Introduction")]

            result = build_epub_async(config, logger)

            assert result.exists()
            assert result.suffix == ".epub"

    def test_build_embeds_mermaid_as_svg(
        self, tmp_project: Path, logger: logging.Logger
    ) -> None:
        """Diagrams land in the EPUB as image/svg+xml items, never placeholders."""
        from build_epub import build_epub_async
        from check_epub_diagrams import check_epub

        (tmp_project / "README.md").write_text(
            "# Test Project\n\n```mermaid\ngraph TD\n    A --> B\n```\n\n"
            "Same diagram again:\n\n```mermaid\ngraph TD\n    A --> B\n```\n",
            encoding="utf-8",
        )
        config = EPUBConfig(root_path=tmp_project, output_path=tmp_project / "t.epub")

        def fake_render(sources: list[str], *_a: Any, **_k: Any) -> list[PeleResult]:
            return [PeleResult(svg=PELE_SVG, diagram_type="flowchart") for _ in sources]

        with (
            patch("build_epub.get_chapter_order") as mock_order,
            patch("build_epub.render_diagrams", side_effect=fake_render),
        ):
            mock_order.return_value = [("README.md", "Introduction")]
            build_epub_async(config, logger)

        with zipfile.ZipFile(config.output_path) as zf:
            names = zf.namelist()
            opf_name = next(n for n in names if n.endswith(".opf"))
            opf = zf.read(opf_name).decode("utf-8")
            chapter = zf.read("EPUB/chap_01.xhtml").decode("utf-8")
            svg = zf.read("EPUB/images/mermaid_1.svg").decode("utf-8")

        assert "EPUB/images/mermaid_1.svg" in names
        assert not any(n.endswith(".png") and "mermaid" in n for n in names)
        item = next(
            line for line in opf.split("<item ") if "images/mermaid_1.svg" in line
        )
        assert 'media-type="image/svg+xml"' in item
        assert chapter.count('src="images/mermaid_1.svg"') == 2
        assert "SVG not found" not in chapter
        assert "var(" not in svg
        assert check_epub(config.output_path) == []


# =============================================================================
# Run tests
# =============================================================================


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
