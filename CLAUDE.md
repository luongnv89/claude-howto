# CLAUDE.md

This file provides guidance to Claude Code (claude.ai/code) when working with code in this repository.

## Project Overview

**Claude How To** is a comprehensive, visual learning guide for Claude Code. It teaches developers to use every Claude Code feature through structured tutorials, production-ready templates, and real-world examples.

- **Version**: 2.2.0 (March 2026)
- **Language**: Python 3.10+
- **Primary Tool**: EPUB builder that generates a downloadable guide from Markdown tutorials
- **Scope**: 10 feature modules covering slash commands, memory, skills, hooks, MCP, subagents, checkpoints, advanced features, plugins, and CLI

## Architecture & Content Structure

```
claude-howto/
├── 01-slash-commands/      # Basics: built-in commands & creating SKILL.md
├── 02-memory/              # CLAUDE.md hierarchy and memory management
├── 03-skills/              # Auto-invocable skills with progressive disclosure
├── 04-subagents/           # Agent delegation and task orchestration
├── 05-mcp/                 # External data sources and integrations
├── 06-hooks/               # Event-driven automation (25 hook types)
├── 07-plugins/             # Bundling features into plugins
├── 08-checkpoints/         # Safe experimentation with rewind
├── 09-advanced-features/   # Planning mode, extended thinking, remote sessions
├── 10-cli/                 # Print mode and CI/CD integration
├── scripts/                # Build and test tooling
│   ├── build_epub.py       # Main EPUB builder (converts MD to EPUB3)
│   ├── pyproject.toml      # Python project config (Ruff, Bandit, pytest)
│   ├── requirements.txt    # Dependencies (ebooklib, markdown, PIL, etc.)
│   └── tests/              # Unit tests for build process
├── resources/              # Logos, diagrams, assets
├── prompts/                # Claude Code prompts (skills, agents)
└── README.md, CATALOG.md, LEARNING-ROADMAP.md, etc.
```

### Key Content Files

- **LEARNING-ROADMAP.md** — Progressive path from beginner to advanced (11-13 hours)
- **CATALOG.md** — Searchable feature index with cross-references
- **INDEX.md** — Table of contents with navigation
- **QUICK_REFERENCE.md** — Cheat sheet for common tasks
- **STYLE_GUIDE.md** — Markdown standards for consistency

