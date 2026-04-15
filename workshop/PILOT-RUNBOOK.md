# Phase 1 Pilot Runbook

For running a 2-3 person internal pilot of the AI Bootcamp CLI before the web UI exists.

## Prerequisites checklist

Run on EACH pilot machine:

```bash
./workshop/bootcamp doctor
```

All 5 checks must PASS. If any FAIL, follow the printed `Fix:` line.

## Setup (one-time, instructor)

```bash
cd workshop

# Open a fresh cohort
./bootcamp open-registration --cohort "pilot-1" --name "Phase 1 Pilot" --deadline "2026-05-31"

# Register pilots (replace IDs/names/emails)
./bootcamp register pilot-a "Alice Pilot" alice@example.com --cohort pilot-1
./bootcamp register pilot-b "Bob Pilot"   bob@example.com   --cohort pilot-1
```

Verify roster:
```bash
./bootcamp dashboard
```

## Per-pilot setup (each pilot does this on their own laptop)

```bash
git clone <repo-url> claude-howto
cd claude-howto/workshop

# Verify environment
./bootcamp doctor

# Authenticate Claude Code (uses your own Claude.ai account)
claude /login

# Run setup with your assigned student-id
./bootcamp setup --student-id pilot-a --project-dir ~/qa-cmd-center
```

Hooks are installed into `~/qa-cmd-center/.claude/`. The setup creates `~/.claude-bootcamp/` for state.

## Running a session (pilot does this)

```bash
cd workshop
./bootcamp start-session 1
```

Read the printed guide path. Open it. Work through the requirements by prompting Claude in your project dir. When you think you're done:

```bash
./bootcamp complete-session 1 --project-dir ~/qa-cmd-center
```

The CLI prints a per-check status table + your per-session score breakdown.

## Monitoring (instructor)

Run continuously on a separate screen:
```bash
watch -n 30 ./bootcamp dashboard
```

Drill into a specific pilot:
```bash
./bootcamp status --student pilot-a --detailed
./bootcamp status --student pilot-a --prompts | tail -50
```

## Troubleshooting

**"Python 3.10+ required"** — install via `brew install python@3.12`. Re-run with `/opt/homebrew/bin/python3 ./bootcamp ...`.

**"Student '...' is not registered"** — instructor needs to run `./bootcamp register ...` first.

**"You must complete session N first"** — the pilot tried to skip ahead. They must complete sessions in order, OR an instructor force-unlocks via `./bootcamp unlock-session N --student pilot-a --reason "catch-up"`.

**Gate fails repeatedly** — after 3 attempts, escalating hints appear automatically. After 5 attempts, auto-unlock fires with a 20% score penalty. The pilot can keep retrying for full credit even after auto-unlock.

**Scores look wrong** — run `./bootcamp grade pilot-a --no-ai` for a fresh recompute. If dashboard avg disagrees with grade total, file a bug — they should match (Phase 1 fixed this).

**No prompts in `status --prompts`** — the hook script in their `~/qa-cmd-center/.claude/settings.json` may not be wired. Verify with: `cat ~/.claude-bootcamp/logs/pilot-a/session-1/prompts.jsonl`.

## Pilot success criteria

- Both pilots complete S1-S3 within 3 hours
- No data loss (scores persist across sessions)
- All gate checks behave as expected
- `dashboard` and `grade ... --no-ai` produce consistent scores
- Instructor reports < 30 min total intervention time

## When to stop the pilot

If 3+ critical bugs surface, halt and patch before continuing. Do NOT escalate to a wider pilot until critical bugs are fixed.

## Reset (between pilots)

```bash
# On each pilot machine
rm -rf ~/.claude-bootcamp ~/qa-cmd-center
```
