#!/bin/bash
# Bash コマンドの事前安全チェック
# フック：PreToolUse（matcher: Bash）
#
# このフックは Bash ツールが実行されるたびに走り、破壊的またはハイリスクなシェル
# コマンドをブロック／警告する。
#
# セットアップ：
#   cp 06-hooks/pre-tool-check.sh ~/.claude/hooks/
#   chmod +x ~/.claude/hooks/pre-tool-check.sh
#
# ~/.claude/settings.json の設定例：
#   {
#     "hooks": {
#       "PreToolUse": [
#         {
#           "matcher": "Bash",
#           "hooks": [
#             {
#               "type": "command",
#               "command": "~/.claude/hooks/pre-tool-check.sh"
#             }
#           ]
#         }
#       ]
#     }
#   }
#
# 入力：以下の形式の JSON を標準入力から受け取る：
#   { "tool_name": "Bash", "tool_input": { "command": "..." } }
#
# 出力規約（Claude Code フックプロトコルに準拠）：
#   - exit 0 → 許可。stdout には JSON（hookSpecificOutput）を出力可能。stderr は
#     黙って捨てられるため、stderr への警告出力は表示されない。許可された
#     コマンドの可観測性を担保するには、監査ログファイルに書き出す。
#   - exit 2 → ブロック。stderr が Claude にブロック理由として返される。
#     ブロック理由を説明する echo は必ず `>&2` で stderr にリダイレクトする。
#     さもないと Claude Code は「No stderr output」と報告する。
#
# 監査ログ：すべての呼び出しを以下に記録する
#   $CLAUDE_PROJECT_DIR/.claude/hooks/audit.log
# 判定（BLOCK/WARN/ALLOW）と一緒に保存するため、stderr が Claude Code に捨てられる
# WARN 階層のマッチも観測できる。

# 標準入力から JSON 全体を読み取る
INPUT=$(cat)

# 移植性のある sed でコマンドを抽出（macOS / Linux 双方互換）
COMMAND=$(echo "$INPUT" | sed -n 's/.*"command"[[:space:]]*:[[:space:]]*"\([^"]*\)".*/\1/p' | head -1)

# 抽出に失敗した場合は生の入力にフォールバック
if [ -z "$COMMAND" ]; then
  COMMAND="$INPUT"
fi

# ── 監査ログ ─────────────────────────────────────────────────────────────────
# すべての呼び出しを最終判定とともに記録する。Claude Code は exit 0 のときに
# stderr を黙って捨てるため、WARN 階層を確実に観測できる唯一の手段がこれ。
# Claude Code 外（ローカルテスト等）では $(pwd) にフォールバックする。
LOG_DIR="${CLAUDE_PROJECT_DIR:-$(pwd)}/.claude/hooks"
LOG_FILE="$LOG_DIR/audit.log"
mkdir -p "$LOG_DIR" 2>/dev/null
log_decision() {
  echo "$(date -u +%FT%TZ) [$1] $COMMAND" >> "$LOG_FILE"
}

# ── ブロックパターン ─────────────────────────────────────────────────────────
# 自動化された文脈ではほぼ確実に破壊的かつ意図的でないため、無条件にブロックする。

BLOCKED_PATTERNS=(
  # `rm -rf /` を厳密に判定するため、`/` の後に空白か行末を要求する。
  # 部分一致だと `rm -rf /tmp/foo` のような正当ケースを誤検出してしまう。
  "rm -rf /([[:space:]]|$)"
  "rm -rf \*"
  "dd if=/dev/zero"
  "dd if=/dev/random"
  ":\(\)\{:\|:&\};:"  # フォーク爆弾（正規表現メタ文字をエスケープ）
  "mkfs\."           # ファイルシステムのフォーマット
  "format c:"        # Windows のディスクフォーマット
)

for pattern in "${BLOCKED_PATTERNS[@]}"; do
  if echo "$COMMAND" | grep -qE "$pattern"; then
    log_decision "BLOCK:$pattern"
    # ここの echo は必ず stderr へ — Claude Code は exit 2 のとき stderr を
    # ブロック理由として表面化する。stdout に書くと「No stderr output」と表示される。
    echo "❌ ブロック：破壊的な可能性のあるコマンドを検出: $pattern" >&2
    echo "   コマンド: $COMMAND" >&2
    exit 2
  fi
done

# ── 警告パターン ─────────────────────────────────────────────────────────────
# リスクは高いが意図的な場合もある。警告を記録して許可する。

WARNING_PATTERNS=(
  "rm -rf"
  "git push --force"
  "git reset --hard"
  "git clean -f"
  "chmod -R 777"
  "sudo rm"
  "DROP TABLE"
  "DROP DATABASE"
  "truncate"
)

MATCHED_WARNINGS=""
for pattern in "${WARNING_PATTERNS[@]}"; do
  if echo "$COMMAND" | grep -qi "$pattern"; then
    MATCHED_WARNINGS="${MATCHED_WARNINGS:+$MATCHED_WARNINGS,}$pattern"
    # フックを手動実行する人間向けに stderr へも警告を出す。
    # Claude Code は exit 0 のときこれを捨てるため、確実な記録は監査ログ
    # （WARN エントリ）参照のこと。
    echo "⚠️  警告：ハイリスクな操作を検出: $pattern" >&2
  fi
done

if [ -n "$MATCHED_WARNINGS" ]; then
  log_decision "WARN:$MATCHED_WARNINGS"
  echo "   コマンド: $COMMAND" >&2
  echo "   続行します — 上記の警告を確認してから続けてください。" >&2
else
  log_decision "ALLOW"
fi

# ── 許可 ────────────────────────────────────────────────────────────────────
exit 0
