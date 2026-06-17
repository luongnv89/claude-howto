#!/usr/bin/env -S uv run --script
# /// script
# dependencies = ["markdown", "beautifulsoup4", "jinja2"]
# ///
"""
Build a static website from the Claude How-To markdown files.

Usage:
    uv run scripts/build_website.py
    uv run scripts/build_website.py --lang vi
    uv run scripts/build_website.py --output site/ --verbose

The website renders the existing markdown files as the single source of truth.
No content is duplicated — re-running this script regenerates the entire site
from the current state of the `.md` files.

Output:
    Creates `site/` (or the path passed to `--output`) containing one HTML page
    per markdown source plus `assets/` with logos and copied images.

Features:
    - Renders the same chapter order as the EPUB build (curriculum order).
    - Rewrites internal `.md` links to corresponding HTML pages on the site.
    - Rewrites repo-file/folder references (`.json`, `.sh`, `.py`, etc.) to
      GitHub source URLs so users can jump to the source on github.com.
    - Self-hosted Tailwind CSS (compiled via standalone CLI), Inter font, and
      `mermaid.min.js` — no third-party CDN scripts at runtime.
    - Light/dark theme toggle, mobile-friendly responsive layout, sidebar.
    - Hostable as plain static files (e.g. GitHub Pages).

Vendor assets (Tailwind CLI binary, Mermaid bundle, font files) are downloaded
on first build and cached under `scripts/.vendor-cache/`. See
`scripts/vendor_assets.py` for details.
"""

from __future__ import annotations

import argparse
import html
import logging
import re
import shutil
import sys
from dataclasses import dataclass, field
from pathlib import Path

import markdown
from bs4 import BeautifulSoup
from jinja2 import Environment, FileSystemLoader, select_autoescape

# Make sibling script modules importable regardless of cwd.
sys.path.insert(0, str(Path(__file__).parent))

from vendor_assets import (
    build_tailwind_css,
    fetch_fonts,
    fetch_mermaid,
    write_vendor_manifest,
)

# =============================================================================
# Configuration
# =============================================================================

REPO_URL = "https://github.com/luongnv89/claude-howto"
DEFAULT_BRANCH = "main"

# Files/dirs that exist in the repo but should not appear on the site.
EXCLUDE_DIRS = {
    ".git",
    ".github",
    ".venv",
    "venv",
    "env",
    "node_modules",
    "__pycache__",
    ".pytest_cache",
    ".ruff_cache",
    "blog-posts",
    "openspec",
    "prompts",
    ".agents",
    "archive",
    "local-progress",
    "promo-video",
    "slides",
    ".gitissue",
    ".asm-improver",
    ".codex",
    ".opencode",
    ".claude",
    "site",
    "scripts",
    "vi",
    "zh",
    "ja",
    "uk",
}

# Top-level markdown files that should not be rendered as standalone pages.
EXCLUDE_TOP_LEVEL = {
    "CLAUDE.md",
    "README.backup.md",
}

EXCLUDE_TOP_LEVEL_PREFIXES = ("update-plan",)

# Match the EPUB chapter ordering.
CHAPTER_ORDER: list[tuple[str, str]] = [
    ("README.md", "Introduction"),
    ("LEARNING-ROADMAP.md", "Learning Roadmap"),
    ("QUICK_REFERENCE.md", "Quick Reference"),
    ("claude_concepts_guide.md", "Claude Concepts Guide"),
    ("01-slash-commands", "Slash Commands"),
    ("02-memory", "Memory"),
    ("03-skills", "Skills"),
    ("04-subagents", "Subagents"),
    ("05-mcp", "MCP Protocol"),
    ("06-hooks", "Hooks"),
    ("07-plugins", "Plugins"),
    ("08-checkpoints", "Checkpoints"),
    ("09-advanced-features", "Advanced Features"),
    ("10-cli", "CLI Reference"),
    ("CATALOG.md", "Feature Catalog"),
    ("INDEX.md", "Index"),
    ("STYLE_GUIDE.md", "Style Guide"),
    ("resources.md", "Resources"),
]


@dataclass
class WebsiteConfig:
    """Configuration for the website builder."""

    root_path: Path
    output_path: Path
    repo_url: str = REPO_URL
    branch: str = DEFAULT_BRANCH
    site_title: str = "Claude Code How-To Guide"
    site_subtitle: str = "Master Claude Code in a Weekend"
    language: str = "en"


