"""Tests for the EPUB builder module."""

from __future__ import annotations

import logging
from pathlib import Path
from unittest.mock import MagicMock, patch

import pytest

# Fixtures are imported from conftest.py automatically by pytest
# Import from parent directory (handled by conftest.py sys.path)
from build_epub import (
    BuildState,
    ChapterCollector,
    EPUBConfig,
    MermaidRenderer,
    MermaidRenderError,
    ValidationError,
    create_chapter_html,
    extract_all_mermaid_blocks,
    get_chapter_order,
    sanitize_mermaid,
    setup_logging,
    validate_inputs,
)

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
        assert config.mmdc_path == "mmdc"

    def test_custom_values(self, tmp_path: Path) -> None:
        """Test that custom values override defaults."""
        config = EPUBConfig(
            root_path=tmp_path,
            output_path=tmp_path / "out.epub",
            title="Custom Title",
            mmdc_path="/usr/local/bin/mmdc",
        )
        assert config.title == "Custom Title"
        assert config.mmdc_path == "/usr/local/bin/mmdc"


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

    def test_sanitize_mermaid_numbered_list(self) -> None:
        """Test that numbered lists in brackets are escaped."""
        input_code = 'A["1. First item"] --> B["2. Second item"]'
        expected = 'A["1\\. First item"] --> B["2\\. Second item"]'
        assert sanitize_mermaid(input_code) == expected

    def test_sanitize_mermaid_no_change(self) -> None:
        """Test that code without numbered lists is unchanged."""
        input_code = "A --> B --> C"
        assert sanitize_mermaid(input_code) == input_code

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
    """Tests for local MermaidRenderer."""

    def _make_renderer(
        self, tmp_path: Path, state: BuildState, logger: logging.Logger
    ) -> MermaidRenderer:
        config = EPUBConfig(
            root_path=tmp_path,
            output_path=tmp_path / "out.epub",
            mmdc_path="mmdc",
        )
        return MermaidRenderer(config, state, logger)

    def test_render_all_success(
        self, tmp_path: Path, state: BuildState, logger: logging.Logger
    ) -> None:
        """Test that render_all uses mmdc and caches results."""
        fake_png = b"\x89PNG\r\n\x1a\n" + b"\x00" * 100
        renderer = self._make_renderer(tmp_path, state, logger)

        with (
            patch("shutil.which", return_value="/usr/bin/mmdc"),
            patch("subprocess.run") as mock_run,
            patch("pathlib.Path.exists", return_value=True),
            patch("pathlib.Path.read_bytes", return_value=fake_png),
        ):
            mock_run.return_value = MagicMock(returncode=0, stderr="")
            results = renderer.render_all([(1, "graph TD\n  A --> B")])

        assert len(results) == 1
        png_bytes, img_name = next(iter(results.values()))
        assert png_bytes == fake_png
        assert img_name.startswith("mermaid_")
        assert img_name.endswith(".png")

    def test_render_all_mmdc_not_found(
        self, tmp_path: Path, state: BuildState, logger: logging.Logger
    ) -> None:
        """Test that missing mmdc raises MermaidRenderError."""
        renderer = self._make_renderer(tmp_path, state, logger)

        with (
            patch("shutil.which", return_value=None),
            pytest.raises(MermaidRenderError, match="mmdc not found"),
        ):
            renderer.render_all([(1, "graph TD\n  A --> B")])

    def test_render_all_mmdc_failure(
        self, tmp_path: Path, state: BuildState, logger: logging.Logger
    ) -> None:
        """Test that mmdc non-zero exit raises MermaidRenderError."""
        renderer = self._make_renderer(tmp_path, state, logger)

        with (
            patch("shutil.which", return_value="/usr/bin/mmdc"),
            patch("subprocess.run") as mock_run,
        ):
            mock_run.return_value = MagicMock(returncode=1, stderr="parse error")
            with pytest.raises(MermaidRenderError, match="mmdc failed"):
                renderer.render_all([(1, "graph TD\n  A --> B")])

    def test_render_all_deduplication(
        self, tmp_path: Path, state: BuildState, logger: logging.Logger
    ) -> None:
        """Test that identical diagrams are only rendered once."""
        fake_png = b"\x89PNG\r\n\x1a\n" + b"\x00" * 100
        renderer = self._make_renderer(tmp_path, state, logger)
        same_code = "graph TD\n  A --> B"

        with (
            patch("shutil.which", return_value="/usr/bin/mmdc"),
            patch("subprocess.run") as mock_run,
            patch("pathlib.Path.exists", return_value=True),
            patch("pathlib.Path.read_bytes", return_value=fake_png),
        ):
            mock_run.return_value = MagicMock(returncode=0, stderr="")
            results = renderer.render_all([(1, same_code), (2, same_code)])

        # mmdc should only be called once for duplicate diagrams
        assert mock_run.call_count == 1
        # Both entries map to the same cached result
        assert len(results) == 1

    def test_render_all_timeout(
        self, tmp_path: Path, state: BuildState, logger: logging.Logger
    ) -> None:
        """Test that a hung mmdc process raises MermaidRenderError."""
        import subprocess as _subprocess

        renderer = self._make_renderer(tmp_path, state, logger)

        with (
            patch("shutil.which", return_value="/usr/bin/mmdc"),
            patch("subprocess.run", side_effect=_subprocess.TimeoutExpired("mmdc", 60)),
            pytest.raises(MermaidRenderError, match="timed out"),
        ):
            renderer.render_all([(1, "graph TD\n  A --> B")])


# =============================================================================
# Integration Tests
# =============================================================================


class TestIntegration:
    """Integration tests for the full build process."""

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


# =============================================================================
# Run tests
# =============================================================================


if __name__ == "__main__":
    pytest.main([__file__, "-v"])
