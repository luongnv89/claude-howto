#!/bin/bash
# すべての bash コマンドを記録する
# フック：PostToolUse:Bash
#
# 標準入力の JSON から実行コマンドを読み取り、ファイルに記録する。
#
# 対応：macOS、Linux、Windows（Git Bash）

# Claude Code フックプロトコルに従い、標準入力から JSON を読み取る
INPUT=$(cat)

# tool_input から bash コマンドを抽出
# 注：sed の [^"]* は JSON 内のエスケープされた引用符で停止する。ダブルクォートを
# 含むコマンドの場合、最初の \" までしかキャプチャできない。これは sed ベースの
# JSON パースの既知の制約だが、ロギング用途としては許容範囲。
COMMAND=$(echo "$INPUT" | sed -n 's/.*"command"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/p' | head -1)

if [ -z "$COMMAND" ]; then
  exit 0
fi

TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S")
LOGFILE="$HOME/.claude/bash-commands.log"

# ログディレクトリが無ければ作成
mkdir -p "$(dirname "$LOGFILE")"

# コマンドを記録
echo "[$TIMESTAMP] $COMMAND" >> "$LOGFILE"

exit 0
