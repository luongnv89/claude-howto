<!-- i18n-source: INDEX.md -->
<!-- i18n-source-sha: d17d515 -->
<!-- i18n-date: 2026-04-27 -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# Claude Code 例題 — 完全索引

本ドキュメントは、機能種別ごとに整理された全サンプルファイルの完全索引である。

## サマリー統計

- **総ファイル数**：100 ファイル超
- **カテゴリ**：10 機能カテゴリ
- **プラグイン**：完全プラグイン 3 個
- **スキル**：完全スキル 6 個
- **フック**：例フック 8 個
- **すぐ使える**：すべての例

---

## 01. スラッシュコマンド（10 ファイル）

日常ワークフロー向けにユーザーが実行するショートカット。

| ファイル | 説明 | ユースケース |
|------|-------------|----------|
| `optimize.md` | コード最適化アナライザ | パフォーマンス問題の検出 |
| `pr.md` | プルリクエスト準備 | PR ワークフロー自動化 |
| `generate-api-docs.md` | API ドキュメント生成 | API ドキュメント生成 |
| `commit.md` | コミットメッセージ補助 | 標準化されたコミット |
| `setup-ci-cd.md` | CI/CD パイプラインセットアップ | DevOps 自動化 |
| `push-all.md` | 全変更を push | 高速 push ワークフロー |
| `unit-test-expand.md` | ユニットテストカバレッジ拡張 | テスト自動化 |
| `doc-refactor.md` | ドキュメントリファクタリング | ドキュメント改善 |
| `pr-slash-command.png` | スクリーンショット例 | 視覚的参考 |
| `README.md` | ドキュメント | セットアップと使用ガイド |

**インストール先**：`.claude/commands/`

**使い方**：`/optimize`、`/pr`、`/generate-api-docs`、`/commit`、`/setup-ci-cd`、`/push-all`、`/unit-test-expand`、`/doc-refactor`

---

## 02. メモリ（6 ファイル）

永続的なコンテキストとプロジェクト規約。

| ファイル | 説明 | スコープ | 配置場所 |
|------|-------------|-------|----------|
| `project-CLAUDE.md` | チームプロジェクト規約 | プロジェクト全体 | `./CLAUDE.md` |
| `directory-api-CLAUDE.md` | API 固有のルール | ディレクトリ | `./src/api/CLAUDE.md` |
| `personal-CLAUDE.md` | 個人の好み | ユーザー | `~/.claude/CLAUDE.md` |
| `memory-saved.png` | スクリーンショット：保存済みメモリ | - | 視覚的参考 |
| `memory-ask-claude.png` | スクリーンショット：Claude に質問 | - | 視覚的参考 |
| `README.md` | ドキュメント | - | リファレンス |

**インストール**：適切な場所にコピー

**使い方**：Claude が自動的に読み込む

---

## 03. スキル（28 ファイル）

スクリプトとテンプレートを含む自動起動機能。

### コードレビュースキル（5 ファイル）
```
code-review/
├── SKILL.md                          # スキル定義
├── scripts/
│   ├── analyze-metrics.py            # コードメトリクス分析
│   └── compare-complexity.py         # 複雑度比較
└── templates/
    ├── review-checklist.md           # レビューチェックリスト
    └── finding-template.md           # 指摘ドキュメント
```

**目的**：セキュリティ、パフォーマンス、品質分析を含む包括的コードレビュー

**自動起動**：コードレビュー時

---

### ブランドボイススキル（4 ファイル）
```
brand-voice/
├── SKILL.md                          # スキル定義
├── templates/
│   ├── email-template.txt            # メールフォーマット
│   └── social-post-template.txt      # SNS フォーマット
└── tone-examples.md                  # メッセージ例
```

**目的**：コミュニケーションでブランドボイスの一貫性を保つ

**自動起動**：マーケティング文の作成時

---

### ドキュメント生成スキル（2 ファイル）
```
doc-generator/
├── SKILL.md                          # スキル定義
└── generate-docs.py                  # Python ドキュメント抽出
```

