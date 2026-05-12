"""Tests for the static website builder."""

from __future__ import annotations

import logging
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))

from build_website import (
    BuildState,
    PageInfo,
    WebsiteConfig,
    _disambiguate_url,
    build_website,
    collect_folder_markdown,
    derive_page_title,
    heading_to_anchor,
    is_excluded_dir,
    relative_link,
    render_markdown,
    replace_mermaid_blocks,
    rewrite_links,
    source_to_site_url,
)

# =============================================================================
# Fixtures
# =============================================================================


@pytest.fixture
def site_root(tmp_path: Path) -> Path:
    """Create a minimal repo-like tree the builder can render."""
    (tmp_path / "README.md").write_text(
        "<picture>\n"
        '  <source media="(prefers-color-scheme: dark)" '
        'srcset="resources/logos/claude-howto-logo-dark.svg">\n'
        '  <img alt="Claude How To" src="resources/logos/claude-howto-logo.svg">\n'
        "</picture>\n\n"
        "# Home Page\n\nWelcome. See [Slash Commands](01-slash-commands/README.md).\n"
        "Also check [script](scripts/build.sh) and the [logo](resources/logos/logo.svg).\n"
    )
    (tmp_path / "LEARNING-ROADMAP.md").write_text(
        "# Learning Roadmap\n\nLink back to [Home](README.md#home-page).\n"
    )

    sc = tmp_path / "01-slash-commands"
    sc.mkdir()
    (sc / "README.md").write_text(
        "# Slash Commands\n\nMermaid time:\n\n```mermaid\nflowchart LR\nA-->B\n```\n\n"
        "See [example](example.md).\n"
    )
    (sc / "example.md").write_text("# Example\n\nGo back to [overview](README.md).\n")

    # Non-markdown repo files
    scripts_dir = tmp_path / "scripts"
    scripts_dir.mkdir()
    (scripts_dir / "build.sh").write_text("#!/bin/bash\necho hi\n")

    logos = tmp_path / "resources" / "logos"
    logos.mkdir(parents=True)
    (logos / "logo.svg").write_text("<svg></svg>")
    (logos / "claude-howto-logo.svg").write_text("<svg></svg>")
    (logos / "claude-howto-logo-dark.svg").write_text("<svg></svg>")

    return tmp_path


@pytest.fixture
def logger() -> logging.Logger:
    return logging.getLogger("test_build_website")


# =============================================================================
# heading_to_anchor parity with check_cross_references
# =============================================================================


class TestHeadingToAnchor:
    def test_simple_title(self) -> None:
        assert heading_to_anchor("Hello World") == "hello-world"

    def test_punctuation_removed(self) -> None:
        assert heading_to_anchor("What's Next?") == "whats-next"

    def test_unicode_preserved(self) -> None:
        assert heading_to_anchor("Hướng dẫn") == "hướng-dẫn"

    def test_emoji_stripped(self) -> None:
        # The validator strips emoji; we mirror that exactly.
        assert heading_to_anchor("🔥 Trending") == "-trending"


# =============================================================================
# source_to_site_url
# =============================================================================


class TestSourceToSiteUrl:
    def test_root_readme_maps_to_index(self) -> None:
        assert source_to_site_url("README.md") == "index.html"

    def test_folder_readme_maps_to_folder_index(self) -> None:
        assert (
            source_to_site_url("01-slash-commands/README.md")
            == "01-slash-commands/index.html"
        )

    def test_other_markdown_uses_html_extension(self) -> None:
        assert (
            source_to_site_url("01-slash-commands/example.md")
            == "01-slash-commands/example.html"
        )


class TestDisambiguateUrl:
    def test_no_collision_passes_through(self) -> None:
        used: set[str] = {"foo.html"}
        assert _disambiguate_url("bar.html", used, "bar.md") == "bar.html"

    def test_case_insensitive_collision_disambiguated(self) -> None:
        # README → index.html lands first; INDEX.md (case-insensitive collision)
        # must get a suffix on macOS / Windows filesystems.
        used: set[str] = {"index.html"}
        result = _disambiguate_url("INDEX.html", used, "INDEX.md")
        assert result.lower() != "index.html"
        assert result.endswith(".html")


