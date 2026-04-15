"""Tests that verify the demo.sh fixtures produce the intended scenarios."""

from pathlib import Path

from workshop.gates.gate_runner import run_gate
from workshop.platform.database import (
    create_cohort, get_connection, get_session_progress,
    register_student, start_session, complete_session, save_score,
)


def _make_bob_fixture(tmp_path: Path) -> Path:
    """Replicate Bob's fixture from demo.sh exactly as it should be after fix."""
    project = tmp_path / "qa-demo-bob"
    (project / "server").mkdir(parents=True)
    (project / "client" / "src").mkdir(parents=True)
    (project / "package.json").write_text(
        '{"name":"qa-command-center","dependencies":'
        '{"express":"^4.18","react":"^18"}}'
    )
    (project / "server" / "index.js").write_text("const express = require('express');")
    (project / "client" / "src" / "App.jsx").write_text(
        "export default function App() { return <h1>Hello</h1>; }"
    )
    # NOTE: deliberately no .claude/skills/ — Bob is the struggling student
    return project


def test_bob_fixture_fails_s1_critical_check(tmp_path):
    """Bob's fixture must fail at least one critical S1 check so auto-unlock can fire."""
    project = _make_bob_fixture(tmp_path)
    results = run_gate(1, project)

    critical_failures = [
        r for r in results
        if not r["passed"] and r.get("critical", True)
    ]
    assert len(critical_failures) >= 1, (
        f"Bob must fail at least one critical S1 check, but all critical checks "
        f"passed. Results: {results}"
    )
    # Specifically the skills checks should be among the failures
    failure_messages = " ".join(r["message"] for r in critical_failures).lower()
    assert "skill" in failure_messages, (
        f"Expected a skills-related critical failure, got: {failure_messages}"
    )


def test_alice_progression_records_each_session(tmp_path):
    """After completing S1, S2, S3, all three should appear in session_progress
    with gate_passed=True. This catches the demo's missing start-session calls."""
    db_path = tmp_path / "test.db"
    conn = get_connection(db_path)
    create_cohort(conn, "test-cohort", "Test Cohort")
    register_student(conn, "alice", "Alice Test", "a@test.com", "test-cohort")

    # Simulate proper flow: start before complete for EACH session
    for s in [1, 2, 3]:
        start_session(conn, "alice", s)
        complete_session(conn, "alice", s, gate_passed=True,
                         gate_details={"checks": [], "total_points": 100,
                                       "max_points": 100})
        save_score(conn, "alice", s, 0, 0, 100, 0, 100)

    progress = get_session_progress(conn, "alice")
    completed = [p for p in progress if p["gate_passed"]]
    assert len(completed) == 3, (
        f"Expected 3 completed sessions, got {len(completed)}: "
        f"{[(p['session_number'], bool(p['gate_passed'])) for p in progress]}"
    )
    conn.close()
