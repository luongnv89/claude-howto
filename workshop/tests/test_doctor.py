"""Tests for the bootcamp doctor preflight."""

from workshop.platform.doctor import (
    Check, run_all_checks, check_python_version,
    check_command_available,
)


def test_check_dataclass_str_renders_pass_and_fail():
    p = Check(name="x", passed=True, message="ok")
    f = Check(name="y", passed=False, message="missing", fix="install y")
    assert "[+]" in str(p) and "PASS" in str(p)
    assert "[-]" in str(f) and "FAIL" in str(f)
    assert "install y" in str(f)


def test_check_python_version_passes_on_310_plus():
    result = check_python_version(min_major=3, min_minor=10)
    assert result.passed is True
    assert "3." in result.message


def test_check_python_version_fails_on_too_old():
    # Force a too-high requirement
    result = check_python_version(min_major=99, min_minor=0)
    assert result.passed is False
    assert "99" in result.message


def test_check_command_available_finds_python():
    import sys
    # `python3` may or may not be on PATH; test with sys.executable instead
    result = check_command_available(sys.executable)
    assert result.passed is True


def test_check_command_available_fails_for_nonsense():
    result = check_command_available("definitely-not-a-command-xyz123")
    assert result.passed is False
    assert "not found" in result.message.lower()


def test_run_all_checks_returns_list_of_checks():
    results = run_all_checks()
    assert isinstance(results, list)
    assert all(isinstance(c, Check) for c in results)
    assert len(results) >= 4  # python, claude, node, git at minimum