**目的**：ソースコードから包括的な API ドキュメントを生成

**自動起動**：API ドキュメントの作成・更新時

---

### リファクタスキル（5 ファイル）
```
refactor/
├── SKILL.md                          # スキル定義
├── scripts/
│   ├── analyze-complexity.py         # 複雑度分析
│   └── detect-smells.py              # コードスメル検出
├── references/
│   ├── code-smells.md                # コードスメルカタログ
│   └── refactoring-catalog.md        # リファクタリングパターン
└── templates/
    └── refactoring-plan.md           # リファクタリング計画テンプレート
```

**目的**：複雑度分析を伴う体系的リファクタリング

**自動起動**：コードリファクタリング時

---

### Claude MD スキル（1 ファイル）
```
claude-md/
└── SKILL.md                          # スキル定義
```

**目的**：CLAUDE.md ファイルの管理と最適化

---

### ブログ草稿スキル（3 ファイル）
```
blog-draft/
├── SKILL.md                          # スキル定義
└── templates/
    ├── draft-template.md             # ブログ草稿テンプレート
    └── outline-template.md           # ブログ構成テンプレート
```

**目的**：一貫した構造でブログ記事を草稿する

**追加**：`README.md` — スキル概要と使用ガイド

**インストール先**：`~/.claude/skills/` または `.claude/skills/`

---

## 04. サブエージェント（9 ファイル）

カスタム能力を持つ専門特化 AI アシスタント。

| ファイル | 説明 | ツール | ユースケース |
|------|-------------|-------|----------|
| `code-reviewer.md` | コード品質分析 | read, grep, diff, lint_runner | 包括的レビュー |
| `test-engineer.md` | テストカバレッジ分析 | read, write, bash, grep | テスト自動化 |
| `documentation-writer.md` | ドキュメント作成 | read, write, grep | ドキュメント生成 |
| `secure-reviewer.md` | セキュリティレビュー（読み取り専用） | read, grep | セキュリティ監査 |
| `implementation-agent.md` | フル実装 | read, write, bash, grep, edit, glob | 機能開発 |
| `debugger.md` | デバッグ専門家 | read, bash, grep | バグ調査 |
| `data-scientist.md` | データ分析専門家 | read, write, bash | データワークフロー |
| `clean-code-reviewer.md` | クリーンコード基準 | read, grep | コード品質 |
| `README.md` | ドキュメント | - | セットアップと使用ガイド |

**インストール先**：`.claude/agents/`

**使い方**：メインエージェントが自動委譲

---

## 05. MCP プロトコル（5 ファイル）

外部ツールおよび API の統合。

| ファイル | 説明 | 連携先 | ユースケース |
|------|-------------|-----------------|----------|
| `github-mcp.json` | GitHub 連携 | GitHub API | PR / issue 管理 |
| `database-mcp.json` | データベースクエリ | PostgreSQL/MySQL | ライブデータクエリ |
| `filesystem-mcp.json` | ファイル操作 | ローカルファイルシステム | ファイル管理 |
| `multi-mcp.json` | 複数サーバ | GitHub + DB + Slack | 完全統合 |
| `README.md` | ドキュメント | - | セットアップと使用ガイド |

**インストール先**：`.mcp.json`（プロジェクトスコープ）または `~/.claude.json`（ユーザースコープ）

**使い方**：`/mcp__github__list_prs` など

---

## 06. フック（9 ファイル）

自動実行されるイベント駆動の自動化スクリプト。