# =============================================================================
# relative_link
# =============================================================================


class TestRelativeLink:
    def test_same_directory(self) -> None:
        assert relative_link("01/index.html", "01/example.html") == "example.html"

    def test_anchor_appended(self) -> None:
        assert (
            relative_link("01/index.html", "02/index.html", "#intro")
            == "../02/index.html#intro"
        )

    def test_self_link_returns_anchor_only(self) -> None:
        assert relative_link("01/index.html", "01/index.html", "#section") == "#section"

    def test_parent_directory(self) -> None:
        assert relative_link("01/index.html", "index.html") == "../index.html"


# =============================================================================
# is_excluded_dir
# =============================================================================


class TestIsExcludedDir:
    def test_hidden_dirs_excluded(self) -> None:
        assert is_excluded_dir(".git") is True

    def test_known_dir_excluded(self) -> None:
        assert is_excluded_dir("node_modules") is True

    def test_chapter_dir_kept(self) -> None:
        assert is_excluded_dir("01-slash-commands") is False


# =============================================================================
# collect_folder_markdown
# =============================================================================


class TestCollectFolderMarkdown:
    def test_readme_first(self, tmp_path: Path) -> None:
        (tmp_path / "b.md").write_text("# B")
        (tmp_path / "README.md").write_text("# Readme")
        (tmp_path / "a.md").write_text("# A")
        files = collect_folder_markdown(tmp_path)
        assert [f.name for f in files] == ["README.md", "a.md", "b.md"]

    def test_skips_hidden_subdirs(self, tmp_path: Path) -> None:
        (tmp_path / "README.md").write_text("# R")
        hidden = tmp_path / ".cache"
        hidden.mkdir()
        (hidden / "junk.md").write_text("# junk")
        files = collect_folder_markdown(tmp_path)
        assert [f.name for f in files] == ["README.md"]


# =============================================================================
# derive_page_title
# =============================================================================


class TestDerivePageTitle:
    def test_uses_h1(self, tmp_path: Path) -> None:
        f = tmp_path / "f.md"
        f.write_text("Some intro\n# The Title\nBody")
        assert derive_page_title(f, "Default") == "The Title"

    def test_falls_back_when_no_h1(self, tmp_path: Path) -> None:
        f = tmp_path / "f.md"
        f.write_text("No heading here")
        assert derive_page_title(f, "Default") == "Default"


# =============================================================================
# replace_mermaid_blocks
# =============================================================================


class TestReplaceMermaidBlocks:
    def test_replaces_fence(self) -> None:
        md = "Before\n\n```mermaid\nflowchart LR\nA-->B\n```\n\nAfter"
        out = replace_mermaid_blocks(md)
        assert '<pre class="mermaid">' in out
        assert "flowchart LR" in out
        assert "```mermaid" not in out

    def test_escapes_html(self) -> None:
        md = "```mermaid\nA --> B<C>\n```\n"
        out = replace_mermaid_blocks(md)
        assert "&lt;C&gt;" in out


# =============================================================================
# render_markdown
# =============================================================================


class TestRenderMarkdown:
    def test_heading_gets_github_anchor(self) -> None:
        html_content = render_markdown("# Hello World\n\nBody")
        assert 'id="hello-world"' in html_content

    def test_duplicate_headings_get_suffix(self) -> None:
        html_content = render_markdown("# Hi\n\n# Hi\n")
        assert 'id="hi"' in html_content
        assert 'id="hi-1"' in html_content


# =============================================================================
# rewrite_links
# =============================================================================


