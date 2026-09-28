"""Tests for check_links.py — file selection and the reachable-URL cache.

`check_url` is replaced with a stub, so no test touches the network. The stub
treats any URL containing "dead" as unreachable and records every request.
"""

from __future__ import annotations

import json
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))

import check_links


@pytest.fixture
def requested(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> list[str]:
    monkeypatch.chdir(tmp_path)
    calls: list[str] = []

    def fake_check_url(url: str) -> tuple[str, bool, str]:
        calls.append(url)
        ok = "dead" not in url
        return url, ok, "ok" if ok else "HTTP 404"

    monkeypatch.setattr(check_links, "check_url", fake_check_url)
    return calls


def test_reachable_urls_are_cached(tmp_path: Path, requested: list[str]) -> None:
    (tmp_path / "a.md").write_text("See https://good.example.org/page\n")

    assert check_links.main([]) == 0
    assert check_links.main([]) == 0
    assert requested == ["https://good.example.org/page"]


def test_dead_urls_are_not_cached(
    tmp_path: Path, requested: list[str], capsys: pytest.CaptureFixture[str]
) -> None:
    (tmp_path / "a.md").write_text("See https://dead.example.org/page\n")

    assert check_links.main([]) == 0  # non-strict reports but passes
    assert check_links.main([], strict=True) == 1
    assert len(requested) == 2
    assert "dead link → https://dead.example.org/page" in capsys.readouterr().out


def test_strict_mode_ignores_and_keeps_cache(
    tmp_path: Path, requested: list[str]
) -> None:
    (tmp_path / "a.md").write_text("See https://good.example.org/page\n")
    assert check_links.main([]) == 0
    before = check_links.CACHE_FILE.read_text()

    assert check_links.main([], strict=True) == 0
    assert len(requested) == 2
    assert check_links.CACHE_FILE.read_text() == before


def test_expired_entries_are_rechecked_and_dropped(
    tmp_path: Path, requested: list[str]
) -> None:
    (tmp_path / "a.md").write_text("See https://good.example.org/page\n")
    check_links.CACHE_FILE.parent.mkdir()
    old = 0.0  # 1970: far past the TTL
    check_links.CACHE_FILE.write_text(
        json.dumps({"https://good.example.org/page": old, "https://gone.org/x": old})
    )

    assert check_links.main([]) == 0
    assert requested == ["https://good.example.org/page"]
    assert list(json.loads(check_links.CACHE_FILE.read_text())) == [
        "https://good.example.org/page"
    ]


def test_corrupt_cache_is_ignored(tmp_path: Path, requested: list[str]) -> None:
    (tmp_path / "a.md").write_text("See https://good.example.org/page\n")
    check_links.CACHE_FILE.parent.mkdir()
    check_links.CACHE_FILE.write_text("{not json")

    assert check_links.main([]) == 0
    assert requested == ["https://good.example.org/page"]


def test_only_given_files_are_checked(tmp_path: Path, requested: list[str]) -> None:
    (tmp_path / "a.md").write_text("See https://a.example.org/\n")
    (tmp_path / "b.md").write_text("See https://b.example.org/\n")

    assert check_links.main(["a.md"]) == 0
    assert requested == ["https://a.example.org/"]


def test_non_markdown_args_fall_back_to_full_scan(
    tmp_path: Path, requested: list[str]
) -> None:
    (tmp_path / "a.md").write_text("See https://a.example.org/\n")

    assert check_links.main(["--lang", "vi"]) == 0
    assert requested == ["https://a.example.org/"]
