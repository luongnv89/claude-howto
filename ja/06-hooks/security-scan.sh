#!/bin/bash
# ファイル書き込み時のセキュリティスキャン
# フック：PostToolUse:Write
#
# ハードコードされたシークレット・API キー・認証情報をファイルからスキャンする。
# 検出時は additionalContext を介して非ブロッキングの警告を出力する。
#
# 対応：macOS、Linux、Windows（Git Bash）

# Claude Code フックプロトコルに従い、標準入力から JSON を読み取る
INPUT=$(cat)

# sed で file_path を抽出（Windows Git Bash を含む全プラットフォーム互換）
# grep -P（Windows Git Bash で使えない）と python3 依存を避ける
FILE_PATH=$(echo "$INPUT" | sed -n 's/.*"file_path"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/p' | head -1)

if [ -z "$FILE_PATH" ] || [ ! -f "$FILE_PATH" ]; then
  exit 0
fi

# バイナリファイル・ベンダディレクトリ・ビルド成果物はスキップ
case "$FILE_PATH" in
  *.png|*.jpg|*.jpeg|*.gif|*.svg|*.ico|*.woff|*.woff2|*.ttf|*.eot) exit 0 ;;
  */node_modules/*|*/.git/*|*/dist/*|*/build/*) exit 0 ;;
esac

ISSUES=""

# ハードコードされたパスワードの検出
# JSON 形式（"password": "value"）とコード形式（password = 'value'）の両方に対応
# 区切り文字には \\n を使う — JSON の改行エスケープとして有効で、printf でも安全に通る
if grep -qiE '"password"[[:space:]]*:[[:space:]]*"[^"]+"' "$FILE_PATH" 2>/dev/null; then
  ISSUES="${ISSUES}- 警告: ハードコードされたパスワードの可能性を検出\\n"
elif grep -qiE '(password|passwd|pwd)[[:space:]]*=[[:space:]]*'"'"'[^'"'"']+'"'"'' "$FILE_PATH" 2>/dev/null; then
  ISSUES="${ISSUES}- 警告: ハードコードされたパスワードの可能性を検出\\n"
fi

# ハードコードされた API キーの検出
if grep -qiE '"(api[_-]?key|apikey|access[_-]?token)"[[:space:]]*:[[:space:]]*"[^"]+"' "$FILE_PATH" 2>/dev/null; then
  ISSUES="${ISSUES}- 警告: ハードコードされた API キーの可能性を検出\\n"
fi

# ハードコードされたシークレット・トークンの検出
if grep -qiE '(secret|token)[[:space:]]*=[[:space:]]*['"'"'"][^'"'"'"]+['"'"'"]' "$FILE_PATH" 2>/dev/null; then
  ISSUES="${ISSUES}- 警告: ハードコードされたシークレットまたはトークンの可能性を検出\\n"
fi

# 秘密鍵の検出
if grep -q "BEGIN.*PRIVATE KEY" "$FILE_PATH" 2>/dev/null; then
  ISSUES="${ISSUES}- 警告: 秘密鍵を検出\\n"
fi

# AWS アクセスキーの検出
if grep -qE "AKIA[0-9A-Z]{16}" "$FILE_PATH" 2>/dev/null; then
  ISSUES="${ISSUES}- 警告: AWS アクセスキーを検出\\n"
fi

# semgrep が利用可能ならスキャン（JSON 出力との混在を避けるため stdout は抑止）
if command -v semgrep &> /dev/null; then
  semgrep --config=auto "$FILE_PATH" --quiet >/dev/null 2>/dev/null
fi

# trufflehog が利用可能ならスキャン（JSON 出力との混在を避けるため stdout は抑止）
if command -v trufflehog &> /dev/null; then
  trufflehog filesystem "$FILE_PATH" --only-verified --quiet >/dev/null 2>/dev/null
fi

# 問題が見つかったら additionalContext として出力（非ブロッキング警告）
# Claude Code PostToolUse プロトコルが要求する hookSpecificOutput 形式を使う
if [ -n "$ISSUES" ]; then
  # ファイルパスを JSON 用にエスケープ（バックスラッシュとダブルクォート）
  # ISSUES は既に \\n を区切り文字に用いている（有効な JSON エスケープ）— ダブルクォートのみエスケープする
  SAFE_PATH=$(printf '%s' "$FILE_PATH" | sed 's/\\/\\\\/g; s/"/\\"/g')
  SAFE_ISSUES=$(printf '%s' "$ISSUES" | sed 's/"/\\"/g')
  printf '{"hookSpecificOutput": {"hookEventName": "PostToolUse", "additionalContext": "セキュリティスキャンで %s に問題を検出しました:\\n%s環境変数の使用を検討してください。"}}' "$SAFE_PATH" "$SAFE_ISSUES"
fi

exit 0
