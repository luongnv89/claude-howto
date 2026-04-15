"""Bootcamp CLI: all subcommands for students and instructors."""

import argparse
import json
import sys
from pathlib import Path

from . import database as db
from . import registration as reg
from . import student_setup as setup
from .config import GRADE_BANDS, SESSION_NAMES, TOTAL_SESSIONS


def main(argv: list[str] | None = None) -> int:
    parser = argparse.ArgumentParser(
        prog="bootcamp",
        description="AI Bootcamp Platform - registration, gating, scoring, and monitoring",
    )
    subparsers = parser.add_subparsers(dest="command", help="Available commands")

    # --- Student commands ---

    setup_parser = subparsers.add_parser(
        "setup", help="Set up your bootcamp environment"
    )
    setup_parser.add_argument("--student-id", required=True, help="Your student ID")
    setup_parser.add_argument(
        "--project-dir", type=Path, default=None,
        help="Path to your QA Command Center project directory",
    )

    start_parser = subparsers.add_parser(
        "start-session", help="Start a session"
    )
    start_parser.add_argument("session", type=int, help="Session number (1-10)")

    complete_parser = subparsers.add_parser(
        "complete-session", help="Complete a session and run gate checks"
    )
    complete_parser.add_argument("session", type=int, help="Session number (1-10)")
    complete_parser.add_argument(
        "--project-dir", type=Path, default=Path.cwd(),
        help="Path to your QA Command Center project (default: current directory)",
    )

    status_parser = subparsers.add_parser(
        "status", help="Check your progress and scores"
    )
    status_parser.add_argument("--student", help="Student ID (instructor use)")
    status_parser.add_argument("--detailed", action="store_true",
                               help="Show detailed breakdown")
    status_parser.add_argument("--prompts", action="store_true",
                               help="Show prompt logs")

    # --- Instructor commands ---

    reg_parser = subparsers.add_parser(
        "register", help="Register a student"
    )
    reg_parser.add_argument("student_id", help="Student ID")
    reg_parser.add_argument("name", help="Student full name")
    reg_parser.add_argument("email", help="Student email")
    reg_parser.add_argument("--cohort", required=True, help="Cohort ID")

    open_parser = subparsers.add_parser(
        "open-registration", help="Open registration for a cohort"
    )
    open_parser.add_argument("--cohort", required=True, help="Cohort ID")
    open_parser.add_argument("--name", help="Cohort display name")
    open_parser.add_argument("--deadline", help="Registration deadline (ISO format)")

    close_parser = subparsers.add_parser(
        "close-registration", help="Close registration for a cohort"
    )
    close_parser.add_argument("--cohort", required=True, help="Cohort ID")

    subparsers.add_parser("dashboard", help="Real-time student dashboard")

    scores_parser = subparsers.add_parser(
        "scores", help="Export scores"
    )
    scores_parser.add_argument(
        "--format", choices=["json", "csv", "html"], default="json",
        help="Output format",
    )
    scores_parser.add_argument("--output", type=Path, help="Output file path")

    grade_parser = subparsers.add_parser(
        "grade", help="Run full scoring for a student"
    )
    grade_parser.add_argument("student_id", help="Student ID to grade")
    grade_parser.add_argument("--no-ai", action="store_true",
                              help="Use heuristic scoring only (no AI)")

    # Instructor override: unlock a session for a student
    unlock_parser = subparsers.add_parser(
        "unlock-session",
        help="[Instructor] Force-unlock a session for a student (bypasses gates)",
    )
    unlock_parser.add_argument("session", type=int, help="Session number to unlock")
    unlock_parser.add_argument("--student", required=True, help="Student ID")
    unlock_parser.add_argument(
        "--reason", default="instructor override",
        help="Reason for override (logged for audit)",
    )

    args = parser.parse_args(argv)

    if not args.command:
        parser.print_help()
        return 1

    conn = db.get_connection()

    try:
        if args.command == "setup":
            return cmd_setup(conn, args)
        elif args.command == "start-session":
            return cmd_start_session(conn, args)
        elif args.command == "complete-session":
            return cmd_complete_session(conn, args)
        elif args.command == "status":
            return cmd_status(conn, args)
        elif args.command == "register":
            return cmd_register(conn, args)
        elif args.command == "open-registration":
            return cmd_open_registration(conn, args)
        elif args.command == "close-registration":
            return cmd_close_registration(conn, args)
        elif args.command == "dashboard":
            return cmd_dashboard(conn)
        elif args.command == "scores":
            return cmd_scores(conn, args)
        elif args.command == "grade":
            return cmd_grade(conn, args)
        elif args.command == "unlock-session":
            return cmd_unlock_session(conn, args)
        else:
            parser.print_help()
            return 1
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return 1
    finally:
        conn.close()


