#!/usr/bin/env python3
"""Validate Markdown rendering correctness in tutorial README files.

Catches mechanical rendering bugs that look fine in a diff but render wrong
on GitHub / in the EPUB build: inner backticks in inline code, unescaped
pipes in table cells, stray $ARGUMENTS / $N outside code, mismatched fences.

Scope: `**/README.md` across the repo (tutorial modules + ja/uk/vi/zh
translations). Excludes `.venv`, `node_modules`, `.git`, `blog-posts`,
`.agents`, `.claude`, and `openspec` — these are not tutorial output.

Each rule is a function `(file_path, content) -> list[str]`. To add a new
rule: write the function, append `(name, fn)` to `RULES`, add fixtures in
`tests/test_check_markdown_rendering.py`.
"""

from __future__ import annotations

import re
import sys
from collections.abc import Callable
from pathlib import Path

IGNORE_DIRS = {
    ".venv",
    "node_modules",
    ".git",
    "blog-posts",
    "openspec",
    "prompts",
    ".agents",
    ".claude",
}

Rule = Callable[[Path, str], list[str]]


def iter_readme_files() -> list[Path]:
    return [
        f
        for f in Path().rglob("README.md")
        if not any(part in IGNORE_DIRS for part in f.parts)
    ]


_FENCE_RE = re.compile(r"^ {0,3}(?:>\s*)*```")


def _mask_fenced_blocks(content: str) -> str:
    """Replace fenced code blocks with blank lines so line numbers survive.

    Triple-backtick fences only. Recognises fences inside blockquotes
    (``` > ``` ``` ```), matching how GitHub renders them. Lines inside
    fences become empty so subsequent rules see no code content but still
    report accurate line numbers.
    """
    out: list[str] = []
    in_fence = False
    for line in content.split("\n"):
        if _FENCE_RE.match(line):
            in_fence = not in_fence
            out.append("")
            continue
        out.append("" if in_fence else line)
    return "\n".join(out)


def _strip_inline_code(line: str) -> str:
    """Remove inline code spans from a single line.

    Strips double-backtick spans first (they may contain single backticks),
    then single-backtick spans. HTML comments are also stripped so rules
    that scan prose ignore explanatory comments.
    """
    line = re.sub(r"<!--.*?-->", "", line)
    line = re.sub(r"``[^`]+``", "", line)
    line = re.sub(r"`[^`\n]+`", "", line)
    return line


def _consume_code_spans(line: str) -> str:
    """Remove well-formed inline code spans from a single line.

    Follows CommonMark inline-code semantics: a run of N backticks opens a
    span; the span closes at the next matching run of N backticks. Spans
    may nest different run-lengths. Anything left after consumption is a
    structural mismatch (an unmatched opening run).
    """
    out: list[str] = []
    i = 0
    n = len(line)
    while i < n:
        if line[i] != "`":
            out.append(line[i])
            i += 1
            continue
        run_start = i
        while i < n and line[i] == "`":
            i += 1
        run_len = i - run_start
        scan = i
        while scan < n:
            if line[scan] == "`":
                close_start = scan
                while scan < n and line[scan] == "`":
                    scan += 1
                if scan - close_start == run_len:
                    i = scan
                    break
            else:
                scan += 1
        else:
            out.append(line[run_start:i])
    return "".join(out)


def rule_backtick_in_inline_code(file_path: Path, content: str) -> list[str]:
    """Flag inline code spans that contain a literal backtick.

    Bug pattern shipped in PR #114: `` `!`command`` `` — a single-backtick
    span containing an inner backtick. The canonical fix is the
    ``` `` `text` `` ``` idiom (double-backticks + space padding).

    Detection: consume well-formed code spans left-to-right per line. Any
    leftover backtick is an unmatched opener — a structural mismatch that
    renders wrong on GitHub.

    Skips fenced code blocks.
    """
    masked = _mask_fenced_blocks(content)
    errors: list[str] = []
    for lineno, line in enumerate(masked.split("\n"), start=1):
        if "`" in _consume_code_spans(line):
            errors.append(
                f"{file_path}:{lineno}: backtick-in-inline-code — "
                "use `` `text` `` (double-backtick + space) to display a literal backtick"
            )
    return errors


