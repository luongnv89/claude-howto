#!/bin/bash
# イベント発生時に通知を送信する
# フック：PostToolUse（matcher: Bash）— すべての Bash 呼び出しの後に実行され、コマンドが git push でなければスクリプトは終了する
# 注：Claude Code にネイティブの PostPush イベントは無い。git push をトリガにするには、
# matcher または本スクリプト内の条件で bash コマンド文字列に "git push" が含まれるかを確認する。

# フック入力を読み取り、Bash コマンドが git push でなければ終了する
INPUT=$(cat)
# コマンド文字列を取り出し（\"msg\" のようなエスケープされた引用符も含む）、その中のどこかにある "git push" をコマンド語として照合する
COMMAND=$(echo "$INPUT" | sed -nE 's/.*"command"[[:space:]]*:[[:space:]]*"(([^"\\]|\\.)*)".*/\1/p' | head -1)
printf '%s\n' "$COMMAND" | grep -qE '(^|[^[:alnum:]_-]|\\n)git[[:space:]]+push([^[:alnum:]_-]|$)' || exit 0

REPO_NAME=$(basename "$(git rev-parse --show-toplevel 2>/dev/null)" 2>/dev/null)
COMMIT_MSG=$(git log -1 --pretty=%B 2>/dev/null)
AUTHOR=$(git log -1 --pretty=%an 2>/dev/null)
BRANCH=$(git rev-parse --abbrev-ref HEAD 2>/dev/null)

# 値を JSON 文字列リテラル（前後の引用符を含む）として出力する。
# コミットメッセージ・作者・ブランチは git から取るため、コミットを push できる人なら
# 誰でも中身を決められる。エスケープせずに JSON へ埋め込むと、`x", "text": "...` の
# ようなメッセージでペイロードを書き換えられ、改行やタブでも JSON が壊れる。
# ここでは \ と " に加え、RFC 8259 の要求どおり制御文字 U+0001-U+001F をすべて
# エスケープする（bash の変数は U+0000 を保持できない）。
# 純粋な bash なので、jq も python3 も不要。
json_string() {
  local s=$1 i hex ch
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

echo "📢 チームへ通知を送信しています..."

# Slack Webhook の例（Webhook URL は自分のものに置き換える）
SLACK_WEBHOOK="${SLACK_WEBHOOK_URL:-}"

if [ -n "$SLACK_WEBHOOK" ]; then
  # ペイロードはエスケープ済みの値だけで組み立てる。printf の %s は値をそのまま埋め込む
  # 長いコミットメッセージでも引数サイズの上限を超えないよう、curl には標準入力で渡す
  printf -v PAYLOAD '{
  "text": %s,
  "attachments": [{
    "color": "good",
    "fields": [
      {"title": "ブランチ", "value": %s, "short": true},
      {"title": "作者", "value": %s, "short": true},
      {"title": "コミット", "value": %s}
    ]
  }]
}' \
    "$(json_string "*$REPO_NAME* に新しい push がありました")" \
    "$(json_string "$BRANCH")" \
    "$(json_string "$AUTHOR")" \
    "$(json_string "$COMMIT_MSG")"

  printf '%s' "$PAYLOAD" | curl -X POST "$SLACK_WEBHOOK" \
    -H 'Content-Type: application/json' \
    --data-binary @- \
    --silent --output /dev/null

  echo "✅ Slack 通知を送信しました"
fi

# Discord Webhook の例（Webhook URL は自分のものに置き換える）
DISCORD_WEBHOOK="${DISCORD_WEBHOOK_URL:-}"

if [ -n "$DISCORD_WEBHOOK" ]; then
  printf -v PAYLOAD '{
  "content": %s,
  "embeds": [{
    "title": %s,
    "color": 3066993,
    "fields": [
      {"name": "ブランチ", "value": %s, "inline": true},
      {"name": "作者", "value": %s, "inline": true}
    ]
  }]
}' \
    "$(json_string "**$REPO_NAME に新しい push がありました**")" \
    "$(json_string "$COMMIT_MSG")" \
    "$(json_string "$BRANCH")" \
    "$(json_string "$AUTHOR")"

  printf '%s' "$PAYLOAD" | curl -X POST "$DISCORD_WEBHOOK" \
    -H 'Content-Type: application/json' \
    --data-binary @- \
    --silent --output /dev/null

  echo "✅ Discord 通知を送信しました"
fi

# Email 通知の例（プレーンテキストなので、JSON 用ではなく元の値を使う）
EMAIL_TO="${TEAM_EMAIL:-}"

if [ -n "$EMAIL_TO" ]; then
  echo "$AUTHOR が $REPO_NAME に push しました" | \
    mail -s "Git Push: $BRANCH" "$EMAIL_TO"

  echo "✅ Email 通知を送信しました"
fi

exit 0
