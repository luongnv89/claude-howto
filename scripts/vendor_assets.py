"""Download and self-host third-party assets (Tailwind, Mermaid, Inter font).

Replaces the previous CDN-based approach so the rendered site has no external
runtime dependencies. Assets are cached under `scripts/.vendor-cache/` and
copied into the built site's `assets/vendor/` directory.

The Tailwind standalone CLI (a Go binary, no Node.js required) is downloaded
on first use and reused thereafter. We pin to Tailwind v3 because the templates
use v3-style runtime configuration; Tailwind v4 deprecated that config format.
"""

from __future__ import annotations

import json
import logging
import os
import platform
import re
import shutil
import stat
import subprocess  # nosec B404 — used only to invoke the bundled Tailwind CLI
import urllib.request
from pathlib import Path

TAILWIND_VERSION = "v3.4.19"
MERMAID_VERSION = "10"
MERMAID_URL = (
    f"https://cdn.jsdelivr.net/npm/mermaid@{MERMAID_VERSION}/dist/mermaid.min.js"
)
GOOGLE_FONTS_CSS_URL = (
    "https://fonts.googleapis.com/css2?"
    "family=Inter:wght@400;500;600;700;800"
    "&family=JetBrains+Mono:wght@400;500;600"
    "&display=swap"
)
GOOGLE_FONTS_UA = (
    "Mozilla/5.0 (Windows NT 10.0; Win64; x64) "
    "AppleWebKit/537.36 (KHTML, like Gecko) "
    "Chrome/120.0.0.0 Safari/537.36"
)

VENDOR_CACHE_DIR_NAME = ".vendor-cache"
TAILWIND_BIN_NAME = "tailwindcss"


def _vendor_cache_dir() -> Path:
    return Path(__file__).parent / VENDOR_CACHE_DIR_NAME


def _detect_tailwind_asset_name() -> str:
    system = platform.system().lower()
    machine = platform.machine().lower()
    if system == "darwin":
        return (
            "tailwindcss-macos-arm64" if machine == "arm64" else "tailwindcss-macos-x64"
        )
    if system == "linux":
        if machine in ("aarch64", "arm64"):
            return "tailwindcss-linux-arm64"
        if machine.startswith("armv7"):
            return "tailwindcss-linux-armv7"
        return "tailwindcss-linux-x64"
    if system == "windows":
        return "tailwindcss-windows-x64.exe"
    raise RuntimeError(f"Unsupported platform for Tailwind CLI: {system}/{machine}")


def _download(url: str, dest: Path, headers: dict[str, str] | None = None) -> None:
    dest.parent.mkdir(parents=True, exist_ok=True)
    if not url.startswith(("http://", "https://")):
        raise ValueError(f"Refusing to fetch non-HTTP URL: {url}")
    req = urllib.request.Request(url, headers=headers or {})
    with urllib.request.urlopen(req) as resp, dest.open("wb") as out:  # nosec B310 — scheme validated above
        shutil.copyfileobj(resp, out)


def ensure_tailwind_binary(logger: logging.Logger) -> Path:
    """Download the Tailwind standalone CLI if not already cached."""
    cache = _vendor_cache_dir()
    bin_path = cache / TAILWIND_BIN_NAME
    if bin_path.exists() and os.access(bin_path, os.X_OK):
        return bin_path

    asset = _detect_tailwind_asset_name()
    url = f"https://github.com/tailwindlabs/tailwindcss/releases/download/{TAILWIND_VERSION}/{asset}"
    logger.info(f"Downloading Tailwind CLI {TAILWIND_VERSION} ({asset})")
    _download(url, bin_path)
    bin_path.chmod(bin_path.stat().st_mode | stat.S_IXUSR | stat.S_IXGRP | stat.S_IXOTH)
    return bin_path