def cmd_setup(conn, args) -> int:
    steps = setup.setup_student(conn, args.student_id, args.project_dir)
    print("Bootcamp setup completed:")
    for step in steps:
        print(f"  [+] {step}")
    print(f"\nWelcome! Run './bootcamp start-session 1' to begin.")
    return 0


def cmd_start_session(conn, args) -> int:
    session = args.session
    if not 1 <= session <= TOTAL_SESSIONS:
        print(f"Error: Session must be between 1 and {TOTAL_SESSIONS}")
        return 1

    student_id = setup.get_student_id()
    if not student_id:
        print("Error: Run './bootcamp setup' first")
        return 1

    # Check prerequisites
    if session > 1:
        last_completed = db.get_last_completed_session(conn, student_id)
        if last_completed < session - 1:
            print(f"Error: You must complete session {session - 1} first.")
            print(f"  Your last completed session: {last_completed or 'none'}")
            print(f"  Run: ./bootcamp complete-session {last_completed + 1}")
            return 1

    # Record session start
    db.start_session(conn, student_id, session)
    setup.set_current_session(session)

    session_name = SESSION_NAMES.get(session, f"Session {session}")
    print(f"\n{'=' * 60}")
    print(f"  Session {session}: {session_name}")
    print(f"{'=' * 60}")
    print(f"\n  Guide: workshop/sessions/s{session:02d}-*/README.md")
    print(f"  Deliverables: workshop/sessions/s{session:02d}-*/deliverables.md")
    print(f"\n  When done: ./bootcamp complete-session {session}")
    print(f"{'=' * 60}\n")
    return 0


