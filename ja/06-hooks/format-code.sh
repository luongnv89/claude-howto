#!/bin/bash
# 書き込み後にコードを自動整形する
# フック：PostToolUse:Write
#
# 標準入力の JSON から対象ファイルパスを読み取り、Claude がファイルを書き込んだ
# 後に、そのファイルに対して適切なフォーマッタをインプレースで実行する。
#
# 対応：macOS、Linux、Windows（Git Bash）

# Claude Code フックプロトコルに従い、標準入力から JSON を読み取る
INPUT=$(cat)

# sed で file_path を抽出（全プラットフォーム互換）
FILE_PATH=$(echo "$INPUT" | sed -n 's/.*"file_path"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/p' | head -1)

if [ -z "$FILE_PATH" ] || [ ! -f "$FILE_PATH" ]; then
  exit 0
fi

# ファイル種別を判定して整形
case "$FILE_PATH" in
  *.js|*.jsx|*.ts|*.tsx)
    if command -v prettier &> /dev/null; then
      prettier --write "$FILE_PATH" 2>/dev/null
    fi
    ;;
  *.py)
    if command -v black &> /dev/null; then
      black "$FILE_PATH" 2>/dev/null
    fi
    ;;
  *.go)
    if command -v gofmt &> /dev/null; then
      gofmt -w "$FILE_PATH" 2>/dev/null
    fi
    ;;
  *.rs)
    if command -v rustfmt &> /dev/null; then
      rustfmt "$FILE_PATH" 2>/dev/null
    fi
    ;;
  *.java)
    if command -v google-java-format &> /dev/null; then
      google-java-format -i "$FILE_PATH" 2>/dev/null
    fi
    ;;
esac

exit 0
