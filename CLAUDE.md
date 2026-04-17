# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Claude How To is a tutorial repository for Claude Code features. This is **documentation-as-code** — the primary output is markdown files organized into numbered learning modules, not an executable application.

**Architecture**: Each module (01-10) covers a specific Claude Code feature with copy-paste templates, Mermaid diagrams, and examples. The build system validates documentation quality and generates an EPUB ebook.

## Common Commands

### Development Environment Setup

```bash
# Install uv (Python package manager)
pip install uv

# Create virtual environment and install Python dependencies
uv venv
source .venv/bin/activate
uv pip install -r scripts/requirements-dev.txt

# Install Node.js tools (markdown linter and Mermaid validator)
npm install -g markdownlint-cli
npm install -g @mermaid-js/mermaid-cli

# Install pre-commit hooks
uv pip install pre-commit
pre-commit install
```

### Pre-commit Quality Checks

```bash
# Run all checks manually
pre-commit run --all-files
```

Pre-commit runs these hooks in order:
1. **ruff-lint / ruff-format** — Python linting and formatting (`scripts/` only)
2. **bandit** — Python security scan (`scripts/` only, excludes `scripts/tests/`)
3. **mypy** — Python type checking (`scripts/` only)
4. **markdown-lint** — Markdown structure and formatting via `markdownlint`
5. **cross-references** — Internal links, anchors, code fence language tags
6. **mermaid-syntax** — Validates all Mermaid diagrams parse correctly
7. **link-check** — External URLs are reachable (non-strict by default; set `LINK_CHECK_STRICT=1` to fail on dead links)
8. **build-epub** — EPUB generates without errors (runs only on `.md` changes)

Steps 1-3 apply only when Python files change; steps 4-8 apply to markdown changes. Vietnamese docs (`vi/**/*.md`) have a parallel set of hooks 5-8.

### Testing

```bash
# Run all tests
pytest scripts/tests/ -v

# Run with coverage
pytest scripts/tests/ -v --cov=scripts --cov-report=html

# Run specific test file
pytest scripts/tests/test_build_epub.py -v
```

Run `pytest` before `pre-commit` when modifying Python scripts; run `pre-commit run --all-files` when modifying markdown.

### Code Quality

```bash
# Lint and format Python code
ruff check scripts/
ruff format scripts/

# Security scan (B101 and B113 are suppressed; tests/ excluded)
bandit -c scripts/pyproject.toml -r scripts/ --exclude scripts/tests/

# Type checking
mypy scripts/ --ignore-missing-imports
```

### EPUB Build

```bash
# Generate ebook (renders Mermaid diagrams via local mmdc binary)
uv run scripts/build_epub.py

# Key options
uv run scripts/build_epub.py --verbose
uv run scripts/build_epub.py --output custom-name.epub
uv run scripts/build_epub.py --lang vi          # Vietnamese edition
uv run scripts/build_epub.py --lang zh          # Chinese edition
uv run scripts/build_epub.py --mmdc-path /path/to/mmdc   # custom mmdc binary
uv run scripts/build_epub.py --puppeteer-config puppeteer.json  # CI sandbox config
```

Mermaid rendering uses the local `mmdc` binary (installed via `npm install -g @mermaid-js/mermaid-cli`) — no internet required. Build failures are typically due to invalid Mermaid syntax or `mmdc` not being on `PATH`.

## Directory Structure

```
├── 01-slash-commands/      # User-invoked shortcuts
├── 02-memory/              # Persistent context examples
├── 03-skills/              # Reusable capabilities
├── 04-subagents/           # Specialized AI assistants
├── 05-mcp/                 # Model Context Protocol examples
├── 06-hooks/               # Event-driven automation
├── 07-plugins/             # Bundled features
├── 08-checkpoints/         # Session snapshots
├── 09-advanced-features/   # Planning, thinking, backgrounds
├── 10-cli/                 # CLI reference
├── vi/                     # Vietnamese translations (mirrors root structure)
├── zh/                     # Chinese translations
├── scripts/
│   ├── build_epub.py           # EPUB generator (local mmdc rendering)
│   ├── check_cross_references.py   # Validates internal links and code fence langs
│   ├── check_links.py          # Checks external URLs (strict mode via env var)
│   ├── check_mermaid.py        # Validates Mermaid syntax
│   └── tests/                  # Unit tests for scripts
├── .pre-commit-config.yaml    # Quality check definitions
└── README.md               # Main guide (also module index)
```

## Content Guidelines

### Module Structure
Each numbered folder follows the pattern:
- **README.md** — Overview of the feature with examples
- **Example files** — Copy-paste templates (`.md` for commands, `.json` for configs, `.sh` for hooks)

### Cross-References
- Use relative paths for internal links (e.g., `(01-slash-commands/README.md)`)
- Code fences must specify language (e.g., ` ```bash `, ` ```python `) — enforced by `check_cross_references.py`
- Anchor links use `#heading-name` format

### Mermaid Diagrams
- All diagrams must parse successfully (checked by `check_mermaid.py`)
- Use Mermaid for flowcharts, sequence diagrams, and architecture visuals

### Link Validation
- External URLs are checked by `check_links.py` on every commit (non-strict)
- CI enforces strict mode (`LINK_CHECK_STRICT=1`) — dead links fail the pipeline
- Use permalinks where possible; avoid linking to ephemeral content

## Key Architecture Points

1. **Numbered folders indicate learning order** — The 01-10 prefix is the recommended learning sequence. Do not reorganize alphabetically.

2. **Scripts are utilities, not the product** — Python scripts in `scripts/` support quality and EPUB generation. Content lives in the numbered module folders.

3. **Pre-commit is the gatekeeper** — All hooks must pass before a PR is accepted. CI runs the same checks with strict link validation.

4. **`--lang` flag cascades** — The `--lang` option works across `build_epub.py`, `check_cross_references.py`, `check_mermaid.py`, and `check_links.py` to target translated docs in `vi/` or `zh/`.

5. **This is a tutorial, not a library** — Focus on clear explanations, copy-paste examples, and visual diagrams. The value is in teaching concepts.

## Commit Conventions

Follow conventional commit format with folder name as scope:
- `feat(slash-commands): Add API documentation generator`
- `docs(memory): Improve personal preferences example`
- `fix(README): Correct table of contents link`
- `refactor(hooks): Simplify hook configuration examples`