class TestRewriteLinks:
    def _state(self) -> BuildState:
        state = BuildState()
        state.source_to_url = {
            "README.md": "index.html",
            "01-slash-commands/README.md": "01-slash-commands/index.html",
        }
        return state

    def _config(self, root: Path) -> WebsiteConfig:
        return WebsiteConfig(
            root_path=root,
            output_path=root / "out",
            repo_url="https://github.com/example/repo",
            branch="main",
        )

    def test_internal_markdown_link_rewritten(
        self, tmp_path: Path, logger: logging.Logger
    ) -> None:
        (tmp_path / "README.md").write_text("# Home")
        (tmp_path / "01-slash-commands").mkdir()
        (tmp_path / "01-slash-commands" / "README.md").write_text("# Slash")
        page = PageInfo(
            source=tmp_path / "README.md",
            rel_source="README.md",
            output_url="index.html",
            title="Home",
            section="Introduction",
            is_section_index=True,
        )
        html_in = '<a href="01-slash-commands/README.md">go</a>'
        out = rewrite_links(
            html_in, page, self._state(), self._config(tmp_path), logger
        )
        assert "01-slash-commands/index.html" in out
        assert ".md" not in out

    def test_anchor_preserved(self, tmp_path: Path, logger: logging.Logger) -> None:
        (tmp_path / "README.md").write_text("# Home")
        (tmp_path / "01-slash-commands").mkdir()
        (tmp_path / "01-slash-commands" / "README.md").write_text("# Slash")
        page = PageInfo(
            source=tmp_path / "README.md",
            rel_source="README.md",
            output_url="index.html",
            title="Home",
            section="Introduction",
            is_section_index=True,
        )
        html_in = '<a href="01-slash-commands/README.md#run">go</a>'
        out = rewrite_links(
            html_in, page, self._state(), self._config(tmp_path), logger
        )
        assert "#run" in out

    def test_non_markdown_link_uses_github_blob(
        self, tmp_path: Path, logger: logging.Logger
    ) -> None:
        (tmp_path / "scripts").mkdir()
        (tmp_path / "scripts" / "build.sh").write_text("#!/bin/bash")
        (tmp_path / "README.md").write_text("# Home")
        page = PageInfo(
            source=tmp_path / "README.md",
            rel_source="README.md",
            output_url="index.html",
            title="Home",
            section="Introduction",
            is_section_index=True,
        )
        html_in = '<a href="scripts/build.sh">script</a>'
        out = rewrite_links(
            html_in, page, self._state(), self._config(tmp_path), logger
        )
        assert "github.com/example/repo/blob/main/scripts/build.sh" in out
        assert 'target="_blank"' in out

    def test_external_link_left_alone(
        self, tmp_path: Path, logger: logging.Logger
    ) -> None:
        page = PageInfo(
            source=tmp_path / "README.md",
            rel_source="README.md",
            output_url="index.html",
            title="Home",
            section="Introduction",
            is_section_index=True,
        )
        (tmp_path / "README.md").write_text("# Home")
        html_in = '<a href="https://anthropic.com">site</a>'
        out = rewrite_links(
            html_in, page, self._state(), self._config(tmp_path), logger
        )
        assert 'href="https://anthropic.com"' in out


# =============================================================================
# Full build smoke test
# =============================================================================


class TestBuildWebsite:
    def test_smoke_build(self, site_root: Path, logger: logging.Logger) -> None:
        out_dir = site_root / "site"
        config = WebsiteConfig(
            root_path=site_root,
            output_path=out_dir,
            repo_url="https://github.com/example/repo",
            branch="main",
        )

        build_website(config, logger)

        # Index page rendered
        index = out_dir / "index.html"
        assert index.exists()
        index_html = index.read_text(encoding="utf-8")
        assert "Home Page" in index_html
        assert "01-slash-commands/index.html" in index_html
        # Non-markdown link rewritten to GitHub
        assert "github.com/example/repo/blob/main/scripts/build.sh" in index_html
        # <source srcset> inside <picture> rewritten to point at assets/
        assert 'srcset="assets/resources/logos/' in index_html

        # Folder index rendered
        sc_index = out_dir / "01-slash-commands" / "index.html"
        assert sc_index.exists()
        sc_html = sc_index.read_text(encoding="utf-8")
        # Mermaid block became a <pre class="mermaid"> block
        assert '<pre class="mermaid">' in sc_html
        # Sibling markdown link rewritten
        assert "example.html" in sc_html

        # Example page rendered
        example_page = out_dir / "01-slash-commands" / "example.html"
        assert example_page.exists()
        example_html = example_page.read_text(encoding="utf-8")
        # Back-link to README rewrites to index.html
        assert "index.html" in example_html

        # Stylesheet copied into assets
        assert (out_dir / "assets" / "site.css").exists()
        # Logo copied into assets
        assert (out_dir / "assets" / "resources" / "logos" / "logo.svg").exists()
