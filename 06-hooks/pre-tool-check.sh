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
# Output: Exit 0 to allow, exit 2 to block, or print JSON to modify behavior.

# Read the full JSON input from stdin
INPUT=$(cat)

# Extract the command using portable sed (compatible with macOS and Linux)
COMMAND=$(echo "$INPUT" | sed -n 's/.*"command"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/p' | head -1)

# Fall back to the raw input if extraction fails
if [ -z "$COMMAND" ]; then
  COMMAND="$INPUT"
fi

# ── Blocked patterns ──────────────────────────────────────────────────────────
# These commands are blocked unconditionally because they are almost always
# destructive and rarely intentional in an automated context.

BLOCKED_PATTERNS=(
  "rm -rf /"
  "rm -rf \*"
  "dd if=/dev/zero"
  "dd if=/dev/random"
  ":(){:|:&};:"      # Fork bomb
  "mkfs\."           # Filesystem format
  "format c:"        # Windows disk format
)

for pattern in "${BLOCKED_PATTERNS[@]}"; do
  if echo "$COMMAND" | grep -qE "$pattern"; then
    echo "❌ Blocked: Potentially destructive command detected: $pattern"
    echo "   Command: $COMMAND"
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

WARNINGS=0
for pattern in "${WARNING_PATTERNS[@]}"; do
  if echo "$COMMAND" | grep -qi "$pattern"; then
    echo "⚠️  Warning: High-risk operation detected: $pattern"
    WARNINGS=$((WARNINGS + 1))
  fi
done

if [ "$WARNINGS" -gt 0 ]; then
  echo "   Command: $COMMAND"
  echo "   Proceeding — review the above warnings before continuing."
fi

# ── Allow ─────────────────────────────────────────────────────────────────────
exit 0