@dataclass
class PageInfo:
    """A single page generated for the site."""

    source: Path  # absolute path to the markdown source
    rel_source: str  # path relative to repo root (POSIX style)
    output_url: str  # site-relative URL, e.g. `01-slash-commands/index.html`
    title: str
    section: str  # the chapter group name (e.g. "Slash Commands")
    is_section_index: bool = False
    content: str | None = None  # cached source text (read once during collection)


@dataclass
class BuildState:
    """Build-time state shared across page rendering."""

    pages: list[PageInfo] = field(default_factory=list)
    source_to_url: dict[str, str] = field(default_factory=dict)


# =============================================================================
# Logging
# =============================================================================


def setup_logging(verbose: bool = False) -> logging.Logger:
    """Configure logging for the website builder."""
    level = logging.DEBUG if verbose else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(asctime)s - %(levelname)s - %(message)s",
        datefmt="%H:%M:%S",
    )
    return logging.getLogger("website_builder")


# =============================================================================
# Anchor algorithm (mirrors check_cross_references.heading_to_anchor)
# =============================================================================


def heading_to_anchor(heading: str) -> str:
    """Convert a heading to a GitHub-style anchor.

    Mirrors `scripts/check_cross_references.heading_to_anchor` so the website
    resolves the same `#anchor` references the validator accepts.
    """
    heading = re.sub(
        r"[\U0001F000-\U0001FFFF"
        r"\U00002702-\U000027B0"
        r"\U0000FE00-\U0000FE0F"
        r"\U0000200D"
        r"\U000000A9\U000000AE"
        r"\U00002000-\U0000206F"
        r"]",
        "",
        heading,
    )
    anchor = re.sub(r"[^\w\s-]", "", heading.lower(), flags=re.UNICODE)
    anchor = anchor.replace(" ", "-")
    return anchor.rstrip("-")


# =============================================================================
# Source discovery
# =============================================================================


def is_excluded_dir(name: str) -> bool:
    return name.startswith(".") or name in EXCLUDE_DIRS


def collect_folder_markdown(folder: Path) -> list[Path]:
    """Return markdown files inside a chapter folder.

    Order: README.md first (if present), then other top-level markdown files
    sorted alphabetically, then markdown files from non-hidden subfolders.
    """
    files: list[Path] = []
    readme = folder / "README.md"
    if readme.exists():
        files.append(readme)

    files.extend(md for md in sorted(folder.glob("*.md")) if md.name != "README.md")

    for sub in sorted(folder.iterdir()):
        if sub.is_dir() and not is_excluded_dir(sub.name):
            files.extend(collect_folder_markdown(sub))

    return files


def is_excluded_top_level_markdown(name: str) -> bool:
    return name in EXCLUDE_TOP_LEVEL or any(
        name.startswith(prefix) for prefix in EXCLUDE_TOP_LEVEL_PREFIXES
    )


def read_source(md_path: Path) -> str | None:
    """Read a markdown source file once, returning None on read failure."""
    try:
        return md_path.read_text(encoding="utf-8")
    except (OSError, UnicodeDecodeError):
        return None


def title_from_content(content: str | None, default: str) -> str:
    """Pick a page title from the first H1, falling back to the default."""
    if content is None:
        return default
    match = re.search(r"^#\s+(.+?)\s*$", content, flags=re.MULTILINE)
    if match:
        return match.group(1).strip()
    return default


def derive_page_title(md_path: Path, default: str) -> str:
    """Pick a page title from a file's first H1, falling back to the default."""
    return title_from_content(read_source(md_path), default)


def source_to_site_url(rel_source: str) -> str:
    """Map `01-slash-commands/README.md` → `01-slash-commands/index.html`."""
    if rel_source == "README.md":
        return "index.html"
    if rel_source.endswith("/README.md"):
        return rel_source[: -len("README.md")] + "index.html"
    if rel_source.endswith(".md"):
        return rel_source[:-3] + ".html"
    return rel_source


