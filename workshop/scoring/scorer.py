"""Main scoring engine: aggregates all analyzers into final score."""

import sqlite3
from pathlib import Path

from ..platform import database as db
from ..platform.config import BOOTCAMP_HOME, LOGS_DIR, TOTAL_SESSIONS
from .deliverable_analyzer import analyze_deliverables
from .efficiency_analyzer import analyze_efficiency
from .prompt_analyzer import analyze_prompts
from .rubric import CONTINUOUS_WEIGHT, FINAL_TASK_WEIGHT, get_grade
from .standards_analyzer import analyze_standards


def score_student(conn: sqlite3.Connection, student_id: str,
                  project_dir: Path | None = None,
                  use_ai: bool = True) -> dict:
    """Run full scoring for a student across all completed sessions.

    Returns dict with component scores and total.
    """
    log_dir = LOGS_DIR / student_id

    # Get completed sessions
    progress = db.get_session_progress(conn, student_id)
    completed = [p for p in progress if p["gate_passed"]]

    if not completed:
        return {
            "prompt_quality": 0,
            "efficiency": 0,
            "deliverable_quality": 0,
            "standards_compliance": 0,
            "total": 0,
            "grade": "Incomplete",
            "sessions_scored": 0,
        }

    # Aggregate scores across sessions
    prompt_scores = []
    efficiency_scores = []
    deliverable_scores = []

    for session in completed:
        sn = session["session_number"]

        # Prompt quality
        pq = analyze_prompts(log_dir, sn, use_ai=use_ai)
        prompt_scores.append(pq["score"])

        # Efficiency
        eff = analyze_efficiency(log_dir, sn, gate_passed=True)
        efficiency_scores.append(eff["score"])

        # Deliverable quality
        dq = analyze_deliverables(conn, student_id, sn)
        deliverable_scores.append(dq["score"])

    # Standards compliance (project-wide, not per-session)
    if project_dir and project_dir.exists():
        standards = analyze_standards(project_dir)
        standards_score = standards["score"]
    else:
        standards_score = 50  # Default if project dir not available

    # Average per-session scores
    avg_prompt = sum(prompt_scores) / len(prompt_scores) if prompt_scores else 0
    avg_efficiency = sum(efficiency_scores) / len(efficiency_scores) if efficiency_scores else 0
    avg_deliverable = sum(deliverable_scores) / len(deliverable_scores) if deliverable_scores else 0

    # Calculate continuous score (75% of total)
    continuous_score = (
        avg_prompt * 0.25
        + avg_efficiency * 0.15
        + avg_deliverable * 0.20
        + standards_score * 0.15
    ) / CONTINUOUS_WEIGHT  # Normalize to 0-100

    # Final task score (25% of total) — from session 10
    final_task_score = 0
    if any(s["session_number"] == TOTAL_SESSIONS for s in completed):
        s10_dq = analyze_deliverables(conn, student_id, TOTAL_SESSIONS)
        final_task_score = s10_dq["score"]

    # Total score
    total = (continuous_score * CONTINUOUS_WEIGHT
             + final_task_score * FINAL_TASK_WEIGHT)

    grade_label, grade_desc = get_grade(total)

    result = {
        "prompt_quality": round(avg_prompt, 1),
        "efficiency": round(avg_efficiency, 1),
        "deliverable_quality": round(avg_deliverable, 1),
        "standards_compliance": round(standards_score, 1),
        "final_task": round(final_task_score, 1),
        "continuous_score": round(continuous_score, 1),
        "total": round(total, 1),
        "grade": grade_label,
        "grade_description": grade_desc,
        "sessions_scored": len(completed),
    }

    # Save per-session scores back to database with PER-SESSION totals
    # (NOT the aggregate `total` — that's a continuous-score across all sessions)
    for idx, session in enumerate(completed):
        sn = session["session_number"]
        per_session_prompt = prompt_scores[idx] if idx < len(prompt_scores) else 0
        per_session_eff = efficiency_scores[idx] if idx < len(efficiency_scores) else 0
        per_session_deliv = deliverable_scores[idx] if idx < len(deliverable_scores) else 0
        # Per-session weighted total (uses continuous-portion weights only,
        # renormalized so a per-session score is on a 0-100 scale)
        per_session_total = (
            per_session_prompt * 0.25
            + per_session_eff * 0.15
            + per_session_deliv * 0.20
            + standards_score * 0.15
        ) / CONTINUOUS_WEIGHT
        db.save_score(
            conn, student_id, sn,
            prompt_quality=per_session_prompt,
            efficiency=per_session_eff,
            deliverable_quality=per_session_deliv,
            standards_compliance=standards_score,
            total=per_session_total,
        )

    return result
