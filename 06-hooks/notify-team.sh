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

REPO_NAME=$(basename "$(git rev-parse --show-toplevel 2>/dev/null)" 2>/dev/null)
COMMIT_MSG=$(git log -1 --pretty=%B 2>/dev/null)
AUTHOR=$(git log -1 --pretty=%an 2>/dev/null)
BRANCH=$(git rev-parse --abbrev-ref HEAD 2>/dev/null)

# Keep at most $2 bytes of $1, without splitting a UTF-8 character.
# The cut counts bytes (LC_ALL=C) so it works in any locale, then drops the
# lead and continuation bytes of a character it cut through, so the result
# is still valid UTF-8 and the payload is still valid JSON.
truncate_utf8() {
  local LC_ALL=C s=$1
  if (( ${#s} > $2 )); then
    s=${s:0:$2}
    case $s in
      *[$'\xc0'-$'\xff']) s=${s%?} ;;
      *[$'\xe0'-$'\xff'][$'\x80'-$'\xbf']) s=${s%??} ;;
      *[$'\xf0'-$'\xff'][$'\x80'-$'\xbf'][$'\x80'-$'\xbf']) s=${s%???} ;;
    esac
  fi
  printf '%s' "$s"
}

# Slack's chat.postMessage docs recommend keeping `text` under 4,000 characters
# and truncate past 40,000 (the incoming-webhook docs give no limit for the
# attachment field used here), so a notification only needs the start of the
# commit message. The caps also bound the time json_string takes, which grows
# faster than the input when a hostile commit fills it with quotes or control
# characters.
COMMIT_MSG=$(truncate_utf8 "$COMMIT_MSG" 4000)
AUTHOR=$(truncate_utf8 "$AUTHOR" 256)
BRANCH=$(truncate_utf8 "$BRANCH" 256)

# Print a value as a JSON string literal, surrounding quotes included.
# The commit message, author and branch come from git, so anyone who can push
# a commit controls them. Pasting them into the JSON unescaped would let a
# message like `x", "text": "...` rewrite the payload, and a newline or tab
# would make it invalid. This escapes \ and " plus every control character
# U+0001-U+001F (a bash variable can't hold U+0000), as RFC 8259 requires.
# Pure bash, so the hook doesn't need jq or python3. LC_ALL=C makes the
# replacements compare bytes instead of decoding UTF-8 characters, which is
# hundreds of times faster on non-ASCII text. That is safe because \, " and the
# control bytes never occur inside a multibyte UTF-8 character.
json_string() {
  local LC_ALL=C s=$1 i hex ch
  s=${s//\\/\\\\}
  s=${s//\"/\\\"}
  s=${s//$'\n'/\\n}
  s=${s//$'\r'/\\r}
  s=${s//$'\t'/\\t}
  for ((i = 1; i < 32; i++)); do
    printf -v hex '%02x' "$i"
    printf -v ch '%b' "\\x$hex"
    s=${s//"$ch"/\\u00$hex}
  done
  printf '"%s"' "$s"
}

echo "📢 Sending notification to team..."

# Slack webhook example (replace with your webhook URL)
SLACK_WEBHOOK="${SLACK_WEBHOOK_URL:-}"

if [ -n "$SLACK_WEBHOOK" ]; then
  # Build the payload from escaped values only; printf's %s copies them as-is
  # and it goes to curl on stdin, so a long commit message can't hit the argument size limit
  printf -v PAYLOAD '{
  "text": %s,
  "attachments": [{
    "color": "good",
    "fields": [
      {"title": "Branch", "value": %s, "short": true},
      {"title": "Author", "value": %s, "short": true},
      {"title": "Commit", "value": %s}
    ]
  }]
}' \
    "$(json_string "New push to *$REPO_NAME*")" \
    "$(json_string "$BRANCH")" \
    "$(json_string "$AUTHOR")" \
    "$(json_string "$COMMIT_MSG")"

  printf '%s' "$PAYLOAD" | curl -X POST "$SLACK_WEBHOOK" \
    -H 'Content-Type: application/json' \
    --data-binary @- \
    --silent --output /dev/null

  echo "✅ Slack notification sent"
fi

# Discord webhook example (replace with your webhook URL)
DISCORD_WEBHOOK="${DISCORD_WEBHOOK_URL:-}"

if [ -n "$DISCORD_WEBHOOK" ]; then
  printf -v PAYLOAD '{
  "content": %s,
  "embeds": [{
    "title": %s,
    "color": 3066993,
    "fields": [
      {"name": "Branch", "value": %s, "inline": true},
      {"name": "Author", "value": %s, "inline": true}
    ]
  }]
}' \
    "$(json_string "**New push to $REPO_NAME**")" \
    "$(json_string "$COMMIT_MSG")" \
    "$(json_string "$BRANCH")" \
    "$(json_string "$AUTHOR")"

  printf '%s' "$PAYLOAD" | curl -X POST "$DISCORD_WEBHOOK" \
    -H 'Content-Type: application/json' \
    --data-binary @- \
    --silent --output /dev/null

  echo "✅ Discord notification sent"
fi

# Email notification example (plain text, so it uses the raw values, not JSON)
EMAIL_TO="${TEAM_EMAIL:-}"

if [ -n "$EMAIL_TO" ]; then
  echo "New push to $REPO_NAME by $AUTHOR" | \
    mail -s "Git Push: $BRANCH" "$EMAIL_TO"

  echo "✅ Email notification sent"
fi

exit 0
