"""The pre-tool-check.sh hook templates block what they promise to block, in every locale copy."""

from __future__ import annotations

import json
import shutil
import subprocess
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parents[2]
COPIES = sorted(ROOT.glob("**/06-hooks/pre-tool-check.sh"))

pytestmark = pytest.mark.skipif(shutil.which("bash") is None, reason="needs bash")


def run_hook(script: Path, command: str, tmp_path: Path) -> int:
    payload = json.dumps({"tool_name": "Bash", "tool_input": {"command": command}})
    result = subprocess.run(
        ["bash", str(script)],
        input=payload,
        capture_output=True,
        text=True,
        env={"PATH": "/usr/bin:/bin", "CLAUDE_PROJECT_DIR": str(tmp_path)},
        check=False,
    )
    return result.returncode


def test_every_locale_copy_is_found():
    assert len(COPIES) >= 3, COPIES


@pytest.mark.parametrize("script", COPIES, ids=lambda p: str(p.relative_to(ROOT)))
@pytest.mark.parametrize(
    "command",
    [
        ":(){:|:&};:",
        ":(){ :|:& };:",
        ":() { : | : & }; :",
    ],
)
def test_fork_bomb_is_blocked_however_it_is_spaced(
    script: Path, command: str, tmp_path: Path
):
    assert run_hook(script, command, tmp_path) == 2


@pytest.mark.parametrize("script", COPIES, ids=lambda p: str(p.relative_to(ROOT)))
@pytest.mark.parametrize("command", ["ls -la", "echo ':)'", "git status"])
def test_ordinary_commands_are_allowed(script: Path, command: str, tmp_path: Path):
    assert run_hook(script, command, tmp_path) == 0
