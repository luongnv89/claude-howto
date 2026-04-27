#!/usr/bin/env bash
# SessionEnd フック：取り組んだモジュールを尋ね、~/.claude-howto-progress.json に
# セッション記録を追記して、学習進捗を永続的に追跡する。
#
# Claude Code セッション終了時に 1 回だけ発火する（応答ごとではない）。
# 標準入力にはフックの JSON ペイロードが流れているため、対話入力には /dev/tty を使う。
#
# 導入：.claude/settings.json の "SessionEnd" イベントに登録する（下記参照）。

PROGRESS_FILE="$HOME/.claude-howto-progress.json"

# ガード：このリポジトリ内でのみ動かす
if [[ "$CLAUDE_PROJECT_DIR" != *"claude-howto"* ]] && [[ "$PWD" != *"claude-howto"* ]]; then
  exit 0
fi

# 進捗ファイルが無ければ作成
if [ ! -f "$PROGRESS_FILE" ]; then
  echo '{"sessions":[]}' > "$PROGRESS_FILE"
fi

DATE=$(date +"%Y-%m-%d")
TIME=$(date +"%H:%M")

echo ""
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo " Claude Code — 学習セッション終了"
echo " $DATE $TIME"
echo "━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━"
echo ""
echo " どのモジュールに取り組みましたか？（例：06,07 / Enter でスキップ）"
echo " 01=Slash  02=Memory  03=Skills  04=Subagents  05=MCP"
echo " 06=Hooks  07=Plugins 08=Checkpoints 09=Advanced 10=CLI"
echo ""
printf " > "
read -r INPUT </dev/tty

if [ -z "$INPUT" ] || [ "$INPUT" = "skip" ]; then
  echo " スキップ — セッションは記録しません。"
  echo ""
  exit 0
fi

# 短縮番号をモジュール名にマップする（bash 3.2 がパースできないため pipeline+while を避ける）
IFS=',' read -ra PARTS <<< "$INPUT"
MODULES_JSON=""
for m in "${PARTS[@]}"; do
  m="${m// /}"  # 空白を除去
  case "$m" in
    01) label='"01-slash-commands"' ;;
    02) label='"02-memory"' ;;
    03) label='"03-skills"' ;;
    04) label='"04-subagents"' ;;
    05) label='"05-mcp"' ;;
    06) label='"06-hooks"' ;;
    07) label='"07-plugins"' ;;
    08) label='"08-checkpoints"' ;;
    09) label='"09-advanced-features"' ;;
    10) label='"10-cli"' ;;
    *)  label="\"$m\"" ;;
  esac
  MODULES_JSON="${MODULES_JSON:+$MODULES_JSON,}$label"
done

printf " メモ？（任意、Enter でスキップ）: "
read -r NOTES </dev/tty

# NOTES は別引数で Python に渡し、JSON エスケープを Python 側に任せる。
# メモに引用符やバックスラッシュが含まれても JSON が壊れないようにするため。
python3 - "$PROGRESS_FILE" "$DATE" "$TIME" "$MODULES_JSON" "$NOTES" <<'PYEOF'
import sys, json

path, date, time_str, modules_raw, notes = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5]

new_session = {
    "date": date,
    "time": time_str,
    "modules": json.loads(f"[{modules_raw}]") if modules_raw else [],
    "notes": notes,
}

with open(path, 'r') as f:
    data = json.load(f)

data.setdefault('sessions', []).append(new_session)

with open(path, 'w') as f:
    json.dump(data, f, indent=2)
PYEOF

echo ""
echo " $PROGRESS_FILE に保存しました"
[ -n "$NOTES" ] && echo " メモ: $NOTES"
echo ""
