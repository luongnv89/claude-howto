#!/bin/bash
# マニフェストファイルが変更された後に、依存関係の既知の脆弱性をチェックする。
# フック：PostToolUse:Write

FILE=$1

if [ -z "$FILE" ]; then
  echo "使い方: $0 <file_path>"
  exit 0
fi

# マッチング用に basename を使う — $1 は絶対パスの可能性がある
BASENAME=$(basename "$FILE")

# 依存関係マニフェストが書き換えられた場合のみ実行
case "$BASENAME" in
  package.json|package-lock.json|yarn.lock|pnpm-lock.yaml| \
  requirements.txt|Pipfile|Pipfile.lock|pyproject.toml| \
  go.mod|go.sum| \
  Cargo.toml|Cargo.lock| \
  Gemfile|Gemfile.lock| \
  composer.json|composer.lock| \
  pom.xml|build.gradle|build.gradle.kts)
    echo "📦 依存関係マニフェストを更新: $FILE — 脆弱性をスキャンしています..."
    ;;
  *)
    exit 0
    ;;
esac

ISSUES_FOUND=0

# ── npm / yarn / pnpm ────────────────────────────────────────────────────────
if [[ "$BASENAME" == package*.json || "$BASENAME" == yarn.lock || "$BASENAME" == pnpm-lock.yaml ]]; then
  if command -v npm &>/dev/null; then
    echo "🔍 npm audit を実行中..."
    if ! npm audit --audit-level=high --json 2>/dev/null | \
        python3 -c "
import sys, json
data = json.load(sys.stdin)
vulns = data.get('metadata', {}).get('vulnerabilities', {})
high = vulns.get('high', 0) + vulns.get('critical', 0)
if high:
    print(f'  ⚠️  {high} 件の高／致命的な npm 脆弱性を検出。実行: npm audit fix')
    sys.exit(1)
" 2>/dev/null; then
      ISSUES_FOUND=1
    else
      echo "  ✅ 高／致命的な npm 脆弱性なし"
    fi
  fi

  if command -v yarn &>/dev/null && [[ "$BASENAME" == yarn.lock ]]; then
    echo "🔍 yarn audit を実行中..."
    if ! yarn audit --level high --json 2>/dev/null | \
        grep -q '"type":"auditAdvisory"' 2>/dev/null; then
      echo "  ✅ 高レベルの yarn 脆弱性なし"
    else
      echo "  ⚠️  yarn audit が脆弱性を検出。実行: yarn audit --level high"
      ISSUES_FOUND=1
    fi
  fi
fi

# ── Python ───────────────────────────────────────────────────────────────────
if [[ "$BASENAME" == requirements.txt || "$BASENAME" == Pipfile* || "$BASENAME" == pyproject.toml ]]; then
  if command -v pip-audit &>/dev/null; then
    echo "🔍 pip-audit を実行中..."
    if pip-audit --format=json 2>/dev/null | \
        python3 -c "
import sys, json
data = json.load(sys.stdin)
vulns = [d for d in data.get('dependencies', []) if d.get('vulns')]
if vulns:
    for dep in vulns:
        for v in dep['vulns']:
            print(f'  ⚠️  {dep[\"name\"]} {dep[\"version\"]}: {v[\"id\"]} — {v[\"fix_versions\"]}')
    sys.exit(1)
" 2>/dev/null; then
      echo "  ✅ Python の脆弱性なし"
    else
      ISSUES_FOUND=1
      echo "  詳細は実行: pip-audit"
    fi
  elif command -v safety &>/dev/null; then
    echo "🔍 safety check を実行中..."
    OUTPUT=$(safety check --short-report 2>&1)
    EXIT_CODE=$?
    if [ $EXIT_CODE -eq 0 ]; then
      echo "  ✅ Python の脆弱性なし"
    elif echo "$OUTPUT" | grep -qiE "vulnerability|CVE|insecure"; then
      echo "$OUTPUT"
      ISSUES_FOUND=1
    else
      echo "  ⚠️  safety check が完了できなかった（ネットワークまたは設定エラー）" >&2
    fi
  fi
fi

# ── Go ───────────────────────────────────────────────────────────────────────
if [[ "$BASENAME" == go.mod || "$BASENAME" == go.sum ]]; then
  if command -v govulncheck &>/dev/null; then
    echo "🔍 govulncheck を実行中..."
    OUTPUT=$(govulncheck ./... 2>&1)
    EXIT_CODE=$?
    if [ $EXIT_CODE -eq 0 ]; then
      echo "  ✅ Go の脆弱性なし"
    elif echo "$OUTPUT" | grep -q "Vulnerability #"; then
      echo "$OUTPUT"
      ISSUES_FOUND=1
    else
      echo "  ⚠️  govulncheck が完了できなかった: $OUTPUT" >&2
    fi
  fi
fi

# ── Rust ─────────────────────────────────────────────────────────────────────
if [[ "$BASENAME" == Cargo.toml || "$BASENAME" == Cargo.lock ]]; then
  if command -v cargo-audit &>/dev/null; then
    echo "🔍 cargo audit を実行中..."
    if ! cargo audit 2>/dev/null; then
      ISSUES_FOUND=1
    else
      echo "  ✅ Rust の脆弱性なし"
    fi
  fi
fi

# ── Ruby ─────────────────────────────────────────────────────────────────────
if [[ "$BASENAME" == Gemfile || "$BASENAME" == Gemfile.lock ]]; then
  if command -v bundler-audit &>/dev/null; then
    echo "🔍 bundler-audit を実行中..."
    bundler-audit check --update 2>/dev/null || ISSUES_FOUND=1
  fi
fi

# ── 汎用フォールバック：trivy ───────────────────────────────────────────────
if command -v trivy &>/dev/null; then
  echo "🔍 trivy fs scan を実行中..."
  if ! trivy fs --exit-code 1 --severity HIGH,CRITICAL --quiet . 2>/dev/null; then
    ISSUES_FOUND=1
  else
    echo "  ✅ trivy は HIGH/CRITICAL の問題を検出せず"
  fi
fi

if [ "$ISSUES_FOUND" -eq 0 ]; then
  echo "✅ 依存関係チェック合格 — 脆弱性は検出されませんでした"
else
  echo ""
  echo "⚠️  脆弱性が検出されました。コミット前に依存関係を確認・更新してください。"
  echo "   このフックは助言のみで、ワークフローをブロックしません。"
fi

# 常に exit 0 — このフックは警告のみで、ブロックしない
exit 0