| ファイル | 説明 | イベント | ユースケース |
|------|-------------|-------|----------|
| `format-code.sh` | コード自動整形 | PreToolUse:Write | コード整形 |
| `pre-commit.sh` | コミット前のテスト実行 | PreToolUse:Bash | テスト自動化 |
| `security-scan.sh` | セキュリティスキャン | PostToolUse:Write | セキュリティチェック |
| `log-bash.sh` | bash コマンド記録 | PostToolUse:Bash | コマンドログ |
| `validate-prompt.sh` | プロンプト検証 | PreToolUse | 入力検証 |
| `notify-team.sh` | 通知送信 | Notification | チーム通知 |
| `context-tracker.py` | コンテキストウィンドウ使用量追跡 | PostToolUse | コンテキスト監視 |
| `context-tracker-tiktoken.py` | トークンベースのコンテキスト追跡 | PostToolUse | 精密なトークン計測 |
| `README.md` | ドキュメント | - | セットアップと使用ガイド |

**インストール先**：`~/.claude/settings.json` で設定

**使い方**：設定で構成し、自動実行される

**フックの種類**（5 系統、28 イベント）：
- ツール系フック：PreToolUse、PostToolUse、PostToolUseFailure、PermissionRequest
- セッション系フック：SessionStart、SessionEnd、Stop、StopFailure、SubagentStart、SubagentStop
- タスク系フック：UserPromptSubmit、TaskCompleted、TaskCreated、TeammateIdle
- ライフサイクル系フック：ConfigChange、CwdChanged、FileChanged、PreCompact、PostCompact、WorktreeCreate、WorktreeRemove、Notification、InstructionsLoaded、Elicitation、ElicitationResult

---

## 07. プラグイン（完全プラグイン 3 個、40 ファイル）

機能のバンドル集。

### PR レビュープラグイン（10 ファイル）
```
pr-review/
├── .claude-plugin/
│   └── plugin.json                   # プラグインマニフェスト
├── commands/
│   ├── review-pr.md                  # 包括的レビュー
│   ├── check-security.md             # セキュリティチェック
│   └── check-tests.md                # テストカバレッジチェック
├── agents/
│   ├── security-reviewer.md          # セキュリティ専門家
│   ├── test-checker.md               # テスト専門家
│   └── performance-analyzer.md       # パフォーマンス専門家
├── mcp/
│   └── github-config.json            # GitHub 連携
├── hooks/
│   └── pre-review.js                 # レビュー前検証
└── README.md                         # プラグインドキュメント
```

**機能**：セキュリティ分析、テストカバレッジ、パフォーマンス影響

**コマンド**：`/review-pr`、`/check-security`、`/check-tests`

**インストール**：`/plugin install pr-review`

---

### DevOps 自動化プラグイン（15 ファイル）
```
devops-automation/
├── .claude-plugin/
│   └── plugin.json                   # プラグインマニフェスト
├── commands/
│   ├── deploy.md                     # デプロイ
│   ├── rollback.md                   # ロールバック
│   ├── status.md                     # システムステータス
│   └── incident.md                   # インシデント対応
├── agents/
│   ├── deployment-specialist.md      # デプロイ専門家
│   ├── incident-commander.md         # インシデント指揮
│   └── alert-analyzer.md             # アラート分析
├── mcp/
│   └── kubernetes-config.json        # Kubernetes 連携
├── hooks/
│   ├── pre-deploy.js                 # デプロイ前チェック
│   └── post-deploy.js                # デプロイ後タスク
├── scripts/
│   ├── deploy.sh                     # デプロイ自動化
│   ├── rollback.sh                   # ロールバック自動化
│   └── health-check.sh               # ヘルスチェック
└── README.md                         # プラグインドキュメント
```

**機能**：Kubernetes デプロイ、ロールバック、監視、インシデント対応

**コマンド**：`/deploy`、`/rollback`、`/status`、`/incident`

**インストール**：`/plugin install devops-automation`

---

### ドキュメントプラグイン（14 ファイル）
```
documentation/
├── .claude-plugin/
│   └── plugin.json                   # プラグインマニフェスト
├── commands/
│   ├── generate-api-docs.md          # API ドキュメント生成
│   ├── generate-readme.md            # README 作成
│   ├── sync-docs.md                  # ドキュメント同期
│   └── validate-docs.md              # ドキュメント検証
├── agents/
│   ├── api-documenter.md             # API ドキュメント専門家
│   ├── code-commentator.md           # コードコメント専門家
│   └── example-generator.md          # 例の作成
├── mcp/
│   └── github-docs-config.json       # GitHub 連携
├── templates/
│   ├── api-endpoint.md               # API エンドポイントテンプレート
│   ├── function-docs.md              # 関数ドキュメントテンプレート
│   └── adr-template.md               # ADR テンプレート
└── README.md                         # プラグインドキュメント
```

