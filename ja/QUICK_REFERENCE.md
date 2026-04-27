<!-- i18n-source: QUICK_REFERENCE.md -->
<!-- i18n-source-sha: d17d515 -->
<!-- i18n-date: 2026-04-27 -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# Claude Code 例題 — クイックリファレンスカード

## 🚀 インストール用クイックコマンド

### スラッシュコマンド
```bash
# 全部インストール
cp 01-slash-commands/*.md .claude/commands/

# 特定のものをインストール
cp 01-slash-commands/optimize.md .claude/commands/
```

### メモリ
```bash
# プロジェクトメモリ
cp 02-memory/project-CLAUDE.md ./CLAUDE.md

# 個人メモリ
cp 02-memory/personal-CLAUDE.md ~/.claude/CLAUDE.md
```

### スキル
```bash
# 個人スキル
cp -r 03-skills/code-review ~/.claude/skills/

# プロジェクトスキル
cp -r 03-skills/code-review .claude/skills/
```

### サブエージェント
```bash
# 全部インストール
cp 04-subagents/*.md .claude/agents/

# 特定のものをインストール
cp 04-subagents/code-reviewer.md .claude/agents/
```

### MCP
```bash
# 認証情報を設定
export GITHUB_TOKEN="your_token"
export DATABASE_URL="postgresql://..."

# 設定をインストール (プロジェクトスコープ)
cp 05-mcp/github-mcp.json .mcp.json

# またはユーザースコープ: ~/.claude.json に追加
```

### フック
```bash
# フックをインストール
mkdir -p ~/.claude/hooks
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh

# 設定で構成 (~/.claude/settings.json)
```

### プラグイン
```bash
# 例からインストール (公開済みなら)
/plugin install pr-review
/plugin install devops-automation
/plugin install documentation
```

### チェックポイント
```bash
# チェックポイントはユーザープロンプトのたびに自動作成される
# 巻き戻しは Esc を 2 回押すか、次を実行:
/rewind

# 選択肢: コードと会話の復元、会話の復元、
# コードの復元、ここから要約、やめる
```

### 高度な機能
```bash
# 設定で構成 (.claude/settings.json)
# 09-advanced-features/config-examples.json を参照

# プランニングモード
/plan Task description

# 権限モード (--permission-mode フラグを使う)
# default        - 危険な操作で承認を求める
# acceptEdits    - ファイル編集を自動承認、それ以外は確認
# plan           - 読み取り専用分析、変更なし
# dontAsk        - 危険なもの以外すべて承認
# auto           - バックグラウンド分類器が自動的に権限を判断
# bypassPermissions - すべて承認 (--dangerously-skip-permissions が必要)

# セッション管理
/resume                # 過去の会話を再開
/rename "name"         # 現在のセッションに名前を付ける
/fork                  # 現在のセッションをフォーク
claude -c              # 直近の会話を継続
claude -r "session"    # 名前 / ID でセッションを再開
```

---

## 📋 機能チートシート

| 機能 | インストール先 | 使い方 |
|---------|-------------|-------|
| **スラッシュコマンド (55 個以上)** | `.claude/commands/*.md` | `/command-name` |
| **メモリ** | `./CLAUDE.md` | 自動ロード |
| **スキル** | `.claude/skills/*/SKILL.md` | 自動起動 |
| **サブエージェント** | `.claude/agents/*.md` | 自動委譲 |
| **MCP** | `.mcp.json` (プロジェクト) または `~/.claude.json` (ユーザー) | `/mcp__server__action` |
| **フック (28 イベント)** | `~/.claude/hooks/*.sh` | イベントトリガー (5 種類) |
| **プラグイン** | `/plugin install` 経由 | すべてをバンドル |
| **チェックポイント** | 組み込み | `Esc+Esc` または `/rewind` |
| **プランニングモード** | 組み込み | `/plan <task>` |
| **権限モード (6 モード)** | 組み込み | `--allowedTools`、`--permission-mode` |
| **セッション** | 組み込み | `/session <command>` |
| **バックグラウンドタスク** | 組み込み | バックグラウンドで実行 |
| **リモートコントロール** | 組み込み | WebSocket API |
| **Web セッション** | 組み込み | `claude web` |
| **Git ワークツリー** | 組み込み | `/worktree` |
| **Auto Memory** | 組み込み | CLAUDE.md に自動保存 |
| **タスクリスト** | 組み込み | `/task list` |
| **バンドルスキル (5 個)** | 組み込み | `/simplify`、`/loop`、`/claude-api`、`/voice`、`/browse` |

