"""Preflight checks for the bootcamp environment.

Run via `./bootcamp doctor`. Returns a list of Check results that are
displayed as a status table. Designed to be student- and instructor-friendly:
each FAIL includes a 'fix' message with concrete remediation.
"""

import shutil
import subprocess
import sys
from dataclasses import dataclass


@dataclass
class Check:
    name: str
    passed: bool
    message: str
    fix: str | None = None

    def __str__(self) -> str:
        icon = "[+]" if self.passed else "[-]"
        status = "PASS" if self.passed else "FAIL"
        out = f"  {icon} {status}: {self.name} -- {self.message}"
        if not self.passed and self.fix:
            out += f"\n      Fix: {self.fix}"
        return out


def check_python_version(min_major: int = 3, min_minor: int = 10) -> Check:
    actual = sys.version_info
    ok = (actual.major, actual.minor) >= (min_major, min_minor)
    msg = f"Python {actual.major}.{actual.minor}.{actual.micro} (require >={min_major}.{min_minor})"
    fix = ("Install a newer Python via Homebrew: brew install python@3.12\n"
           "      Or via uv: pip install uv && uv python install 3.12")
    return Check("Python version", ok, msg, fix if not ok else None)


def check_command_available(cmd: str, version_arg: str = "--version") -> Check:
    path = shutil.which(cmd)
    if not path:
        return Check(
            f"`{cmd}` on PATH",
            False,
            f"`{cmd}` not found on PATH",
            f"Install {cmd} (see docs)",
        )
    try:
        v = subprocess.run(
            [path, version_arg], capture_output=True, text=True, timeout=5,
        )
        version = (v.stdout or v.stderr).strip().splitlines()[0] if (v.stdout or v.stderr) else "(no version)"
    except Exception:
        version = "(unknown version)"
    return Check(f"`{cmd}` on PATH", True, f"{path} -- {version}")


def check_claude_cli() -> Check:
    return check_command_available("claude")


def check_node() -> Check:
    return check_command_available("node")


def check_git_configured() -> Check:
    name = subprocess.run(
        ["git", "config", "--global", "user.name"],
        capture_output=True, text=True,
    ).stdout.strip()
    if name:
        return Check("Git user.name configured", True, name)
    return Check(
        "Git user.name configured",
        False,
        "git config --global user.name is empty",
        "Run: git config --global user.name 'Your Name'",
    )


def check_bootcamp_home_writable() -> Check:
    from .config import BOOTCAMP_HOME
    try:
        BOOTCAMP_HOME.mkdir(parents=True, exist_ok=True)
        probe = BOOTCAMP_HOME / ".doctor-probe"
        probe.write_text("ok")
        probe.unlink()
        return Check(
            "Bootcamp home writable",
            True,
            f"{BOOTCAMP_HOME} is writable",
        )
    except Exception as e:
        return Check(
            "Bootcamp home writable",
            False,
            f"{BOOTCAMP_HOME} not writable: {e}",
            f"Check permissions on {BOOTCAMP_HOME.parent}",
        )


def run_all_checks() -> list[Check]:
    return [
        check_python_version(),
        check_claude_cli(),
        check_node(),
        check_git_configured(),
        check_bootcamp_home_writable(),
    ]


def doctor_main() -> int:
    """Print the status table; return 0 if all PASS, 1 otherwise."""
    print("\n  Bootcamp doctor — environment preflight")
    print(f"  {'=' * 60}\n")
    results = run_all_checks()
    for r in results:
        print(r)
    failed = [r for r in results if not r.passed]
    print(f"\n  {'=' * 60}")
    if failed:
        print(f"  {len(failed)} check(s) FAILED. Fix the issues above before continuing.\n")
        return 1
    print(f"  All {len(results)} checks PASSED.\n")
    return 0
