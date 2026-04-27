#!/bin/bash
# ユーザプロンプトを検証する
# フック：UserPromptSubmit
#
# 標準入力の JSON からユーザプロンプトを読み取り、危険な操作をブロックする。
#
# 対応：macOS、Linux、Windows（Git Bash）

# Claude Code フックプロトコルに従い、標準入力から JSON を読み取る
INPUT=$(cat)

# JSON 入力からプロンプト本文を抽出
# Claude Code は UserPromptSubmit を "user_prompt" で送る（無ければ "prompt" にフォールバック）
PROMPT=$(echo "$INPUT" | sed -n 's/.*"user_prompt"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/p' | head -1)
if [ -z "$PROMPT" ]; then
  PROMPT=$(echo "$INPUT" | sed -n 's/.*"prompt"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/p' | head -1)
fi

if [ -z "$PROMPT" ]; then
  exit 0
fi

# 危険な操作の検出
DANGEROUS_PATTERNS=(
  "rm -rf /"
  "delete database"
  "drop database"
  "format disk"
  "dd if="
)

for pattern in "${DANGEROUS_PATTERNS[@]}"; do
  if echo "$PROMPT" | grep -qi "$pattern"; then
    printf '{"decision": "block", "reason": "危険な操作を検出: %s"}' "$pattern"
    exit 0
  fi
done

# 本番デプロイの検出
if echo "$PROMPT" | grep -qiE "(deploy|push).*production"; then
  if [ ! -f ".deployment-approved" ]; then
    echo '{"decision": "block", "reason": "本番デプロイには承認が必要です。続行するには .deployment-approved ファイルを作成してください。"}'
    exit 0
  fi
fi

# 特定操作におけるコンテキスト要件のチェック
if echo "$PROMPT" | grep -qi "refactor"; then
  if [ ! -d "tests" ] && [ ! -d "test" ]; then
    printf '{"additionalContext": "警告: テスト無しのリファクタリングはリスクを伴います。先にテストを書くことを検討してください。"}'
  fi
fi

exit 0
