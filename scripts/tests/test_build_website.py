"""Tests for the static website builder."""

from __future__ import annotations

import hashlib
import json
import logging
import re
import shutil
import subprocess
import sys
from pathlib import Path

import pytest
from bs4 import BeautifulSoup

sys.path.insert(0, str(Path(__file__).parent.parent))

import check_cross_references
from build_website import (
    BuildState,
    PageInfo,
    WebsiteConfig,
    _disambiguate_url,
    build_website,
    collect_folder_markdown,
    collect_pages,
    derive_page_title,
    heading_to_anchor,
    is_excluded_dir,
    is_excluded_top_level_markdown,
    relative_link,
    render_markdown,
    replace_mermaid_blocks,
    rewrite_links,
    source_to_site_url,
)

# Invisible characters, spelled as escapes so editors can't strip them silently.
ZWNJ = "\u200c"  # zero-width non-joiner (Persian, kept in GitHub heading ids)
ZWJ = "\u200d"  # zero-width joiner (stripped)

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
    (tmp_path / "CONTRIBUTING.md").write_text("# Contributing\n\nHelp improve docs.")
    (tmp_path / "CLAUDE.md").write_text("# Internal Agent Notes\n")
    (tmp_path / "update-plan-2026-05-02.md").write_text("# Temporary Plan\n")

    sc = tmp_path / "01-slash-commands"
    sc.mkdir()
    (sc / "README.md").write_text(
        "# Slash Commands\n\n## Advanced Usage\n\nMermaid time:\n\n```mermaid\nflowchart LR\nA-->B\n```\n\n"
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

    def test_zero_width_non_joiner_preserved(self) -> None:
        # Persian uses U+200C inside words; GitHub keeps it in heading ids.
        assert (
            heading_to_anchor(f"نام{ZWNJ}گذاری فایل و پوشه")
            == f"نام{ZWNJ}گذاری-فایل-و-پوشه"
        )

    @pytest.mark.parametrize(
        "heading",
        [
            f"نام{ZWNJ}گذاری فایل و پوشه",
            "[v2.1.245] — 2026-08-25",
            f"A{ZWJ}B test",
            "Hướng dẫn bắt đầu nhanh",
        ],
    )
    def test_matches_validator(self, heading: str) -> None:
        assert heading_to_anchor(heading) == check_cross_references.heading_to_anchor(
            heading
        )


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


class TestIsExcludedTopLevelMarkdown:
    def test_internal_agent_file_excluded(self) -> None:
        assert is_excluded_top_level_markdown("CLAUDE.md") is True

    def test_temporary_update_plan_excluded(self) -> None:
        assert is_excluded_top_level_markdown("update-plan-2026-05-02.md") is True

    def test_project_doc_included(self) -> None:
        assert is_excluded_top_level_markdown("CONTRIBUTING.md") is False


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


class TestCollectPages:
    def test_additional_top_level_docs_are_collected(
        self, site_root: Path, logger: logging.Logger
    ) -> None:
        state = collect_pages(
            WebsiteConfig(root_path=site_root, output_path=site_root / "site"), logger
        )
        assert "CONTRIBUTING.md" in state.source_to_url
        assert state.source_to_url["CONTRIBUTING.md"] == "CONTRIBUTING.html"
        assert "CLAUDE.md" not in state.source_to_url
        assert "update-plan-2026-05-02.md" not in state.source_to_url


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

    def test_repo_directory_link_uses_github_tree(
        self, tmp_path: Path, logger: logging.Logger
    ) -> None:
        (tmp_path / "scripts").mkdir()
        (tmp_path / "README.md").write_text("# Home")
        page = PageInfo(
            source=tmp_path / "README.md",
            rel_source="README.md",
            output_url="index.html",
            title="Home",
            section="Introduction",
            is_section_index=True,
        )
        html_in = '<a href="scripts/">scripts</a>'
        out = rewrite_links(
            html_in, page, self._state(), self._config(tmp_path), logger
        )
        assert "github.com/example/repo/tree/main/scripts" in out
        assert "github.com/example/repo/blob/main/scripts" not in out

    def test_repo_root_link_uses_github_tree(
        self, tmp_path: Path, logger: logging.Logger
    ) -> None:
        (tmp_path / "README.md").write_text("# Home")
        page = PageInfo(
            source=tmp_path / "README.md",
            rel_source="README.md",
            output_url="index.html",
            title="Home",
            section="Introduction",
            is_section_index=True,
        )
        html_in = '<a href=".">repo root</a>'
        out = rewrite_links(
            html_in, page, self._state(), self._config(tmp_path), logger
        )
        assert "github.com/example/repo/tree/main" in out
        assert "github.com/example/repo/blob/main/." not in out

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

        build_website(config, logger, skip_vendor=True)

        # Index page rendered
        index = out_dir / "index.html"
        assert index.exists()
        index_html = index.read_text(encoding="utf-8")
        assert "Home Page" in index_html
        assert "01-slash-commands/index.html" in index_html
        assert "CONTRIBUTING.html" in index_html
        # Non-markdown link rewritten to GitHub
        assert "github.com/example/repo/blob/main/scripts/build.sh" in index_html
        # <source srcset> inside <picture> rewritten to point at assets/
        assert 'srcset="assets/resources/logos/' in index_html

        # Additional top-level docs rendered
        assert (out_dir / "CONTRIBUTING.html").exists()
        assert not (out_dir / "CLAUDE.html").exists()
        assert not (out_dir / "update-plan-2026-05-02.html").exists()

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

        # Diagrams render with the self-hosted Pele bundle, not Mermaid.js.
        assert "vendor/pele/pele.global.js" in sc_html
        assert "pele.mount(" in sc_html
        assert "vendor/mermaid/" not in sc_html
        # A diagram Pele rejects (reported on m.error, not thrown) gets its
        # source back instead of a bare error message.
        assert "m.error !== undefined" in sc_html
        assert "container.replaceWith(pre)" in sc_html
        # Zoom stays on, and zoom makes a shrunk diagram a tab stop: every
        # <svg> Pele draws (it draws a new one on resize and font load) is
        # named in onRender after the nearest heading.
        assert "zoom: 'auto'" in sc_html
        assert "onRender: nameDiagram" in sc_html
        assert "svg.setAttribute('aria-label'" in sc_html
        assert "svg.hasAttribute('aria-labelledby')" in sc_html

        # Stylesheet copied into assets
        assert (out_dir / "assets" / "site.css").exists()
        # Logo copied into assets
        assert (out_dir / "assets" / "resources" / "logos" / "logo.svg").exists()
        # Template no longer references third-party CDNs.
        for hostile in (
            "cdn.tailwindcss.com",
            "cdn.jsdelivr.net",
            "fonts.googleapis.com",
        ):
            assert hostile not in index_html, (
                f"Built HTML still references {hostile} — CDN should be self-hosted"
            )


# =============================================================================
# vendor_assets module smoke test
# =============================================================================


class TestVendorAssets:
    def test_module_exports(self) -> None:
        """vendor_assets exposes the API build_website depends on."""
        import vendor_assets

        for attr in (
            "build_tailwind_css",
            "fetch_pele",
            "ensure_pele_bundle",
            "fetch_fonts",
            "write_vendor_manifest",
            "ensure_tailwind_binary",
            "TAILWIND_VERSION",
            "PELE_VERSION",
        ):
            assert hasattr(vendor_assets, attr), f"missing {attr}"
        for gone in ("fetch_mermaid", "MERMAID_VERSION", "MERMAID_URL"):
            assert not hasattr(vendor_assets, gone), f"{gone} should be removed"

    def test_pele_version_is_pinned_exactly(self) -> None:
        """The Pele bundle is pinned to an exact X.Y.Z with a digest per file."""
        import re

        import vendor_assets

        assert re.fullmatch(r"\d+\.\d+\.\d+", vendor_assets.PELE_VERSION)
        assert f"pele@{vendor_assets.PELE_VERSION}" in vendor_assets.PELE_BASE_URL
        assert set(vendor_assets.PELE_FILES) == {
            "dist/pele.js",
            "dist/pele.global.js",
            "LICENSE",
        }
        for digest in vendor_assets.PELE_FILES.values():
            assert re.fullmatch(r"[0-9a-f]{64}", digest)

    def test_detect_tailwind_asset_name(self) -> None:
        """Platform detection returns one of the known asset names."""
        from vendor_assets import _detect_tailwind_asset_name

        known = {
            "tailwindcss-macos-arm64",
            "tailwindcss-macos-x64",
            "tailwindcss-linux-arm64",
            "tailwindcss-linux-armv7",
            "tailwindcss-linux-x64",
            "tailwindcss-windows-x64.exe",
        }
        assert _detect_tailwind_asset_name() in known

    def test_download_rejects_non_http_scheme(self, tmp_path: Path) -> None:
        """The _download helper refuses file:/ftp:/etc. — defense-in-depth."""
        from vendor_assets import _download

        with pytest.raises(ValueError, match="non-HTTP URL"):
            _download("file:///etc/passwd", tmp_path / "out.bin")

    def test_font_css_cache_uses_sha256_url_key(
        self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch, logger: logging.Logger
    ) -> None:
        """Font CSS variants get distinct ten-character SHA-256 cache keys."""
        import vendor_assets

        cache_dir = tmp_path / "vendor-cache"
        monkeypatch.setattr(vendor_assets, "_vendor_cache_dir", lambda: cache_dir)
        urls = [
            vendor_assets.GOOGLE_FONTS_CSS_URL,
            vendor_assets.GOOGLE_FONTS_CSS_URL + "&variant=regression",
        ]
        downloads: list[str] = []

        def fake_download(
            url: str, dest: Path, headers: dict[str, str] | None = None
        ) -> None:
            del headers
            downloads.append(url)
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_text(f"/* {url} */", encoding="utf-8")

        monkeypatch.setattr(vendor_assets, "_download", fake_download)

        keys: list[str] = []
        for index, url in enumerate(urls):
            monkeypatch.setattr(vendor_assets, "GOOGLE_FONTS_CSS_URL", url)
            vendor_assets.fetch_fonts(tmp_path / f"output-{index}", logger)
            key = hashlib.sha256(url.encode("utf-8")).hexdigest()[:10]
            keys.append(key)
            assert len(key) == 10
            assert (cache_dir / "fonts" / f"fonts-{key}.css").is_file()

        assert keys[0] != keys[1]
        assert downloads == urls


# =============================================================================
# Pele bundle: pinned, sha256-verified on every use
# =============================================================================


_FAKE_PELE = {
    "dist/pele.js": b"export function render() {}\n",
    "dist/pele.global.js": b"var pele = (() => ({}))();\n",
    "LICENSE": b"MIT License\n",
}


class TestPeleBundle:
    @pytest.fixture
    def fake_pele(
        self, tmp_path: Path, monkeypatch: pytest.MonkeyPatch
    ) -> tuple[Path, list[str], dict[str, bytes]]:
        """Point the vendor cache at tmp_path and serve fake bundle bytes."""
        import vendor_assets

        cache_root = tmp_path / "vendor-cache"
        monkeypatch.setattr(vendor_assets, "_vendor_cache_dir", lambda: cache_root)
        monkeypatch.setattr(
            vendor_assets,
            "PELE_FILES",
            {rel: hashlib.sha256(data).hexdigest() for rel, data in _FAKE_PELE.items()},
        )
        served = dict(_FAKE_PELE)
        downloads: list[str] = []

        def fake_download(
            url: str, dest: Path, headers: dict[str, str] | None = None
        ) -> None:
            del headers
            rel = url.removeprefix(vendor_assets.PELE_BASE_URL + "/")
            downloads.append(rel)
            dest.parent.mkdir(parents=True, exist_ok=True)
            dest.write_bytes(served[rel])

        monkeypatch.setattr(vendor_assets, "_download", fake_download)
        cache = cache_root / "pele" / vendor_assets.PELE_VERSION
        return cache, downloads, served

    def test_good_bytes_cached_and_not_redownloaded(
        self,
        fake_pele: tuple[Path, list[str], dict[str, bytes]],
        logger: logging.Logger,
    ) -> None:
        import vendor_assets

        cache, downloads, _ = fake_pele
        assert vendor_assets.ensure_pele_bundle(logger) == cache
        assert sorted(downloads) == sorted(_FAKE_PELE)
        assert (cache / "pele.mjs").read_bytes() == _FAKE_PELE["dist/pele.js"]
        assert (cache / "LICENSE").read_bytes() == _FAKE_PELE["LICENSE"]

        downloads.clear()
        vendor_assets.ensure_pele_bundle(logger)
        assert downloads == [], "verified cache must not be downloaded again"

    def test_corrupted_cache_is_redownloaded(
        self,
        fake_pele: tuple[Path, list[str], dict[str, bytes]],
        logger: logging.Logger,
    ) -> None:
        import vendor_assets

        cache, downloads, _ = fake_pele
        vendor_assets.ensure_pele_bundle(logger)
        (cache / "pele.mjs").write_bytes(b"tampered")
        downloads.clear()

        vendor_assets.ensure_pele_bundle(logger)

        assert downloads == ["dist/pele.js"]
        assert (cache / "pele.mjs").read_bytes() == _FAKE_PELE["dist/pele.js"]

    def test_esm_bundle_is_cached_under_an_mjs_name(
        self,
        fake_pele: tuple[Path, list[str], dict[str, bytes]],
        logger: logging.Logger,
    ) -> None:
        # Node.js 20.0-20.18 and 22.0-22.6 load a bare .js file with no
        # "type": "module" beside it as CommonJS and fail on `export`.
        import vendor_assets

        cache, downloads, _ = fake_pele
        cache.mkdir(parents=True)
        # A cache written before the rename holds only pele.js.
        (cache / "pele.js").write_bytes(_FAKE_PELE["dist/pele.js"])

        vendor_assets.ensure_pele_bundle(logger)

        assert vendor_assets.PELE_ESM_BUNDLE == "pele.mjs"
        assert "dist/pele.js" in downloads
        assert (cache / "pele.mjs").read_bytes() == _FAKE_PELE["dist/pele.js"]

    def test_mismatching_download_raises_and_leaves_no_file(
        self,
        fake_pele: tuple[Path, list[str], dict[str, bytes]],
        logger: logging.Logger,
    ) -> None:
        import vendor_assets

        cache, _, served = fake_pele
        served["dist/pele.global.js"] = b"not the pinned bundle"

        with pytest.raises(RuntimeError, match="Checksum mismatch"):
            vendor_assets.ensure_pele_bundle(logger)

        assert not (cache / "pele.global.js").exists()
        assert not (cache / "pele.global.js.part").exists()

    def test_fetch_pele_copies_bundle_and_license(
        self,
        fake_pele: tuple[Path, list[str], dict[str, bytes]],
        tmp_path: Path,
        logger: logging.Logger,
    ) -> None:
        import vendor_assets

        target = tmp_path / "site" / "assets" / "vendor" / "pele"
        script = vendor_assets.fetch_pele(target, logger)

        assert script == target / "pele.global.js"
        assert script.read_bytes() == _FAKE_PELE["dist/pele.global.js"]
        assert (target / "LICENSE").read_bytes() == _FAKE_PELE["LICENSE"]

    def test_manifest_records_pele_not_mermaid(self, tmp_path: Path) -> None:
        import vendor_assets

        vendor_assets.write_vendor_manifest(tmp_path, fonts_count=3)
        manifest = json.loads((tmp_path / "manifest.json").read_text("utf-8"))
        assert manifest["pele"] == vendor_assets.PELE_VERSION
        assert "mermaid" not in manifest


# =============================================================================
# Diagram styles (site.css)
# =============================================================================

SITE_CSS = Path(__file__).parent.parent / "website_templates" / "site.css"
# Light fills that site lessons set on nodes without a text colour.
SOURCE_NODE_FILLS = ("#e1f5ff", "#e1f5fe", "#fff9c4")


def _css_rule(css: str, selector: str) -> str:
    match = re.search(rf"^{re.escape(selector)}\s*\{{(.*?)\}}", css, re.M | re.S)
    assert match, f"no rule for {selector!r} in site.css"
    return match.group(1)


def _css_color(rule: str, prop: str) -> str:
    match = re.search(rf"(?<![\w-]){re.escape(prop)}:\s*(#[0-9a-fA-F]{{6}})", rule)
    assert match, f"no {prop} colour in rule"
    return match.group(1)


def _contrast(first: str, second: str) -> float:
    def luminance(color: str) -> float:
        channels = [int(color[i : i + 2], 16) / 255 for i in (1, 3, 5)]
        r, g, b = (
            c / 12.92 if c <= 0.04045 else ((c + 0.055) / 1.055) ** 2.4
            for c in channels
        )
        return 0.2126 * r + 0.7152 * g + 0.0722 * b

    high, low = sorted((luminance(first), luminance(second)), reverse=True)
    return (high + 0.05) / (low + 0.05)


class TestDiagramStyles:
    @pytest.mark.parametrize("selector", [".mermaid", ".dark .mermaid"])
    def test_border_has_3_to_1_contrast(self, selector: str) -> None:
        # --pele-bg mirrors the page background (bg-slate-50 / bg-slate-950).
        rule = _css_rule(SITE_CSS.read_text("utf-8"), selector)
        border = _css_color(rule, "--pele-border")
        for surface in ("--pele-bg", "--pele-surface", "--pele-surface-alt"):
            assert _contrast(border, _css_color(rule, surface)) >= 3, surface

    def test_layout_rules_leave_the_source_fallback_alone(self) -> None:
        css = SITE_CSS.read_text("utf-8")
        assert "background" not in _css_rule(css, ".mermaid")
        assert "background: transparent" in _css_rule(css, "div.mermaid")

    def test_diagram_starts_below_the_zoom_buttons(self) -> None:
        # Pele 1.6.0 draws its zoom box 8px below the top of a diagram it
        # shrank to fit (two 24px buttons, 2px gap, 2px padding, 1px border:
        # 56px tall) and sets [hidden] on it when the diagram fits.
        rule = _css_rule(
            SITE_CSS.read_text("utf-8"),
            "div.mermaid:has(> .pele-zoom:not([hidden]))",
        )
        match = re.search(r"padding-top:\s*([^;]+);", rule)
        assert match, "no padding-top in the zoom-box rule"
        value = match.group(1)
        room = sum(float(n) for n in re.findall(r"([\d.]+)px", value))
        room += 16 * sum(float(n) for n in re.findall(r"([\d.]+)rem", value))
        assert room > 8 + 56
        # Side padding would narrow the width Pele lays the diagram out to.
        assert "padding-right" not in rule
        assert "padding-left" not in rule

    def test_dark_labels_on_source_fills_are_readable(self) -> None:
        rule = _css_rule(
            SITE_CSS.read_text("utf-8"),
            '.dark .mermaid .pele-node:has(> [style*="fill:"]) '
            '> .pele-label:not([style*="fill:"])',
        )
        label = _css_color(rule, "fill")
        for fill in SOURCE_NODE_FILLS:
            assert _contrast(label, fill) >= 4.5, fill


# =============================================================================
# Landing page
# =============================================================================


def _write_roadmap(path: Path, modules: list[dict]) -> Path:
    data = {
        "levels": [
            {
                "id": "beginner",
                "name": "Level 1 — Beginner",
                "title": "Getting started",
                "summary": "Start here.",
                "modules": modules,
            }
        ]
    }
    path.write_text(json.dumps(data), encoding="utf-8")
    return path


def _roadmap_module(lessons: list[dict], **overrides) -> dict:
    module = {
        "id": "slash-commands",
        "number": "01",
        "title": "Slash Commands",
        "source": "01-slash-commands/README.md",
        "time": "30 min",
        "tagline": "Commands.",
        "lessons": lessons,
    }
    module.update(overrides)
    return module


class TestLanding:
    def _config(self, site_root: Path, out_dir: Path, roadmap: Path) -> WebsiteConfig:
        return WebsiteConfig(
            root_path=site_root,
            output_path=out_dir,
            repo_url="https://github.com/example/repo",
            branch="main",
            landing=True,
            roadmap_path=roadmap,
        )

    def test_landing_build(
        self, site_root: Path, tmp_path: Path, logger: logging.Logger
    ) -> None:
        roadmap = _write_roadmap(
            tmp_path / "roadmap.json",
            [
                _roadmap_module(
                    [
                        {
                            "id": "overview",
                            "title": "Overview",
                            "heading": "Slash Commands",
                        },
                        {
                            "id": "advanced",
                            "title": "Advanced usage",
                            "heading": "Advanced Usage",
                        },
                    ]
                )
            ],
        )
        out_dir = site_root / "site"
        build_website(
            self._config(site_root, out_dir, roadmap), logger, skip_vendor=True
        )

        index = out_dir / "index.html"
        assert index.exists()
        index_html = index.read_text(encoding="utf-8")
        soup = BeautifulSoup(index_html, "html.parser")
        # The landing takes index.html
        assert soup.select_one("#roadmap") is not None
        assert soup.select_one('[data-lesson="slash-commands/overview"]') is not None
        # The header CTA and live copy status remain available in the rendered page.
        assert soup.select_one('header .nav-cta[href="#roadmap"]') is not None
        copy_status = soup.select_one("#copy-status")
        assert copy_status is not None
        assert copy_status.get("role") == "status"
        assert copy_status.get("aria-live") == "polite"
        # Lesson anchors resolve into the module page
        assert "01-slash-commands/index.html#advanced-usage" in index_html
        # Landing assets are copied and referenced alongside the site CSS
        assert (out_dir / "assets" / "landing.css").exists()
        assert (out_dir / "assets" / "landing.js").exists()
        assert soup.select_one('link[href="assets/landing.css"]') is not None
        assert soup.select_one('script[src="assets/landing.js"]') is not None
        # The landing must not pull in the docs-page stylesheet or CDNs
        assert "tailwind.css" not in index_html
        for hostile in ("cdn.tailwindcss.com", "fonts.googleapis.com"):
            assert hostile not in index_html

        # The README moved to guide.html
        guide = out_dir / "guide.html"
        assert guide.exists()
        assert "Home Page" in guide.read_text(encoding="utf-8")

        # Links from other pages to README.md now resolve to guide.html
        roadmap_page = (out_dir / "LEARNING-ROADMAP.html").read_text(encoding="utf-8")
        assert "guide.html#home-page" in roadmap_page
        assert "index.html#home-page" not in roadmap_page

    def test_landing_missing_heading(
        self, site_root: Path, tmp_path: Path, logger: logging.Logger
    ) -> None:
        roadmap = _write_roadmap(
            tmp_path / "roadmap.json",
            [
                _roadmap_module(
                    [
                        {
                            "id": "ghost",
                            "title": "Ghost",
                            "heading": "Does Not Exist",
                        }
                    ]
                )
            ],
        )
        with pytest.raises(RuntimeError, match="Does Not Exist"):
            build_website(
                self._config(site_root, site_root / "site", roadmap),
                logger,
                skip_vendor=True,
            )

    def test_landing_missing_source(
        self, site_root: Path, tmp_path: Path, logger: logging.Logger
    ) -> None:
        roadmap = _write_roadmap(
            tmp_path / "roadmap.json",
            [
                _roadmap_module(
                    [{"id": "x", "title": "X", "heading": "X"}],
                    source="99-nope/README.md",
                )
            ],
        )
        with pytest.raises(RuntimeError, match=r"99-nope/README\.md"):
            build_website(
                self._config(site_root, site_root / "site", roadmap),
                logger,
                skip_vendor=True,
            )

    def test_landing_duplicate_ids(
        self, site_root: Path, tmp_path: Path, logger: logging.Logger
    ) -> None:
        lesson = {"id": "overview", "title": "Overview", "heading": "Slash Commands"}
        roadmap = _write_roadmap(
            tmp_path / "roadmap.json",
            [_roadmap_module([lesson, dict(lesson)])],
        )
        with pytest.raises(RuntimeError, match="duplicate lesson id"):
            build_website(
                self._config(site_root, site_root / "site", roadmap),
                logger,
                skip_vendor=True,
            )

    def test_landing_real_repo(self, tmp_path: Path, logger: logging.Logger) -> None:
        """Every heading in the shipped roadmap.json must resolve to an anchor."""
        repo_root = Path(__file__).resolve().parents[2]
        out_dir = tmp_path / "site"
        config = WebsiteConfig(
            root_path=repo_root,
            output_path=out_dir,
            landing=True,
        )
        build_website(config, logger, skip_vendor=True)
        index_html = (out_dir / "index.html").read_text(encoding="utf-8")
        assert 'id="roadmap"' in index_html
        assert 'data-lesson="slash-commands/overview"' in index_html
        assert (out_dir / "guide.html").exists()

    def test_landing_off_keeps_readme_index(
        self, site_root: Path, logger: logging.Logger
    ) -> None:
        out_dir = site_root / "site"
        config = WebsiteConfig(
            root_path=site_root,
            output_path=out_dir,
            landing=False,
        )
        build_website(config, logger, skip_vendor=True)
        index_html = (out_dir / "index.html").read_text(encoding="utf-8")
        assert "Home Page" in index_html
        assert 'id="roadmap"' not in index_html
        assert not (out_dir / "guide.html").exists()


LANDING_JS_NODE_HARNESS = r"""
const assert = require("assert");
const fs = require("fs");
const vm = require("vm");
const source = fs.readFileSync(process.argv[1], "utf8");

function element(id = null, classes = [], attrs = {}) {
  const names = new Set(classes);
  const listeners = {};
  const item = {
    id, attrs, style: {}, hidden: false, textContent: "",
    classList: {
      add(...values) { values.forEach((value) => names.add(value)); },
      remove(...values) { values.forEach((value) => names.delete(value)); },
      contains(value) { return names.has(value); },
      toggle(value, force) {
        const next = force === undefined ? !names.has(value) : force;
        if (next) names.add(value); else names.delete(value);
        return next;
      },
    },
    getAttribute(name) { return name === "id" ? item.id : item.attrs[name] ?? null; },
    setAttribute(name, value) { item.attrs[name] = String(value); },
    addEventListener(name, handler) { (listeners[name] ||= []).push(handler); },
    dispatch(name) { (listeners[name] || []).forEach((handler) => handler({ target: item })); },
    querySelector: () => null,
    querySelectorAll: () => [],
    closest: () => null,
    appendChild: () => {},
    removeChild: () => {},
    select: () => {},
  };
  return item;
}

function makeEnvironment(spec) {
  const ids = new Map();
  const register = (id, classes = []) => {
    const item = element(id, classes);
    ids.set(id, item);
    return item;
  };
  const copy = element(null, [], { "data-copy": "echo copied" });
  const label = element();
  label.classList.add("copy-label");
  label.textContent = "Copy";
  copy.querySelector = (selector) => selector === ".copy-label" ? label : null;
  const document = {
    documentElement: element(null, ["no-js"]),
    body: element(),
    getElementById: (id) => ids.get(id) || null,
    querySelectorAll: (selector) => selector === "[data-copy]" ? [copy] : [],
    createElement: () => element(),
    addEventListener: () => {},
  };
  register("top", ["nav"]);
  register("nav-toggle");
  register("nav-menu");
  register("copy-status");

  let clipboardCalls = 0;
  let execCalls = 0;
  let copiedText = null;
  let resolveClipboard;
  const timers = new Map();
  let nextTimer = 1;
  document.execCommand = () => {
    execCalls += 1;
    if (spec.exec === "throw") throw new Error("copy denied");
    return spec.exec === "true";
  };
  const clipboard = spec.clipboard ? {
    writeText(text) {
      clipboardCalls += 1;
      copiedText = text;
      if (spec.clipboard === "deferred") {
        return new Promise((resolve) => { resolveClipboard = resolve; });
      }
      return spec.clipboard === "reject"
        ? Promise.reject(new Error("clipboard unavailable"))
        : Promise.resolve();
    },
  } : null;
  const navigator = { clipboard };
  const storage = new Map();
  const window = {
    innerHeight: 800,
    localStorage: {
      getItem: (key) => storage.get(key) || null,
      setItem: (key, value) => storage.set(key, value),
    },
    matchMedia: () => ({ matches: false }),
    setTimeout: (fn) => {
      const id = nextTimer++;
      timers.set(id, fn);
      return id;
    },
    clearTimeout: (id) => timers.delete(id),
    addEventListener: () => {},
    requestAnimationFrame: () => {},
    confirm: () => true,
    navigator,
  };
  return {
    copy, document, top: ids.get("top"),
    context: { console, Date, document, navigator, Promise, window },
    counters: () => ({ clipboardCalls, copiedText, execCalls }),
    resolveClipboard: () => resolveClipboard(),
    flushTimers: () => {
      const pending = Array.from(timers.values());
      timers.clear();
      pending.forEach((fn) => fn());
    },
  };
}

function runCase(spec) {
  const env = makeEnvironment(spec);
  vm.runInNewContext(source, env.context, { filename: "landing.js" });
  env.copy.dispatch("click");
  return new Promise((resolve) => setImmediate(() => {
    const label = env.copy.querySelector(".copy-label");
    const status = env.document.getElementById("copy-status");
    resolve({
      name: spec.name, label: label.textContent, status: status.textContent,
      copied: env.copy.classList.contains("copied"),
      navEnhanced: env.top.classList.contains("nav-enhanced"),
      ...env.counters(),
    });
  }));
}

async function runRapidClicks() {
  const spec = { clipboard: null, exec: "true" };
  const env = makeEnvironment(spec);
  vm.runInNewContext(source, env.context, { filename: "landing.js" });
  const label = env.copy.querySelector(".copy-label");
  const status = env.document.getElementById("copy-status");
  env.copy.dispatch("click");
  assert.strictEqual(label.textContent, "Copied");
  spec.exec = "false";
  env.copy.dispatch("click");
  assert.strictEqual(label.textContent, "Copy failed");
  env.flushTimers();
  assert.strictEqual(label.textContent, "Copy");
  assert.strictEqual(status.textContent, "Unable to copy to clipboard");
  assert.strictEqual(env.copy.classList.contains("copied"), false);

  const pending = makeEnvironment({ clipboard: "deferred", exec: "false" });
  vm.runInNewContext(source, pending.context, { filename: "landing.js" });
  pending.copy.dispatch("click");
  pending.context.navigator.clipboard = null;
  pending.copy.dispatch("click");
  pending.resolveClipboard();
  await new Promise((resolve) => setImmediate(resolve));
  assert.strictEqual(pending.copy.querySelector(".copy-label").textContent, "Copy failed");
  assert.strictEqual(pending.document.getElementById("copy-status").textContent, "Unable to copy to clipboard");
  pending.flushTimers();
  assert.strictEqual(pending.copy.querySelector(".copy-label").textContent, "Copy");
  return { name: "rapid-clicks" };
}

const cases = [
  ["clipboard-success", "resolve", "false", "Copied", "Copied to clipboard", true, 0, 1, "echo copied"],
  ["legacy-false", null, "false", "Copy failed", "Unable to copy to clipboard", false, 1, 0, null],
  ["legacy-throw", null, "throw", "Copy failed", "Unable to copy to clipboard", false, 1, 0, null],
  ["rejection-legacy-success", "reject", "true", "Copied", "Copied to clipboard", true, 1, 1, "echo copied"],
  ["rejection-legacy-false", "reject", "false", "Copy failed", "Unable to copy to clipboard", false, 1, 1, "echo copied"],
];
Promise.all([
  ...cases.map(([name, clipboard, exec]) => runCase({ name, clipboard, exec })),
  runRapidClicks(),
])
  .then((results) => {
    results.slice(0, cases.length).forEach((result, index) => {
      const [, , , label, status, copied, execCalls, clipboardCalls, copiedText] = cases[index];
      assert.deepStrictEqual(
        [result.label, result.status, result.copied, result.execCalls, result.clipboardCalls, result.copiedText, result.navEnhanced],
        [label, status, copied, execCalls, clipboardCalls, copiedText, true], result.name,
      );
    });
    process.stdout.write(JSON.stringify(results));
  })
  .catch((error) => {
    console.error(error.stack || error);
    process.exitCode = 1;
  });
"""


class TestLandingJavaScript:
    @pytest.mark.skipif(shutil.which("node") is None, reason="node is required")
    def test_copy_fallbacks_and_mobile_nav_enhancement(self) -> None:
        node = shutil.which("node")
        assert node is not None
        landing_js = Path(__file__).parent.parent / "website_templates" / "landing.js"
        result = subprocess.run(
            [node, "-e", LANDING_JS_NODE_HARNESS, str(landing_js)],
            capture_output=True,
            text=True,
            check=False,
        )
        assert result.returncode == 0, result.stderr
        results = json.loads(result.stdout)
        assert {result["name"] for result in results} == {
            "clipboard-success",
            "legacy-false",
            "legacy-throw",
            "rejection-legacy-success",
            "rejection-legacy-false",
            "rapid-clicks",
        }
