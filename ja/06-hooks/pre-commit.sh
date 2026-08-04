#!/bin/bash
# コミット前にテストを実行する
# フック：PreToolUse（matcher: Bash）— コマンドが git commit か判定する
# 注：「PreCommit」フックイベントは存在しない。PreToolUse と Bash matcher の組み合わせで
# コマンドを検査し、git commit を検出する。
#
# 終了コード：2 はツール呼び出しをブロックし、stderr の内容をブロック理由として提示する。
# それ以外の非ゼロ値は「ブロックしないエラー」であり、コミットはそのまま続行してしまう。
# 出典：https://code.claude.com/docs/en/hooks

echo "🧪 コミット前にテストを実行しています..."

# package.json の有無を確認（Node.js プロジェクト）
if [ -f "package.json" ]; then
  if grep -q "\"test\":" package.json; then
    npm test
    if [ $? -ne 0 ]; then
      echo "❌ テスト失敗。コミットをブロックします。" >&2
      exit 2
    fi
  fi
fi

# pytest が使えるか確認（Python プロジェクト）
if [ -f "pytest.ini" ] || [ -f "setup.py" ]; then
  if command -v pytest &> /dev/null; then
    pytest
    if [ $? -ne 0 ]; then
      echo "❌ テスト失敗。コミットをブロックします。" >&2
      exit 2
    fi
  fi
fi

# go.mod の有無を確認（Go プロジェクト）
if [ -f "go.mod" ]; then
  go test ./...
  if [ $? -ne 0 ]; then
    echo "❌ テスト失敗。コミットをブロックします。" >&2
    exit 2
  fi
fi

# Cargo.toml の有無を確認（Rust プロジェクト）
if [ -f "Cargo.toml" ]; then
  cargo test
  if [ $? -ne 0 ]; then
    echo "❌ テスト失敗。コミットをブロックします。" >&2
    exit 2
  fi
fi

echo "✅ 全テスト合格。コミットを続行します。"
exit 0
