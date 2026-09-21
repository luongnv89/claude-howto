#!/bin/bash
# Pre-tool safety check for Bash commands
# Hook: PreToolUse (matcher: Bash)
#
# This hook runs before every Bash tool execution and blocks or warns on
# potentially destructive or high-risk shell commands.
#
# Setup:
#   cp 06-hooks/pre-tool-check.sh ~/.claude/hooks/
#   chmod +x ~/.claude/hooks/pre-tool-check.sh
#
# Configure in ~/.claude/settings.json:
#   {
#     "hooks": {
#       "PreToolUse": [
#         {
#           "matcher": "Bash",
#           "hooks": [
#             {
#               "type": "command",
#               "command": "~/.claude/hooks/pre-tool-check.sh"
#             }
#           ]
#         }
#       ]
#     }
#   }
#
# Input: JSON via stdin with the shape:
#   { "tool_name": "Bash", "tool_input": { "command": "..." } }
#
# Output convention (per Claude Code hook protocol):
#   - exit 0 → allow. stdout may contain JSON (hookSpecificOutput); stderr
#     is silently discarded, so warnings printed to stderr are NOT visible.
#     For observability on allowed commands, write to an audit log file.
#   - exit 2 → block. stderr is surfaced back to Claude as the block reason.
#     Any echo explaining *why* a command was blocked MUST be redirected to
#     stderr with `>&2`, otherwise Claude Code reports "No stderr output".
#
# Audit log: every invocation is recorded to
#   $CLAUDE_PROJECT_DIR/.claude/hooks/audit.log
# with the decision (BLOCK/WARN/ALLOW), so you can observe WARN-tier
# matches even though their stderr output is dropped by Claude Code.

# Read the full JSON input from stdin
INPUT=$(cat)

# Extract the command using portable sed (compatible with macOS and Linux)
COMMAND=$(echo "$INPUT" | sed -n 's/.*"command"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/p' | head -1)

# Fall back to the raw input if extraction fails
if [ -z "$COMMAND" ]; then
  COMMAND="$INPUT"
fi

# ── Audit log ─────────────────────────────────────────────────────────────────
# Records every invocation with the final decision. This is the only reliable
# way to observe the WARN tier, because Claude Code silently drops stderr on
# exit 0. Falls back to $(pwd) when the hook is invoked outside Claude Code
# (e.g. for local testing).
LOG_DIR="${CLAUDE_PROJECT_DIR:-$(pwd)}/.claude/hooks"
LOG_FILE="$LOG_DIR/audit.log"
mkdir -p "$LOG_DIR" 2>/dev/null
log_decision() {
  echo "$(date -u +%FT%TZ) [$1] $COMMAND" >> "$LOG_FILE"
}

# ── Blocked patterns ──────────────────────────────────────────────────────────
# These commands are blocked unconditionally because they are almost always
# destructive and rarely intentional in an automated context.

BLOCKED_PATTERNS=(
  # Anchor `rm -rf /` so `/` must be followed by whitespace or end of line,
  # otherwise substring matching would falsely flag e.g. `rm -rf /tmp/foo`.
  "rm -rf /([[:space:]]|$)"
  "rm -rf \*"
  "dd if=/dev/zero"
  "dd if=/dev/random"
  ":\(\)\{:\|:&\};:"  # Fork bomb (regex metachars escaped)
  "mkfs\."           # Filesystem format
  "format c:"        # Windows disk format
)

for pattern in "${BLOCKED_PATTERNS[@]}"; do
  if echo "$COMMAND" | grep -qE "$pattern"; then
    log_decision "BLOCK:$pattern"
    # These echoes MUST go to stderr — Claude Code surfaces stderr as the
    # block reason on exit 2. Writing to stdout would show "No stderr output".
    echo "❌ Blocked: Potentially destructive command detected: $pattern" >&2
    echo "   Command: $COMMAND" >&2
    exit 2
  fi
done

# ── Warning patterns ──────────────────────────────────────────────────────────
# These patterns are risky but may be intentional. Log a warning and allow.

WARNING_PATTERNS=(
  "rm -rf"
  "git push --force"
  "git reset --hard"
  "git clean -f"
  "chmod -R 777"
  "sudo rm"
  "DROP TABLE"
  "DROP DATABASE"
  "truncate"
)

MATCHED_WARNINGS=""
for pattern in "${WARNING_PATTERNS[@]}"; do
  if echo "$COMMAND" | grep -qi "$pattern"; then
    MATCHED_WARNINGS="${MATCHED_WARNINGS:+$MATCHED_WARNINGS,}$pattern"
    # Mirror the warning on stderr for humans running the hook manually.
    # Claude Code drops this on exit 0 — the audit log is the reliable
    # record (see WARN entries).
    echo "⚠️  Warning: High-risk operation detected: $pattern" >&2
  fi
done

if [ -n "$MATCHED_WARNINGS" ]; then
  log_decision "WARN:$MATCHED_WARNINGS"
  echo "   Command: $COMMAND" >&2
  echo "   Proceeding — review the above warnings before continuing." >&2
else
  log_decision "ALLOW"
fi

# ── Allow ─────────────────────────────────────────────────────────────────────
exit 0
