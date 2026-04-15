"""Single source of truth for prompt logs: JSONL files matching hook output.

Format (one JSON object per line):
    {"type": "prompt"|"response", "student": "alice", "session": 1,
     "timestamp": "2026-04-15T12:00:00Z", "content": "..."}

Layout:
    {LOGS_DIR}/{student_id}/session-{N}/prompts.jsonl  -- prompt events
    {LOGS_DIR}/{student_id}/session-{N}/responses.jsonl -- response events
"""

import json
from datetime import datetime, timezone
from pathlib import Path


def _now() -> str:
    return datetime.now(timezone.utc).strftime("%Y-%m-%dT%H:%M:%SZ")


def _session_dir(log_dir: Path, session: int) -> Path:
    return log_dir / f"session-{session}"


def _append_event(log_dir: Path, session: int, event_type: str,
                  content: str, filename: str) -> None:
    sd = _session_dir(log_dir, session)
    sd.mkdir(parents=True, exist_ok=True)
    entry = {
        "type": event_type,
        "student": log_dir.name,  # student_id is the parent dir name
        "session": session,
        "timestamp": _now(),
        "content": content,
    }
    with (sd / filename).open("a", encoding="utf-8") as f:
        f.write(json.dumps(entry, ensure_ascii=False) + "\n")


def append_prompt(log_dir: Path, session: int, content: str) -> None:
    """Append a 'prompt' event to {log_dir}/session-{N}/prompts.jsonl."""
    _append_event(log_dir, session, "prompt", content, "prompts.jsonl")


def append_response(log_dir: Path, session: int, content: str) -> None:
    """Append a 'response' event to {log_dir}/session-{N}/responses.jsonl."""
    _append_event(log_dir, session, "response", content, "responses.jsonl")


def _read_jsonl(path: Path) -> list[dict]:
    if not path.exists():
        return []
    out = []
    for line in path.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line:
            continue
        try:
            out.append(json.loads(line))
        except json.JSONDecodeError:
            continue  # tolerate malformed lines (hook writes can be partial)
    return out


def read_prompts(log_dir: Path, session: int) -> list[str]:
    """Return the content of all prompt events for the given session, in order."""
    events = _read_jsonl(_session_dir(log_dir, session) / "prompts.jsonl")
    return [e.get("content", "") for e in events if e.get("type") == "prompt"]


def count_prompts(log_dir: Path, session: int) -> int:
    return len(read_prompts(log_dir, session))


def read_all_events(log_dir: Path, session: int) -> list[dict]:
    """Return prompts + responses, sorted by timestamp."""
    sd = _session_dir(log_dir, session)
    events = _read_jsonl(sd / "prompts.jsonl") + _read_jsonl(sd / "responses.jsonl")
    events.sort(key=lambda e: e.get("timestamp", ""))
    return events