**機能**：API ドキュメント、README 生成、ドキュメント同期、検証

**コマンド**：`/generate-api-docs`、`/generate-readme`、`/sync-docs`、`/validate-docs`

**インストール**：`/plugin install documentation`

**追加**：`README.md` — プラグイン概要と使用ガイド

---

## 08. チェックポイントと巻き戻し（2 ファイル）

会話状態を保存し、別アプローチを探索する。

| ファイル | 説明 | 内容 |
|------|-------------|---------|
| `README.md` | ドキュメント | 包括的なチェックポイントガイド |
| `checkpoint-examples.md` | 実用例 | DB マイグレーション、パフォーマンス最適化、UI 反復、デバッグ |
| | | |

**主要概念**：
- **チェックポイント**：会話状態のスナップショット
- **巻き戻し**：以前のチェックポイントへ戻る
- **分岐点**：複数のアプローチを探索する

**使い方**：
```
# チェックポイントはユーザープロンプトのたびに自動作成される
# 巻き戻しは Esc を 2 回押すか、次を実行:
/rewind
# 選択肢: コードと会話の復元、会話の復元、
# コードの復元、ここから要約、やめる
```

**ユースケース**：
- 別実装を試す
- ミスからのリカバリ
- 安全な実験
- 解決策の比較
- A/B テスト

---

## 09. 高度な機能（3 ファイル）

複雑なワークフロー向けの高度な機能。

| ファイル | 説明 | 機能 |
|------|-------------|----------|
| `README.md` | 完全ガイド | 全高度機能のドキュメント |
| `config-examples.json` | 設定例 | ユースケース別の 10 種以上の設定 |
| `planning-mode-examples.md` | プランニング例 | REST API、DB マイグレーション、リファクタリング |
| スケジュールタスク | `/loop` および cron ツールによる反復タスク | 自動化された反復ワークフロー |
| Chrome 連携 | ヘッドレス Chromium によるブラウザ自動化 | Web テストとスクレイピング |
| リモートコントロール（拡張） | 接続方式、セキュリティ、比較表 | リモートセッション管理 |
| キーバインドカスタマイズ | カスタムキーバインド、コード対応、コンテキスト | パーソナライズされたショートカット |
| デスクトップアプリ（拡張） | コネクタ、launch.json、エンタープライズ機能 | デスクトップ統合 |
| | | |

**カバーされる高度機能**：

### プランニングモード
- 詳細な実装計画の作成
- 時間見積もりとリスク評価
- 体系的なタスク分解

### 拡張思考
- 複雑な問題に対する深い推論
- アーキテクチャ意思決定の分析
- トレードオフの評価

### バックグラウンドタスク
- ブロックなしの長時間処理
- 並列開発ワークフロー
- タスク管理と監視

### 権限モード
- **default**：危険な操作で承認を求める
- **acceptEdits**：ファイル編集を自動承認、それ以外は確認
- **plan**：読み取り専用分析、変更なし
- **auto**：安全な操作を自動承認、危険なものは確認
- **dontAsk**：危険なもの以外すべて承認
- **bypassPermissions**：すべて承認（`--dangerously-skip-permissions` が必要）

### ヘッドレスモード（`claude -p`）
- CI/CD 統合
- 自動化されたタスク実行
- バッチ処理

### セッション管理
- 複数の作業セッション
- セッション切替と保存
- セッション永続化

### インタラクティブ機能
- キーボードショートカット
- コマンド履歴
- タブ補完
- 複数行入力

### 設定
- 包括的な設定管理
- 環境別設定
- プロジェクト別カスタマイズ