def cmd_complete_session(conn, args) -> int:
    session = args.session
    if not 1 <= session <= TOTAL_SESSIONS:
        print(f"Error: Session must be between 1 and {TOTAL_SESSIONS}")
        return 1

    student_id = setup.get_student_id()
    if not student_id:
        print("Error: Run './bootcamp setup' first")
        return 1

    print(f"\nRunning gate checks for Session {session}...")
    print("-" * 40)

    # Import and run gate
    try:
        from workshop.gates.gate_runner import run_gate
        results = run_gate(session, args.project_dir)
    except ImportError:
        # Fallback: basic gate check
        results = _basic_gate_check(session, args.project_dir)

    # Display results — separate critical vs bonus checks
    critical_passed = True
    bonus_failed = []
    total_points = 0
    max_points = 0

    for check in results:
        is_critical = check.get("critical", True)
        status = "PASS" if check["passed"] else "FAIL"
        tag = "" if is_critical else " (bonus)"
        icon = "[+]" if check["passed"] else "[-]"
        print(f"  {icon} {status}: {check['message']}{tag} ({check['points']} pts)")
        if check["passed"]:
            total_points += check["points"]
        elif is_critical:
            critical_passed = False
        else:
            bonus_failed.append(check["message"])
        max_points += check["points"]

    print("-" * 40)
    print(f"  Score: {total_points}/{max_points}")

    # Record results
    gate_details = {
        "checks": results,
        "total_points": total_points,
        "max_points": max_points,
    }

    # Gate passes if all CRITICAL checks pass (bonus checks affect score only)
    gate_passed = critical_passed
    db.complete_session(conn, student_id, session, gate_passed, gate_details)

    # Compute deliverable_quality from gate points
    quality_score = (total_points / max_points * 100) if max_points > 0 else 0

    # Compute per-session components inline (heuristic, fast — no AI calls here)
    from workshop.scoring.efficiency_analyzer import analyze_efficiency
    from workshop.scoring.prompt_analyzer import analyze_prompts
    from workshop.scoring.standards_analyzer import analyze_standards
    from workshop.platform.config import LOGS_DIR

    log_dir = LOGS_DIR / student_id
    prompt_result = analyze_prompts(log_dir, session, use_ai=False)
    eff_result = analyze_efficiency(log_dir, session, gate_passed=critical_passed)
    if args.project_dir.exists():
        std_result = analyze_standards(args.project_dir)
        standards_score = std_result["score"]
    else:
        standards_score = 0

    # Per-session weighted total (continuous-portion weights, renormalized
    # so a per-session score is on a 0-100 scale).
    per_session_total = (
        prompt_result["score"] * 0.25
        + eff_result["score"] * 0.15
        + quality_score * 0.20
        + standards_score * 0.15
    ) / 0.75

    db.save_score(
        conn, student_id, session,
        prompt_quality=prompt_result["score"],
        efficiency=eff_result["score"],
        deliverable_quality=quality_score,
        standards_compliance=standards_score,
        total=per_session_total,
    )

    if gate_passed:
        print(f"\n  Session {session} COMPLETED! (score: {quality_score:.0f}/100)")
        if bonus_failed:
            print(f"  Note: {len(bonus_failed)} bonus check(s) missed "
                  f"(affects score, not progression)")
        if session < TOTAL_SESSIONS:
            print(f"  Next: ./bootcamp start-session {session + 1}")
        else:
            print("  Congratulations! You have completed all sessions!")
            print("  Run: ./bootcamp status --detailed")
        return 0

    # --- Gate failed: escalating response based on attempt count ---
    from .config import AUTO_UNLOCK_ATTEMPT, AUTO_UNLOCK_PENALTY, HINT_ESCALATION_ATTEMPT

    attempts = db.get_attempt_count(conn, student_id, session)
    failed_critical = [c for c in results
                       if not c["passed"] and c.get("critical", True)]

    print(f"\n  Attempt {attempts}/{AUTO_UNLOCK_ATTEMPT} "
          f"— {len(failed_critical)} critical check(s) failed:")

    for check in failed_critical:
        print(f"    [-] {check['message']}")

    # Escalation level 1: basic feedback (attempts 1-2)
    if attempts < HINT_ESCALATION_ATTEMPT:
        print(f"\n  Fix the issues and retry: ./bootcamp complete-session {session}")
        remaining = AUTO_UNLOCK_ATTEMPT - attempts
        print(f"  ({remaining} more attempts before auto-unlock with score penalty)")

    # Escalation level 2: detailed hints (attempts 3-4)
    elif attempts < AUTO_UNLOCK_ATTEMPT:
        print(f"\n  DETAILED HINTS (attempt {attempts}):")
        for check in failed_critical:
            hint = _get_hint_for_check(check["message"], session)
            print(f"    -> {check['message']}")
            print(f"       Hint: {hint}")
        remaining = AUTO_UNLOCK_ATTEMPT - attempts
        print(f"\n  Retry: ./bootcamp complete-session {session}")
        print(f"  ({remaining} more attempt(s) before auto-unlock with "
              f"{int(AUTO_UNLOCK_PENALTY * 100)}% score penalty)")

    # Escalation level 3: auto-unlock (attempt 5+)
    else:
        penalty_pct = int(AUTO_UNLOCK_PENALTY * 100)
        penalized_score = quality_score * (1 - AUTO_UNLOCK_PENALTY)
        print(f"\n  AUTO-UNLOCKED after {attempts} attempts.")
        print(f"  Score penalty: -{penalty_pct}% "
              f"(session score: {penalized_score:.0f}/100 instead of {quality_score:.0f})")
        print(f"  You can still fix issues and re-run for full credit:")
        print(f"    ./bootcamp complete-session {session}")

        # Force-pass the gate with penalty
        db.mark_auto_unlocked(conn, student_id, session)
        db.save_score(
            conn, student_id, session,
            prompt_quality=0, efficiency=0,
            deliverable_quality=penalized_score,
            standards_compliance=0,
            total=penalized_score,
        )

        if session < TOTAL_SESSIONS:
            print(f"\n  Next: ./bootcamp start-session {session + 1}")
        return 0

    return 1