def build_tailwind_css(
    output_css: Path,
    template_dir: Path,
    site_dir: Path,
    logger: logging.Logger,
) -> None:
    """Compile a single CSS file using the Tailwind standalone CLI."""
    bin_path = ensure_tailwind_binary(logger)
    config = template_dir / "tailwind.config.js"
    input_css = template_dir / "tailwind.input.css"
    if not config.exists():
        raise RuntimeError(f"Tailwind config not found: {config}")
    if not input_css.exists():
        raise RuntimeError(f"Tailwind input CSS not found: {input_css}")

    output_css.parent.mkdir(parents=True, exist_ok=True)
    cmd = [
        str(bin_path),
        "--config",
        str(config),
        "--input",
        str(input_css),
        "--output",
        str(output_css),
        "--minify",
    ]
    logger.info(f"Compiling Tailwind CSS → {output_css}")
    # Run from the project root so relative `content` globs in the config
    # resolve against the built site directory.
    cwd = site_dir.parent if site_dir.parent.exists() else Path.cwd()
    env = os.environ.copy()
    env["TAILWIND_SITE_DIR"] = str(site_dir)
    env["TAILWIND_TEMPLATE_DIR"] = str(template_dir)
    result = subprocess.run(  # nosec B603 — cmd is a fixed argv list, no shell, no user input
        cmd,
        cwd=str(cwd),
        env=env,
        capture_output=True,
        text=True,
        check=False,
    )
    if result.returncode != 0:
        raise RuntimeError(
            f"Tailwind CLI failed (exit {result.returncode}):\n{result.stderr}"
        )
    if result.stderr.strip():
        logger.debug(f"Tailwind CLI: {result.stderr.strip()}")


def fetch_mermaid(target_dir: Path, logger: logging.Logger) -> Path:
    """Download Mermaid's UMD bundle into `target_dir` and return its path."""
    cache = _vendor_cache_dir() / "mermaid"
    cache.mkdir(parents=True, exist_ok=True)
    cached = cache / f"mermaid-{MERMAID_VERSION}.min.js"
    if not cached.exists():
        logger.info(f"Downloading Mermaid {MERMAID_VERSION}")
        _download(MERMAID_URL, cached)

    target_dir.mkdir(parents=True, exist_ok=True)
    target = target_dir / "mermaid.min.js"
    shutil.copy2(cached, target)
    return target


_FONT_URL_RE = re.compile(r"url\((https://fonts\.gstatic\.com/[^)]+)\)")


def fetch_fonts(target_dir: Path, logger: logging.Logger) -> Path:
    """Download Google Fonts CSS + WOFF2 files, rewrite URLs to relative paths."""
    cache = _vendor_cache_dir() / "fonts"
    cache.mkdir(parents=True, exist_ok=True)
    css_cache = cache / "fonts.css"
    files_cache = cache / "files"
    files_cache.mkdir(parents=True, exist_ok=True)

    if not css_cache.exists():
        logger.info("Downloading Google Fonts CSS")
        _download(
            GOOGLE_FONTS_CSS_URL, css_cache, headers={"User-Agent": GOOGLE_FONTS_UA}
        )

    css = css_cache.read_text(encoding="utf-8")
    url_map: dict[str, str] = {}
    for url in _FONT_URL_RE.findall(css):
        # Stable filename derived from the gstatic path so duplicates collapse.
        name = url.rsplit("/", 1)[-1]
        local = files_cache / name
        if not local.exists():
            logger.debug(f"Fetching font file: {name}")
            _download(url, local)
        url_map[url] = f"files/{name}"

    rewritten = css
    for url, rel in url_map.items():
        rewritten = rewritten.replace(url, rel)

    target_dir.mkdir(parents=True, exist_ok=True)
    (target_dir / "fonts.css").write_text(rewritten, encoding="utf-8")

    target_files = target_dir / "files"
    target_files.mkdir(parents=True, exist_ok=True)
    for f in files_cache.iterdir():
        if f.is_file():
            shutil.copy2(f, target_files / f.name)
    return target_dir / "fonts.css"


def write_vendor_manifest(target_dir: Path, fonts_count: int) -> None:
    """Record what was vendored — useful for debugging."""
    manifest = {
        "tailwind": TAILWIND_VERSION,
        "mermaid": MERMAID_VERSION,
        "fonts": {"family": ["Inter", "JetBrains Mono"], "files": fonts_count},
    }
    target_dir.mkdir(parents=True, exist_ok=True)
    (target_dir / "manifest.json").write_text(
        json.dumps(manifest, indent=2), encoding="utf-8"
    )