### スケジュールタスク
- `/loop` コマンドによる反復タスク
- cron ツール：CronCreate、CronList、CronDelete
- 自動化された反復ワークフロー

### Chrome 連携
- ヘッドレス Chromium によるブラウザ自動化
- Web テストおよびスクレイピング能力
- ページ操作とデータ抽出

### リモートコントロール（拡張）
- 接続方式とプロトコル
- セキュリティ上の留意事項とベストプラクティス
- リモートアクセスオプションの比較表

### キーバインドカスタマイズ
- カスタムキーバインド設定
- 複数キーショートカットのコード対応
- コンテキストに応じたキーバインドの有効化

### デスクトップアプリ（拡張）
- IDE 統合のためのコネクタ
- launch.json 設定
- エンタープライズ機能とデプロイ

---

## 10. CLI 利用（1 ファイル）

コマンドラインインターフェースの利用パターンとリファレンス。

| ファイル | 説明 | 内容 |
|------|-------------|---------|
| `README.md` | CLI ドキュメント | フラグ、オプション、利用パターン |

**主な CLI 機能**：
- `claude` — 対話セッションを開始
- `claude -p "prompt"` — ヘッドレス / 非対話モード
- `claude web` — Web セッションを起動
- `claude --model` — モデル選択（Sonnet 4.6、Opus 4.7、Haiku 4.5）
- `claude --permission-mode` — 権限モードの設定
- `claude --remote` — WebSocket 経由のリモートコントロール有効化

---

## ドキュメントファイル（13 ファイル）

| ファイル | 場所 | 説明 |
|------|----------|-------------|
| `README.md` | `/` | メイン例題概要 |
| `INDEX.md` | `/` | この完全索引 |
| `QUICK_REFERENCE.md` | `/` | クイックリファレンスカード |
| `README.md` | `/01-slash-commands/` | スラッシュコマンドガイド |
| `README.md` | `/02-memory/` | メモリガイド |
| `README.md` | `/03-skills/` | スキルガイド |
| `README.md` | `/04-subagents/` | サブエージェントガイド |
| `README.md` | `/05-mcp/` | MCP ガイド |
| `README.md` | `/06-hooks/` | フックガイド |
| `README.md` | `/07-plugins/` | プラグインガイド |
| `README.md` | `/08-checkpoints/` | チェックポイントガイド |
| `README.md` | `/09-advanced-features/` | 高度な機能ガイド |
| `README.md` | `/10-cli/` | CLI ガイド |

---

## 完全ファイルツリー

