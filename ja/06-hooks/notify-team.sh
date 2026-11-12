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

# $1 の先頭から最大 $2 バイトを取り出す。UTF-8 の文字の途中では切らない。
# どのロケールでも同じ結果になるよう、バイト単位（LC_ALL=C）で切り、
# 途中で切れた文字の先頭バイトと継続バイトを捨てる。結果は正しい UTF-8 のままなので、
# ペイロードも正しい JSON のまま。
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

# Slack はメッセージを 4,000 文字以内にするよう勧めており、40,000 文字を超えると切り捨てる。
# 通知にはコミットメッセージの冒頭があれば十分。悪意あるコミットが引用符や制御文字で
# 埋め尽くすと json_string の処理時間は入力長以上の勢いで伸びるが、上限を設ければ抑えられる。
COMMIT_MSG=$(truncate_utf8 "$COMMIT_MSG" 4000)
AUTHOR=$(truncate_utf8 "$AUTHOR" 256)
BRANCH=$(truncate_utf8 "$BRANCH" 256)

# 値を JSON 文字列リテラル（前後の引用符を含む）として出力する。
# コミットメッセージ・作者・ブランチは git から取るため、コミットを push できる人なら
# 誰でも中身を決められる。エスケープせずに JSON へ埋め込むと、`x", "text": "...` の
# ようなメッセージでペイロードを書き換えられ、改行やタブでも JSON が壊れる。
# ここでは \ と " に加え、RFC 8259 の要求どおり制御文字 U+0001-U+001F をすべて
# エスケープする（bash の変数は U+0000 を保持できない）。
# 純粋な bash なので、jq も python3 も不要。LC_ALL=C で置換を UTF-8 の文字単位ではなく
# バイト単位にすると、非 ASCII のテキストで数百倍速くなる。\ と " と制御文字のバイトは
# UTF-8 の多バイト文字の中には現れないので、バイト単位でも安全。
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