Each numbered lesson directory (01-10) contains:
- **README.md** — Tutorial with diagrams and examples
- **examples/** — Copy-paste templates and working code
- Supporting files (configs, scripts, SKILL.md files)

## Build System

### EPUB Generation

The `scripts/build_epub.py` tool converts the Markdown tutorials into a self-contained EPUB3 ebook:

```bash
python scripts/build_epub.py
# Output: claude-howto-v2.2.0.epub
```

**Process**:
1. Reads all Markdown files in dependency order
2. Processes Mermaid diagrams (converts to PNG)
3. Handles image references and links
4. Validates EPUB structure
5. Creates metadata and manifest

**Dependencies**: ebooklib, markdown, BeautifulSoup4, Pillow, httpx

### Common Commands

| Task | Command | Notes |
|------|---------|-------|
| **Build EPUB** | `python scripts/build_epub.py` | Output: `claude-howto-v2.2.0.epub` |
| **Run tests** | `pytest scripts/tests/ -v` | Python 3.10+ |
| **Run specific test** | `pytest scripts/tests/test_build_epub.py::test_function_name -v` | Single test |
| **Test coverage** | `pytest scripts/tests/ --cov=scripts --cov-report=html` | HTML report in `htmlcov/` |
| **Lint code** | `ruff check scripts/` | Auto-fix with `--fix` |
| **Format code** | `ruff format scripts/` | Enforces 88-char line length |
| **Security scan** | `bandit -c pyproject.toml -r scripts/` | Excludes tests by default |
| **Type check** | `mypy scripts/ --ignore-missing-imports` | Static analysis |
| **Pre-commit** | `pre-commit run --all-files` | Runs Ruff, Bandit, YAML checks |

### Python Environment Setup

```bash
# Create virtual environment (Python 3.10+)
python3 -m venv .venv
source .venv/bin/activate  # macOS/Linux
# or .venv\Scripts\activate  # Windows

# Install dependencies
pip install -r requirements.txt     # Core (EPUB builder only)
pip install -r requirements-dev.txt # For testing + development

# Or with uv (faster package manager)
uv venv
uv pip install -r requirements-dev.txt
```

## Testing & Quality

### Test Structure

- **Location**: `scripts/tests/`
- **Runner**: pytest with asyncio support
- **Coverage minimum**: 80%
- **Key tests**:
  - `test_build_epub.py` — EPUB generation and structure validation
  - Asset handling and image processing
  - Markdown parsing and link validation

### Pre-commit Hooks

The `.pre-commit-config.yaml` runs automatically on commit:
- **Ruff formatter** — Code formatting (88 chars)
- **Ruff linter** — Code quality (E/W/F/I/B/C4/UP/SIM/etc.)
- **Bandit** — Security vulnerability scan
- **YAML validator** — Config files
- **Merge conflict detector**

Run manually: `pre-commit run --all-files`

### GitHub Actions Workflow

Triggered on push/PR to `main`:
1. **Unit Tests** (Python 3.10, 3.11, 3.12) — MUST pass
2. **Ruff Lint** — Non-blocking warnings
3. **Bandit Security** — Non-blocking warnings
4. **Type Check** (mypy) — Non-blocking warnings
5. **Build EPUB** — MUST pass (depends on tests)
6. **Summary** — Artifacts and status

## Development Workflow

### When Adding Content

1. **Create a lesson**: Add to `NN-feature-name/README.md`
2. **Use Markdown standards**: Follow STYLE_GUIDE.md
3. **Include Mermaid diagrams**: `build_epub.py` converts them
4. **Add examples**: Create `NN-feature-name/examples/`
5. **Link between modules**: Use `@import` or relative links
6. **Test locally**: `python scripts/build_epub.py` (verify images render)

### When Modifying Build Scripts

1. **Add/update tests**: `scripts/tests/test_*.py`
2. **Run test suite**: `pytest scripts/tests/ -v`
3. **Check coverage**: Maintain 80%+ coverage
4. **Run security scan**: `bandit -r scripts/`
5. **Lint and format**: `ruff format scripts/ && ruff check scripts/`

### Naming Conventions

- **Branch names**: `add/feature`, `fix/issue`, `docs/improvement`
- **Commit messages**: Conventional commits (feat:, fix:, docs:, refactor:)
- **Files**: kebab-case for Markdown, snake_case for Python
- **Directories**: Two-digit prefix for lessons (01-, 02-, etc.)

## Key Files to Know

| File | Purpose |
|------|---------|
| `scripts/build_epub.py` | Main builder — processes MD → EPUB3 |
| `scripts/pyproject.toml` | Python config (Ruff, Bandit, pytest) |
| `CONTRIBUTING.md` | Contribution guidelines |
| `.github/TESTING.md` | Detailed testing documentation |
| `LEARNING-ROADMAP.md` | Self-assessment + learning paths |
| `.pre-commit-config.yaml` | Automated checks before commit |

## Important Notes

### Markdown Best Practices

- Use Mermaid diagrams for architecture/flow visualization
- Include code examples with language syntax highlighting
- Link to related lessons using relative paths or anchors
- Keep line length reasonable for readability
- Use `@import` syntax to avoid duplicating content across files

### Image & Asset Handling

- Place images in `resources/` or subdirectories
- Use relative paths in Markdown: `![alt](resources/image.png)`
- The EPUB builder automatically fetches images and embeds them
- Mermaid diagrams are auto-converted to PNG during build

### EPUB Output

- Built EPUB is a single self-contained file
- Includes all images, styles, and metadata
- Compatible with most e-readers (Apple Books, Kindle, Kobo, etc.)
- Output location: project root as `claude-howto-vX.X.X.epub`

## Related Documentation

- **[CONTRIBUTING.md](CONTRIBUTING.md)** — How to contribute new content
- **[TESTING.md](.github/TESTING.md)** — Detailed test setup and CI/CD
- **[STYLE_GUIDE.md](STYLE_GUIDE.md)** — Markdown writing standards
- **[QUICK_REFERENCE.md](QUICK_REFERENCE.md)** — Command cheatsheet
- **[Official Claude Code Docs](https://code.claude.com/docs)** — Official reference

## Workflow Tips

When working on lessons:
1. Refer to existing lessons (01-10) as templates
2. Use the LEARNING-ROADMAP.md to understand progression
3. Test EPUB build locally before committing
4. Include practical, copy-paste examples
5. Verify all links work (internal and external)

When writing about Claude Code features:
1. Check official docs for latest syntax
2. Show real-world use cases
3. Include architecture diagrams (Mermaid)
4. Highlight common pitfalls
5. Link to other relevant lessons
