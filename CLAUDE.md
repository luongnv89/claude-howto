# CLAUDE.md

Tutorial repo. Output is markdown in numbered modules `01-` through `10-`, not an app. Scripts in `scripts/` exist only to validate docs and build the EPUB.

See also `.claude/CLAUDE.md` for stack/commands and `STYLE_GUIDE.md` for lesson structure.

## Critical commands

```bash
# Quality gate (also runs on commit via pre-commit hooks)
pre-commit run --all-files

# Tests
pytest scripts/tests/ -v

# EPUB build (renders Mermaid with the local mmdc CLI — no network, needs mmdc on PATH)
uv run scripts/build_epub.py

# Python tooling
ruff check scripts/ && ruff format scripts/
mypy scripts/ --ignore-missing-imports
bandit -c scripts/pyproject.toml -r scripts/ --exclude scripts/tests/
```

Pre-commit runs 5 doc checks on `.md` changes: markdown-lint, cross-references, mermaid-syntax, link-check, markdown-rendering. All must pass. The EPUB build is **not** a pre-commit hook — it runs in CI only (`build-epub` job in `.github/workflows/test.yml`), because it needs a local `mmdc` binary that has no working arm64 build.

## Architecture map

- `01-` … `10-` — tutorial modules. **Numbered prefix = learning order**, not alphabetical. Do not reorganize.
- Each module: `README.md` + copy-paste templates (`.md`, `.json`, `.sh`).
- `scripts/` — utilities (EPUB builder, link/mermaid/cross-ref validators). Not the product.
- `02-memory/*.md` — CLAUDE.md templates users copy into their own projects. Don't confuse with this file.
- `openspec/` — spec-driven change proposals.

## Hard rules

- **YOU MUST NOT commit or push without explicit user request.**
- **YOU MUST NOT add `Co-Authored-By: Claude`** to any commit message.
- Always activate `.venv` before running Python scripts (check `venv/`, `.venv/`, `env/`).
- Internal links use **relative paths** (e.g. `01-slash-commands/README.md`); anchors use `#heading-name`.
- Code fences **must** declare a language (`bash`, `python`, `json`, …) — the cross-reference check fails otherwise.
- External URLs must be reachable and stable. No ephemeral links.
- Mermaid diagrams must parse (validated pre-commit, and only when `mmdc` is installed — the check skips with a warning otherwise). A broken EPUB build is usually invalid Mermaid or a missing/failing `mmdc`.
- Commit format: `type(scope): subject` where `scope` matches the module folder (e.g. `feat(slash-commands):`, `docs(memory):`, `fix(README):`).
- Do not reorganize the `01-`–`10-` numbering. The order is the curriculum.

## Workflow preferences

- For lesson edits, follow `STYLE_GUIDE.md` for structure/naming/diagrams.
- Small fixes → minimal diff. Don't rewrite a section to fix a typo.
- When adding a module page: README + templates first, then update root `README.md` index and `LEARNING-ROADMAP.md` if order/timing changes.
- Tutorial > library: prioritize clear explanations and copy-paste examples over reusable abstractions.
- If a quality check fails, fix the underlying issue. Don't bypass with `--no-verify`.

## Token Efficiency
- Never re-read files you just wrote or edited. You know the contents.
- Never re-run commands to "verify" unless the outcome was uncertain.
- Don't echo back large blocks of code or file contents unless asked.
- Batch related edits into single operations. Don't make 5 edits when 1 handles it.
- Skip confirmations like "I'll continue..." Just do it.
- If a task needs 1 tool call, don't use 3. Plan before acting.
- Do not summarize what you just did unless the result is ambiguous or you need additional input.