```
claude-howto/
├── README.md                                    # メイン概要
├── INDEX.md                                     # このファイル
├── QUICK_REFERENCE.md                           # クイックリファレンスカード
├── claude_concepts_guide.md                     # オリジナルガイド
│
├── 01-slash-commands/                           # スラッシュコマンド
│   ├── optimize.md
│   ├── pr.md
│   ├── generate-api-docs.md
│   ├── commit.md
│   ├── setup-ci-cd.md
│   ├── push-all.md
│   ├── unit-test-expand.md
│   ├── doc-refactor.md
│   ├── pr-slash-command.png
│   └── README.md
│
├── 02-memory/                                   # メモリ
│   ├── project-CLAUDE.md
│   ├── directory-api-CLAUDE.md
│   ├── personal-CLAUDE.md
│   ├── memory-saved.png
│   ├── memory-ask-claude.png
│   └── README.md
│
├── 03-skills/                                   # スキル
│   ├── code-review/
│   │   ├── SKILL.md
│   │   ├── scripts/
│   │   │   ├── analyze-metrics.py
│   │   │   └── compare-complexity.py
│   │   └── templates/
│   │       ├── review-checklist.md
│   │       └── finding-template.md
│   ├── brand-voice/
│   │   ├── SKILL.md
│   │   ├── templates/
│   │   │   ├── email-template.txt
│   │   │   └── social-post-template.txt
│   │   └── tone-examples.md
│   ├── doc-generator/
│   │   ├── SKILL.md
│   │   └── generate-docs.py
│   ├── refactor/
│   │   ├── SKILL.md
│   │   ├── scripts/
│   │   │   ├── analyze-complexity.py
│   │   │   └── detect-smells.py
│   │   ├── references/
│   │   │   ├── code-smells.md
│   │   │   └── refactoring-catalog.md
│   │   └── templates/
│   │       └── refactoring-plan.md
│   ├── claude-md/
│   │   └── SKILL.md
│   ├── blog-draft/
│   │   ├── SKILL.md
│   │   └── templates/
│   │       ├── draft-template.md
│   │       └── outline-template.md
│   └── README.md
│
├── 04-subagents/                                # サブエージェント
│   ├── code-reviewer.md
│   ├── test-engineer.md
│   ├── documentation-writer.md
│   ├── secure-reviewer.md
│   ├── implementation-agent.md
│   ├── debugger.md
│   ├── data-scientist.md
│   ├── clean-code-reviewer.md
│   └── README.md
│
├── 05-mcp/                                      # MCP プロトコル
│   ├── github-mcp.json
│   ├── database-mcp.json
│   ├── filesystem-mcp.json
│   ├── multi-mcp.json
│   └── README.md
│
├── 06-hooks/                                    # フック
│   ├── format-code.sh
│   ├── pre-commit.sh
│   ├── security-scan.sh
│   ├── log-bash.sh
│   ├── validate-prompt.sh
│   ├── notify-team.sh
│   ├── context-tracker.py
│   ├── context-tracker-tiktoken.py
│   └── README.md
│
├── 07-plugins/                                  # プラグイン
│   ├── pr-review/
│   │   ├── .claude-plugin/
│   │   │   └── plugin.json
│   │   ├── commands/
│   │   │   ├── review-pr.md
│   │   │   ├── check-security.md
│   │   │   └── check-tests.md
│   │   ├── agents/
│   │   │   ├── security-reviewer.md
│   │   │   ├── test-checker.md
│   │   │   └── performance-analyzer.md
│   │   ├── mcp/
│   │   │   └── github-config.json
│   │   ├── hooks/
│   │   │   └── pre-review.js
│   │   └── README.md
│   ├── devops-automation/
│   │   ├── .claude-plugin/
│   │   │   └── plugin.json
│   │   ├── commands/
│   │   │   ├── deploy.md
│   │   │   ├── rollback.md
│   │   │   ├── status.md
│   │   │   └── incident.md
│   │   ├── agents/
│   │   │   ├── deployment-specialist.md
│   │   │   ├── incident-commander.md
│   │   │   └── alert-analyzer.md
│   │   ├── mcp/
│   │   │   └── kubernetes-config.json
│   │   ├── hooks/
│   │   │   ├── pre-deploy.js
│   │   │   └── post-deploy.js
│   │   ├── scripts/
│   │   │   ├── deploy.sh
│   │   │   ├── rollback.sh
│   │   │   └── health-check.sh
│   │   └── README.md
│   ├── documentation/
│   │   ├── .claude-plugin/
│   │   │   └── plugin.json
│   │   ├── commands/
│   │   │   ├── generate-api-docs.md
│   │   │   ├── generate-readme.md
│   │   │   ├── sync-docs.md
│   │   │   └── validate-docs.md
│   │   ├── agents/
│   │   │   ├── api-documenter.md
│   │   │   ├── code-commentator.md
│   │   │   └── example-generator.md
│   │   ├── mcp/
│   │   │   └── github-docs-config.json
│   │   ├── templates/
│   │   │   ├── api-endpoint.md
│   │   │   ├── function-docs.md
│   │   │   └── adr-template.md
│   │   └── README.md
│   └── README.md
│
├── 08-checkpoints/                              # チェックポイント
│   ├── checkpoint-examples.md
│   └── README.md
│
├── 09-advanced-features/                        # 高度な機能
│   ├── config-examples.json
│   ├── planning-mode-examples.md
│   └── README.md
│
└── 10-cli/                                      # CLI 利用
    └── README.md
```

