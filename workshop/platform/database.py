"""SQLite database for bootcamp state: students, progress, scores.

Note: prompt logs are NOT stored here. They live as JSONL files on disk
(see workshop.platform.jsonl_log) — same format the hooks write directly.
The legacy `log_prompt` / `get_prompt_logs` / `get_prompt_count` functions
are kept as thin compat wrappers around jsonl_log.
"""

import json
import sqlite3
from datetime import datetime, timezone
from pathlib import Path

from .config import DB_PATH, LOGS_DIR
from . import jsonl_log

SCHEMA = """
CREATE TABLE IF NOT EXISTS cohorts (
    id TEXT PRIMARY KEY,
    name TEXT NOT NULL,
    registration_open INTEGER DEFAULT 1,
    deadline TEXT,
    created_at TEXT DEFAULT (datetime('now'))
);

CREATE TABLE IF NOT EXISTS students (
    id TEXT PRIMARY KEY,
    cohort_id TEXT REFERENCES cohorts(id),
    name TEXT NOT NULL,
    email TEXT,
    registered_at TEXT DEFAULT (datetime('now')),
    setup_completed INTEGER DEFAULT 0
);

CREATE TABLE IF NOT EXISTS session_progress (
    student_id TEXT REFERENCES students(id),
    session_number INTEGER,
    started_at TEXT,
    completed_at TEXT,
    gate_passed INTEGER DEFAULT 0,
    gate_details TEXT,
    attempt_count INTEGER DEFAULT 0,
    auto_unlocked INTEGER DEFAULT 0,
    PRIMARY KEY (student_id, session_number)
);

CREATE TABLE IF NOT EXISTS scores (
    student_id TEXT REFERENCES students(id),
    session_number INTEGER,
    prompt_quality REAL DEFAULT 0,
    efficiency REAL DEFAULT 0,
    deliverable_quality REAL DEFAULT 0,
    standards_compliance REAL DEFAULT 0,
    total REAL DEFAULT 0,
    scored_at TEXT DEFAULT (datetime('now')),
    PRIMARY KEY (student_id, session_number)
);

"""


def get_connection(db_path: Path | None = None) -> sqlite3.Connection:
    """Get a database connection, creating the schema if needed."""
    path = db_path or DB_PATH
    path.parent.mkdir(parents=True, exist_ok=True)
    conn = sqlite3.connect(str(path))
    conn.row_factory = sqlite3.Row
    conn.execute("PRAGMA foreign_keys = ON")
    conn.executescript(SCHEMA)
    return conn


def _now() -> str:
    return datetime.now(timezone.utc).isoformat()


# --- Cohort operations ---


def create_cohort(conn: sqlite3.Connection, cohort_id: str, name: str,
                  deadline: str | None = None) -> None:
    conn.execute(
        "INSERT INTO cohorts (id, name, deadline) VALUES (?, ?, ?)",
        (cohort_id, name, deadline),
    )
    conn.commit()


def set_registration_open(conn: sqlite3.Connection, cohort_id: str,
                          is_open: bool) -> None:
    conn.execute(
        "UPDATE cohorts SET registration_open = ? WHERE id = ?",
        (int(is_open), cohort_id),
    )
    conn.commit()


def get_cohort(conn: sqlite3.Connection, cohort_id: str) -> sqlite3.Row | None:
    return conn.execute(
        "SELECT * FROM cohorts WHERE id = ?", (cohort_id,)
    ).fetchone()


def get_active_cohort(conn: sqlite3.Connection) -> sqlite3.Row | None:
    return conn.execute(
        "SELECT * FROM cohorts ORDER BY created_at DESC LIMIT 1"
    ).fetchone()


# --- Student operations ---


def register_student(conn: sqlite3.Connection, student_id: str, name: str,
                     email: str, cohort_id: str) -> None:
    cohort = get_cohort(conn, cohort_id)
    if not cohort:
        raise ValueError(f"Cohort '{cohort_id}' does not exist")
    if not cohort["registration_open"]:
        raise ValueError(f"Registration is closed for cohort '{cohort_id}'")
    if cohort["deadline"]:
        if _now() > cohort["deadline"]:
            raise ValueError(f"Registration deadline has passed for cohort '{cohort_id}'")
    conn.execute(
        "INSERT INTO students (id, cohort_id, name, email) VALUES (?, ?, ?, ?)",
        (student_id, cohort_id, name, email),
    )
    conn.commit()


def mark_setup_completed(conn: sqlite3.Connection, student_id: str) -> None:
    conn.execute(
        "UPDATE students SET setup_completed = 1 WHERE id = ?",
        (student_id,),
    )
    conn.commit()


def get_student(conn: sqlite3.Connection, student_id: str) -> sqlite3.Row | None:
    return conn.execute(
        "SELECT * FROM students WHERE id = ?", (student_id,)
    ).fetchone()


def list_students(conn: sqlite3.Connection,
                  cohort_id: str | None = None) -> list[sqlite3.Row]:
    if cohort_id:
        return conn.execute(
            "SELECT * FROM students WHERE cohort_id = ? ORDER BY name",
            (cohort_id,),
        ).fetchall()
    return conn.execute("SELECT * FROM students ORDER BY name").fetchall()


# --- Session progress ---


