#!/bin/bash
# Send notifications on events
# Hook: PostToolUse (matcher: Bash) — runs after every Bash call; the script exits unless the command is a git push
# Note: Claude Code has no native PostPush event. To trigger on git push, check the bash command
# string for "git push" using a matcher or conditional logic within this script.

# Read the hook input and exit unless the Bash command is a git push
INPUT=$(cat)
# Extract the command (escaped quotes like \"msg\" are kept) and match "git push" as a command word anywhere in it
COMMAND=$(echo "$INPUT" | sed -nE 's/.*"command"[[:space:]]*:[[:space:]]*"(([^"\\]|\\.)*)".*/\1/p' | head -1)
printf '%s\n' "$COMMAND" | grep -qE '(^|[^[:alnum:]_-]|\\n)git[[:space:]]+push([^[:alnum:]_-]|$)' || exit 0

REPO_NAME=$(basename $(git rev-parse --show-toplevel 2>/dev/null) 2>/dev/null)
# Escape values before interpolating them into the JSON payloads below.
# A commit message is attacker-influenceable in shared repos (anyone whose
# commit gets pushed), and a raw quote or backslash in it would break out of
# its JSON string and inject new fields into the payload. Raw newlines would
# make the payload invalid JSON outright (commit messages are multi-line),
# so flatten them to spaces.
json_escape() {
  printf '%s' "$1" | sed -e 's/\\/\\\\/g' -e 's/"/\\"/g' | tr '\n' ' '
}
REPO_NAME=$(json_escape "$REPO_NAME")
COMMIT_MSG=$(json_escape "$COMMIT_MSG")
AUTHOR=$(json_escape "$AUTHOR")
BRANCH=$(json_escape "$BRANCH")
COMMIT_MSG=$(git log -1 --pretty=%B 2>/dev/null)
AUTHOR=$(git log -1 --pretty=%an 2>/dev/null)
BRANCH=$(git rev-parse --abbrev-ref HEAD 2>/dev/null)

echo "📢 Sending notification to team..."

# Slack webhook example (replace with your webhook URL)
SLACK_WEBHOOK="${SLACK_WEBHOOK_URL:-}"

if [ -n "$SLACK_WEBHOOK" ]; then
  curl -X POST "$SLACK_WEBHOOK" \
    -H 'Content-Type: application/json' \
    -d "{
      \"text\": \"New push to *$REPO_NAME*\",
      \"attachments\": [{
        \"color\": \"good\",
        \"fields\": [
          {\"title\": \"Branch\", \"value\": \"$BRANCH\", \"short\": true},
          {\"title\": \"Author\", \"value\": \"$AUTHOR\", \"short\": true},
          {\"title\": \"Commit\", \"value\": \"$COMMIT_MSG\"}
        ]
      }]
    }" \
    --silent --output /dev/null

  echo "✅ Slack notification sent"
fi

# Discord webhook example (replace with your webhook URL)
DISCORD_WEBHOOK="${DISCORD_WEBHOOK_URL:-}"

if [ -n "$DISCORD_WEBHOOK" ]; then
  curl -X POST "$DISCORD_WEBHOOK" \
    -H 'Content-Type: application/json' \
    -d "{
      \"content\": \"**New push to $REPO_NAME**\",
      \"embeds\": [{
        \"title\": \"$COMMIT_MSG\",
        \"color\": 3066993,
        \"fields\": [
          {\"name\": \"Branch\", \"value\": \"$BRANCH\", \"inline\": true},
          {\"name\": \"Author\", \"value\": \"$AUTHOR\", \"inline\": true}
        ]
      }]
    }" \
    --silent --output /dev/null

  echo "✅ Discord notification sent"
fi

# Email notification example
EMAIL_TO="${TEAM_EMAIL:-}"

if [ -n "$EMAIL_TO" ]; then
  echo "New push to $REPO_NAME by $AUTHOR" | \
    mail -s "Git Push: $BRANCH" "$EMAIL_TO"

  echo "✅ Email notification sent"
fi

exit 0
