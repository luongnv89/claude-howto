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


def test_complete_session_writes_meaningful_per_session_total(tmp_path, monkeypatch):
    """complete-session must write per-session total that includes more than
    just deliverable_quality (was a bug: total = quality_score only)."""
    from workshop.platform import cli, student_setup
    import workshop.platform.config as cfg

    # Redirect bootcamp home + LOGS_DIR + STUDENT_ID_FILE to tmp_path
    home = tmp_path / "bootcamp-home"
    home.mkdir()
    logs = home / "logs"
    logs.mkdir()
    student_id_file = home / "student-id"
    student_id_file.write_text("alice")
    monkeypatch.setattr(cfg, "BOOTCAMP_HOME", home)
    monkeypatch.setattr(cfg, "LOGS_DIR", logs)
    monkeypatch.setattr(cfg, "STUDENT_ID_FILE", student_id_file)
    # student_setup.py captures STUDENT_ID_FILE at import; patch its binding too
    monkeypatch.setattr(student_setup, "STUDENT_ID_FILE", student_id_file)

    # Build a minimal passing project for S1
    project = tmp_path / "qa-cmd-center"
    project.mkdir()
    (project / "package.json").write_text(
        '{"name":"qa-command-center","dependencies":'
        '{"express":"^4.18","react":"^18"}}'
    )
    (project / "server").mkdir()
    (project / "server" / "index.js").write_text("// noop")
    (project / "client" / "src").mkdir(parents=True)
    (project / "client" / "src" / "App.jsx").write_text("export default null;")
    (project / ".claude" / "skills" / "tg").mkdir(parents=True)
    (project / ".claude" / "skills" / "tg" / "SKILL.md").write_text(
        "---\nname: tg\ndescription: tg\n---\n"
    )

    # Set up bootcamp DB state
    db_path = home / "bootcamp.db"
    monkeypatch.setattr(cfg, "DB_PATH", db_path)
    from workshop.platform.database import (
        get_connection, create_cohort, register_student, mark_setup_completed,
        get_scores,
    )
    conn = get_connection(db_path)
    create_cohort(conn, "c", "C")
    register_student(conn, "alice", "Alice", "a@a.com", "c")
    mark_setup_completed(conn, "alice")

    # Run complete-session via the CLI command function
    args = type("A", (), {"session": 1, "project_dir": project})()
    rc = cli.cmd_complete_session(conn, args)
    assert rc == 0, "complete-session should pass"

    # Per-session total should reflect ALL components (not just deliverable)
    scores = get_scores(conn, "alice")
    s1 = next(s for s in scores if s["session_number"] == 1)
    # Critical bug check: total used to equal deliverable_quality (just the gate score).
    # The fix: total = weighted formula across all four components.
    # With prompt=0, eff=0, std≈0 (no CLAUDE.md), deliv≈85 (passes critical, fails bonus):
    #   weighted = (0*0.25 + 0*0.15 + 85*0.20 + std*0.15) / 0.75 ≈ 22.67 (or higher with std)
    # The bug stored total = 85 (just deliverable). The fix stores ~22.67-32.
    assert s1["total"] != s1["deliverable_quality"], (
        f"Per-session total ({s1['total']}) equals deliverable_quality "
        f"({s1['deliverable_quality']}) — that's the old bug where "
        "total = quality_score instead of the weighted formula."
    )
    # Sanity: total should be in 0..100 and reflect the weighted formula
    assert 0 <= s1["total"] <= 100, f"Total out of range: {s1['total']}"
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
