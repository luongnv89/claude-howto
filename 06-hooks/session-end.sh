#!/usr/bin/env bash
# SessionEnd hook: prompts for modules worked on, then appends a session record
# to ~/.claude-howto-progress.json for persistent learning progress tracking.
#
# Fires once when the Claude Code session terminates — not after every response.
# Uses /dev/tty for interactive input since stdin carries the hook's JSON payload.
#
# Install: add to .claude/settings.json under the "SessionEnd" event (see below).

PROGRESS_FILE="$HOME/.claude-howto-progress.json"

# Guard: only run inside this repo
if [[ "$CLAUDE_PROJECT_DIR" != *"claude-howto"* ]] && [[ "$PWD" != *"claude-howto"* ]]; then
  exit 0
fi

# Create progress file if it doesn't exist
if [ ! -f "$PROGRESS_FILE" ]; then
  echo '{"sessions":[]}' > "$PROGRESS_FILE"
fi

DATE=$(date +"%Y-%m-%d")
TIME=$(date +"%H:%M")

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo " Claude Code — Learning Session End"
echo " $DATE $TIME"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo " Which modules did you work on? (e.g. 06,07 or press Enter to skip)"
echo " 01=Slash  02=Memory  03=Skills  04=Subagents  05=MCP"
echo " 06=Hooks  07=Plugins 08=Checkpoints 09=Advanced 10=CLI"
echo ""
printf " > "
read -r INPUT </dev/tty

if [ -z "$INPUT" ] || [ "$INPUT" = "skip" ]; then
  echo " Skipped — no session logged."
  echo ""
  exit 0
fi

# Map short numbers to module names
MODULES_JSON=$(echo "$INPUT" | tr ',' '\n' | tr -d ' ' | while read -r m; do
  case "$m" in
    01) echo '"01-slash-commands"' ;;
    02) echo '"02-memory"' ;;
    03) echo '"03-skills"' ;;
    04) echo '"04-subagents"' ;;
    05) echo '"05-mcp"' ;;
    06) echo '"06-hooks"' ;;
    07) echo '"07-plugins"' ;;
    08) echo '"08-checkpoints"' ;;
    09) echo '"09-advanced-features"' ;;
    10) echo '"10-cli"' ;;
    *)  echo "\"$m\"" ;;
  esac
done | paste -sd ',' -)

printf " Notes? (optional, press Enter to skip): "
read -r NOTES </dev/tty

SESSION="{\"date\":\"$DATE\",\"time\":\"$TIME\",\"modules\":[${MODULES_JSON}],\"notes\":\"${NOTES}\"}"

# Append session using Python (available on macOS/Linux by default)
python3 - "$PROGRESS_FILE" "$SESSION" <<'PYEOF'
import sys, json

path, new_session = sys.argv[1], json.loads(sys.argv[2])

with open(path, 'r') as f:
    data = json.load(f)

data.setdefault('sessions', []).append(new_session)

with open(path, 'w') as f:
    json.dump(data, f, indent=2)
PYEOF

echo ""
echo " Saved to $PROGRESS_FILE"
[ -n "$NOTES" ] && echo " Notes: $NOTES"
echo ""