# Hints for common gate failures — nudge thinking, don't give answers
_HINTS = {
    "package.json": "A Node.js project starts somewhere. What file does npm look for first?",
    "express": "You're building a 'full-stack' app. What's on the backend? What serves your API?",
    "react": "Your frontend framework was mentioned in the session goals. What tool scaffolds it fast?",
    "CLAUDE.md": "Claude needs persistent context about YOUR project. Where does that live?",
    "rules": "CLAUDE.md is one file. What if different parts of your project have different rules?",
    "SKILL.md": "A skill is more than just a file name — what makes Claude auto-invoke it? Where do skills live?",
    "skills": "Auto-invocation depends on metadata. What structure at the top of a markdown file holds metadata?",
    "agents": "Agents are specialists. How does Claude know what a specialist does and what tools they can use?",
    "frontmatter": "This is a YAML concept. Look at an existing skill in 03-skills/ — what bracket the metadata?",
    ".mcp.json": "MCP connects Claude to external services. How do you tell Claude which services and where?",
    "github": "You need Claude to talk to GitHub. Is there an MCP server for that? Where would you find it?",
    "jira": "Jira is an Atlassian product. Is there a pattern for how Atlassian MCP servers are configured?",
    "atlassian": "Atlassian Cloud needs authentication. What credential does the API require, and where does it go?",
    "settings.json": "Hooks need to be registered somewhere Claude reads on startup. Which config file?",
    "hook": "Hooks respond to events. What events can you intercept? Which one fires before a tool runs?",
    "plugin": "A plugin bundles things. What manifest format describes what's inside a plugin?",
    "csv": "Parsing CSV reliably is tricky — edge cases everywhere. Is there a well-known library for this?",
    "setting": "User preferences need to persist. Where do they live, and how do they load on startup?",
    "ci": "Automation runs when events happen in your repo. What's GitHub's native automation system?",
    "navigation": "SPAs need routing without full page reloads. What's the standard React library for that?",
    "responsive": "Responsive design adapts to screen size. What CSS feature queries screen dimensions?",
    "chart": "Dashboards need visualizations. What charting libraries integrate well with React?",
    "test case": "A test case has a structure: what fields does every ISTQB test case need?",
    "bug": "A bug report should be actionable. What fields would a developer need to fix it?",
    "severity": "ISTQB defines severity levels. How many, and what do they represent?",
    "dashboard": "A dashboard summarizes. What metrics matter most for a QA team at a glance?",
}


def _get_hint_for_check(message: str, session: int) -> str:
    """Return a direction-pointing hint for a failed gate check."""
    message_lower = message.lower()
    for keyword, hint in _HINTS.items():
        if keyword.lower() in message_lower:
            return hint
    return (f"Re-read the 'What You Will Build' and 'Requirements' sections in "
            f"workshop/sessions/s{session:02d}-*/README.md — what's missing?")


def _basic_gate_check(session: int, project_dir: Path) -> list[dict]:
    """Fallback gate check when gate modules aren't available."""
    return [{
        "passed": True,
        "message": f"Basic check for session {session} (full gates not installed)",
        "points": 10,
    }]


