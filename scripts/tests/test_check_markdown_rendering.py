"""Tests for check_markdown_rendering.py — positive + negative per rule."""

from __future__ import annotations

import sys
from pathlib import Path

import pytest

sys.path.insert(0, str(Path(__file__).parent.parent))

import check_markdown_rendering as cmr


@pytest.fixture
def repo(tmp_path: Path, monkeypatch: pytest.MonkeyPatch) -> Path:
    monkeypatch.chdir(tmp_path)
    return tmp_path


# ----- rule_backtick_in_inline_code -----------------------------------------


def test_backtick_in_inline_code_flagged(repo: Path) -> None:
    (repo / "README.md").write_text("Use `!`command`` for shell substitution.\n")
    errors = cmr.rule_backtick_in_inline_code(
        Path("README.md"), (repo / "README.md").read_text()
    )
    assert any("backtick-in-inline-code" in e for e in errors)


def test_double_backtick_idiom_passes(repo: Path) -> None:
    (repo / "README.md").write_text("Use `` `!command` `` for shell substitution.\n")
    errors = cmr.rule_backtick_in_inline_code(
        Path("README.md"), (repo / "README.md").read_text()
    )
    assert errors == []


def test_backtick_inside_fence_ignored(repo: Path) -> None:
    content = "Before\n\n```\nfoo `!`command`` bar\n```\n\nAfter\n"
    (repo / "README.md").write_text(content)
    errors = cmr.rule_backtick_in_inline_code(Path("README.md"), content)
    assert errors == []


def test_backtick_inside_blockquote_fence_ignored(repo: Path) -> None:
    content = (
        "> note\n"
        ">\n"
        "> ```json\n"
        '> { "key": "value with `inner` backtick" }\n'
        "> ```\n"
    )
    (repo / "README.md").write_text(content)
    errors = cmr.rule_backtick_in_inline_code(Path("README.md"), content)
    assert errors == []


def test_backtick_line_number_reported(repo: Path) -> None:
    content = "line 1\nline 2 with `a`b` content\nline 3\n"
    errors = cmr.rule_backtick_in_inline_code(Path("README.md"), content)
    assert errors and ":2:" in errors[0]


# ----- rule_unescaped_pipe_in_table -----------------------------------------


def test_unescaped_pipe_in_table_flagged(repo: Path) -> None:
    content = "| col1 | col2 |\n" "|------|------|\n" "| a | b | c |\n"
    errors = cmr.rule_unescaped_pipe_in_table(Path("README.md"), content)
    assert any("unescaped-pipe-in-table" in e for e in errors)


def test_escaped_pipe_passes(repo: Path) -> None:
    content = "| col1 | col2 |\n" "|------|------|\n" "| [color\\|default] | b |\n"
    errors = cmr.rule_unescaped_pipe_in_table(Path("README.md"), content)
    assert errors == []


def test_pipe_inside_inline_code_in_cell_passes(repo: Path) -> None:
    content = "| col1 | col2 |\n" "|------|------|\n" "| `a \\| b` | text |\n"
    errors = cmr.rule_unescaped_pipe_in_table(Path("README.md"), content)
    assert errors == []


def test_pipe_outside_table_ignored(repo: Path) -> None:
    content = "This is | a sentence with a pipe in prose.\n"
    errors = cmr.rule_unescaped_pipe_in_table(Path("README.md"), content)
    assert errors == []


# ----- rule_stray_argument_placeholder --------------------------------------


def test_stray_arguments_in_prose_flagged(repo: Path) -> None:
    content = "Run the command and pass $ARGUMENTS to the script.\n"
    errors = cmr.rule_stray_argument_placeholder(Path("README.md"), content)
    assert any("stray-argument-placeholder" in e for e in errors)


def test_arguments_in_inline_code_passes(repo: Path) -> None:
    content = "Pass `$ARGUMENTS` and `$0` to the script.\n"
    errors = cmr.rule_stray_argument_placeholder(Path("README.md"), content)
    assert errors == []


def test_arguments_in_fenced_code_passes(repo: Path) -> None:
    content = "Example:\n\n```bash\nfix-issue $ARGUMENTS\n```\n"
    errors = cmr.rule_stray_argument_placeholder(Path("README.md"), content)
    assert errors == []


def test_dollar_digit_not_flagged(repo: Path) -> None:
    # `$N` is intentionally not flagged — see rule docstring.
    content = "The script reads $0 from the prompt.\n"
    errors = cmr.rule_stray_argument_placeholder(Path("README.md"), content)
    assert errors == []


def test_currency_dollar_amounts_pass(repo: Path) -> None:
    cases = [
        "Pay $5 today.",
        "Costs $5/month.",
        "Total: $1,000 plan.",
        "Refund: $5.99 fee.",
    ]
    for case in cases:
        errors = cmr.rule_stray_argument_placeholder(Path("README.md"), case)
        assert errors == [], f"false-positive on prose currency: {case!r}"


# ----- rule_unmatched_fence -------------------------------------------------


def test_matched_fences_pass() -> None:
    content = "```\ncode\n```\n\n```python\nmore\n```\n"
    errors = cmr.rule_unmatched_fence(Path("README.md"), content)
    assert errors == []


def test_unmatched_fence_flagged() -> None:
    content = "```bash\nthis fence never closes\n"
    errors = cmr.rule_unmatched_fence(Path("README.md"), content)
    assert any("unmatched-fence" in e for e in errors)


# ----- main() integration ---------------------------------------------------


def test_main_clean_repo_returns_zero(
    repo: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    (repo / "README.md").write_text("# Doc\n\nClean content.\n")
    assert cmr.main() == 0
    assert "Markdown rendering clean" in capsys.readouterr().out


def test_main_dirty_repo_returns_one(
    repo: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    (repo / "README.md").write_text("Bad: `a`b` here.\n")
    assert cmr.main() == 1
    assert "Markdown rendering errors" in capsys.readouterr().out


def test_main_ignores_excluded_dirs(
    repo: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    (repo / "README.md").write_text("# Clean\n")
    bad_dir = repo / ".venv"
    bad_dir.mkdir()
    (bad_dir / "README.md").write_text("Bad: `a`b` here.\n")
    assert cmr.main() == 0
    assert "Markdown rendering clean" in capsys.readouterr().out


def test_main_scans_translation_dirs(
    repo: Path, capsys: pytest.CaptureFixture[str]
) -> None:
    (repo / "README.md").write_text("# Clean\n")
    for lang in ("ja", "uk", "vi", "zh"):
        d = repo / lang
        d.mkdir()
        (d / "README.md").write_text("Bad: `a`b` here.\n")
    assert cmr.main() == 1
    out = capsys.readouterr().out
    for lang in ("ja", "uk", "vi", "zh"):
        assert lang in out
