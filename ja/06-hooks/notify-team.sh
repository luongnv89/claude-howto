#!/bin/bash
# イベント発生時に通知を送信する
# フック：PostToolUse（matcher: Bash）— bash コマンドの後に実行し、スクリプト側で git push を判別する
# 注：Claude Code にネイティブの PostPush イベントは無い。git push をトリガにするには、
# matcher または本スクリプト内の条件で bash コマンド文字列に "git push" が含まれるかを確認する。

REPO_NAME=$(basename $(git rev-parse --show-toplevel 2>/dev/null) 2>/dev/null)
COMMIT_MSG=$(git log -1 --pretty=%B 2>/dev/null)
AUTHOR=$(git log -1 --pretty=%an 2>/dev/null)
BRANCH=$(git rev-parse --abbrev-ref HEAD 2>/dev/null)

echo "📢 チームへ通知を送信しています..."

# Slack Webhook の例（Webhook URL は自分のものに置き換える）
SLACK_WEBHOOK="${SLACK_WEBHOOK_URL:-}"

if [ -n "$SLACK_WEBHOOK" ]; then
  curl -X POST "$SLACK_WEBHOOK" \
    -H 'Content-Type: application/json' \
    -d "{
      \"text\": \"*$REPO_NAME* に新しい push がありました\",
      \"attachments\": [{
        \"color\": \"good\",
        \"fields\": [
          {\"title\": \"ブランチ\", \"value\": \"$BRANCH\", \"short\": true},
          {\"title\": \"作者\", \"value\": \"$AUTHOR\", \"short\": true},
          {\"title\": \"コミット\", \"value\": \"$COMMIT_MSG\"}
        ]
      }]
    }" \
    --silent --output /dev/null

  echo "✅ Slack 通知を送信しました"
fi

# Discord Webhook の例（Webhook URL は自分のものに置き換える）
DISCORD_WEBHOOK="${DISCORD_WEBHOOK_URL:-}"

if [ -n "$DISCORD_WEBHOOK" ]; then
  curl -X POST "$DISCORD_WEBHOOK" \
    -H 'Content-Type: application/json' \
    -d "{
      \"content\": \"**$REPO_NAME に新しい push がありました**\",
      \"embeds\": [{
        \"title\": \"$COMMIT_MSG\",
        \"color\": 3066993,
        \"fields\": [
          {\"name\": \"ブランチ\", \"value\": \"$BRANCH\", \"inline\": true},
          {\"name\": \"作者\", \"value\": \"$AUTHOR\", \"inline\": true}
        ]
      }]
    }" \
    --silent --output /dev/null

  echo "✅ Discord 通知を送信しました"
fi

# Email 通知の例
EMAIL_TO="${TEAM_EMAIL:-}"

if [ -n "$EMAIL_TO" ]; then
  echo "$AUTHOR が $REPO_NAME に push しました" | \
    mail -s "Git Push: $BRANCH" "$EMAIL_TO"

  echo "✅ Email 通知を送信しました"
fi

exit 0