def rule_unescaped_pipe_in_table(file_path: Path, content: str) -> list[str]:
    """Flag table rows whose unescaped pipe count differs from the header.

    A table row is `|...|...|`. The header row sets the column count; body
    rows must have the same count. A bare `|` in a cell (e.g. `[color|default]`)
    inflates the count and breaks rendering. The fix is `\\|`.

    Pipes inside inline-code spans are ignored (they need escaping too, but
    that's a separate idiom). The separator row `|---|---|` is ignored.
    """
    masked = _mask_fenced_blocks(content)
    errors: list[str] = []
    lines = masked.split("\n")

    def cell_count(line: str) -> int:
        scannable = _strip_inline_code(line.strip())
        return len(re.findall(r"(?<!\\)\|", scannable))

    i = 0
    while i < len(lines):
        line = lines[i].strip()
        if (
            line.startswith("|")
            and line.endswith("|")
            and i + 1 < len(lines)
            and re.match(r"^\s*\|[\s\-:|]+\|\s*$", lines[i + 1])
        ):
            header_pipes = cell_count(line)
            j = i + 2
            while j < len(lines):
                row = lines[j].strip()
                if not (row.startswith("|") and row.endswith("|")):
                    break
                if cell_count(row) != header_pipes:
                    errors.append(
                        f"{file_path}:{j + 1}: unescaped-pipe-in-table — "
                        "row cell count differs from header; escape literal `|` as `\\|`"
                    )
                j += 1
            i = j
        else:
            i += 1
    return errors


def rule_stray_argument_placeholder(file_path: Path, content: str) -> list[str]:
    """Flag `$ARGUMENTS` appearing in prose outside code.

    Tutorial snippets reference these inside fenced code blocks or inline
    code (`` `$ARGUMENTS` ``). When `$ARGUMENTS` appears in bare prose it
    usually means a tutorial snippet bled into the surrounding paragraph.

    Single-digit `$N` was considered but dropped: shell-arg `$0`..`$9` is
    syntactically indistinguishable from prose currency (`$5 today`,
    `$1,000`, `$5/month`) without semantic context, and currency is
    legitimate translator content. `$ARGUMENTS` is unambiguous.
    """
    masked = _mask_fenced_blocks(content)
    errors: list[str] = []
    pattern = re.compile(r"\$ARGUMENTS\b")
    for lineno, line in enumerate(masked.split("\n"), start=1):
        stripped = _strip_inline_code(line)
        if pattern.search(stripped):
            errors.append(
                f"{file_path}:{lineno}: stray-argument-placeholder — "
                "wrap `$ARGUMENTS` in backticks or move into a code fence"
            )
    return errors


def rule_unmatched_fence(file_path: Path, content: str) -> list[str]:
    """Flag files with an odd number of triple-backtick fences.

    Redundant safety net — `scripts/check_cross_references.py` also
    enforces this. Kept here so the validator stays self-contained.
    """
    fences = re.findall(r"^\s*```", content, re.MULTILINE)
    if len(fences) % 2 != 0:
        return [
            f"{file_path}:1: unmatched-fence — "
            "odd number of triple-backtick fences in file"
        ]
    return []


RULES: list[tuple[str, Rule]] = [
    ("backtick-in-inline-code", rule_backtick_in_inline_code),
    ("unescaped-pipe-in-table", rule_unescaped_pipe_in_table),
    ("stray-argument-placeholder", rule_stray_argument_placeholder),
    ("unmatched-fence", rule_unmatched_fence),
]


def main() -> int:
    errors: list[str] = []
    files = iter_readme_files()
    for file_path in files:
        content = file_path.read_text(encoding="utf-8")
        for _name, rule in RULES:
            errors.extend(rule(file_path, content))

    if errors:
        print("❌ Markdown rendering errors:")
        for e in errors:
            print(f"  - {e}")
        return 1

    print(
        f"✅ Markdown rendering clean ({len(files)} README files, {len(RULES)} rules)"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
