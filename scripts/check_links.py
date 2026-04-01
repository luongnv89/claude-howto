#!/usr/bin/env python3
"""Check external URLs in Markdown files are reachable."""

import re
import sys
import urllib.error
import urllib.request
from concurrent.futures import ThreadPoolExecutor, as_completed
from pathlib import Path

IGNORE_DIRS = {".venv", "node_modules", ".git", "blog-posts", "openspec", "prompts"}
TIMEOUT = 10
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
}
SKIP_DOMAIN_SUFFIXES = (".example.com", ".example.org", ".internal")

URL_RE = re.compile(r"https?://[a-zA-Z0-9][a-zA-Z0-9\-._~:/?#\[\]@!$&'()*+,;=%]+")


def is_skipped(url: str) -> bool:
    try:
        domain = url.split("/")[2]
    except IndexError:
        return True  # malformed URL
    if any(skip == domain or domain.endswith("." + skip) for skip in SKIP_DOMAINS):
        return True
    return any(domain.endswith(suffix) for suffix in SKIP_DOMAIN_SUFFIXES)


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


def main(strict: bool = False) -> int:
    urls: dict[str, list[str]] = {}  # url -> [file, ...]

    md_files = [
        f
        for f in Path().rglob("*.md")
        if not any(part in IGNORE_DIRS for part in f.parts)
    ]

    for file_path in md_files:
        content = file_path.read_text()
        for url in URL_RE.findall(content):
            urls.setdefault(url, []).append(str(file_path))

    if not urls:
        print("✅ No external URLs found")
        return 0

    errors = []
    with ThreadPoolExecutor(max_workers=10) as pool:
        futures = {pool.submit(check_url, url): url for url in urls}
        for future in as_completed(futures):
            url, ok, reason = future.result()
            if not ok:
                errors.extend(f"{f}: dead link → {url} ({reason})" for f in urls[url])

    if errors:
        print("❌ Dead links found:")
        for e in sorted(errors):
            print(f"  - {e}")
        # In non-strict mode (pre-commit), report but don't block the commit.
        # Set LINK_CHECK_STRICT=1 (as CI does) to enforce failures.
        return 1 if strict else 0

    print(f"✅ All external URLs reachable ({len(urls)} checked)")
    return 0


if __name__ == "__main__":
    import os

    sys.exit(main(strict=os.environ.get("LINK_CHECK_STRICT") == "1"))
