#!/usr/bin/env python3
"""Validate cross-references, anchors, and code fences in Markdown files."""

import re
import sys
from pathlib import Path

IGNORE_DIRS = {".venv", "node_modules", ".git"}


def iter_md_files():
    for f in Path().rglob("*.md"):
        if not any(part in IGNORE_DIRS for part in f.parts):
            yield f


def heading_to_anchor(heading: str) -> str:
    # Strip emoji (non-ASCII) and punctuation, matching GitHub's anchor generation
    heading = heading.encode("ascii", "ignore").decode()
    return re.sub(r"[^\w\s-]", "", heading.lower()).strip().replace(" ", "-")


def main() -> int:
    errors = []

    for file_path in iter_md_files():
        content = file_path.read_text()

        # Relative .md links must resolve
        errors.extend(
            f"{file_path}: broken cross-reference → '{link_path}'"
            for link_path in re.findall(r"\[[^\]]+\]\(([^)#]+\.md)[^)]*\)", content)
            if not (file_path.parent / link_path).resolve().exists()
        )

        # In-page anchors must match a real heading
        anchors = re.findall(r"\[[^\]]+\]\(#([^)]+)\)", content)
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
    import os

    strict = os.environ.get("CROSS_REF_STRICT") == "1"
    result = main()
    sys.exit(result if strict else 0)
