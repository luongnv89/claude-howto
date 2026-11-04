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


# U+200C ZERO WIDTH NON-JOINER: Persian uses it inside words, and GitHub keeps
# it in heading ids (e.g. the rendered fa/STYLE_GUIDE.md in PR #208). Spelled as
# escapes so editors can't strip them silently.
ZWNJ = "\u200c"
ZWJ = "\u200d"
PERSIAN_HEADING = f"نام{ZWNJ}گذاری فایل و پوشه"
PERSIAN_ANCHOR = f"نام{ZWNJ}گذاری-فایل-و-پوشه"


def test_heading_anchor_keeps_zero_width_non_joiner() -> None:
    assert check_cross_references.heading_to_anchor(PERSIAN_HEADING) == PERSIAN_ANCHOR


def test_heading_anchor_still_strips_em_dash_and_zero_width_joiner() -> None:
    assert (
        check_cross_references.heading_to_anchor("[v2.1.245] — 2026-08-25")
        == "v21245--2026-08-25"
    )
    assert check_cross_references.heading_to_anchor(f"A{ZWJ}B test") == "ab-test"
    # U+FE0F is a combining mark, but it sits in the emoji ranges stripped
    # before the mark check, so emoji-prefixed ids are unchanged.
    assert (
        check_cross_references.heading_to_anchor("Rocket \u2764\ufe0f launch")
        == "rocket--launch"
    )


# U+0654 ARABIC HAMZA ABOVE is a combining mark (category Mn): GitHub keeps it
# in heading ids, but Python's \w does not match it. Spelled as an escape so
# editors can't normalize it away.
HAMZA_ABOVE = "\u0654"
ARABIC_HEADING = f"مجموعه{HAMZA_ABOVE} استاندارد ایموجی"
ARABIC_ANCHOR = f"مجموعه{HAMZA_ABOVE}-استاندارد-ایموجی"


def test_heading_anchor_keeps_combining_marks() -> None:
    assert check_cross_references.heading_to_anchor(ARABIC_HEADING) == ARABIC_ANCHOR


@pytest.mark.parametrize(
    ("heading", "anchor"),
    [
        # Decomposed Latin: "cafe" + U+0301 COMBINING ACUTE ACCENT.
        ("cafe\u0301", "cafe\u0301"),
        # Arabic harakat (U+064B-U+0652) and other marks stay put too.
        ("مُقَدِّمة", "مُقَدِّمة"),
        # Devanagari vowel signs (Mc) and virama (Mn).
        ("हिन्दी", "हिन्दी"),
    ],
)
def test_heading_anchor_keeps_other_combining_marks(heading: str, anchor: str) -> None:
    assert check_cross_references.heading_to_anchor(heading) == anchor


@pytest.mark.parametrize(
    ("heading", "anchor"),
    [
        ("Hướng dẫn bắt đầu nhanh", "hướng-dẫn-bắt-đầu-nhanh"),
        ("快速入门 (Quick Start)", "快速入门-quick-start"),
        ("Швидкий старт: встановлення", "швидкий-старт-встановлення"),
        ("クイックスタート — 概要", "クイックスタート--概要"),
    ],
)
def test_heading_anchor_unchanged_for_existing_locales(
    heading: str, anchor: str
) -> None:
    assert check_cross_references.heading_to_anchor(heading) == anchor


def test_in_page_link_keeping_zwnj_passes(
    repo: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    (repo / "README.md").write_text(
        f"# {PERSIAN_HEADING}\n\n[link](#{PERSIAN_ANCHOR})\n", encoding="utf-8"
    )

    assert check_cross_references.main() == 0
    assert "broken anchor" not in capsys.readouterr().out


def test_in_page_link_missing_zwnj_is_reported(
    repo: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    anchor_without_zwnj = PERSIAN_ANCHOR.replace(ZWNJ, "")
    (repo / "README.md").write_text(
        f"# {PERSIAN_HEADING}\n\n[link](#{anchor_without_zwnj})\n", encoding="utf-8"
    )

    assert check_cross_references.main() == 1
    assert "broken anchor" in capsys.readouterr().out


def test_in_page_link_keeping_combining_marks_passes(
    repo: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    (repo / "README.md").write_text(
        f"# {ARABIC_HEADING}\n\n[link](#{ARABIC_ANCHOR})\n", encoding="utf-8"
    )

    assert check_cross_references.main() == 0
    assert "broken anchor" not in capsys.readouterr().out


def test_in_page_link_missing_combining_mark_is_reported(
    repo: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    anchor_without_mark = ARABIC_ANCHOR.replace(HAMZA_ABOVE, "")
    (repo / "README.md").write_text(
        f"# {ARABIC_HEADING}\n\n[link](#{anchor_without_mark})\n", encoding="utf-8"
    )

    assert check_cross_references.main() == 1
    assert "broken anchor" in capsys.readouterr().out
