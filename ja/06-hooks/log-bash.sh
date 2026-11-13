#!/bin/bash
# すべての bash コマンドを記録する
# フック：PostToolUse（matcher: Bash）
#
# 標準入力の JSON から実行コマンドを読み取り、ファイルに記録する。
#
# 対応：macOS、Linux、Windows（Git Bash）

# Claude Code フックプロトコルに従い、標準入力から JSON を読み取る
INPUT=$(cat)

# tool_input から bash コマンドを抽出
# パターンはエスケープされた引用符（\"）を読み飛ばすため、ダブルクォートを含む文字列も
# 全体が記録される。コマンドは JSON 上の表記のまま記録する（\" は \" のまま、改行は
# \n と書かれる）ので、各エントリは 1 行に収まる。
COMMAND=$(echo "$INPUT" | sed -nE 's/.*"command"[[:space:]]*:[[:space:]]*"(([^"\\]|\\.)*)".*/\1/p' | head -1)

if [ -z "$COMMAND" ]; then
  exit 0
fi

TIMESTAMP=$(date "+%Y-%m-%d %H:%M:%S")
LOGFILE="$HOME/.claude/bash-commands.log"

# ログディレクトリが無ければ作成する。
# ログにはコマンド引数として渡されたシークレット（トークン、パスワード、API キー）が
# 含まれ得るため、新しいファイルとディレクトリは所有者のみアクセス可能な権限で作成し、
# 旧バージョンが作成した既存のログも 0600 に絞る。
umask 077
mkdir -p "$(dirname "$LOGFILE")"
touch "$LOGFILE"
chmod 600 "$LOGFILE"

# コマンドを記録
echo "[$TIMESTAMP] $COMMAND" >> "$LOGFILE"

exit 0
