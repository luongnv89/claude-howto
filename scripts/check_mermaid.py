#!/usr/bin/env python3
"""Validate Mermaid diagram syntax in Markdown files using mmdc.

Usage:
    python scripts/check_mermaid.py              # every Markdown file in the repo
    python scripts/check_mermaid.py a.md b.md    # only these files (pre-commit)

Each mmdc call launches a headless Chromium, so the check is kept cheap by:
- validating only the files passed on the command line, when any are given;
- rendering each distinct diagram once (translations share many diagrams);
- running mmdc in parallel;
- remembering diagrams that already passed in `.cache/mermaid-ok/`, keyed by
  the diagram text and the mmdc version. Delete that directory to re-check.
  A full-repo scan (no file arguments) prunes markers no diagram uses.
"""

from __future__ import annotations

import hashlib
import json
import os
import re
import shutil
import subprocess  # nosec B404
import sys
import tempfile
from concurrent.futures import ThreadPoolExecutor
from pathlib import Path

IGNORE_DIRS = {".venv", "node_modules", ".git", "blog-posts", ".agents"}
CACHE_DIR = Path(".cache/mermaid-ok")
MERMAID_RE = re.compile(r"```mermaid\n(.*?)```", re.DOTALL)
TIMEOUT = 60
# Each worker is a Chromium instance (~150 MB), so cap the pool.
MAX_WORKERS = min(4, os.cpu_count() or 1)


def iter_md_files(paths: list[str]) -> list[Path]:
    if paths:
        candidates = [Path(p) for p in paths if p.endswith(".md")]
    else:
        candidates = list(Path().rglob("*.md"))
    return [
        f
        for f in candidates
        if f.is_file() and not any(part in IGNORE_DIRS for part in f.parts)
    ]


def collect_blocks(paths: list[str]) -> dict[str, list[str]]:
    """Map each distinct diagram to where it appears, so it is rendered once."""
    locations: dict[str, list[str]] = {}  # block -> ["file (block N)", ...]
    for file_path in iter_md_files(paths):
        content = file_path.read_text(encoding="utf-8")
        for i, block in enumerate(MERMAID_RE.findall(content)):
            locations.setdefault(block, []).append(f"{file_path} (block {i + 1})")
    return locations


def mmdc_version() -> str:
    try:
        result = subprocess.run(  # nosec B603 B607
            ["mmdc", "--version"],
            capture_output=True,
            text=True,
            check=False,
            timeout=TIMEOUT,
        )
    except subprocess.TimeoutExpired:
        return "unknown"
    return result.stdout.strip() or "unknown"


def cache_key(block: str, version: str) -> str:
    return hashlib.sha256(f"{version}\0{block}".encode()).hexdigest()


def prune_cache(live: set[str]) -> None:
    """Delete markers no current diagram uses. Only valid after a full-repo scan."""
    if CACHE_DIR.exists():
        for marker in CACHE_DIR.iterdir():
            if marker.name not in live:
                marker.unlink(missing_ok=True)


def render_block(block: str, extra_args: list[str]) -> str | None:
    """Run mmdc on one diagram. Return the error message, or None if it parses."""
    with tempfile.TemporaryDirectory() as tmpdir:
        src = Path(tmpdir) / "diagram.mmd"
        out = Path(tmpdir) / "diagram.svg"
        src.write_text(block, encoding="utf-8")
        try:
            result = subprocess.run(  # nosec B603 B607
                ["mmdc", "-i", str(src), "-o", str(out), *extra_args],
                capture_output=True,
                text=True,
                check=False,
                timeout=TIMEOUT,
            )
        except subprocess.TimeoutExpired:
            return f"mmdc timed out after {TIMEOUT}s"
    if result.returncode != 0:
        return result.stderr.strip() or f"mmdc exited with {result.returncode}"
    return None


def main(argv: list[str]) -> int:
    if not shutil.which("mmdc"):
        print(
            "⚠ mmdc not found — skipping Mermaid validation (install @mermaid-js/mermaid-cli)"
        )
        return 0

    locations = collect_blocks(argv)
    if not locations:
        if not argv:
            prune_cache(set())
        print("✅ No Mermaid diagrams in the checked files")
        return 0

    total = sum(len(locs) for locs in locations.values())
    version = mmdc_version()
    keys = {block: cache_key(block, version) for block in locations}
    pending = [b for b in locations if not (CACHE_DIR / keys[b]).exists()]

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

    errors: list[str] = []
    try:
        with ThreadPoolExecutor(max_workers=MAX_WORKERS) as pool:
            results = pool.map(lambda b: render_block(b, extra_args), pending)
            for block, error in zip(pending, results, strict=True):
                if error is None:
                    CACHE_DIR.mkdir(parents=True, exist_ok=True)
                    (CACHE_DIR / keys[block]).touch()
                else:
                    errors.extend(f"{loc}: {error}" for loc in locations[block])
    finally:
        if puppeteer_config_path:
            Path(puppeteer_config_path).unlink(missing_ok=True)

    # A full-repo scan sees every live diagram, so any other marker is stale.
    if not argv:
        prune_cache(set(keys.values()))

    cached = len(locations) - len(pending)
    print(
        f"✅ Checked {total} Mermaid diagram(s): {len(locations)} unique, "
        f"{len(pending)} rendered, {cached} cached"
    )
    if errors:
        print("\n❌ Mermaid errors:")
        for e in sorted(errors):
            print(f"  - {e}")
        return 1

    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
