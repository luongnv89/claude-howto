"""Test that dashboard view and grade command produce consistent scores."""

from pathlib import Path

from workshop.platform.database import (
    create_cohort, get_connection, get_scores, get_all_scores,
    register_student, start_session, complete_session, save_score,
    mark_setup_completed,
)
from workshop.scoring.scorer import score_student


def _setup_alice_with_three_passed_sessions(db_path: Path):
    """Simulate Alice having completed S1-S3 with deliverable=100 each."""
    conn = get_connection(db_path)
    create_cohort(conn, "test-cohort", "Test")
    register_student(conn, "alice", "Alice", "a@test.com", "test-cohort")
    mark_setup_completed(conn, "alice")
    for s in [1, 2, 3]:
        start_session(conn, "alice", s)
        complete_session(conn, "alice", s, True,
                         {"checks": [], "total_points": 100, "max_points": 100})
        # complete-session stores per-session: only deliverable filled
        save_score(conn, "alice", s, 0, 0, 100, 0, 20)  # total=20 (weighted)
    return conn


def test_grade_does_not_overwrite_per_session_totals_with_aggregate(tmp_path):
    """After running grade, per-session 'total' columns must remain per-session,
    not be overwritten with the aggregate score across all sessions."""
    db_path = tmp_path / "test.db"
    conn = _setup_alice_with_three_passed_sessions(db_path)

    # Capture per-session totals BEFORE grade
    before = {s["session_number"]: s["total"] for s in get_scores(conn, "alice")}
    assert before == {1: 20, 2: 20, 3: 20}

    # Run grade (heuristic mode, no AI)
    score_student(conn, "alice", project_dir=tmp_path / "no-project",
                  use_ai=False)

    # Per-session totals should still be per-session values, not the aggregate
    after = {s["session_number"]: s["total"] for s in get_scores(conn, "alice")}
    # All three should be the same per-session value (since input is identical)
    assert len(set(after.values())) == 1, (
        f"All three sessions had identical inputs, expected identical per-session "
        f"totals after grade. Got: {after}"
    )
    # And running grade twice should produce identical per-session storage
    score_student(conn, "alice", project_dir=tmp_path / "no-project",
                  use_ai=False)
    after2 = {s["session_number"]: s["total"] for s in get_scores(conn, "alice")}
    assert after == after2, (
        f"Running grade twice produced different per-session totals — "
        f"first: {after}, second: {after2}"
    )
    conn.close()


def test_dashboard_average_matches_grade_continuous_score(tmp_path):
    """The dashboard's avg_score (computed from stored per-session totals)
    should equal the grade command's reported continuous_score."""
    db_path = tmp_path / "test.db"
    conn = _setup_alice_with_three_passed_sessions(db_path)

    grade_result = score_student(conn, "alice",
                                 project_dir=tmp_path / "no-project",
                                 use_ai=False)

    # Dashboard reads from get_all_scores, which AVG()s the stored 'total' column
    dashboard_rows = get_all_scores(conn)
    alice_row = next(r for r in dashboard_rows if r["id"] == "alice")
    dashboard_avg = alice_row["avg_score"]

    # Dashboard avg of per-session totals should match the continuous_score
    assert abs(dashboard_avg - grade_result["continuous_score"]) < 0.5, (
        f"Dashboard avg ({dashboard_avg}) and grade continuous_score "
        f"({grade_result['continuous_score']}) disagree by more than 0.5 pts"
    )
    conn.close()