def _disambiguate_url(url: str, used_lower: set[str], rel_source: str) -> str:
    """Avoid case-insensitive filesystem collisions (e.g. INDEX.html ↔ index.html).

    macOS/Windows treat `INDEX.html` and `index.html` as the same file. When
    two source files would resolve to URLs that differ only in case, suffix
    the second one with the source stem so both pages survive the build.
    """
    if url.lower() not in used_lower:
        return url
    parent, sep, leaf = url.rpartition("/")
    stem, dot, ext = leaf.rpartition(".")
    src_stem = Path(rel_source).stem.lower()
    candidate = f"{parent}{sep}{stem}-{src_stem}{dot}{ext}"
    suffix = 2
    while candidate.lower() in used_lower:
        candidate = f"{parent}{sep}{stem}-{src_stem}-{suffix}{dot}{ext}"
        suffix += 1
    return candidate


def collect_pages(config: WebsiteConfig, logger: logging.Logger) -> BuildState:
    """Walk the configured chapter order and produce a flat list of pages."""
    state = BuildState()
    seen: set[str] = set()
    used_urls: set[str] = set()

    for item, display_name in CHAPTER_ORDER:
        item_path = config.root_path / item
        if not item_path.exists():
            logger.debug(f"Skipping missing chapter target: {item}")
            continue

        if item_path.is_file() and item_path.suffix == ".md":
            if is_excluded_top_level_markdown(item) or item in seen:
                continue
            seen.add(item)
            content = read_source(item_path)
            page_title = title_from_content(content, display_name)
            url = _disambiguate_url(source_to_site_url(item), used_urls, item)
            used_urls.add(url.lower())
            state.pages.append(
                PageInfo(
                    source=item_path,
                    rel_source=item,
                    output_url=url,
                    title=page_title,
                    section=display_name,
                    is_section_index=True,
                    content=content,
                )
            )
        elif item_path.is_dir():
            folder_files = collect_folder_markdown(item_path)
            for md in folder_files:
                rel = md.relative_to(config.root_path).as_posix()
                if rel in seen:
                    continue
                seen.add(rel)
                is_index = md.name == "README.md" and md.parent == item_path
                content = read_source(md)
                title = title_from_content(
                    content, display_name if is_index else md.stem
                )
                url = _disambiguate_url(source_to_site_url(rel), used_urls, rel)
                used_urls.add(url.lower())
                state.pages.append(
                    PageInfo(
                        source=md,
                        rel_source=rel,
                        output_url=url,
                        title=title,
                        section=display_name,
                        is_section_index=is_index,
                        content=content,
                    )
                )
        else:
            logger.warning(f"Chapter target is not a file or directory: {item}")

    for md in sorted(config.root_path.glob("*.md")):
        rel = md.relative_to(config.root_path).as_posix()
        if is_excluded_top_level_markdown(md.name) or rel in seen:
            continue
        seen.add(rel)
        title_default = md.stem.replace("-", " ").replace("_", " ").title()
        content = read_source(md)
        title = title_from_content(content, title_default)
        url = _disambiguate_url(source_to_site_url(rel), used_urls, rel)
        used_urls.add(url.lower())
        state.pages.append(
            PageInfo(
                source=md,
                rel_source=rel,
                output_url=url,
                title=title,
                section="Additional Docs",
                is_section_index=False,
                content=content,
            )
        )

    for page in state.pages:
        state.source_to_url[page.rel_source] = page.output_url

    logger.info(f"Collected {len(state.pages)} pages across the curriculum")
    return state


# =============================================================================
# Link rewriting
# =============================================================================


def is_external(href: str) -> bool:
    return href.startswith(("http://", "https://", "mailto:", "tel:"))


def relative_link(from_url: str, to_url: str, anchor: str = "") -> str:
    """Build a relative URL from `from_url` to `to_url` (both site-relative)."""
    if from_url == to_url:
        return anchor or ""
    from_parts = from_url.split("/")[:-1]
    to_parts = to_url.split("/")

    common = 0
    for a, b in zip(from_parts, to_parts, strict=False):
        if a != b:
            break
        common += 1

    ups = [".."] * (len(from_parts) - common)
    downs = to_parts[common:]
    parts = ups + downs
    rel = "/".join(parts) if parts else to_parts[-1]
    return rel + anchor


