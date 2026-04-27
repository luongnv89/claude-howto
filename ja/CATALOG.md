<!-- i18n-source: CATALOG.md -->
<!-- i18n-source-sha: d17d515 -->
<!-- i18n-date: 2026-04-27 -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# Claude Code 機能カタログ

> Claude Code 全機能のクイックリファレンス：コマンド、エージェント、スキル、プラグイン、フック。

**ナビゲーション**：[コマンド](#スラッシュコマンド) | [権限モード](#権限モード) | [サブエージェント](#サブエージェント) | [スキル](#スキル) | [プラグイン](#プラグイン) | [MCP サーバ](#mcp-サーバ) | [フック](#フック) | [メモリ](#メモリファイル) | [新機能](#新機能2026-年-4-月)

---

## サマリー

| 機能 | 組み込み | 例 | 合計 | リファレンス |
|---------|----------|----------|-------|-----------|
| **スラッシュコマンド** | 60 個以上 | 8 | 68 個以上 | [01-slash-commands/](01-slash-commands/) |
| **サブエージェント** | 6 | 11 | 17 | [04-subagents/](04-subagents/) |
| **スキル** | バンドル 5 | 4 | 9 | [03-skills/](03-skills/) |
| **プラグイン** | - | 3 | 3 | [07-plugins/](07-plugins/) |
| **MCP サーバ** | 1 | 8 | 9 | [05-mcp/](05-mcp/) |
| **フック** | 28 イベント | 8 | 8 | [06-hooks/](06-hooks/) |
| **メモリ** | 7 種類 | 3 | 3 | [02-memory/](02-memory/) |
| **合計** | **99** | **45** | **119** | |

---

## スラッシュコマンド

コマンドはユーザーが起動する、特定の動作を実行するショートカットである。

### 組み込みコマンド

| コマンド | 説明 | 利用シーン |
|---------|-------------|-------------|
| `/help` | ヘルプ情報を表示 | 初心者、コマンド習得 |
| `/btw` | 一時的な脇道質問 — メインコンテキストを汚さない | ちょっとした横道質問 |
| `/chrome` | Chrome 連携を設定 | ブラウザ自動化 |
| `/clear` | 会話履歴をクリア | やり直し、コンテキスト削減 |
| `/diff` | 対話式 diff ビューア | 変更レビュー |
| `/config` | 設定を表示・編集 | 動作カスタマイズ |
| `/status` | セッション状態を表示 | 現状確認 |
| `/agents` | 利用可能エージェントを表示 | 委譲オプション確認 |
| `/skills` | 利用可能スキルを表示 | 自動起動機能の確認 |
| `/hooks` | 設定済みフックを表示 | 自動化のデバッグ |
| `/insights` | セッションパターンを分析 | セッション最適化 |
| `/install-slack-app` | Claude Slack アプリのインストール | Slack 連携 |
| `/keybindings` | キーボードショートカットをカスタマイズ | キーカスタマイズ |
| `/mcp` | MCP サーバを一覧表示 | 外部統合の確認 |
| `/memory` | 読み込まれたメモリファイルを表示 | コンテキスト読込デバッグ |
| `/mobile` | モバイル用 QR コードを生成 | モバイルアクセス |
| `/passes` | 使用パスを表示 | サブスクリプション情報 |
| `/plugin` | プラグインを管理 | 拡張のインストール / 削除 |
| `/plan` | プランニングモードに入る | 複雑な実装 |
| `/proactive` | `/loop` のエイリアス（v2.1.105） | `/loop` と同じ |
| `/recap` | セッションに戻ってきたときに要約を表示 | 離席後のコンテキスト把握 |
| `/rewind` | チェックポイントへ巻き戻し | 変更取消、別案探索 |
| `/checkpoint` | チェックポイント管理 | 状態の保存 / 復元 |
| `/cost` | `/usage` のコストタブを開くエイリアス（v2.1.118+） | 支出監視 |
| `/context` | コンテキストウィンドウ使用量を表示 | 会話長の管理 |
| `/export` | 会話をエクスポート | 参照用に保存 |
| `/extra-usage` | 追加使用上限を設定 | レート制限管理 |
| `/feedback` | フィードバックやバグ報告を送信 | 問題報告 |
| `/login` | Anthropic で認証 | 機能アクセス |
| `/logout` | サインアウト | アカウント切替 |
| `/sandbox` | サンドボックスモード切替 | 安全なコマンド実行 |
| `/doctor` | 診断を実行 | 問題のトラブルシューティング |
| `/reload-plugins` | インストール済みプラグインを再読込 | プラグイン管理 |
| `/release-notes` | リリースノートを表示 | 新機能の確認 |
| `/remote-control` | リモートコントロールを有効化 | リモートアクセス |
| `/permissions` | 権限を管理 | アクセス制御 |
| `/session` | セッションを管理 | マルチセッションワークフロー |
| `/rename` | 現在のセッションを改名 | セッション整理 |
| `/resume` | 過去のセッションを再開 | 作業の継続 |
| `/todo` | TODO リストを表示・管理 | タスク追跡 |
| `/tui` | フルスクリーン TUI（テキストユーザーインターフェース）モード切替 | フルスクリーン / tmux でのちらつきのない描画 |
| `/tasks` | バックグラウンドタスクを表示 | 非同期処理の監視 |
| `/copy` | 直前の応答をクリップボードにコピー | 出力の素早い共有 |
| `/teleport` | セッションを別マシンに転送 | リモートでの作業継続 |
| `/desktop` | Claude デスクトップアプリを開く | デスクトップへ切替 |
| `/theme` | カラーテーマを変更。v2.1.118 で `~/.claude/themes/<name>.json` 経由のカスタムテーマが追加（プラグインは `themes/` ディレクトリを同梱可能） | 外観のカスタマイズ |
| `/usage` | 使用量・コスト・統計の正規コマンド — `/cost` と `/stats` を 1 つのタブビューに統合（v2.1.118） | クォータとコストの監視 |
| `/focus` | フォーカスビュー（注意散漫を防ぐ出力表示）を切替 | 長時間タスク中の視覚的ノイズ低減 |
| `/fork` | 現在の会話をフォーク | 別案の探索 |
| `/stats` | `/usage` の stats タブを開くエイリアス（v2.1.118+） | セッション指標の確認 |
| `/statusline` | ステータスラインを設定 | ステータス表示のカスタマイズ |
| `/stickers` | セッションステッカーを表示 | 楽しいご褒美 |
| `/fast` | 高速出力モード切替 | 応答の高速化 |
| `/terminal-setup` | ターミナル統合を設定 | ターミナル機能のセットアップ |
| `/undo` | `/rewind` のエイリアス（v2.1.108） | `/rewind` と同じ |
| `/upgrade` | アップデート確認 | バージョン管理 |
| `/team-onboarding` | このプロジェクトの Claude Code 利用状況からオンボーディングガイドを生成 | 新メンバーのオンボーディング（v2.1.101） |
| `/ultraplan` | プランニングタスクを Claude Code Web セッションに渡す（plan モード） | 重い計画作業のオフロード（Research Preview、v2.1.91+） |
| `/ultrareview` | 現在の変更に対するクラウドのマルチエージェントコードレビューを実行 | マージ前の深いマルチエージェントレビュー（v2.1.112） |
| `/less-permission-prompts` | トランスクリプトをスキャンし、よく使う読取専用ツールの優先許可リストを提案 | プロジェクトでの権限プロンプト繰り返しを削減（v2.1.112） |

### カスタムコマンド（例）

| コマンド | 説明 | 利用シーン | スコープ | インストール |
|---------|-------------|-------------|-------|--------------|
| `/optimize` | コードを最適化分析 | パフォーマンス改善 | プロジェクト | `cp 01-slash-commands/optimize.md .claude/commands/` |
| `/pr` | プルリクエスト準備 | PR 提出前 | プロジェクト | `cp 01-slash-commands/pr.md .claude/commands/` |
| `/generate-api-docs` | API ドキュメント生成 | API のドキュメント化 | プロジェクト | `cp 01-slash-commands/generate-api-docs.md .claude/commands/` |
| `/commit` | コンテキスト付き git コミット作成 | 変更のコミット | ユーザー | `cp 01-slash-commands/commit.md .claude/commands/` |
| `/push-all` | ステージ・コミット・プッシュ | 高速デプロイ | ユーザー | `cp 01-slash-commands/push-all.md .claude/commands/` |
| `/doc-refactor` | ドキュメント再構成 | ドキュメント改善 | プロジェクト | `cp 01-slash-commands/doc-refactor.md .claude/commands/` |
| `/setup-ci-cd` | CI/CD パイプライン構築 | 新規プロジェクト | プロジェクト | `cp 01-slash-commands/setup-ci-cd.md .claude/commands/` |
| `/unit-test-expand` | テストカバレッジ拡張 | テスト強化 | プロジェクト | `cp 01-slash-commands/unit-test-expand.md .claude/commands/` |

> **スコープ**：`ユーザー` = 個人ワークフロー（`~/.claude/commands/`）、`プロジェクト` = チーム共有（`.claude/commands/`）

**リファレンス**：[01-slash-commands/](01-slash-commands/) | [公式ドキュメント](https://code.claude.com/docs/en/interactive-mode)

**クイックインストール（全カスタムコマンド）**：
```bash
cp 01-slash-commands/*.md .claude/commands/
```

---

## 権限モード

Claude Code はツール使用の許可を制御する 6 つの権限モードをサポートする。

| モード | 説明 | 利用シーン |
|------|-------------|-------------|
| `default` | ツール呼び出しごとに確認 | 標準的な対話利用 |
| `acceptEdits` | ファイル編集を自動承認、それ以外は確認 | 信頼できる編集ワークフロー |
| `plan` | 読み取り専用ツールのみ、書き込みなし | 計画と探索 |
| `auto` | プロンプトなしですべてのツールを承認 | 完全自律動作（Research Preview） |
| `bypassPermissions` | すべての権限チェックをスキップ | CI/CD、ヘッドレス環境 |
| `dontAsk` | 権限が必要なツールをスキップ | 非対話スクリプト |

> **注**：`auto` モードは Research Preview 機能（2026 年 3 月）。`bypassPermissions` は信頼されたサンドボックス環境でのみ利用すること。

**リファレンス**：[公式ドキュメント](https://code.claude.com/docs/en/permissions)

---

## サブエージェント

特定タスク向けに分離コンテキストを持つ専門特化 AI アシスタント。

### 組み込みサブエージェント

| エージェント | 説明 | ツール | モデル | 利用シーン |
|-------|-------------|-------|-------|-------------|
| **general-purpose** | 多段タスク、調査 | 全ツール | モデル継承 | 複雑な調査、複数ファイルタスク |
| **Plan** | 実装計画 | Read、Glob、Grep、Bash | モデル継承 | アーキテクチャ設計、計画 |
| **Explore** | コードベース探索 | Read、Glob、Grep | Haiku 4.5 | 高速検索、コード理解 |
| **Bash** | コマンド実行 | Bash | モデル継承 | Git 操作、ターミナル作業 |
| **statusline-setup** | ステータスライン設定 | Bash、Read、Write | Sonnet 4.6 | ステータスライン表示の設定 |
| **Claude Code Guide** | ヘルプとドキュメント | Read、Glob、Grep | Haiku 4.5 | ヘルプ、機能学習 |

### サブエージェント設定フィールド

| フィールド | 型 | 説明 |
|-------|------|-------------|
| `name` | 文字列 | エージェント識別子 |
| `description` | 文字列 | エージェントの役割 |
| `model` | 文字列 | モデル上書き（例：`haiku-4.5`） |
| `tools` | 配列 | 許可ツール一覧 |
| `effort` | 文字列 | 推論努力レベル（`low`、`medium`、`high`） |
| `initialPrompt` | 文字列 | エージェント開始時に注入されるシステムプロンプト |
| `disallowedTools` | 配列 | 当エージェントに明示的に禁止するツール |

### カスタムサブエージェント（例）

| エージェント | 説明 | 利用シーン | スコープ | インストール |
|-------|-------------|-------------|-------|--------------|
| `code-reviewer` | 包括的なコード品質 | コードレビュー | プロジェクト | `cp 04-subagents/code-reviewer.md .claude/agents/` |
| `code-architect` | 機能アーキテクチャ設計 | 新機能計画 | プロジェクト | `cp 04-subagents/code-architect.md .claude/agents/` |
| `code-explorer` | コードベース深掘り分析 | 既存機能の理解 | プロジェクト | `cp 04-subagents/code-explorer.md .claude/agents/` |
| `clean-code-reviewer` | クリーンコード原則レビュー | 保守性レビュー | プロジェクト | `cp 04-subagents/clean-code-reviewer.md .claude/agents/` |
| `test-engineer` | テスト戦略とカバレッジ | テスト計画 | プロジェクト | `cp 04-subagents/test-engineer.md .claude/agents/` |
| `documentation-writer` | 技術ドキュメント | API ドキュメント、ガイド | プロジェクト | `cp 04-subagents/documentation-writer.md .claude/agents/` |
| `secure-reviewer` | セキュリティ重視レビュー | セキュリティ監査 | プロジェクト | `cp 04-subagents/secure-reviewer.md .claude/agents/` |
| `implementation-agent` | フル機能実装 | 機能開発 | プロジェクト | `cp 04-subagents/implementation-agent.md .claude/agents/` |
| `debugger` | 根本原因分析 | バグ調査 | ユーザー | `cp 04-subagents/debugger.md .claude/agents/` |
| `data-scientist` | SQL クエリ、データ分析 | データタスク | ユーザー | `cp 04-subagents/data-scientist.md .claude/agents/` |
| `performance-optimizer` | プロファイリングとチューニング | ボトルネック調査 | プロジェクト | `cp 04-subagents/performance-optimizer.md .claude/agents/` |

> **スコープ**：`ユーザー` = 個人（`~/.claude/agents/`）、`プロジェクト` = チーム共有（`.claude/agents/`）

**リファレンス**：[04-subagents/](04-subagents/) | [公式ドキュメント](https://code.claude.com/docs/en/sub-agents)

**クイックインストール（全カスタムエージェント）**：
```bash
cp 04-subagents/*.md .claude/agents/
```

---

## スキル

指示書、スクリプト、テンプレートを伴う自動起動機能。

### スキル例

| スキル | 説明 | 自動起動の条件 | スコープ | インストール |
|-------|-------------|-------------------|-------|--------------|
| `code-review` | 包括的なコードレビュー | "Review this code", "Check quality" | プロジェクト | `cp -r 03-skills/code-review .claude/skills/` |
| `brand-voice` | ブランド一貫性チェック | マーケティングコピー作成時 | プロジェクト | `cp -r 03-skills/brand-voice .claude/skills/` |
| `doc-generator` | API ドキュメント生成 | "Generate docs", "Document API" | プロジェクト | `cp -r 03-skills/doc-generator .claude/skills/` |
| `refactor` | 体系的リファクタリング（Martin Fowler） | "Refactor this", "Clean up code" | ユーザー | `cp -r 03-skills/refactor ~/.claude/skills/` |

> **スコープ**：`ユーザー` = 個人（`~/.claude/skills/`）、`プロジェクト` = チーム共有（`.claude/skills/`）

### スキル構造

```
~/.claude/skills/skill-name/
├── SKILL.md          # スキル定義と指示
├── scripts/          # 補助スクリプト
└── templates/        # 出力テンプレート
```

### スキルフロントマターのフィールド

スキルは設定のため `SKILL.md` 内で YAML フロントマターをサポートする。

| フィールド | 型 | 説明 |
|-------|------|-------------|
| `name` | 文字列 | スキル表示名 |
| `description` | 文字列 | スキルの役割 |
| `autoInvoke` | 配列 | 自動起動のトリガーフレーズ |
| `effort` | 文字列 | 推論努力レベル（`low`、`medium`、`high`） |
| `shell` | 文字列 | スクリプト実行に使うシェル（`bash`、`zsh`、`sh`） |

**リファレンス**：[03-skills/](03-skills/) | [公式ドキュメント](https://code.claude.com/docs/en/skills)

**クイックインストール（全スキル）**：
```bash
cp -r 03-skills/* ~/.claude/skills/
```

### バンドルスキル

| スキル | 説明 | 自動起動の条件 |
|-------|-------------|-------------------|
| `/simplify` | 品質目線でコードレビュー | コード執筆後 |
| `/batch` | 複数ファイルでプロンプト実行 | バッチ処理 |
| `/debug` | 失敗テスト・エラーのデバッグ | デバッグセッション |
| `/loop` | 一定間隔でプロンプト実行 | 反復タスク |
| `/claude-api` | Claude API でアプリ構築 | API 開発 |

---

## プラグイン

コマンド、エージェント、MCP サーバ、フックをまとめたバンドル。

### プラグイン例

| プラグイン | 説明 | 構成要素 | 利用シーン | スコープ | インストール |
|--------|-------------|------------|-------------|-------|--------------|
| `pr-review` | PR レビューワークフロー | コマンド 3、エージェント 3、GitHub MCP | コードレビュー | プロジェクト | `/plugin install pr-review` |
| `devops-automation` | デプロイと監視 | コマンド 4、エージェント 3、K8s MCP | DevOps タスク | プロジェクト | `/plugin install devops-automation` |
| `documentation` | ドキュメント生成スイート | コマンド 4、エージェント 3、テンプレート | ドキュメント | プロジェクト | `/plugin install documentation` |

> **スコープ**：`プロジェクト` = チーム共有、`ユーザー` = 個人ワークフロー

### プラグイン構造

```
.claude-plugin/
├── plugin.json       # マニフェストファイル
├── commands/         # スラッシュコマンド
├── agents/           # サブエージェント
├── skills/           # スキル
├── mcp/              # MCP 設定
├── hooks/            # フックスクリプト
└── scripts/          # ユーティリティスクリプト
```

**リファレンス**：[07-plugins/](07-plugins/) | [公式ドキュメント](https://code.claude.com/docs/en/plugins)

**プラグイン管理コマンド**：
```bash
/plugin list              # インストール済みプラグイン一覧
/plugin install <name>    # プラグインをインストール
/plugin remove <name>     # プラグインを削除
/plugin update <name>     # プラグインを更新
```

---

## MCP サーバ

外部ツールおよび API アクセスのための Model Context Protocol サーバ。

### 一般的な MCP サーバ

| サーバ | 説明 | 利用シーン | スコープ | インストール |
|--------|-------------|-------------|-------|--------------|
| **GitHub** | PR 管理、issue、コード | GitHub ワークフロー | プロジェクト | `claude mcp add github -- npx -y @modelcontextprotocol/server-github` |
| **Database** | SQL クエリ、データアクセス | DB 操作 | プロジェクト | `claude mcp add db -- npx -y @modelcontextprotocol/server-postgres` |
| **Filesystem** | 高度なファイル操作 | 複雑なファイルタスク | ユーザー | `claude mcp add fs -- npx -y @modelcontextprotocol/server-filesystem` |
| **Slack** | チームコミュニケーション | 通知、更新 | プロジェクト | 設定で構成 |
| **Google Docs** | ドキュメントアクセス | ドキュメント編集・レビュー | プロジェクト | 設定で構成 |
| **Asana** | プロジェクト管理 | タスク追跡 | プロジェクト | 設定で構成 |
| **Stripe** | 決済データ | 財務分析 | プロジェクト | 設定で構成 |
| **Memory** | 永続メモリ | セッション横断の想起 | ユーザー | 設定で構成 |
| **Context7** | ライブラリドキュメント | 最新ドキュメント検索 | 組み込み | 組み込み |

> **スコープ**：`プロジェクト` = チーム（`.mcp.json`）、`ユーザー` = 個人（`~/.claude.json`）、`組み込み` = プリインストール

### MCP 設定例

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["-y", "@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "${GITHUB_TOKEN}"
      }
    }
  }
}
```

**リファレンス**：[05-mcp/](05-mcp/) | [MCP プロトコルドキュメント](https://modelcontextprotocol.io)

**クイックインストール（GitHub MCP）**：
```bash
export GITHUB_TOKEN="your_token" && claude mcp add github -- npx -y @modelcontextprotocol/server-github
```

---

## フック

Claude Code のイベントでシェルコマンドを自動実行するイベント駆動の自動化。

### フックイベント

| イベント | 説明 | 発火タイミング | ユースケース |
|-------|-------------|----------------|-----------|
| `SessionStart` | セッション開始・再開 | セッション初期化時 | セットアップタスク |
| `InstructionsLoaded` | 指示読み込み完了 | CLAUDE.md またはルールファイルの読込時 | カスタム指示の処理 |
| `UserPromptSubmit` | プロンプト処理前 | ユーザーがメッセージ送信時 | 入力検証 |
| `PreToolUse` | ツール実行前 | 任意のツールが走る前 | 検証、ログ |
| `PermissionRequest` | 権限ダイアログ表示 | 機微な操作の前 | カスタム承認フロー |
| `PostToolUse` | ツール成功後 | 任意のツール完了後 | 整形、通知 |
| `PostToolUseFailure` | ツール実行失敗 | ツールエラー後 | エラー処理、ログ |
| `Notification` | 通知送信 | Claude が通知送信時 | 外部アラート |
| `SubagentStart` | サブエージェント生成 | サブエージェントタスク開始時 | サブエージェントコンテキスト初期化 |
| `SubagentStop` | サブエージェント終了 | サブエージェントタスク完了時 | アクション連鎖 |
| `Stop` | Claude が応答完了 | 応答完了時 | 後処理、レポート |
| `StopFailure` | API エラーでターン終了 | API エラー発生時 | エラー復旧、ログ |
| `TeammateIdle` | チームメンバーエージェントがアイドル | エージェントチーム協調時 | 作業の分配 |
| `TaskCompleted` | タスク完了マーク | タスク完了時 | タスク後処理 |
| `TaskCreated` | TaskCreate でタスク作成 | 新タスク作成時 | タスク追跡、ログ |
| `ConfigChange` | 設定更新 | 設定変更時 | 設定変更への対応 |
| `CwdChanged` | 作業ディレクトリ変更 | ディレクトリ変更時 | ディレクトリ別セットアップ |
| `FileChanged` | 監視ファイルの変更 | ファイル変更時 | ファイル監視、再ビルド |
| `PreCompact` | コンパクト操作前 | コンテキスト圧縮時 | 状態保全 |
| `PostCompact` | コンパクト完了後 | コンパクト完了時 | コンパクト後アクション |
| `WorktreeCreate` | ワークツリー作成中 | Git ワークツリー作成時 | ワークツリー環境セットアップ |
| `WorktreeRemove` | ワークツリー削除中 | Git ワークツリー削除時 | ワークツリーリソースのクリーンアップ |
| `Elicitation` | MCP サーバが入力を要求 | MCP elicitation 発生時 | 入力検証 |
| `ElicitationResult` | ユーザーが elicitation に応答 | ユーザー応答時 | 応答処理 |
| `SessionEnd` | セッション終了 | セッション終了時 | クリーンアップ、状態保存 |

### フック例

| フック | 説明 | イベント | スコープ | インストール |
|------|-------------|-------|-------|--------------|
| `validate-bash.py` | コマンド検証 | PreToolUse:Bash | プロジェクト | `cp 06-hooks/validate-bash.py .claude/hooks/` |
| `security-scan.py` | セキュリティスキャン | PostToolUse:Write | プロジェクト | `cp 06-hooks/security-scan.py .claude/hooks/` |
| `format-code.sh` | 自動整形 | PostToolUse:Write | ユーザー | `cp 06-hooks/format-code.sh ~/.claude/hooks/` |
| `validate-prompt.py` | プロンプト検証 | UserPromptSubmit | プロジェクト | `cp 06-hooks/validate-prompt.py .claude/hooks/` |
| `context-tracker.py` | トークン使用量追跡 | Stop | ユーザー | `cp 06-hooks/context-tracker.py ~/.claude/hooks/` |
| `pre-commit.sh` | コミット前検証 | PreToolUse:Bash | プロジェクト | `cp 06-hooks/pre-commit.sh .claude/hooks/` |
| `log-bash.sh` | コマンドログ | PostToolUse:Bash | ユーザー | `cp 06-hooks/log-bash.sh ~/.claude/hooks/` |
| `dependency-check.sh` | マニフェスト変更時の脆弱性スキャン | PostToolUse:Write | プロジェクト | `cp 06-hooks/dependency-check.sh .claude/hooks/` |

> **スコープ**：`プロジェクト` = チーム（`.claude/settings.json`）、`ユーザー` = 個人（`~/.claude/settings.json`）

### フック設定

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "command": "~/.claude/hooks/validate-bash.py"
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Write",
        "command": "~/.claude/hooks/format-code.sh"
      }
    ]
  }
}
```

**リファレンス**：[06-hooks/](06-hooks/) | [公式ドキュメント](https://code.claude.com/docs/en/hooks)

**クイックインストール（全フック）**：
```bash
mkdir -p ~/.claude/hooks && cp 06-hooks/*.sh ~/.claude/hooks/ && chmod +x ~/.claude/hooks/*.sh
```

---

## メモリファイル

セッション横断で自動読み込みされる永続コンテキスト。

### メモリの種類

| 種類 | 配置場所 | スコープ | 利用シーン |
|------|----------|-------|-------------|
| **マネージドポリシー** | 組織管理ポリシー | 組織 | 組織全体の標準を強制 |
| **プロジェクト** | `./CLAUDE.md` | プロジェクト（チーム） | チーム規約、プロジェクト文脈 |
| **プロジェクトルール** | `.claude/rules/` | プロジェクト（チーム） | モジュール化されたプロジェクトルール |
| **ユーザー** | `~/.claude/CLAUDE.md` | ユーザー（個人） | 個人の好み |
| **ユーザールール** | `~/.claude/rules/` | ユーザー（個人） | モジュール化された個人ルール |
| **ローカル** | `./CLAUDE.local.md` | ローカル（git 無視） | マシン固有の上書き（2026 年 3 月時点で公式ドキュメントに記載なし、レガシーの可能性） |
| **Auto Memory** | 自動 | セッション | 自動取得された洞察と訂正 |

> **スコープ**：`組織` = 管理者管理、`プロジェクト` = git でチーム共有、`ユーザー` = 個人の好み、`ローカル` = コミット非対象、`セッション` = 自動管理

**リファレンス**：[02-memory/](02-memory/) | [公式ドキュメント](https://code.claude.com/docs/en/memory)

**クイックインストール**：
```bash
cp 02-memory/project-CLAUDE.md ./CLAUDE.md
cp 02-memory/personal-CLAUDE.md ~/.claude/CLAUDE.md
```

---

## 新機能（2026 年 4 月）

| 機能 | 説明 | 使い方 |
|---------|-------------|------------|
| **/focus** | 注意散漫を防ぐ出力表示のためのフォーカスビュー切替（v2.1.110） | `/focus` で長時間タスク中の視覚的ノイズを低減 |
| **/proactive** | `/loop` のエイリアス — 同じ反復タスク動作（v2.1.105） | `/proactive` を `/loop` と互換に利用 |
| **/recap** | 既存セッションに戻ったときに要約を表示（v2.1.108） | 離席後に `/recap` を実行して文脈を取り戻す |
| **/tui** | フルスクリーン TUI モードを切替してちらつきのない描画（v2.1.110） | フルスクリーンターミナルや tmux で `/tui` を使う |
| **/undo** | `/rewind` のエイリアス — 直前のチェックポイントへ戻す（v2.1.108） | `/undo` を `/rewind` と互換に利用 |
| **Monitor ツール** | バックグラウンドコマンドの stdout を監視し、ポーリングではなくイベントで反応（v2.1.98+） | [高度な機能](09-advanced-features/) 経由で Monitor ツールを利用 |
| **/team-onboarding** | プロジェクトの Claude Code 設定からオンボーディングガイドを自動生成（v2.1.101） | プロジェクトで `/team-onboarding` を実行 |
| **Ultraplan 自動作成** | 初回 `/ultraplan` 実行時にクラウド環境を自動作成、手動セットアップ不要（v2.1.101） | `/ultraplan <prompt>` を使う |
| **リモートコントロール** | API 経由で Claude Code セッションを遠隔制御 | リモートコントロール API でプロンプト送信と応答取得をプログラム的に行う |
| **Web セッション** | ブラウザベース環境で Claude Code を実行 | `claude web` または Anthropic Console でアクセス |
| **デスクトップアプリ** | Claude Code のネイティブデスクトップアプリ | `/desktop` または Anthropic サイトからダウンロード |
| **Agent Teams** | 関連タスクで複数エージェントを協調 | コラボレーションと文脈共有を行う teammate エージェントを設定 |
| **タスクリスト** | バックグラウンドタスクの管理と監視 | `/tasks` でバックグラウンド処理を表示・管理 |
| **プロンプト候補** | コンテキスト依存のコマンド候補 | 現在の文脈に応じて候補が自動表示 |
| **Git ワークツリー** | 並列開発のための隔離 git ワークツリー | ワークツリーコマンドで安全な並列ブランチ作業 |
| **サンドボックス化** | 安全のための隔離実行環境 | `/sandbox` で切替、制限環境内でコマンドを実行 |
| **MCP OAuth** | MCP サーバ向け OAuth 認証 | 安全なアクセスのため MCP サーバ設定で OAuth 認証情報を構成 |
| **MCP ツール検索** | MCP ツールを動的に検索・発見 | 接続済みサーバ全体で利用可能な MCP ツールを検索 |
| **スケジュールタスク** | `/loop` および cron ツールで反復タスクを設定 | `/loop 5m /command` または CronCreate ツールを使う |
| **Chrome 連携** | ヘッドレス Chromium によるブラウザ自動化 | `--chrome` フラグまたは `/chrome` コマンドを使う |
| **キーバインドカスタマイズ** | コード対応を含むキーバインドのカスタマイズ | `/keybindings` を使うか `~/.claude/keybindings.json` を編集 |
| **Auto Mode** | 権限プロンプトなしの完全自律動作（Research Preview） | `--mode auto` または `/permissions auto` を使う、2026 年 3 月 |
| **チャンネル** | 複数チャネル通信（Telegram、Slack など）（Research Preview） | チャンネルプラグインを設定、2026 年 3 月 |
| **音声入力** | プロンプトの音声入力 | マイクアイコンまたは音声キーバインドを使う |
| **Agent フック種別** | シェルコマンド実行ではなくサブエージェントを生成するフック | フック設定で `"type": "agent"` を指定 |
| **Prompt フック種別** | プロンプトテキストを会話に注入するフック | フック設定で `"type": "prompt"` を指定 |
| **MCP Elicitation** | MCP サーバがツール実行中にユーザー入力を要求できる | `Elicitation` および `ElicitationResult` フックイベントで処理 |
| **プラグイン LSP サポート** | プラグイン経由の Language Server Protocol 統合 | エディタ機能のため `plugin.json` で LSP サーバを設定 |
| **マネージド Drop-in** | 組織管理のドロップイン設定（v2.1.83） | 管理ポリシーで管理者が設定、全ユーザーに自動適用 |

---

## クイックリファレンスマトリクス

### 機能選定ガイド

| 必要なもの | 推奨機能 | 理由 |
|------|---------------------|-----|
| 高速ショートカット | スラッシュコマンド | 手動、即時 |
| 永続コンテキスト | メモリ | 自動読み込み |
| 複雑な自動化 | スキル | 自動起動 |
| 専門タスク | サブエージェント | コンテキスト分離 |
| 外部データ | MCP サーバ | リアルタイムアクセス |
| イベント自動化 | フック | イベントトリガー |
| 完全ソリューション | プラグイン | オールインワン |

### インストール優先順位

| 優先度 | 機能 | コマンド |
|----------|---------|---------|
| 1. 必須 | メモリ | `cp 02-memory/project-CLAUDE.md ./CLAUDE.md` |
| 2. 日常利用 | スラッシュコマンド | `cp 01-slash-commands/*.md .claude/commands/` |
| 3. 品質 | サブエージェント | `cp 04-subagents/*.md .claude/agents/` |
| 4. 自動化 | フック | `cp 06-hooks/*.sh ~/.claude/hooks/ && chmod +x ~/.claude/hooks/*.sh` |
| 5. 外部 | MCP | `claude mcp add github -- npx -y @modelcontextprotocol/server-github` |
| 6. 高度 | スキル | `cp -r 03-skills/* ~/.claude/skills/` |
| 7. 完全 | プラグイン | `/plugin install pr-review` |

---

## ワンコマンド完全インストール

このリポジトリの全例題をインストールする：

```bash
# ディレクトリを作成
mkdir -p .claude/{commands,agents,skills} ~/.claude/{hooks,skills}

# 全機能をインストール
cp 01-slash-commands/*.md .claude/commands/ && \
cp 02-memory/project-CLAUDE.md ./CLAUDE.md && \
cp -r 03-skills/* ~/.claude/skills/ && \
cp 04-subagents/*.md .claude/agents/ && \
cp 06-hooks/*.sh ~/.claude/hooks/ && \
chmod +x ~/.claude/hooks/*.sh
```

---

## 追加リソース

- [Claude Code 公式ドキュメント](https://code.claude.com/docs/en/overview)
- [MCP プロトコル仕様](https://modelcontextprotocol.io)
- [学習ロードマップ](LEARNING-ROADMAP.md)
- [メイン README](README.md)

---

**最終更新**：2026 年 4 月 24 日
**Claude Code バージョン**：2.1.119
**情報源**：
- https://code.claude.com/docs/en/overview
- https://code.claude.com/docs/en/commands
- https://code.claude.com/docs/en/hooks
- https://github.com/anthropics/claude-code/releases/tag/v2.1.118
**互換モデル**：Claude Sonnet 4.6、Claude Opus 4.7、Claude Haiku 4.5