---

## 🎯 よくあるユースケース

### コードレビュー
```bash
# 方法 1: スラッシュコマンド
cp 01-slash-commands/optimize.md .claude/commands/
# 利用: /optimize

# 方法 2: サブエージェント
cp 04-subagents/code-reviewer.md .claude/agents/
# 利用: 自動委譲

# 方法 3: スキル
cp -r 03-skills/code-review ~/.claude/skills/
# 利用: 自動起動

# 方法 4: プラグイン (推奨)
/plugin install pr-review
# 利用: /review-pr
```

### ドキュメント
```bash
# スラッシュコマンド
cp 01-slash-commands/generate-api-docs.md .claude/commands/

# サブエージェント
cp 04-subagents/documentation-writer.md .claude/agents/

# スキル
cp -r 03-skills/doc-generator ~/.claude/skills/

# プラグイン (完全ソリューション)
/plugin install documentation
```

### DevOps
```bash
# 完全プラグイン
/plugin install devops-automation

# コマンド: /deploy、/rollback、/status、/incident
```

### チーム標準
```bash
# プロジェクトメモリ
cp 02-memory/project-CLAUDE.md ./CLAUDE.md

# チーム向けに編集
vim CLAUDE.md
```

### 自動化とフック
```bash
# フックをインストール (28 イベント、5 種類: command, http, mcp_tool, prompt, agent)
mkdir -p ~/.claude/hooks
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh

# 例:
# - コミット前テスト: pre-commit.sh
# - コード自動整形: format-code.sh
# - セキュリティスキャン: security-scan.sh

# 完全自律ワークフローのための Auto Mode
claude --enable-auto-mode -p "Refactor and test the auth module"
# あるいは Shift+Tab で対話的にモードを切替
```

### 安全なリファクタリング
```bash
# チェックポイントは各プロンプト前に自動作成される
# リファクタリングを試す
# うまくいけば: 続行
# 失敗したら: Esc+Esc を押すか /rewind で戻る
```

### 複雑な実装
```bash
# プランニングモードを使う
/plan Implement user authentication system

# Claude が詳細な計画を作る
# レビューして承認
# Claude が体系的に実装する
```

### CI/CD 統合
```bash
# ヘッドレスモードで実行 (非対話)
claude -p "Run all tests and generate report"

# CI 用権限モードつき
claude -p "Run tests" --permission-mode dontAsk

# 完全自律 CI タスクのための Auto Mode
claude --enable-auto-mode -p "Run tests and fix failures"

# 自動化のためのフックつき
# 09-advanced-features/README.md を参照
```

### 学習と実験
```bash
# 安全な分析のため plan モードを使う
claude --permission-mode plan

# 安全に実験 - チェックポイントは自動作成される
# 巻き戻しが必要なら: Esc+Esc または /rewind
```

### Agent Teams
```bash
# Agent Teams を有効化
export CLAUDE_AGENT_TEAMS=1

# あるいは settings.json で
{ "agentTeams": { "enabled": true } }

# 開始: "Implement feature X using a team approach"
```

### スケジュールタスク
```bash
# 5 分ごとにコマンドを実行
/loop 5m /check-status

# 一回限りのリマインダー
/loop 30m "remind me to check the deploy"
```

---

## 📁 ファイル配置リファレンス

```
Your Project/
├── .claude/
│   ├── commands/              # スラッシュコマンドはここ
│   ├── agents/                # サブエージェントはここ
│   ├── skills/                # プロジェクトスキルはここ
│   └── settings.json          # プロジェクト設定 (フックなど)
├── .mcp.json                  # MCP 設定 (プロジェクトスコープ)
├── CLAUDE.md                  # プロジェクトメモリ
└── src/
    └── api/
        └── CLAUDE.md          # ディレクトリ固有メモリ

User Home/
├── .claude/
│   ├── commands/              # 個人コマンド
│   ├── agents/                # 個人エージェント
│   ├── skills/                # 個人スキル
│   ├── hooks/                 # フックスクリプト
│   ├── settings.json          # ユーザー設定
│   ├── managed-settings.d/    # 管理設定 (エンタープライズ / 組織)
│   └── CLAUDE.md              # 個人メモリ
└── .claude.json               # 個人 MCP 設定 (ユーザースコープ)
```

