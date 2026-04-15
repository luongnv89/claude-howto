"""Test the JSONL prompt log reader (single source of truth for prompts)."""

import json

from workshop.platform.jsonl_log import (
    append_prompt, append_response, read_prompts, read_all_events,
    count_prompts,
)


def test_append_and_read_prompts(tmp_path):
    log_dir = tmp_path / "logs" / "alice"
    append_prompt(log_dir, session=1, content="Make a button")
    append_prompt(log_dir, session=1, content="Make it red")
    append_prompt(log_dir, session=2, content="Different session")

    s1 = read_prompts(log_dir, session=1)
    assert len(s1) == 2
    assert s1[0] == "Make a button"
    assert s1[1] == "Make it red"

    s2 = read_prompts(log_dir, session=2)
    assert s2 == ["Different session"]


def test_count_prompts(tmp_path):
    log_dir = tmp_path / "logs" / "alice"
    for i in range(5):
        append_prompt(log_dir, session=1, content=f"prompt {i}")
    assert count_prompts(log_dir, session=1) == 5
    assert count_prompts(log_dir, session=2) == 0


def test_read_all_events_includes_responses(tmp_path):
    log_dir = tmp_path / "logs" / "alice"
    append_prompt(log_dir, session=1, content="p1")
    append_response(log_dir, session=1, content="r1")
    append_prompt(log_dir, session=1, content="p2")

    events = read_all_events(log_dir, session=1)
    assert len(events) == 3
    assert events[0]["type"] == "prompt"
    assert any(e["type"] == "response" for e in events)


def test_jsonl_format_matches_hook_output(tmp_path):
    """The on-disk format must match what hooks/log-prompt.sh produces:
       {"type":"prompt","student":"alice","session":1,"timestamp":"...","content":"..."}"""
    log_dir = tmp_path / "logs" / "alice"
    append_prompt(log_dir, session=1, content='Has "quotes" and \\backslashes')

    jsonl_file = log_dir / "session-1" / "prompts.jsonl"
    line = jsonl_file.read_text().strip()
    parsed = json.loads(line)  # Must be valid JSON
    assert parsed["type"] == "prompt"
    assert parsed["session"] == 1
    assert parsed["content"] == 'Has "quotes" and \\backslashes'
    assert "timestamp" in parsed


def test_missing_session_dir_returns_empty(tmp_path):
    log_dir = tmp_path / "logs" / "nobody"
    assert read_prompts(log_dir, session=1) == []
    assert count_prompts(log_dir, session=1) == 0
    assert read_all_events(log_dir, session=1) == []