---

## ユースケース別クイックスタート

### コード品質とレビュー
```bash
# スラッシュコマンドをインストール
cp 01-slash-commands/optimize.md .claude/commands/

# サブエージェントをインストール
cp 04-subagents/code-reviewer.md .claude/agents/

# スキルをインストール
cp -r 03-skills/code-review ~/.claude/skills/

# あるいは完全プラグインをインストール
/plugin install pr-review
```

### DevOps とデプロイ
```bash
# プラグインをインストール (すべて含む)
/plugin install devops-automation
```

### ドキュメント
```bash
# スラッシュコマンドをインストール
cp 01-slash-commands/generate-api-docs.md .claude/commands/

# サブエージェントをインストール
cp 04-subagents/documentation-writer.md .claude/agents/

# スキルをインストール
cp -r 03-skills/doc-generator ~/.claude/skills/

# あるいは完全プラグインをインストール
/plugin install documentation
```

### チーム標準
```bash
# プロジェクトメモリをセットアップ
cp 02-memory/project-CLAUDE.md ./CLAUDE.md

# チームの標準に合わせて編集
```

### 外部統合
```bash
# 環境変数を設定
export GITHUB_TOKEN="your_token"
export DATABASE_URL="postgresql://..."

# MCP 設定をインストール (プロジェクトスコープ)
cp 05-mcp/multi-mcp.json .mcp.json
```

### 自動化と検証
```bash
# フックをインストール
mkdir -p ~/.claude/hooks
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh

# 設定でフックを構成 (~/.claude/settings.json)
# 06-hooks/README.md を参照
```

### 安全な実験
```bash
# チェックポイントはユーザープロンプトのたびに自動作成される
# 巻き戻し: Esc+Esc を押すか /rewind
# 巻き戻しメニューから何を復元するか選択

# 例は 08-checkpoints/README.md を参照
```

### 高度なワークフロー
```bash
# 高度な機能を設定
# 09-advanced-features/config-examples.json を参照

# プランニングモードを使う
/plan Implement feature X

# 権限モードを使う
claude --permission-mode plan          # コードレビュー (読み取り専用)
claude --permission-mode acceptEdits   # 編集を自動承認
claude --permission-mode auto          # 安全な操作を自動承認

# CI/CD のためのヘッドレスモードで実行
claude -p "Run tests and report results"

# バックグラウンドタスクを実行
Run tests in background

# 完全ガイドは 09-advanced-features/README.md を参照
```

---

## 機能カバレッジマトリクス

| カテゴリ | コマンド | エージェント | MCP | フック | スクリプト | テンプレート | ドキュメント | 画像 | 合計 |
|----------|----------|--------|-----|-------|---------|-----------|------|--------|-------|
| **01 スラッシュコマンド** | 8 | - | - | - | - | - | 1 | 1 | **10** |
| **02 メモリ** | - | - | - | - | - | 3 | 1 | 2 | **6** |
| **03 スキル** | - | - | - | - | 5 | 9 | 1 | - | **28** |
| **04 サブエージェント** | - | 8 | - | - | - | - | 1 | - | **9** |
| **05 MCP** | - | - | 4 | - | - | - | 1 | - | **5** |
| **06 フック** | - | - | - | 8 | - | - | 1 | - | **9** |
| **07 プラグイン** | 11 | 9 | 3 | 3 | 3 | 3 | 4 | - | **40** |
| **08 チェックポイント** | - | - | - | - | - | - | 1 | 1 | **2** |
| **09 高度な機能** | - | - | - | - | - | - | 1 | 2 | **3** |
| **10 CLI** | - | - | - | - | - | - | 1 | - | **1** |

---

## 学習パス

### 初級（第 1 週）
1. ✅ `README.md` を読む
2. ✅ スラッシュコマンドを 1〜2 個インストール
3. ✅ プロジェクトメモリファイルを作成
4. ✅ 基本コマンドを試す

