#!/bin/bash
# Log all bash commands
# Hook: PostToolUse:Bash
#
# Reads the executed command from stdin JSON and logs it to a file.
#
# Compatible with: macOS, Linux, Windows (Git Bash)

# Read JSON input from stdin (Claude Code hook protocol)
INPUT=$(cat)

# Extract the bash command from tool_input
COMMAND=$(echo "$INPUT" | sed -n 's/.*"command"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/p' | head -1)

if [ -z "$COMMAND" ]; then
  exit 0
fi

TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S")
LOGFILE="$HOME/.claude/bash-commands.log"

# Create log directory if it doesn't exist
mkdir -p "$(dirname "$LOGFILE")"

# Log the command
echo "[$TIMESTAMP] $COMMAND" >> "$LOGFILE"

exit 0