def _resolve_repo_relative(href: str, page_dir: Path, root_path: Path) -> str | None:
    """Resolve `href` relative to `page_dir` and return its repo-relative path."""
    resolved = (page_dir / href).resolve()
    try:
        rel_to_root = resolved.relative_to(root_path)
    except ValueError:
        return None
    return rel_to_root.as_posix()


def _github_source_url(
    config: WebsiteConfig, rel_str: str, *, is_dir: bool, anchor: str = ""
) -> str:
    kind = "tree" if is_dir else "blob"
    if rel_str == ".":
        return f"{config.repo_url}/{kind}/{config.branch}{anchor}"
    return f"{config.repo_url}/{kind}/{config.branch}/{rel_str}{anchor}"


def _rewrite_anchor(
    a: object,
    page: PageInfo,
    state: BuildState,
    config: WebsiteConfig,
    logger: logging.Logger,
) -> None:
    """Rewrite a single `<a href>` to its site URL or GitHub source URL."""
    href = a.get("href", "")  # type: ignore[attr-defined]
    if not href or is_external(href) or href.startswith("#"):
        return

    anchor = ""
    if "#" in href:
        href, anchor_part = href.split("#", 1)
        anchor = "#" + anchor_part
    if not href:
        return

    rel_str = _resolve_repo_relative(href, page.source.parent, config.root_path)
    if rel_str is None:
        logger.debug(f"Link outside repo skipped: {href} (in {page.rel_source})")
        return

    candidates = [rel_str]
    resolved = (page.source.parent / href).resolve()
    if not rel_str.endswith(".md") and resolved.is_dir():
        candidates.append(rel_str + "/README.md")

    for candidate in candidates:
        if candidate in state.source_to_url:
            a["href"] = relative_link(  # type: ignore[index]
                page.output_url, state.source_to_url[candidate], anchor
            )
            return

    github_url = _github_source_url(
        config, rel_str, is_dir=resolved.is_dir(), anchor=anchor
    )
    a["href"] = github_url  # type: ignore[index]
    a["target"] = "_blank"  # type: ignore[index]
    a["rel"] = "noopener noreferrer"  # type: ignore[index]


def _rewrite_asset_ref(
    element: object,
    attr: str,
    raw_value: str,
    page: PageInfo,
    config: WebsiteConfig,
) -> None:
    """Rewrite a single asset reference (img.src / source.srcset) to assets/."""
    if not raw_value or is_external(raw_value):
        return
    first = raw_value.split(",", 1)[0].strip().split(" ", 1)[0]
    if not first or is_external(first):
        return
    rel_str = _resolve_repo_relative(first, page.source.parent, config.root_path)
    if rel_str is None:
        return
    target = "assets/" + rel_str
    element[attr] = relative_link(page.output_url, target)  # type: ignore[index]


def rewrite_links_in_soup(
    soup: BeautifulSoup,
    page: PageInfo,
    state: BuildState,
    config: WebsiteConfig,
    logger: logging.Logger,
) -> None:
    """Rewrite anchor/image hrefs of `soup` in place to resolve on the site."""
    for a in soup.find_all("a"):
        _rewrite_anchor(a, page, state, config, logger)

    for img in soup.find_all("img"):
        _rewrite_asset_ref(img, "src", img.get("src", ""), page, config)
        if img.get("src"):
            img["loading"] = "lazy"

    for source in soup.find_all("source"):
        _rewrite_asset_ref(source, "srcset", source.get("srcset", ""), page, config)


def rewrite_links(
    html_content: str,
    page: PageInfo,
    state: BuildState,
    config: WebsiteConfig,
    logger: logging.Logger,
) -> str:
    """String wrapper around :func:`rewrite_links_in_soup`."""
    soup = BeautifulSoup(html_content, "html.parser")
    rewrite_links_in_soup(soup, page, state, config, logger)
    return str(soup)


# =============================================================================
# Mermaid handling
# =============================================================================


MERMAID_BLOCK_RE = re.compile(r"```mermaid\n(.*?)```", re.DOTALL)


def replace_mermaid_blocks(md_content: str) -> str:
    """Replace ```mermaid``` fences with `<pre class="mermaid">` for client-side render."""

    def _replace(match: re.Match[str]) -> str:
        code = match.group(1)
        return f'<pre class="mermaid">{html.escape(code)}</pre>'

    return MERMAID_BLOCK_RE.sub(_replace, md_content)