---

## 🔍 例の探し方

### カテゴリ別
- **スラッシュコマンド**：`01-slash-commands/`
- **メモリ**：`02-memory/`
- **スキル**：`03-skills/`
- **サブエージェント**：`04-subagents/`
- **MCP**：`05-mcp/`
- **フック**：`06-hooks/`
- **プラグイン**：`07-plugins/`
- **チェックポイント**：`08-checkpoints/`
- **高度な機能**：`09-advanced-features/`
- **CLI**：`10-cli/`

### ユースケース別
- **パフォーマンス**：`01-slash-commands/optimize.md`
- **セキュリティ**：`04-subagents/secure-reviewer.md`
- **テスト**：`04-subagents/test-engineer.md`
- **ドキュメント**：`03-skills/doc-generator/`
- **DevOps**：`07-plugins/devops-automation/`

### 複雑度別
- **シンプル**：スラッシュコマンド
- **中程度**：サブエージェント、メモリ
- **高度**：スキル、フック
- **完全**：プラグイン

---

## 🎓 学習パス

### 1 日目
```bash
# 概要を読む
cat README.md

# コマンドをインストール
cp 01-slash-commands/optimize.md .claude/commands/

# 試す
/optimize
```

### 2〜3 日目
```bash
# メモリをセットアップ
cp 02-memory/project-CLAUDE.md ./CLAUDE.md
vim CLAUDE.md

# サブエージェントをインストール
cp 04-subagents/code-reviewer.md .claude/agents/
```

### 4〜5 日目
```bash
# MCP をセットアップ
export GITHUB_TOKEN="your_token"
cp 05-mcp/github-mcp.json .mcp.json

# MCP コマンドを試す
/mcp__github__list_prs
```

### 第 2 週
```bash
# スキルをインストール
cp -r 03-skills/code-review ~/.claude/skills/

# 自動起動させる
# こう言うだけ: "Review this code for issues"
```

### 第 3 週以降
```bash
# 完全プラグインをインストール
/plugin install pr-review

# バンドル機能を使う
/review-pr
/check-security
/check-tests
```

---

## 新機能（2026 年 3 月）

| 機能 | 説明 | 使い方 |
|---------|-------------|-------|
| **Auto Mode** | バックグラウンド分類器による完全自律動作 | `--enable-auto-mode` フラグ、`Shift+Tab` でモード切替 |
| **チャンネル** | Discord と Telegram 統合 | `--channels` フラグ、Discord / Telegram ボット |
| **音声入力** | コマンドとコンテキストを Claude に音声で伝える | `/voice` コマンド |
| **フック (28 イベント)** | 5 種類に拡張されたフックシステム | command、http、mcp_tool、prompt、agent の各フック種別 |
| **MCP Elicitation** | MCP サーバが実行時にユーザー入力を要求できる | サーバが要明確化なら自動プロンプト |
| **Plugin LSP** | プラグインの Language Server Protocol サポート | `userConfig`、`${CLAUDE_PLUGIN_DATA}` 変数 |
| **リモートコントロール** | WebSocket API で Claude Code を制御 | 外部統合のための `claude --remote` |
| **Web セッション** | ブラウザベースの Claude Code インターフェース | 起動：`claude web` |
| **デスクトップアプリ** | ネイティブデスクトップアプリ | claude.ai/download からダウンロード |
| **タスクリスト** | バックグラウンドタスクの管理 | `/task list`、`/task status <id>` |
| **Auto Memory** | 会話からの自動メモリ保存 | Claude が CLAUDE.md に主要コンテキストを自動保存 |
| **Git ワークツリー** | 並列開発のための隔離ワークスペース | `/worktree` で隔離ワークスペースを作成 |
| **モデル選択** | Sonnet 4.6、Opus 4.7、Haiku 4.5 を切替 | `/model` または `--model` フラグ |
| **Agent Teams** | タスク上の複数エージェントを協調 | 環境変数 `CLAUDE_AGENT_TEAMS=1` で有効化 |
| **スケジュールタスク** | `/loop` による反復タスク | `/loop 5m /command` または CronCreate ツール |
| **Chrome 連携** | ブラウザ自動化 | `--chrome` フラグまたは `/chrome` コマンド |
| **キーバインドカスタマイズ** | カスタムキーバインド | `/keybindings` コマンド |

