"""Tests for check_mermaid.py — file selection, dedup, caching, error reporting.

A fake `mmdc` shell script stands in for the real CLI: it fails on any
diagram containing the word BROKEN and logs every render call.
"""

from __future__ import annotations

import os
import stat
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))

import check_mermaid

FAKE_MMDC = """#!/bin/sh
if [ "$1" = "--version" ]; then echo "11.0.0"; exit 0; fi
echo render >> "$MMDC_LOG"
if grep -q BROKEN "$2"; then echo "Parse error" >&2; exit 1; fi
exit 0
"""


@pytest.fixture
def repo(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    bin_dir = tmp_path / "bin"
    bin_dir.mkdir()
    mmdc = bin_dir / "mmdc"
    mmdc.write_text(FAKE_MMDC)
    mmdc.chmod(mmdc.stat().st_mode | stat.S_IEXEC)

    work = tmp_path / "work"
    work.mkdir()
    monkeypatch.chdir(work)
    monkeypatch.setenv("PATH", f"{bin_dir}{os.pathsep}{os.environ['PATH']}")
    monkeypatch.setenv("MMDC_LOG", str(tmp_path / "mmdc.log"))
    return work


def render_count(repo: Path) -> int:
    log = repo.parent / "mmdc.log"
    return len(log.read_text().splitlines()) if log.exists() else 0


def diagram(body: str) -> str:
    return f"# Doc\n\n```mermaid\n{body}\n```\n"


def test_identical_diagrams_render_once(repo: Path) -> None:
    (repo / "a.md").write_text(diagram("graph TD; A-->B"))
    (repo / "b.md").write_text(diagram("graph TD; A-->B"))

    assert check_mermaid.main([]) == 0
    assert render_count(repo) == 1


def test_passing_diagrams_are_cached(repo: Path) -> None:
    (repo / "a.md").write_text(diagram("graph TD; A-->B"))

    assert check_mermaid.main([]) == 0
    assert check_mermaid.main([]) == 0
    assert render_count(repo) == 1


def test_failing_diagrams_are_not_cached_and_report_every_location(
    repo: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    (repo / "a.md").write_text(diagram("graph TD; BROKEN"))
    (repo / "b.md").write_text(diagram("graph TD; BROKEN"))

    assert check_mermaid.main([]) == 1
    assert check_mermaid.main([]) == 1
    assert render_count(repo) == 2
    out = capsys.readouterr().out
    assert "a.md (block 1): Parse error" in out
    assert "b.md (block 1): Parse error" in out


def test_only_given_files_are_checked(repo: Path) -> None:
    (repo / "good.md").write_text(diagram("graph TD; A-->B"))
    (repo / "bad.md").write_text(diagram("graph TD; BROKEN"))

    assert check_mermaid.main(["good.md"]) == 0
    assert check_mermaid.main(["bad.md"]) == 1


def test_ignored_dirs_and_non_markdown_args_are_skipped(repo: Path) -> None:
    (repo / "node_modules").mkdir()
    (repo / "node_modules" / "x.md").write_text(diagram("graph TD; BROKEN"))
    (repo / "notes.txt").write_text(diagram("graph TD; BROKEN"))

    assert check_mermaid.main([]) == 0
    assert check_mermaid.main(["node_modules/x.md", "notes.txt"]) == 0
    assert render_count(repo) == 0


def test_skips_when_mmdc_missing(
    repo: Path, monkeypatch: pytest.MonkeyPatch, capsys: pytest.CaptureFixture[str]
) -> None:
    monkeypatch.setenv("PATH", "")
    (repo / "a.md").write_text(diagram("graph TD; BROKEN"))

    assert check_mermaid.main([]) == 0
    assert "mmdc not found" in capsys.readouterr().out


def test_no_diagrams_skips_mmdc(repo: Path, capsys: pytest.CaptureFixture[str]) -> None:
    (repo / "a.md").write_text("# No diagrams here\n")

    assert check_mermaid.main(["a.md"]) == 0
    assert render_count(repo) == 0
    assert "No Mermaid diagrams" in capsys.readouterr().out
    assert not (repo.parent / "mmdc.log").exists()


def test_full_scan_prunes_stale_markers(repo: Path) -> None:
    (repo / "a.md").write_text(diagram("graph TD; A-->B"))
    assert check_mermaid.main([]) == 0
    old_markers = set(check_mermaid.CACHE_DIR.iterdir())

    (repo / "a.md").write_text(diagram("graph TD; A-->C"))
    assert check_mermaid.main(["a.md"]) == 0
    assert old_markers < set(check_mermaid.CACHE_DIR.iterdir())  # file mode keeps them

    assert check_mermaid.main([]) == 0
    remaining = set(check_mermaid.CACHE_DIR.iterdir())
    assert len(remaining) == 1
    assert not old_markers & remaining
