#!/usr/bin/env python3
"""Check external URLs in Markdown files are reachable.

Usage:
    python scripts/check_links.py              # every Markdown file in the repo
    python scripts/check_links.py a.md b.md    # only these files (pre-commit)

Arguments that are not `.md` paths are ignored; with no `.md` paths the whole
repo is scanned. Set LINK_CHECK_STRICT=1 (as CI does) to fail on dead links.

Outside strict mode, URLs that answered within the last 24 hours are read from
`.cache/links-ok.json` instead of being requested again. Strict mode always
checks every URL. Delete the file to force a full re-check.
"""

from __future__ import annotations

import json
import os
import re
import sys
import tempfile
import time
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
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
TIMEOUT = 10
CACHE_FILE = Path(".cache/links-ok.json")
CACHE_TTL = 24 * 3600
# Domains/patterns to skip: badges, placeholders, and bot-blocking hosts
SKIP_DOMAINS = {
    "shields.io",
    "img.shields.io",
    "star-history.com",
    "api.star-history.com",
    "example.com",
    "localhost",
    "127.0.0.1",
    "my-webhook.example.com",
    "git.internal",
    # Wikipedia blocks HEAD requests — GET also unreliable in CI without network
    "en.wikipedia.org",
    "wikipedia.org",
    # GitHub API requires auth — unauthenticated requests return 404 for protected endpoints
    "api.github.com",
    # Claude Code native-binary download host — directory listing returns 404, artifacts are
    # fetched programmatically by the installer via the full filename path
    "downloads.claude.ai",
}
SKIP_DOMAIN_SUFFIXES = (".example.com", ".example.org", ".internal")
# Placeholder/template URLs that are intentionally non-resolvable
SKIP_URL_PATTERNS = {
    "github.com/org/",
    "github.com/user/",
    "github.com/your-org/",
    "docs.example.com",
}

URL_RE = re.compile(r"https?://[a-zA-Z0-9][a-zA-Z0-9\-._~:/?#\[\]@!$&'()*+,;=%]+")


def iter_md_files(args: list[str]) -> list[Path]:
    paths = [Path(a) for a in args if a.endswith(".md")]
    candidates = paths or list(Path().rglob("*.md"))
    return [
        f
        for f in candidates
        if f.is_file() and not any(part in IGNORE_DIRS for part in f.parts)
    ]


def collect_urls(md_files: list[Path]) -> dict[str, list[str]]:
    """Map each URL to the files that contain it."""
    urls: dict[str, list[str]] = {}
    for file_path in md_files:
        content = file_path.read_text()
        for raw_url in URL_RE.findall(content):
            # Strip trailing Markdown/punctuation characters the regex may over-capture
            # from link syntax like [text](https://url/) or **https://url)**
            clean_url = raw_url.rstrip(")>*_`':.,;").split("#")[0]
            # Skip bare-hostname partials. URL_RE stops at backslashes, so a
            # regex string inside a JSON config example like
            # "footerLinksRegexes": ["https://jira\\.example\\.com/.*"] is
            # captured as just "https://jira" — a hostname with no dot that is
            # not a resolvable URL but a truncated pattern. Real public URLs
            # have a dotted host; localhost-style single-label hosts are in
            # SKIP_DOMAINS already, so dropping dotless hosts here loses no
            # genuine link coverage.
            host = clean_url.split("/", 3)[2] if "://" in clean_url else ""
            if host and "." not in host.split(":", 1)[0]:
                continue
            urls.setdefault(clean_url, []).append(str(file_path))
    return urls


def load_cache(now: float) -> dict[str, float]:
    """Return {url: last-ok timestamp} for entries younger than CACHE_TTL."""
    try:
        data = json.loads(CACHE_FILE.read_text())
    except (OSError, ValueError):
        return {}
    if not isinstance(data, dict):
        return {}
    return {
        url: ts
        for url, ts in data.items()
        if isinstance(ts, int | float) and now - ts < CACHE_TTL
    }


def save_cache(cache: dict[str, float]) -> None:
    """Write the cache atomically so an interrupted run can't corrupt it."""
    CACHE_FILE.parent.mkdir(parents=True, exist_ok=True)
    with tempfile.NamedTemporaryFile(
        "w", dir=CACHE_FILE.parent, suffix=".tmp", delete=False
    ) as tmp:
        json.dump(cache, tmp, indent=0, sort_keys=True)
    Path(tmp.name).replace(CACHE_FILE)


def is_skipped(url: str) -> bool:
    try:
        domain = url.split("/", 3)[2].split(":", 1)[0]
    except IndexError:
        return True  # malformed URL
    if any(skip == domain or domain.endswith("." + skip) for skip in SKIP_DOMAINS):
        return True
    if any(domain.endswith(suffix) for suffix in SKIP_DOMAIN_SUFFIXES):
        return True
    return any(pattern in url for pattern in SKIP_URL_PATTERNS)


def check_url(url: str) -> tuple[str, bool, str]:
    if is_skipped(url):
        return url, True, "skipped"
    try:
        req = urllib.request.Request(
            url, headers={"User-Agent": "Mozilla/5.0"}, method="HEAD"
        )
        with urllib.request.urlopen(req, timeout=TIMEOUT):  # nosec B310
            return url, True, "ok"
    except urllib.error.HTTPError as e:
        # 403/429 often means the server is up but blocks bots — treat as ok
        if e.code in (401, 403, 405, 429):
            return url, True, f"http {e.code} (ignored)"
        return url, False, f"HTTP {e.code}"
    except Exception as e:
        return url, False, str(e)


def main(args: list[str], strict: bool = False) -> int:
    urls = collect_urls(iter_md_files(args))

    if not urls:
        print("✅ No external URLs found")
        return 0

    now = time.time()
    cache = {} if strict else load_cache(now)
    to_check = [url for url in urls if url not in cache]

    errors: list[str] = []
    with ThreadPoolExecutor(max_workers=10) as pool:
        futures = [pool.submit(check_url, url) for url in to_check]
        for future in as_completed(futures):
            url, ok, reason = future.result()
            if ok:
                cache[url] = now
            else:
                errors.extend(f"{f}: dead link → {url} ({reason})" for f in urls[url])

    if not strict:
        save_cache(cache)

    if errors:
        print("❌ Dead links found:")
        for e in sorted(errors):
            print(f"  - {e}")
        # In non-strict mode (pre-commit), report but don't block the commit.
        # Set LINK_CHECK_STRICT=1 (as CI does) to enforce failures.
        return 1 if strict else 0

    cached = len(urls) - len(to_check)
    print(
        f"✅ All external URLs reachable ({len(urls)} checked: "
        f"{len(to_check)} requested, {cached} cached)"
    )
    return 0


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:], strict=os.environ.get("LINK_CHECK_STRICT") == "1"))
