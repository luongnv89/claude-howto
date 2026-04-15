"""Test the bootcamp CLI entry script's Python version guard."""

import subprocess
import sys
from pathlib import Path

BOOTCAMP = Path(__file__).resolve().parent.parent / "bootcamp"


def test_bootcamp_entry_runs_under_current_python():
    """The bootcamp script should execute and show help on a supported Python."""
    result = subprocess.run(
        [sys.executable, str(BOOTCAMP), "--help"],
        capture_output=True, text=True, timeout=10,
    )
    # Help shown OR exit 1 (no command) — both acceptable; key is no Python error
    assert "AI Bootcamp Platform" in (result.stdout + result.stderr), (
        f"Expected help text. stdout={result.stdout!r} stderr={result.stderr!r}"
    )


def test_bootcamp_entry_has_version_guard():
    """The bootcamp script must check Python version before importing CLI code."""
    content = BOOTCAMP.read_text()
    assert "sys.version_info" in content, (
        "Expected sys.version_info check at top of bootcamp script "
        "(before imports of workshop modules)"
    )
    # Guard must come before importing workshop.platform.cli (which uses 3.10+ syntax)
    guard_idx = content.find("sys.version_info")
    import_idx = content.find("from workshop.platform.cli")
    assert guard_idx < import_idx, (
        "Version guard must appear BEFORE 'from workshop.platform.cli' import"
    )
