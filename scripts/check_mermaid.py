#!/usr/bin/env python3
"""Validate Mermaid diagram syntax in Markdown files by rendering them with Pele.

Every ```mermaid block under the current directory is rendered with the same
pinned, sha256-verified Pele bundle that the website and the EPUB use, so a
block that passes here renders there too. Identical blocks are rendered once.

Strict mode (``--strict``, or ``PELE_REQUIRED`` / ``CI`` set to 1/true/yes)
fails when Pele cannot run (Node.js >= 20 missing, bundle download or checksum
failure) and when no Mermaid block is found at all. Without strict mode a
missing Pele only prints a warning, so a contributor without Node.js can still
commit; CI and the pre-commit hooks run strict.
"""

from __future__ import annotations

import argparse
import logging
import os
import re
import sys
from collections import Counter
from dataclasses import dataclass
from pathlib import Path

# Make sibling script modules importable regardless of cwd.
sys.path.insert(0, str(Path(__file__).parent))

from pele_renderer import (
    MIN_NODE_MAJOR,
    PeleHelperError,
    PeleUnavailableError,
    render_diagrams,
)
from vendor_assets import PELE_VERSION

IGNORE_DIRS = {".venv", "node_modules", ".git", "blog-posts", ".agents"}
MERMAID_BLOCK_RE = re.compile(r"```[ \t]*mermaid[^\n]*\n(.*?)```", re.DOTALL)
TRUTHY = {"1", "true", "yes"}


@dataclass(frozen=True)
class MermaidBlock:
    """One ```mermaid block: where it is and what it contains."""

    path: Path
    line: int
    index: int
    source: str


def _env_truthy(name: str) -> bool:
    return os.environ.get(name, "").strip().lower() in TRUTHY


def is_strict(flag: bool) -> bool:
    """Strict when asked on the command line or when running in CI."""
    return flag or _env_truthy("PELE_REQUIRED") or _env_truthy("CI")


def find_markdown_files(root: Path) -> list[Path]:
    """All Markdown files under `root`, minus IGNORE_DIRS, in a stable order."""
    return sorted(
        f
        for f in root.rglob("*.md")
        if not any(part in IGNORE_DIRS for part in f.parts)
    )


def extract_blocks(path: Path) -> list[MermaidBlock]:
    """Return every ```mermaid block in `path` with its fence line number."""
    content = path.read_text(encoding="utf-8")
    return [
        MermaidBlock(
            path=path,
            line=content.count("\n", 0, match.start()) + 1,
            index=index,
            source=match.group(1),
        )
        for index, match in enumerate(MERMAID_BLOCK_RE.finditer(content), start=1)
    ]


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        description="Validate Mermaid diagrams in Markdown files with Pele."
    )
    parser.add_argument(
        "--strict",
        action="store_true",
        help="fail when Pele cannot run or no Mermaid block is found "
        "(also enabled by PELE_REQUIRED or CI)",
    )
    args = parser.parse_args(argv)
    strict = is_strict(args.strict)

    md_files = find_markdown_files(Path())
    blocks = [block for path in md_files for block in extract_blocks(path)]
    if not blocks:
        if strict:
            print(
                f"❌ No Mermaid blocks found in {len(md_files)} Markdown file(s) "
                "— refusing a vacuous pass in strict mode"
            )
            return 1
        print("✅ No Mermaid blocks found")
        return 0
    return validate_blocks(blocks, strict=strict)


def validate_blocks(blocks: list[MermaidBlock], *, strict: bool) -> int:
    """Render the unique sources once and report failures per block."""
    unique_sources = list(dict.fromkeys(block.source for block in blocks))
    logger = logging.getLogger("check_mermaid")
    try:
        results = render_diagrams(unique_sources, logger)
    except PeleUnavailableError as exc:
        if strict:
            print(f"❌ Pele is unavailable: {exc}")
            return 1
        print(
            f"⚠ Pele is unavailable ({exc}) — skipping Mermaid validation "
            f"(install Node.js >= {MIN_NODE_MAJOR})"
        )
        return 0
    except PeleHelperError as exc:
        print(f"❌ Pele helper failed: {exc}")
        return 1

    by_source = dict(zip(unique_sources, results, strict=True))
    errors = []
    for block in blocks:
        error = by_source[block.source].error
        if error is not None:
            errors.append(
                f"{block.path}:{block.line} (block {block.index}): {error.describe()}"
            )

    if errors:
        print(f"❌ Pele {PELE_VERSION} rejected {len(errors)} Mermaid block(s):")
        for message in errors:
            print(f"  - {message}")
        return 1

    types = Counter(r.diagram_type or "unknown" for r in results)
    summary = ", ".join(f"{name} {count}" for name, count in sorted(types.items()))
    files = len({block.path for block in blocks})
    print(
        f"✅ Pele {PELE_VERSION} rendered {len(blocks)} Mermaid block(s) "
        f"({len(unique_sources)} unique) from {files} file(s): {summary}"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main())
