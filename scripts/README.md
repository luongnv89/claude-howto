<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# Build Scripts

This directory contains two generators that turn the tutorial markdown files
into distributable formats:

- [**EPUB Builder**](#epub-builder-script) — `build_epub.py`
- [**Static Website Builder**](#static-website-builder) — `build_website.py`

Both treat the `.md` files as the single source of truth — re-run the relevant
script after editing markdown to regenerate the output.

---

# EPUB Builder Script

Build an EPUB ebook from the Claude How-To markdown files.

## Features

- Organizes chapters by folder structure (01-slash-commands, 02-memory, etc.)
- Renders Mermaid diagrams as PNG images via Kroki.io API
- Async concurrent fetching - renders all diagrams in parallel
- Generates a cover image from the project logo
- Converts internal markdown links to EPUB chapter references
- Strict error mode - fails if any diagram cannot be rendered

## Requirements

- Python 3.10+
- [uv](https://github.com/astral-sh/uv)
- Internet connection for Mermaid diagram rendering

## Quick Start

```bash
# Simplest way - uv handles everything
uv run scripts/build_epub.py
```

## Development Setup

```bash
# Create virtual environment
uv venv

# Activate and install dependencies
source .venv/bin/activate
uv pip install -r requirements-dev.txt

# Run tests
pytest scripts/tests/ -v

# Run the script
python scripts/build_epub.py
```

## Command-Line Options

```
usage: build_epub.py [-h] [--root ROOT] [--output OUTPUT] [--verbose]
                     [--timeout TIMEOUT] [--max-concurrent MAX_CONCURRENT]

options:
  -h, --help            show this help message and exit
  --root, -r ROOT       Root directory (default: repo root)
  --output, -o OUTPUT   Output path (default: claude-howto-guide.epub)
  --verbose, -v         Enable verbose logging
  --timeout TIMEOUT     API timeout in seconds (default: 30)
  --max-concurrent N    Max concurrent requests (default: 10)
```

## Examples

```bash
# Build with verbose output
uv run scripts/build_epub.py --verbose

# Custom output location
uv run scripts/build_epub.py --output ~/Desktop/claude-guide.epub

# Limit concurrent requests (if rate-limited)
uv run scripts/build_epub.py --max-concurrent 5
```

## Output

Creates `claude-howto-guide.epub` in the repository root directory.

The EPUB includes:
- Cover image with project logo
- Table of contents with nested sections
- All markdown content converted to EPUB-compatible HTML
- Mermaid diagrams rendered as PNG images

## Running Tests

```bash
# With virtual environment
source .venv/bin/activate
pytest scripts/tests/ -v

# Or with uv directly
uv run --with pytest --with pytest-asyncio \
    --with ebooklib --with markdown --with beautifulsoup4 \
    --with httpx --with pillow --with tenacity \
    pytest scripts/tests/ -v
```

## Dependencies

Managed via PEP 723 inline script metadata:

| Package | Purpose |
|---------|---------|
| `ebooklib` | EPUB generation |
| `markdown` | Markdown to HTML conversion |
| `beautifulsoup4` | HTML parsing |
| `httpx` | Async HTTP client |
| `pillow` | Cover image generation |
| `tenacity` | Retry logic |

## Troubleshooting

**Build fails with network error**: Check internet connectivity and Kroki.io status. Try `--timeout 60`.

**Rate limiting**: Reduce concurrent requests with `--max-concurrent 3`.

**Missing logo**: The script generates a text-only cover if `claude-howto-logo.png` is not found.

---

# Static Website Builder

Generate an elegant, mobile-friendly static website from the same markdown
files used by the EPUB build. The website is the rendered view; the `.md`
files remain the single source of truth.

## Features

- One HTML page per markdown source — internal `.md` links are rewritten to
  the corresponding pages on the site
- References to non-markdown repo files (templates, scripts, JSON) become
  GitHub blob URLs that open the source on github.com
- Mermaid diagrams render client-side via `mermaid.min.js`, served from the
  built site (no CDN at runtime)
- Tailwind CSS compiled with the standalone CLI (Go binary, no Node.js) and
  served from the built site — responsive layout with sidebar nav, in-page
  TOC, dark mode toggle, and prev/next page navigation
- Inter + JetBrains Mono fonts are self-hosted alongside the CSS — no
  third-party requests at page load
- Mirrors the EPUB curriculum order (`01-` … `10-` plus top-level docs)
- Hostable as plain static files — designed to deploy to GitHub Pages

## Quick Start

```bash
# Build the English website into ./site/
uv run scripts/build_website.py

# Preview locally
python -m http.server --directory site 8080
# then open http://localhost:8080
```

## Command-Line Options

```
usage: build_website.py [-h] [--root ROOT] [--output OUTPUT]
                        [--lang {en,vi,zh,ja,uk}] [--repo-url REPO_URL]
                        [--branch BRANCH] [--verbose]

options:
  --root, -r ROOT       Source root (default: repo root)
  --output, -o OUTPUT   Output directory (default: <repo>/site)
  --lang LANG           Language to build: en | vi | zh | ja | uk
  --repo-url URL        GitHub repo for blob links (default: luongnv89/claude-howto)
  --branch BRANCH       Branch for blob links (default: main)
  --verbose, -v         Enable verbose logging
```

## GitHub Pages Deploy

The repo ships a workflow at `.github/workflows/pages.yml` that builds the
site on every push to `main` (when any `.md` or generator file changes) and
publishes via `actions/deploy-pages`. Enable GitHub Pages in repo settings
with **Source: GitHub Actions** to activate it.

## Architecture

`build_website.py` reuses the chapter-ordering logic from `build_epub.py` and
ships HTML templates under `scripts/website_templates/`:

- `page.html.j2` — per-page Jinja2 template with sidebar nav, TOC, prev/next
- `tailwind.config.js`, `tailwind.input.css` — config + entry CSS for the
  Tailwind standalone CLI; the CLI scans the built HTML and produces
  `site/assets/tailwind.css` with just the utilities actually used
- `site.css` — small layer of site-specific styles plus Pygments theme

The Tailwind CLI binary, Mermaid bundle, and font files are downloaded on
first build into `scripts/.vendor-cache/` (gitignored) — see
`scripts/vendor_assets.py`.

Heading anchors are generated using the exact algorithm in
`check_cross_references.heading_to_anchor`, so `#anchor` links validated by
the pre-commit hook resolve correctly on the rendered site.