---

## ヒントとコツ

### カスタマイズ
- 例題はそのままから始める
- 自分のニーズに合わせて改造する
- チームに共有する前にテストする
- 設定をバージョン管理する

### ベストプラクティス
- チーム標準にはメモリを使う
- 完全ワークフローにはプラグインを使う
- 複雑タスクにはサブエージェントを使う
- 単純タスクにはスラッシュコマンドを使う

### トラブルシューティング
```bash
# ファイル配置を確認
ls -la .claude/commands/
ls -la .claude/agents/

# YAML 構文を検証
head -20 .claude/agents/code-reviewer.md

# MCP 接続をテスト
echo $GITHUB_TOKEN
```

---

## 📊 機能マトリクス

| 必要なもの | 使う機能 | 例 |
|------|----------|---------|
| 高速ショートカット | スラッシュコマンド (55 個以上) | `01-slash-commands/optimize.md` |
| チーム標準 | メモリ | `02-memory/project-CLAUDE.md` |
| 自動ワークフロー | スキル | `03-skills/code-review/` |
| 専門タスク | サブエージェント | `04-subagents/code-reviewer.md` |
| 外部データ | MCP（+ Elicitation） | `05-mcp/github-mcp.json` |
| イベント自動化 | フック (28 イベント、5 種類) | `06-hooks/pre-commit.sh` |
| 完全ソリューション | プラグイン (+ LSP サポート) | `07-plugins/pr-review/` |
| 安全な実験 | チェックポイント | `08-checkpoints/checkpoint-examples.md` |
| 完全自律 | Auto Mode | `--enable-auto-mode` または `Shift+Tab` |
| チャット連携 | チャンネル | `--channels`（Discord、Telegram） |
| CI/CD パイプライン | CLI | `10-cli/README.md` |

---

## 🔗 クイックリンク

- **メインガイド**：`README.md`
- **完全索引**：`INDEX.md`
- **サマリー**：`EXAMPLES_SUMMARY.md`
- **オリジナルガイド**：`claude_concepts_guide.md`

---

## 📞 よくある質問

**Q：どれを使えばよいか？**
A：スラッシュコマンドから始め、必要に応じて機能を追加する。

**Q：機能を組み合わせられるか？**
A：できる。連携動作する。メモリ + コマンド + MCP は強力。

**Q：チームと共有するには？**
A：`.claude/` ディレクトリを git にコミットする。

**Q：シークレットはどうするか？**
A：環境変数を使い、ハードコードしない。

**Q：例を改造してよいか？**
A：もちろん。カスタマイズ用のテンプレートである。

---

## ✅ チェックリスト

スタート用チェックリスト：

- [ ] `README.md` を読む
- [ ] スラッシュコマンドを 1 つインストール
- [ ] そのコマンドを試す
- [ ] プロジェクト `CLAUDE.md` を作成
- [ ] サブエージェントを 1 つインストール
- [ ] MCP 統合を 1 つセットアップ
- [ ] スキルを 1 つインストール
- [ ] 完全プラグインを試す
- [ ] 自分のニーズに合わせてカスタマイズ
- [ ] チームと共有する

---

**クイックスタート**：`cat README.md`

**完全索引**：`cat INDEX.md`

**このカード**：手元に置いてクイックリファレンスとして！

---
**最終更新**：2026 年 4 月 24 日
**Claude Code バージョン**：2.1.119
**情報源**：
- https://code.claude.com/docs/en/overview
- https://code.claude.com/docs/en/hooks
- https://code.claude.com/docs/en/commands
- https://github.com/anthropics/claude-code/releases/tag/v2.1.119
**互換モデル**：Claude Sonnet 4.6、Claude Opus 4.7、Claude Haiku 4.5
