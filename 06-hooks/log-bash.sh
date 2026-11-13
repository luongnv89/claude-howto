#!/bin/bash
# Log all bash commands
# Hook: PostToolUse (matcher: Bash)
#
# Reads the executed command from stdin JSON and logs it to a file.
#
# Compatible with: macOS, Linux, Windows (Git Bash)

# Read JSON input from stdin (Claude Code hook protocol)
INPUT=$(cat)

# Extract the bash command from tool_input
# The pattern skips escaped quotes (\"), so double-quoted strings are logged in
# full. The command is logged as it appears in the JSON: \" stays \" and a
# newline is written as \n, which keeps each entry on one line.
COMMAND=$(echo "$INPUT" | sed -nE 's/.*"command"[[:space:]]*:[[:space:]]*"(([^"\\]|\\.)*)".*/\1/p' | head -1)

if [ -z "$COMMAND" ]; then
  exit 0
fi

TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S")
LOGFILE="$HOME/.claude/bash-commands.log"

# Create log directory if it doesn't exist.
# The log can contain secrets passed as command arguments (tokens, passwords,
# API keys), so new files and directories are created owner-only, and an
# existing log from an older version is tightened to 0600.
umask 077
mkdir -p "$(dirname "$LOGFILE")"
touch "$LOGFILE"
chmod 600 "$LOGFILE"

# Log the command
echo "[$TIMESTAMP] $COMMAND" >> "$LOGFILE"

exit 0
