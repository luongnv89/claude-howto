"""Tests for sync_translations.py — English source collection and status report.

Regression coverage for the source-filter bug (#283): every locale tree and
virtualenv used to be treated as English sources, flooding the report with
~94% false positives.
"""

from __future__ import annotations

import sys
from pathlib import Path, PureWindowsPath

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))

from sync_translations import (
    EXCLUDED_DIRS,
    check_translation_status,
    is_english_source,
)


@pytest.fixture
def repo(tmp_path: Path) -> Path:
    """A minimal repository: English sources, locale trees, and vi/ mirror."""
    # English source documents
    (tmp_path / "README.md").write_text("# Intro\n")
    (tmp_path / "01-slash-commands").mkdir()
    (tmp_path / "01-slash-commands" / "optimize.md").write_text("# Optimize\n")
    # scripts/ is mirrored by vi/scripts, so it must stay a source
    (tmp_path / "scripts").mkdir()
    (tmp_path / "scripts" / "README.md").write_text("# Scripts\n")

    # Other locale trees: translations, never English sources
    for locale in ("ja", "zh", "ko", "uk", "fa"):
        (tmp_path / locale).mkdir()
        (tmp_path / locale / "README.md").write_text(f"# {locale}\n")

    # vi/ mirror: only the root README is translated so far
    (tmp_path / "vi").mkdir()
    (tmp_path / "vi" / "README.md").write_text("# Gioi thieu\n")

    # Environment artifact: never a source
    (tmp_path / ".venv").mkdir()
    (tmp_path / ".venv" / "deps.md").write_text("# deps\n")
    return tmp_path


def test_locale_trees_are_not_sources(repo: Path) -> None:
    sources = {
        f.relative_to(repo).as_posix()
        for f in repo.rglob("*.md")
        if is_english_source(f, repo)
    }
    assert "ja/README.md" not in sources
    assert "zh/README.md" not in sources
    assert "ko/README.md" not in sources
    assert "uk/README.md" not in sources
    assert "fa/README.md" not in sources
    assert "vi/README.md" not in sources


def test_venv_is_not_a_source(repo: Path) -> None:
    sources = {
        f.relative_to(repo).as_posix()
        for f in repo.rglob("*.md")
        if is_english_source(f, repo)
    }
    assert ".venv/deps.md" not in sources


def test_mirrored_trees_stay_sources(repo: Path) -> None:
    sources = {
        f.relative_to(repo).as_posix()
        for f in repo.rglob("*.md")
        if is_english_source(f, repo)
    }
    assert "scripts/README.md" in sources
    assert "01-slash-commands/optimize.md" in sources


def test_exclusion_uses_path_parts_not_substrings(repo: Path) -> None:
    # "vi/" substring matching would also exclude files that merely contain
    # "vi/" inside a longer directory name.
    tricky = repo / "avi" / "README.md"
    tricky.parent.mkdir()
    tricky.write_text("# not a locale\n")
    assert is_english_source(tricky, repo)


def test_windows_style_paths_exclude_locale_dirs() -> None:
    # On Windows, Path stringifies with backslashes; the old "vi/" substring
    # test never matched and vi/ files leaked into the English set.
    root = PureWindowsPath("C:/repo")
    assert not is_english_source(PureWindowsPath("C:/repo/vi/README.md"), root)
    assert not is_english_source(PureWindowsPath("C:/repo/ja/README.md"), root)
    assert is_english_source(PureWindowsPath("C:/repo/README.md"), root)


def test_excluded_dirs_is_os_safe() -> None:
    # Guard against regressions to string-based matching.
    assert "vi" in EXCLUDED_DIRS
    assert ".venv" in EXCLUDED_DIRS


def test_status_report_counts_only_real_gaps(repo: Path) -> None:
    outdated, not_translated = check_translation_status(repo)
    not_translated_files = {str(item["file"]) for item in not_translated}

    # Only the genuinely untranslated English sources appear.
    assert not_translated_files == {
        "01-slash-commands/optimize.md",
        "scripts/README.md",
    }
    assert outdated == []


def test_status_report_detects_outdated(repo: Path) -> None:
    import os

    vi_readme = repo / "vi" / "README.md"
    en_readme = repo / "README.md"
    # Make the vi copy one day older than the English one.
    old = en_readme.stat().st_mtime - 86400
    os.utime(vi_readme, (old, old))

    outdated, not_translated = check_translation_status(repo)
    assert [str(item["file"]) for item in outdated] == ["README.md"]
    assert "README.md" not in {str(item["file"]) for item in not_translated}
