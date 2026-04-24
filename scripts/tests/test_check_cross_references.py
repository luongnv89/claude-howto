"""Tests for check_cross_references.py — focus on repo-root boundary."""

from __future__ import annotations

import os
import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))

import check_cross_references


@pytest.fixture
def repo(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    monkeypatch.chdir(tmp_path)
    return tmp_path


def test_links_escaping_repo_root_are_skipped(
    repo: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    outside = repo.parent / "outside.md"
    outside.write_text("# Outside")

    rel = os.path.relpath(outside, repo)
    (repo / "README.md").write_text(f"# Doc\n\n[escape]({rel})\n")

    assert check_cross_references.main() == 0
    assert "broken cross-reference" not in capsys.readouterr().out


def test_broken_in_repo_link_is_reported(
    repo: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    (repo / "README.md").write_text("# Doc\n\n[missing](does-not-exist.md)\n")

    assert check_cross_references.main() == 1
    assert "broken cross-reference" in capsys.readouterr().out


def test_valid_in_repo_link_passes(
    repo: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    (repo / "other.md").write_text("# Other")
    (repo / "README.md").write_text("# Doc\n\n[ok](other.md)\n")

    assert check_cross_references.main() == 0
    assert "All cross-references valid" in capsys.readouterr().out


def test_numbered_lesson_dir_missing_readme_is_reported(
    repo: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    (repo / "README.md").write_text("# Doc")
    (repo / "01-intro").mkdir()

    assert check_cross_references.main() == 1
    assert "01-intro: missing README.md" in capsys.readouterr().out