def start_session(conn: sqlite3.Connection, student_id: str,
                  session_number: int) -> None:
    conn.execute(
        """INSERT OR REPLACE INTO session_progress
           (student_id, session_number, started_at, gate_passed, gate_details)
           VALUES (?, ?, ?, 0, NULL)""",
        (student_id, session_number, _now()),
    )
    conn.commit()


def complete_session(conn: sqlite3.Connection, student_id: str,
                     session_number: int, gate_passed: bool,
                     gate_details: dict) -> None:
    conn.execute(
        """UPDATE session_progress
           SET completed_at = ?, gate_passed = ?, gate_details = ?,
               attempt_count = attempt_count + 1
           WHERE student_id = ? AND session_number = ?""",
        (_now(), int(gate_passed), json.dumps(gate_details),
         student_id, session_number),
    )
    conn.commit()


def get_attempt_count(conn: sqlite3.Connection, student_id: str,
                      session_number: int) -> int:
    row = conn.execute(
        """SELECT attempt_count FROM session_progress
           WHERE student_id = ? AND session_number = ?""",
        (student_id, session_number),
    ).fetchone()
    return row["attempt_count"] if row else 0


def mark_auto_unlocked(conn: sqlite3.Connection, student_id: str,
                       session_number: int) -> None:
    conn.execute(
        """UPDATE session_progress
           SET gate_passed = 1, auto_unlocked = 1
           WHERE student_id = ? AND session_number = ?""",
        (student_id, session_number),
    )
    conn.commit()


def get_session_progress(conn: sqlite3.Connection,
                         student_id: str) -> list[sqlite3.Row]:
    return conn.execute(
        """SELECT * FROM session_progress
           WHERE student_id = ? ORDER BY session_number""",
        (student_id,),
    ).fetchall()


def get_last_completed_session(conn: sqlite3.Connection,
                               student_id: str) -> int:
    row = conn.execute(
        """SELECT MAX(session_number) as last_session
           FROM session_progress
           WHERE student_id = ? AND gate_passed = 1""",
        (student_id,),
    ).fetchone()
    return row["last_session"] if row and row["last_session"] else 0


# --- Scores ---


def save_score(conn: sqlite3.Connection, student_id: str,
               session_number: int, prompt_quality: float,
               efficiency: float, deliverable_quality: float,
               standards_compliance: float, total: float) -> None:
    conn.execute(
        """INSERT OR REPLACE INTO scores
           (student_id, session_number, prompt_quality, efficiency,
            deliverable_quality, standards_compliance, total, scored_at)
           VALUES (?, ?, ?, ?, ?, ?, ?, ?)""",
        (student_id, session_number, prompt_quality, efficiency,
         deliverable_quality, standards_compliance, total, _now()),
    )
    conn.commit()


def get_scores(conn: sqlite3.Connection,
               student_id: str) -> list[sqlite3.Row]:
    return conn.execute(
        "SELECT * FROM scores WHERE student_id = ? ORDER BY session_number",
        (student_id,),
    ).fetchall()


def get_total_score(conn: sqlite3.Connection, student_id: str) -> float:
    row = conn.execute(
        "SELECT AVG(total) as avg_score FROM scores WHERE student_id = ?",
        (student_id,),
    ).fetchone()
    return row["avg_score"] if row and row["avg_score"] else 0.0


def get_all_scores(conn: sqlite3.Connection) -> list[sqlite3.Row]:
    return conn.execute(
        """SELECT s.id, s.name, s.email,
                  COALESCE(AVG(sc.total), 0) as avg_score,
                  COUNT(sp.session_number) as sessions_completed
           FROM students s
           LEFT JOIN scores sc ON s.id = sc.student_id
           LEFT JOIN session_progress sp ON s.id = sp.student_id AND sp.gate_passed = 1
           GROUP BY s.id
           ORDER BY avg_score DESC""",
    ).fetchall()


# --- Prompt logs (compat layer over jsonl_log; SQLite no longer stores them) ---


def log_prompt(conn: sqlite3.Connection, student_id: str,
               session_number: int, event_type: str, content: str) -> None:
    """Append to the JSONL file. `conn` is unused (kept for backward compat)."""
    log_dir = LOGS_DIR / student_id
    if event_type == "prompt":
        jsonl_log.append_prompt(log_dir, session_number, content)
    else:
        jsonl_log.append_response(log_dir, session_number, content)


def get_prompt_logs(conn: sqlite3.Connection, student_id: str,
                    session_number: int | None = None) -> list[dict]:
    """Read JSONL events. Returns list of dicts with keys matching the old
    sqlite3.Row shape: student_id, session_number, timestamp, event_type, content."""
    log_dir = LOGS_DIR / student_id
    if session_number is not None:
        sessions = [session_number]
    else:
        sessions = list(range(1, 11))
    rows = []
    for sn in sessions:
        for ev in jsonl_log.read_all_events(log_dir, sn):
            rows.append({
                "student_id": ev.get("student", student_id),
                "session_number": ev.get("session", sn),
                "timestamp": ev.get("timestamp", ""),
                "event_type": ev.get("type", ""),
                "content": ev.get("content", ""),
            })
    return rows


def get_prompt_count(conn: sqlite3.Connection, student_id: str,
                     session_number: int) -> int:
    """Count prompt events (not responses) for a session via JSONL."""
    return jsonl_log.count_prompts(LOGS_DIR / student_id, session_number)