# =============================================================================
# Markdown rendering
# =============================================================================


def normalise_heading_ids_in_soup(soup: BeautifulSoup) -> None:
    """Force GitHub-style anchor ids on every heading of `soup`, in place.

    `python-markdown`'s `toc` extension generates its own slug; we re-write them
    so they match `check_cross_references.heading_to_anchor`.
    """
    used: dict[str, int] = {}
    for level in ("h1", "h2", "h3", "h4", "h5", "h6"):
        for h in soup.find_all(level):
            text = h.get_text(strip=True)
            anchor = heading_to_anchor(text)
            if not anchor:
                continue
            count = used.get(anchor, 0)
            final = anchor if count == 0 else f"{anchor}-{count}"
            used[anchor] = count + 1
            h["id"] = final


def normalise_heading_ids(html_content: str) -> str:
    """String wrapper around :func:`normalise_heading_ids_in_soup`."""
    soup = BeautifulSoup(html_content, "html.parser")
    normalise_heading_ids_in_soup(soup)
    return str(soup)


def extract_toc_from_soup(soup: BeautifulSoup) -> list[dict[str, str]]:
    """Pull H2/H3 headings of `soup` into a flat list for in-page navigation."""
    toc: list[dict[str, str]] = []
    for h in soup.find_all(["h2", "h3"]):
        anchor = h.get("id")
        if not anchor:
            continue
        toc.append(
            {
                "level": h.name,
                "text": h.get_text(strip=True),
                "anchor": anchor,
            }
        )
    return toc


def extract_toc(html_content: str) -> list[dict[str, str]]:
    """String wrapper around :func:`extract_toc_from_soup`."""
    return extract_toc_from_soup(BeautifulSoup(html_content, "html.parser"))


def render_markdown_to_soup(md_content: str) -> BeautifulSoup:
    """Render markdown to a parsed soup with GitHub-style heading ids applied.

    Parsing the rendered HTML once here lets the caller run TOC extraction and
    link rewriting against the same tree instead of reparsing per stage.
    """
    md_content = replace_mermaid_blocks(md_content)
    html_content = markdown.markdown(
        md_content,
        extensions=["tables", "fenced_code", "codehilite", "toc"],
        extension_configs={"codehilite": {"guess_lang": False}},
    )
    soup = BeautifulSoup(html_content, "html.parser")
    normalise_heading_ids_in_soup(soup)
    return soup


def render_markdown(md_content: str) -> str:
    """Convert markdown to HTML using the same extensions as the EPUB build."""
    return str(render_markdown_to_soup(md_content))


# =============================================================================
# Asset copying
# =============================================================================


ASSET_EXTENSIONS = {
    ".svg",
    ".png",
    ".jpg",
    ".jpeg",
    ".gif",
    ".webp",
    ".ico",
}


def copy_assets(
    config: WebsiteConfig, state: BuildState, logger: logging.Logger
) -> None:
    """Copy images referenced by any rendered page into `<output>/assets/`."""
    assets_dir = config.output_path / "assets"
    assets_dir.mkdir(parents=True, exist_ok=True)
    copied: set[Path] = set()

    for page in state.pages:
        content = page.content if page.content is not None else read_source(page.source)
        if content is None:
            continue
        for match in re.finditer(r"!\[[^\]]*\]\(([^)]+)\)", content):
            src = match.group(1).split(" ", 1)[0]
            if is_external(src):
                continue
            resolved = (page.source.parent / src).resolve()
            if not resolved.exists() or not resolved.is_file():
                continue
            if resolved.suffix.lower() not in ASSET_EXTENSIONS:
                continue
            try:
                rel = resolved.relative_to(config.root_path)
            except ValueError:
                continue
            target = assets_dir / rel
            if target in copied:
                continue
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(resolved, target)
            copied.add(target)

    # Always copy the logo set so the site header can reuse it.
    logo_dir = config.root_path / "resources" / "logos"
    if logo_dir.exists():
        for logo in logo_dir.glob("*.svg"):
            try:
                rel = logo.relative_to(config.root_path)
            except ValueError:
                continue
            target = assets_dir / rel
            target.parent.mkdir(parents=True, exist_ok=True)
            shutil.copy2(logo, target)
            copied.add(target)

    logger.info(f"Copied {len(copied)} asset file(s) into {assets_dir}")


