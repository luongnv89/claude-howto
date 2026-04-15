"""Shared test fixtures for bootcamp platform tests."""

import sqlite3
import tempfile
from pathlib import Path

import pytest

from workshop.platform.database import get_connection


@pytest.fixture(autouse=True)
def _isolate_logs_dir(monkeypatch, tmp_path):
    """Redirect LOGS_DIR (used by jsonl_log compat layer + scorer) to a tmp dir
    per test so on-disk JSONL writes don't leak between tests or pollute
    ~/.claude-bootcamp."""
    isolated = tmp_path / "logs"
    isolated.mkdir()
    # Patch every module that does `from ..config import LOGS_DIR` at import time
    import workshop.platform.config as cfg
    import workshop.platform.database as db_mod
    import workshop.scoring.scorer as scorer_mod
    monkeypatch.setattr(cfg, "LOGS_DIR", isolated)
    monkeypatch.setattr(db_mod, "LOGS_DIR", isolated)
    monkeypatch.setattr(scorer_mod, "LOGS_DIR", isolated)
    yield


@pytest.fixture
def db_conn():
    """Create an in-memory database connection for testing."""
    with tempfile.NamedTemporaryFile(suffix=".db", delete=False) as f:
        db_path = Path(f.name)
    conn = get_connection(db_path)
    yield conn
    conn.close()
    db_path.unlink(missing_ok=True)


@pytest.fixture
def sample_cohort(db_conn):
    """Create a sample cohort with registration open."""
    from workshop.platform.database import create_cohort
    create_cohort(db_conn, "test-cohort", "Test Cohort 2026")
    return "test-cohort"


@pytest.fixture
def sample_student(db_conn, sample_cohort):
    """Create a sample registered student."""
    from workshop.platform.database import register_student
    register_student(db_conn, "student001", "Alice Test",
                     "alice@test.com", sample_cohort)
    return "student001"


@pytest.fixture
def sample_project(tmp_path):
    """Create a minimal project directory for gate testing."""
    project = tmp_path / "qa-command-center"
    project.mkdir()

    # package.json
    (project / "package.json").write_text(
        '{"name":"qa-command-center","dependencies":{"express":"^4.18","react":"^18"},'
        '"scripts":{"dev":"vite","start":"node server/index.js"}}'
    )

    # Server
    server_dir = project / "server"
    server_dir.mkdir()
    (server_dir / "index.js").write_text("const express = require('express');")

    # Client
    client_dir = project / "client" / "src"
    client_dir.mkdir(parents=True)
    for name in ["App.jsx", "TestCaseList.jsx", "BugTracker.jsx"]:
        (client_dir / name).write_text(f"export default function {name.split('.')[0]}() {{}}")

    # CLAUDE.md
    (project / "CLAUDE.md").write_text(
        "# QA Command Center\n## Standards\nUse ISTQB severity levels.\n"
        "## API Convention\nReturn JSON responses.\n"
    )

    # .claude directories
    (project / ".claude" / "rules").mkdir(parents=True)
    (project / ".claude" / "rules" / "api.md").write_text("Use REST conventions")

    skills_dir = project / ".claude" / "skills" / "test-generator"
    skills_dir.mkdir(parents=True)
    (skills_dir / "SKILL.md").write_text(
        "---\nname: test-generator\ndescription: Generate test suites\n---\n"
        "# Test Generator\nGenerates test suites using ISTQB techniques."
    )

    skills_dir2 = project / ".claude" / "skills" / "qa-review"
    skills_dir2.mkdir(parents=True)
    (skills_dir2 / "SKILL.md").write_text(
        "---\nname: qa-review\ndescription: Review code from QA perspective\n---\n"
        "# QA Review"
    )

    return project
