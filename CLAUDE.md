# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

Claude How To is a tutorial repository for Claude Code features. This is **documentation-as-code** — the primary output is markdown files organized into numbered learning modules, not an executable application.

**Architecture**: Each module (01-10) covers a specific Claude Code feature with copy-paste templates, Mermaid diagrams, and examples. The build system validates documentation quality and generates an EPUB ebook.

## Common Commands

### Pre-commit Quality Checks

All documentation must pass four quality checks before commits (these run automatically via pre-commit hooks):

```bash
# Install pre-commit hooks (runs on every commit)
pre-commit install

# Run all checks manually
pre-commit run --all-files
```

The four checks are:
1. **markdown-lint** — Markdown structure and formatting via `markdownlint`
2. **cross-references** — Internal links, anchors, code fence syntax (Python script)
3. **mermaid-syntax** — Validates all Mermaid diagrams parse correctly (Python script)
4. **link-check** — External URLs are reachable (Python script)
5. **build-epub** — EPUB generates without errors (on `.md` changes)

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

### Testing

Python scripts in `scripts/` have unit tests:

```bash
# Run all tests
pytest scripts/tests/ -v

# Run with coverage
pytest scripts/tests/ -v --cov=scripts --cov-report=html

# Run specific test
pytest scripts/tests/test_build_epub.py -v
```

### Code Quality

```bash
# Lint and format Python code
ruff check scripts/
ruff format scripts/

# Security scan
bandit -c scripts/pyproject.toml -r scripts/ --exclude scripts/tests/

# Type checking
mypy scripts/ --ignore-missing-imports
```

### EPUB Build

```bash
# Generate ebook (renders Mermaid diagrams via Kroki.io API)
uv run scripts/build_epub.py

# With options
uv run scripts/build_epub.py --verbose --output custom-name.epub --max-concurrent 5
```

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
├── scripts/
│   ├── build_epub.py           # EPUB generator (renders Mermaid via Kroki API)
│   ├── check_cross_references.py   # Validates internal links
│   ├── check_links.py          # Checks external URLs
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
- Files are organized by feature complexity and dependencies

### Mermaid Diagrams
- All diagrams must parse successfully (checked by pre-commit hook)
- EPUB build renders diagrams via Kroki.io API (requires internet)
- Use Mermaid for flowcharts, sequence diagrams, and architecture visuals

### Cross-References
- Use relative paths for internal links (e.g., `(01-slash-commands/README.md)`)
- Code fences must specify language (e.g., ` ```bash `, ` ```python `)
- Anchor links use `#heading-name` format

### Link Validation
- External URLs must be reachable (checked by pre-commit hook)
- Avoid linking to ephemeral content
- Use permalinks where possible

## Key Architecture Points

1. **Numbered folders indicate learning order** — The 01-10 prefix represents the recommended sequence for learning Claude Code features. This numbering is intentional; do not reorganize alphabetically.

2. **Scripts are utilities, not the product** — The Python scripts in `scripts/` support documentation quality and EPUB generation. The actual content is in the numbered module folders.

3. **Pre-commit is the gatekeeper** — All four quality checks must pass before a PR is accepted. The CI pipeline runs these same checks as a second pass.

4. **Mermaid rendering requires network** — The EPUB build calls Kroki.io API to render diagrams. Build failures here are typically network issues or invalid Mermaid syntax.

5. **This is a tutorial, not a library** — When adding content, focus on clear explanations, copy-paste examples, and visual diagrams. The value is in teaching concepts, not providing reusable code.

## Commit Conventions

Follow conventional commit format:
- `feat(slash-commands): Add API documentation generator`
- `docs(memory): Improve personal preferences example`
- `fix(README): Correct table of contents link`
- `refactor(hooks): Simplify hook configuration examples`

Scope should match the folder name when applicable.