# =============================================================================
# Page rendering
# =============================================================================


def build_nav_skeleton(state: BuildState) -> list[dict[str, object]]:
    """Group pages into sidebar sections once, keyed by section name.

    The grouping (sections + ordered page list) is identical for every page,
    so it is computed a single time and reused. `localize_nav` then turns the
    absolute page URLs into per-page relative URLs — an O(n) pass instead of
    re-grouping all pages for every page (which was O(n²)).
    """
    sections: list[dict[str, object]] = []
    section_map: dict[str, dict[str, object]] = {}

    for page in state.pages:
        section = section_map.get(page.section)
        if section is None:
            section = {"name": page.section, "items": []}
            section_map[page.section] = section
            sections.append(section)

        items = section["items"]
        assert isinstance(items, list)
        items.append(page)

    return sections


def localize_nav(
    skeleton: list[dict[str, object]], current_url: str
) -> list[dict[str, object]]:
    """Resolve the shared nav skeleton into relative URLs for `current_url`."""
    localized: list[dict[str, object]] = []
    for section in skeleton:
        pages = section["items"]
        assert isinstance(pages, list)
        localized.append(
            {
                "name": section["name"],
                "items": [
                    {
                        "title": page.title,
                        "url": relative_link(current_url, page.output_url),
                        "is_current": page.output_url == current_url,
                        "is_index": page.is_section_index,
                    }
                    for page in pages
                ],
            }
        )
    return localized


def render_pages(
    config: WebsiteConfig,
    state: BuildState,
    env: Environment,
    logger: logging.Logger,
) -> None:
    """Render each markdown page into `<output>/<output_url>`."""
    template = env.get_template("page.html.j2")
    total = len(state.pages)

    nav_skeleton = build_nav_skeleton(state)

    for idx, page in enumerate(state.pages):
        nav = localize_nav(nav_skeleton, page.output_url)
        if page.content is not None:
            md_content = page.content
        else:
            try:
                md_content = page.source.read_text(encoding="utf-8")
            except UnicodeDecodeError as e:
                raise RuntimeError(f"Failed to read {page.source}: {e}") from e

        # Parse the rendered markdown once, then run heading-id normalisation,
        # TOC extraction, and link rewriting against the same tree before a
        # single serialization — avoids reparsing the HTML three times per page.
        soup = render_markdown_to_soup(md_content)
        toc = extract_toc_from_soup(soup)
        rewrite_links_in_soup(soup, page, state, config, logger)
        html_content = str(soup)

        prev_page = state.pages[idx - 1] if idx > 0 else None
        next_page = state.pages[idx + 1] if idx < total - 1 else None

        rendered = template.render(
            site_title=config.site_title,
            site_subtitle=config.site_subtitle,
            page_title=page.title,
            section=page.section,
            content=html_content,
            toc=toc,
            nav=nav,
            current_url=page.output_url,
            base_path=relative_link(page.output_url, "index.html").rsplit(
                "index.html", 1
            )[0],
            assets_prefix=relative_link(page.output_url, "assets/").rsplit(
                "assets/", 1
            )[0]
            + "assets/",
            prev_page=(
                {
                    "title": prev_page.title,
                    "url": relative_link(page.output_url, prev_page.output_url),
                }
                if prev_page
                else None
            ),
            next_page=(
                {
                    "title": next_page.title,
                    "url": relative_link(page.output_url, next_page.output_url),
                }
                if next_page
                else None
            ),
            github_source_url=f"{config.repo_url}/blob/{config.branch}/{page.rel_source}",
            repo_url=config.repo_url,
        )

        out_file = config.output_path / page.output_url
        out_file.parent.mkdir(parents=True, exist_ok=True)
        out_file.write_text(rendered, encoding="utf-8")
        logger.debug(f"Wrote {out_file}")

    logger.info(f"Rendered {total} HTML page(s) into {config.output_path}")


# =============================================================================
# Build orchestration
# =============================================================================


