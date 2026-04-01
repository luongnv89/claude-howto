#!/usr/bin/env python3
"""Validate Mermaid diagram syntax in Markdown files using mmdc."""

import json
import os
import re
import shutil
import subprocess  # nosec B404
import sys
import tempfile
from pathlib import Path

IGNORE_DIRS = {".venv", "node_modules", ".git", "blog-posts", ".agents"}


def main() -> int:
    if not shutil.which("mmdc"):
        print(
            "⚠ mmdc not found — skipping Mermaid validation (install @mermaid-js/mermaid-cli)"
        )
        return 0

    errors = []
    checked = 0

    # On GitHub Actions Linux runners, Chrome/Puppeteer requires --no-sandbox.
    # Write a temporary puppeteer config when MERMAID_PUPPETEER_NO_SANDBOX is set.
    puppeteer_config_path = None
    extra_args: list[str] = []
    if os.environ.get("MERMAID_PUPPETEER_NO_SANDBOX") == "true":
        with tempfile.NamedTemporaryFile(
            suffix=".json", mode="w", delete=False
        ) as pcfg:
            json.dump({"args": ["--no-sandbox", "--disable-setuid-sandbox"]}, pcfg)
            puppeteer_config_path = pcfg.name
        extra_args = ["-p", puppeteer_config_path]

    md_files = [
        f
        for f in Path().rglob("*.md")
        if not any(part in IGNORE_DIRS for part in f.parts)
    ]

    try:
        for file_path in md_files:
            content = file_path.read_text()
            blocks = re.findall(r"```mermaid\n(.*?)```", content, re.DOTALL)
            for i, block in enumerate(blocks):
                with tempfile.NamedTemporaryFile(
                    suffix=".mmd", mode="w", delete=False
                ) as tmp:
                    tmp.write(block)
                    tmp_path = tmp.name
                out_path = str(Path(tmp_path).with_suffix(".svg"))
                try:
                    result = subprocess.run(  # nosec B603 B607
                        ["mmdc", "-i", tmp_path, "-o", out_path, *extra_args],
                        capture_output=True,
                        text=True,
                        check=False,
                    )
                    if result.returncode != 0:
                        errors.append(
                            f"{file_path} (block {i + 1}): {result.stderr.strip()}"
                        )
                    else:
                        checked += 1
                finally:
                    Path(tmp_path).unlink(missing_ok=True)
                    Path(out_path).unlink(missing_ok=True)
    finally:
        if puppeteer_config_path:
            Path(puppeteer_config_path).unlink(missing_ok=True)

    print(f"✅ Checked {checked} Mermaid diagram(s)")
    if errors:
        print("\n❌ Mermaid errors:")
        for e in errors:
            print(f"  - {e}")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main())
