#!/usr/bin/env python3
"""Validate cross-references, anchors, and code fences in Markdown files."""

import re
import sys
from pathlib import Path

IGNORE_DIRS = {
    ".venv",
    "node_modules",
    ".git",
    "blog-posts",
    "openspec",
    "prompts",
    ".agents",
}
IGNORE_FILES = {"README.backup.md"}


def iter_md_files():
    for f in Path().rglob("*.md"):
        if (
            not any(part in IGNORE_DIRS for part in f.parts)
            and f.name not in IGNORE_FILES
        ):
            yield f


def heading_to_anchor(heading: str) -> str:
    # Match GitHub's anchor generation: strip emoji and special punctuation,
    # keep Unicode letters (including Vietnamese diacritics), lowercase,
    # replace spaces with hyphens, strip leading/trailing hyphens.
    # 1. Remove emoji (characters outside BMP or in known emoji ranges)
    heading = re.sub(
        r"[\U0001F000-\U0001FFFF"  # Supplementary Multilingual Plane symbols
        r"\U00002702-\U000027B0"  # Dingbats
        r"\U0000FE00-\U0000FE0F"  # Variation selectors
        r"\U0000200D"  # Zero-width joiner
        r"\U000000A9\U000000AE"  # (C) (R)
        r"\U00002000-\U0000206F"  # General punctuation (some emoji-adjacent)
        r"]",
        "",
        heading,
    )
    # 2. Remove punctuation but keep Unicode word chars, spaces, and hyphens
    anchor = re.sub(r"[^\w\s-]", "", heading.lower(), flags=re.UNICODE)
    # 3. Replace spaces with hyphens
    anchor = anchor.replace(" ", "-")
    # 4. Strip trailing hyphens (keep leading hyphens for emoji-prefixed headings)
    return anchor.rstrip("-")


def strip_code_blocks(content: str) -> str:
    """Remove fenced code blocks and inline code spans to avoid scanning example links."""
    # Strip fenced code blocks (``` ... ```)
    content = re.sub(r"```[^\n]*\n.*?```", "", content, flags=re.DOTALL)
    # Strip inline code spans (` ... `)
    content = re.sub(r"`[^`\n]+`", "", content)
    return content


def main() -> int:
    errors: list[str] = []

    for file_path in iter_md_files():
        content = file_path.read_text(encoding="utf-8")
        # Strip code blocks before scanning for links/anchors to avoid false positives
        # from documentation examples inside code fences.
        scannable = strip_code_blocks(content)

        # Relative .md links must resolve
        errors.extend(
            f"{file_path}: broken cross-reference → '{link_path}'"
            for link_path in re.findall(r"\[[^\]]+\]\(([^)#]+\.md)[^)]*\)", scannable)
            if not (file_path.parent / link_path).resolve().exists()
        )

        # In-page anchors must match a real heading
        anchors = re.findall(r"\[[^\]]+\]\(#([^)]+)\)", scannable)
        if anchors:
            headings = re.findall(r"^#{1,6}\s+(.+)$", content, re.MULTILINE)
            valid_anchors = {heading_to_anchor(h) for h in headings}
            errors.extend(
                f"{file_path}: broken anchor → '#{anchor}'"
                for anchor in anchors
                if anchor not in valid_anchors
            )

        # Unmatched code fences (only count fences at start of line)
        if len(re.findall(r"^```", content, re.MULTILINE)) % 2 != 0:
            errors.append(f"{file_path}: unmatched code fences")

    # All numbered lesson dirs must have README.md
    for i in range(1, 11):
        errors.extend(
            f"{d}: missing README.md"
            for d in Path().glob(f"{i:02d}-*")
            if d.is_dir() and not (d / "README.md").exists()
        )

    if errors:
        print("❌ Cross-reference errors:")
        for e in errors:
            print(f"  - {e}")
        return 1

    md_count = sum(1 for _ in iter_md_files())
    print(f"✅ All cross-references valid ({md_count} files checked)")
    return 0


if __name__ == "__main__":
    sys.exit(main())