### 中級（第 2〜3 週）
1. ✅ GitHub MCP をセットアップ
2. ✅ サブエージェントをインストール
3. ✅ タスク委譲を試す
4. ✅ スキルをインストール

### 上級（第 4 週〜）
1. ✅ 完全プラグインをインストール
2. ✅ カスタムスラッシュコマンドを作成
3. ✅ カスタムサブエージェントを作成
4. ✅ カスタムスキルを作成
5. ✅ 自分のプラグインを構築

### エキスパート（第 5 週〜）
1. ✅ 自動化のためのフックをセットアップ
2. ✅ 実験のためチェックポイントを使う
3. ✅ プランニングモードを設定
4. ✅ 権限モードを効果的に使う
5. ✅ CI/CD のためヘッドレスモードをセットアップ
6. ✅ セッション管理を習得

---

## キーワード検索

### パフォーマンス
- `01-slash-commands/optimize.md` — パフォーマンス分析
- `04-subagents/code-reviewer.md` — パフォーマンスレビュー
- `03-skills/code-review/` — パフォーマンスメトリクス
- `07-plugins/pr-review/agents/performance-analyzer.md` — パフォーマンス専門家

### セキュリティ
- `04-subagents/secure-reviewer.md` — セキュリティレビュー
- `03-skills/code-review/` — セキュリティ分析
- `07-plugins/pr-review/` — セキュリティチェック

### テスト
- `04-subagents/test-engineer.md` — テストエンジニア
- `07-plugins/pr-review/commands/check-tests.md` — テストカバレッジ

### ドキュメント
- `01-slash-commands/generate-api-docs.md` — API ドキュメントコマンド
- `04-subagents/documentation-writer.md` — ドキュメント作成エージェント
- `03-skills/doc-generator/` — ドキュメント生成スキル
- `07-plugins/documentation/` — 完全ドキュメントプラグイン

### デプロイ
- `07-plugins/devops-automation/` — 完全 DevOps ソリューション

### 自動化
- `06-hooks/` — イベント駆動自動化
- `06-hooks/pre-commit.sh` — コミット前自動化
- `06-hooks/format-code.sh` — 自動整形
- `09-advanced-features/` — CI/CD のためのヘッドレスモード

### 検証
- `06-hooks/security-scan.sh` — セキュリティ検証
- `06-hooks/validate-prompt.sh` — プロンプト検証

### 実験
- `08-checkpoints/` — 巻き戻しによる安全な実験
- `08-checkpoints/checkpoint-examples.md` — 実用例

### プランニング
- `09-advanced-features/planning-mode-examples.md` — プランニングモード例
- `09-advanced-features/README.md` — 拡張思考

### 設定
- `09-advanced-features/config-examples.json` — 設定例

---

## 注意事項

- すべての例はそのまま利用できる
- 自分のニーズに合わせて改造する
- 例は Claude Code のベストプラクティスに従う
- 各カテゴリには詳細手順つきの独自 README がある
- スクリプトには適切なエラー処理が含まれる
- テンプレートはカスタマイズ可能

---

## コントリビュート

例題を追加したい場合は次の構造に従う：
1. 適切なサブディレクトリを作成
2. 利用方法つき README.md を含める
3. 命名規則に従う
4. 入念にテストする
5. この索引を更新する

---

**最終更新**：2026 年 4 月 24 日
**Claude Code バージョン**：2.1.119
**情報源**：
- https://code.claude.com/docs/en/overview
- https://code.claude.com/docs/en/hooks
- https://code.claude.com/docs/en/commands
- https://github.com/anthropics/claude-code/releases/tag/v2.1.119
**互換モデル**：Claude Sonnet 4.6、Claude Opus 4.7、Claude Haiku 4.5
**例題総数**：100 ファイル超
**カテゴリ**：10 機能
**フック**：自動化スクリプト 8 個
**設定例**：10 シナリオ以上
**すぐ使える**：すべての例