def build_website(
    config: WebsiteConfig,
    logger: logging.Logger,
    *,
    skip_vendor: bool = False,
) -> Path:
    """Generate the full static site at `config.output_path`.

    ``skip_vendor=True`` skips the Tailwind CLI compile and the Mermaid/font
    downloads — used by tests that don't need network access.
    """
    if not config.root_path.is_dir():
        raise RuntimeError(f"Root path is not a directory: {config.root_path}")

    config.output_path.mkdir(parents=True, exist_ok=True)

    template_dir = Path(__file__).parent / "website_templates"
    env = Environment(
        loader=FileSystemLoader(str(template_dir)),
        autoescape=select_autoescape(["html", "xml"]),
        trim_blocks=True,
        lstrip_blocks=True,
    )

    state = collect_pages(config, logger)
    if not state.pages:
        raise RuntimeError(
            f"No markdown pages found under {config.root_path}; "
            "check that the chapter directories exist."
        )

    render_pages(config, state, env, logger)
    copy_assets(config, state, logger)

    # Self-hosted vendor assets — drop all CDN dependencies.
    assets_dir = config.output_path / "assets"
    css_source = template_dir / "site.css"
    if css_source.exists():
        css_target = assets_dir / "site.css"
        css_target.parent.mkdir(parents=True, exist_ok=True)
        shutil.copy2(css_source, css_target)

    if skip_vendor:
        logger.info("Skipping vendor asset fetch (skip_vendor=True)")
    else:
        vendor_dir = assets_dir / "vendor"
        fetch_mermaid(vendor_dir / "mermaid", logger)
        fonts_css = fetch_fonts(vendor_dir / "fonts", logger)
        # Run Tailwind LAST so it can scan the rendered HTML for class usage.
        build_tailwind_css(
            output_css=assets_dir / "tailwind.css",
            template_dir=template_dir,
            site_dir=config.output_path,
            logger=logger,
        )
        fonts_files = vendor_dir / "fonts" / "files"
        write_vendor_manifest(
            vendor_dir,
            fonts_count=sum(1 for _ in fonts_files.iterdir())
            if fonts_files.exists()
            else 0,
        )
        logger.debug(f"Fonts CSS: {fonts_css}")

    logger.info(f"Website build complete: {config.output_path}")
    return config.output_path


# =============================================================================
# CLI
# =============================================================================


def main() -> int:
    parser = argparse.ArgumentParser(
        description="Build a static website from Claude How-To markdown files."
    )
    parser.add_argument(
        "--root",
        "-r",
        type=Path,
        default=None,
        help="Root directory containing markdown files (default: repo root)",
    )
    parser.add_argument(
        "--output",
        "-o",
        type=Path,
        default=None,
        help="Output directory for the generated site (default: <repo>/site)",
    )
    parser.add_argument(
        "--lang",
        type=str,
        default="en",
        choices=["en", "vi", "zh", "ja", "uk"],
        help="Language code for the source tree (default: en — root markdown)",
    )
    parser.add_argument(
        "--repo-url",
        type=str,
        default=REPO_URL,
        help=f"GitHub repository URL for blob links (default: {REPO_URL})",
    )
    parser.add_argument(
        "--branch",
        type=str,
        default=DEFAULT_BRANCH,
        help=f"Branch name for GitHub blob links (default: {DEFAULT_BRANCH})",
    )
    parser.add_argument(
        "--verbose", "-v", action="store_true", help="Enable verbose logging"
    )

    args = parser.parse_args()

    repo_root = (args.root or Path(__file__).parent.parent).resolve()

    lang_root_map = {
        "en": repo_root,
        "vi": repo_root / "vi",
        "zh": repo_root / "zh",
        "ja": repo_root / "ja",
        "uk": repo_root / "uk",
    }
    source_root = lang_root_map[args.lang].resolve()

    default_output = repo_root / ("site" if args.lang == "en" else f"site-{args.lang}")
    output_path = (args.output or default_output).resolve()

    logger = setup_logging(args.verbose)
    config = WebsiteConfig(
        root_path=source_root,
        output_path=output_path,
        repo_url=args.repo_url,
        branch=args.branch,
        language=args.lang,
    )

    try:
        build_website(config, logger)
        print(f"Successfully built website at: {output_path}")
        return 0
    except (OSError, RuntimeError) as exc:
        logger.error(f"Build failed: {exc}")
        return 1
    except KeyboardInterrupt:
        logger.warning("Build interrupted by user")
        return 130


if __name__ == "__main__":
    sys.exit(main())
