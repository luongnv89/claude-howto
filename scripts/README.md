<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

> 🌐 [中文版本](README.zh.md) | [English Version](README.md)

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