def cmd_status(conn, args) -> int:
    student_id = args.student or setup.get_student_id()
    if not student_id:
        print("Error: No student ID. Run './bootcamp setup' or use --student")
        return 1

    student = db.get_student(conn, student_id)
    if not student:
        print(f"Error: Student '{student_id}' not found")
        return 1

    print(f"\n  Student: {student['name']} ({student_id})")
    print(f"  Cohort: {student['cohort_id']}")
    print(f"  Setup: {'Completed' if student['setup_completed'] else 'Pending'}")

    # Session progress
    progress = db.get_session_progress(conn, student_id)
    progress_map = {p["session_number"]: p for p in progress}

    print(f"\n  {'Session':<25} {'Status':<15} {'Gate':<10}")
    print(f"  {'-' * 50}")
    for i in range(1, TOTAL_SESSIONS + 1):
        name = SESSION_NAMES.get(i, f"Session {i}")
        label = f"S{i}: {name}"
        p = progress_map.get(i)
        if p and p["gate_passed"]:
            status = "Completed"
            gate = "PASSED"
        elif p and p["started_at"]:
            status = "In Progress"
            gate = "-"
        else:
            status = "Not Started"
            gate = "-"
        print(f"  {label:<25} {status:<15} {gate:<10}")

    # Scores
    scores = db.get_scores(conn, student_id)
    if scores:
        total_avg = sum(s["total"] for s in scores) / len(scores)
        grade_label = _get_grade_label(total_avg)
        print(f"\n  Average Score: {total_avg:.1f}/100 ({grade_label})")

        if args.detailed:
            print(f"\n  {'Session':<12} {'Quality':<10} {'Efficiency':<12} "
                  f"{'Deliverables':<14} {'Standards':<12} {'Total':<8}")
            print(f"  {'-' * 68}")
            for s in scores:
                print(f"  S{s['session_number']:<10} "
                      f"{s['prompt_quality']:<10.1f} "
                      f"{s['efficiency']:<12.1f} "
                      f"{s['deliverable_quality']:<14.1f} "
                      f"{s['standards_compliance']:<12.1f} "
                      f"{s['total']:<8.1f}")

    # Prompt logs (JSONL files on disk — single source of truth)
    if args.prompts:
        from workshop.platform.config import LOGS_DIR
        from workshop.platform.jsonl_log import read_all_events

        all_events = []
        for n in range(1, TOTAL_SESSIONS + 1):
            for ev in read_all_events(LOGS_DIR / student_id, n):
                all_events.append(ev)
        if all_events:
            print(f"\n  Prompt History ({len(all_events)} entries):")
            for ev in all_events[-20:]:
                content = ev.get("content", "")[:80]
                print(f"    [{ev.get('timestamp','?')}] "
                      f"S{ev.get('session','?')} "
                      f"({ev.get('type','?')}): {content}")

    return 0


def cmd_register(conn, args) -> int:
    msg = reg.register_student(conn, args.student_id, args.name,
                               args.email, args.cohort)
    print(msg)
    return 0


def cmd_open_registration(conn, args) -> int:
    msg = reg.open_registration(conn, args.cohort, args.name, args.deadline)
    print(msg)
    return 0


def cmd_close_registration(conn, args) -> int:
    msg = reg.close_registration(conn, args.cohort)
    print(msg)
    return 0


def cmd_dashboard(conn) -> int:
    all_scores = db.get_all_scores(conn)
    if not all_scores:
        print("No students registered yet.")
        return 0

    print(f"\n  {'Student':<20} {'Name':<20} {'Sessions':<10} "
          f"{'Avg Score':<12} {'Grade':<15}")
    print(f"  {'=' * 77}")
    for row in all_scores:
        grade = _get_grade_label(row["avg_score"])
        print(f"  {row['id']:<20} {row['name']:<20} "
              f"{row['sessions_completed']:<10} "
              f"{row['avg_score']:<12.1f} {grade:<15}")
    print()
    return 0


def cmd_scores(conn, args) -> int:
    all_scores = db.get_all_scores(conn)
    if not all_scores:
        print("No scores available.")
        return 0

    data = [dict(row) for row in all_scores]

    if args.format == "json":
        output = json.dumps(data, indent=2)
    elif args.format == "csv":
        import csv
        import io
        buf = io.StringIO()
        writer = csv.DictWriter(buf, fieldnames=data[0].keys())
        writer.writeheader()
        writer.writerows(data)
        output = buf.getvalue()
    elif args.format == "html":
        output = _scores_to_html(data)
    else:
        output = json.dumps(data, indent=2)

    if args.output:
        args.output.write_text(output)
        print(f"Scores exported to {args.output}")
    else:
        print(output)
    return 0


