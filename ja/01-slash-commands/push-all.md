<!-- i18n-source: 01-slash-commands/push-all.md -->
<!-- i18n-source-sha: 7f2e773 -->
<!-- i18n-date: 2026-04-27 -->

---
description: 全変更をステージング、コミット、リモートへ push する（取り扱い注意）
allowed-tools: Bash(git add:*), Bash(git status:*), Bash(git commit:*), Bash(git push:*), Bash(git diff:*), Bash(git log:*), Bash(git pull:*)
---

# すべてをコミット・push する

⚠️ **注意**: すべての変更をステージング・コミットし、リモートへ push する。すべての変更がひとまとまりであると確信できる場合のみ使うこと。

## ワークフロー

### 1. 変更を分析

並列で実行する:
- `git status` — 変更／追加／削除／追跡外ファイルを表示
- `git diff --stat` — 変更統計を表示
- `git log -1 --oneline` — メッセージスタイル参考のため直近のコミットを表示

### 2. 安全性チェック

**❌ 検出時は STOP し WARN を出すべき項目:**
- シークレット: `.env*`、`*.key`、`*.pem`、`credentials.json`、`secrets.yaml`、`id_rsa`、`*.p12`、`*.pfx`、`*.cer`
- API キー: `*_API_KEY`、`*_SECRET`、`*_TOKEN` などの変数で実値が入っているもの（`your-api-key`、`xxx`、`placeholder` などのプレースホルダではないもの）
- 大きなファイル: Git LFS なしの `>10MB`
- ビルド成果物: `node_modules/`、`dist/`、`build/`、`__pycache__/`、`*.pyc`、`.venv/`
- 一時ファイル: `.DS_Store`、`thumbs.db`、`*.swp`、`*.tmp`

**API キー検証:**
変更ファイルに以下のようなパターンがないか確認する:
```bash
OPENAI_API_KEY=sk-proj-xxxxx  # ❌ 実キーを検出！
AWS_SECRET_KEY=AKIA...         # ❌ 実キーを検出！
STRIPE_API_KEY=sk_live_...    # ❌ 実キーを検出！

# ✅ 許容されるプレースホルダ:
API_KEY=your-api-key-here
SECRET_KEY=placeholder
TOKEN=xxx
API_KEY=<your-key>
SECRET=${YOUR_SECRET}
```

**✅ 確認事項:**
- `.gitignore` が適切に設定されている
- マージ競合がない
- 正しいブランチである（main／master の場合は警告）
- API キーはプレースホルダのみ

### 3. 確認を求める

サマリを提示する:
```
📊 Changes Summary:
- X files modified, Y added, Z deleted
- Total: +AAA insertions, -BBB deletions

🔒 Safety: ✅ No secrets | ✅ No large files | ⚠️ [warnings]
🌿 Branch: [name] → origin/[name]

I will: git add . → commit → push

Type 'yes' to proceed or 'no' to cancel.
```

**明示的な "yes" を待ってから先へ進む。**

### 4. 実行（確認後）

順番に実行する:
```bash
git add .
git status  # ステージングを確認
```

### 5. コミットメッセージを生成

変更を分析し、Conventional Commits 形式のコミットを作成する:

**形式:**
```
[type]: Brief summary (max 72 characters)

- Key change 1
- Key change 2
- Key change 3
```

**Types:** `feat`、`fix`、`docs`、`style`、`refactor`、`test`、`chore`、`perf`、`build`、`ci`

**例:**
```
docs: Update concept README files with comprehensive documentation

- Add architecture diagrams and tables
- Include practical examples
- Expand best practices sections
```

### 6. コミットと push

```bash
git commit -m "$(cat <<'EOF'
[Generated commit message]
EOF
)"
git push  # 失敗時: git pull --rebase && git push
git log -1 --oneline --decorate  # 確認
```

### 7. 成功を通知

```
✅ Successfully pushed to remote!

Commit: [hash] [message]
Branch: [branch] → origin/[branch]
Files changed: X (+insertions, -deletions)
```

## エラーハンドリング

- **git add 失敗**: 権限、ロックされたファイル、リポジトリ初期化済みかを確認
- **git commit 失敗**: pre-commit フックを修正、git config（user.name／email）を確認
- **git push 失敗**:
  - non-fast-forward: `git pull --rebase && git push`
  - リモートブランチなし: `git push -u origin [branch]`
  - 保護ブランチ: PR ワークフローを使う

## 使うべきとき

✅ **適している場面:**
- 複数ファイルにまたがるドキュメント更新
- テストとドキュメントを伴う機能追加
- 複数ファイルにまたがるバグ修正
- プロジェクト全体のフォーマット／リファクタリング
- 設定変更

❌ **避けるべき場面:**
- 何をコミットするか不明確
- シークレット／機密データを含む
- レビューなしの保護ブランチ
- マージ競合がある
- 粒度の細かいコミット履歴を残したい
- pre-commit フックが失敗している

## 代替案

ユーザーがより細かく制御したい場合は次を提案する:
1. **選択的ステージング**: 特定ファイルをレビュー／ステージング
2. **インタラクティブステージング**: パッチ単位の選択に `git add -p`
3. **PR ワークフロー**: ブランチを作成 → push → PR（`/pr` コマンドを使う）

**⚠️ 注意**: push する前に必ず変更を確認する。迷ったら、より細かい制御のため個別の git コマンドを使う。

---
**Last Updated**: April 9, 2026