def cmd_grade(conn, args) -> int:
    student = db.get_student(conn, args.student_id)
    if not student:
        print(f"Error: Student '{args.student_id}' not found")
        return 1

    print(f"Grading student: {student['name']} ({args.student_id})")

    if args.no_ai:
        print("Using heuristic scoring (--no-ai mode)")
    else:
        print("Using AI-assisted scoring")

    # Import scoring engine
    try:
        from workshop.scoring.scorer import score_student
        result = score_student(conn, args.student_id, use_ai=not args.no_ai)
        print(f"\nFinal Score: {result['total']:.1f}/100 "
              f"({_get_grade_label(result['total'])})")
        print(f"  Prompt Quality:       {result['prompt_quality']:.1f}")
        print(f"  Efficiency:           {result['efficiency']:.1f}")
        print(f"  Deliverable Quality:  {result['deliverable_quality']:.1f}")
        print(f"  Standards Compliance: {result['standards_compliance']:.1f}")
    except ImportError:
        print("Scoring engine not available. Run basic scoring.")
        scores = db.get_scores(conn, args.student_id)
        if scores:
            avg = sum(s["total"] for s in scores) / len(scores)
            print(f"Average gate score: {avg:.1f}/100")
        else:
            print("No scores recorded yet.")

    return 0


def cmd_unlock_session(conn, args) -> int:
    """Instructor override: force-unlock a session for a student."""
    session = args.session
    student_id = args.student
    reason = args.reason

    if not 1 <= session <= TOTAL_SESSIONS:
        print(f"Error: Session must be between 1 and {TOTAL_SESSIONS}")
        return 1

    student = db.get_student(conn, student_id)
    if not student:
        print(f"Error: Student '{student_id}' not found")
        return 1

    # Mark the previous session as passed (so the target session unlocks)
    if session > 1:
        prev = session - 1
        gate_details = {
            "checks": [],
            "total_points": 0,
            "max_points": 0,
            "override": True,
            "reason": reason,
        }
        # Ensure previous session has a start record
        db.start_session(conn, student_id, prev)
        db.complete_session(conn, student_id, prev, True, gate_details)
        print(f"  Session {prev} force-completed for {student['name']}")

    # Also start the target session
    db.start_session(conn, student_id, session)
    print(f"  Session {session} unlocked for {student['name']}")
    print(f"  Reason: {reason}")
    print(f"\n  Note: Override recorded in gate_details. Score will reflect")
    print(f"  0 points for skipped gate checks. Student can still retry")
    print(f"  './bootcamp complete-session {session - 1}' for a real score.")
    return 0


def _get_grade_label(score: float) -> str:
    for low, high, label in GRADE_BANDS:
        if low <= score <= high:
            return label
    return "Ungraded"


def _scores_to_html(data: list[dict]) -> str:
    rows = ""
    for row in data:
        grade = _get_grade_label(row.get("avg_score", 0))
        rows += (
            f"<tr><td>{row['id']}</td><td>{row['name']}</td>"
            f"<td>{row.get('sessions_completed', 0)}</td>"
            f"<td>{row.get('avg_score', 0):.1f}</td>"
            f"<td>{grade}</td></tr>\n"
        )
    return f"""<!DOCTYPE html>
<html><head><title>Bootcamp Scores</title>
<style>
body {{ font-family: system-ui; margin: 2rem; }}
table {{ border-collapse: collapse; width: 100%; }}
th, td {{ border: 1px solid #ddd; padding: 8px; text-align: left; }}
th {{ background: #1a1a2e; color: white; }}
tr:nth-child(even) {{ background: #f2f2f2; }}
</style></head>
<body>
<h1>AI Bootcamp - Score Report</h1>
<table>
<tr><th>Student ID</th><th>Name</th><th>Sessions</th><th>Score</th><th>Grade</th></tr>
{rows}
</table>
</body></html>"""
