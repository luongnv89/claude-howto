<!-- i18n-source: README.md -->
<!-- i18n-source-sha: d17d515 -->
<!-- i18n-date: 2026-04-27 -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

<p align="center">
  <a href="https://github.com/trending">
    <img src="https://img.shields.io/badge/GitHub-🔥%20%231%20Trending-purple?style=for-the-badge&logo=github"/>
  </a>
</p>

[![GitHub Stars](https://img.shields.io/github/stars/luongnv89/claude-howto?style=flat&color=gold)](https://github.com/luongnv89/claude-howto/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/luongnv89/claude-howto?style=flat)](https://github.com/luongnv89/claude-howto/network/members)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](../LICENSE)
[![Version](https://img.shields.io/badge/version-2.1.119-brightgreen)](../CHANGELOG.md)
[![Claude Code](https://img.shields.io/badge/Claude_Code-2.1+-purple)](https://code.claude.com)

🌐 **Language / Ngôn ngữ / 语言 / Мова / 言語:** [English](../README.md) | [Tiếng Việt](../vi/README.md) | [中文](../zh/README.md) | [Українська](../uk/README.md) | [日本語](README.md)

# Claude Code を週末でマスターする

`claude` と打ち込むだけの段階から、エージェント、フック、スキル、MCP サーバを束ねる段階へ。視覚的なチュートリアル、コピペで使えるテンプレート、ガイド付き学習パスで導く。

**[15 分で始める](#15-分で始める)** | **[自分のレベルを見つける](#どこから始めればよいか分からない)** | **[機能カタログを見る](CATALOG.md)**

---

## 目次

- [課題](#課題)
- [Claude How To が解決する方法](#claude-how-to-が解決する方法)
- [仕組み](#仕組み)
- [どこから始めればよいか分からない？](#どこから始めればよいか分からない)
- [15 分で始める](#15-分で始める)
- [何が作れるか](#何が作れるか)
- [FAQ](#faq)
- [コントリビュート](#コントリビュート)
- [ライセンス](#ライセンス)

---

## 課題

Claude Code をインストールし、いくつかプロンプトを実行した。次は何をすべきか。

- **公式ドキュメントは機能を説明するが、組み合わせ方は示さない。** スラッシュコマンドの存在は知っていても、フック、メモリ、サブエージェントと連携させて、本当に時間を節約するワークフローに組み立てる方法は分からない。
- **明確な学習パスがない。** MCP をフックの前に学ぶべきか。スキルをサブエージェントの前に学ぶべきか。結局すべてを流し読みして、何一つマスターできない。
- **例題が基本的すぎる。** 「hello world」のスラッシュコマンドでは、メモリを使い、専門エージェントに委譲し、セキュリティスキャンを自動実行する本番品質のコードレビューパイプラインは作れない。

Claude Code の力の 90% を眠らせたままで、しかも自分が何を知らないかすら分かっていない状態である。

---

## Claude How To が解決する方法

これは単なる機能リファレンスではない。**構造化された、視覚的な、サンプル駆動のガイド** であり、Claude Code の各機能の使い方を、今日プロジェクトにそのままコピーして使える実践テンプレートとともに教える。

| | 公式ドキュメント | 本ガイド |
|--|---------------|------------|
| **形式** | リファレンスドキュメント | Mermaid 図つきの視覚的チュートリアル |
| **深さ** | 機能の説明 | 内部の動作原理 |
| **例** | 基本的なスニペット | すぐ使える本番品質テンプレート |
| **構造** | 機能別の編成 | 段階的な学習パス（初級から上級まで） |
| **オンボーディング** | 自己学習 | 所要時間つきガイド付きロードマップ |
| **自己評価** | なし | 弱点を見つけて個別パスを構築するインタラクティブ・クイズ |

### 得られるもの

- **10 個のチュートリアルモジュール**：スラッシュコマンドからカスタムエージェントチームまで、Claude Code の全機能を網羅
- **コピペ可能な設定**：スラッシュコマンド、CLAUDE.md テンプレート、フックスクリプト、MCP 設定、サブエージェント定義、フルプラグインバンドル
- **Mermaid 図** で各機能の内部動作を可視化し、「どう」だけでなく「なぜ」を理解できる
- **ガイド付き学習パス** によって 11〜13 時間で初級者からパワーユーザーまで到達できる
- **組み込みの自己評価**：Claude Code 内で `/self-assessment` または `/lesson-quiz hooks` を実行して弱点を特定できる

**[学習パスを始める ->](LEARNING-ROADMAP.md)**

---

## 仕組み

### 1. 自分のレベルを見つける

[自己評価クイズ](LEARNING-ROADMAP.md#-自分のレベルを見つける) を受けるか、Claude Code 内で `/self-assessment` を実行する。すでに知っていることに基づいた個別ロードマップが得られる。

### 2. ガイド付きパスを進む

10 モジュールを順に進める。各モジュールは前のモジュールの上に積み上がる。学びながら、テンプレートをそのままプロジェクトにコピーする。

### 3. 機能を組み合わせてワークフローにする

真の力は機能の組み合わせにある。スラッシュコマンド、メモリ、サブエージェント、フックを連携させて、コードレビュー、デプロイ、ドキュメント生成を自動化するパイプラインの作り方を学ぶ。

### 4. 理解度を試す

各モジュールの後に `/lesson-quiz [トピック]` を実行する。クイズが見落とした箇所を特定するため、弱点をすばやく埋められる。

**[15 分で始める](#15-分で始める)**

---

## 21,800 名以上の開発者に信頼されている

- **GitHub スター 21,800 個以上**：日常的に Claude Code を使う開発者から
- **フォーク 2,585 件以上**：自チームのワークフローに合わせて応用するチームから
- **積極的にメンテナンス**：Claude Code のリリースに同期（最新は v2.1.119、2026 年 4 月）
- **コミュニティ駆動**：実際の運用設定を共有する開発者からのコントリビュート

[![Star History Chart](https://api.star-history.com/svg?repos=luongnv89/claude-howto&type=Date)](https://star-history.com/#luongnv89/claude-howto&Date)

---

## どこから始めればよいか分からない？

自己評価を受けるか、レベルを選ぶ。

| レベル | できること | スタート地点 | 所要時間 |
|-------|-----------|------------|------|
| **初級** | Claude Code を起動して対話 | [スラッシュコマンド](01-slash-commands/) | 約 2.5 時間 |
| **中級** | CLAUDE.md とカスタムコマンドを使う | [スキル](03-skills/) | 約 3.5 時間 |
| **上級** | MCP サーバとフックを設定する | [高度な機能](09-advanced-features/) | 約 5 時間 |

**全 10 モジュールの完全学習パス：**

| 順序 | モジュール | レベル | 所要時間 |
|-------|--------|-------|------|
| 1 | [スラッシュコマンド](01-slash-commands/) | 初級 | 30 分 |
| 2 | [メモリ](02-memory/) | 初級+ | 45 分 |
| 3 | [チェックポイント](08-checkpoints/) | 中級 | 45 分 |
| 4 | [CLI 基礎](10-cli/) | 初級+ | 30 分 |
| 5 | [スキル](03-skills/) | 中級 | 1 時間 |
| 6 | [フック](06-hooks/) | 中級 | 1 時間 |
| 7 | [MCP](05-mcp/) | 中級+ | 1 時間 |
| 8 | [サブエージェント](04-subagents/) | 中級+ | 1.5 時間 |
| 9 | [高度な機能](09-advanced-features/) | 上級 | 2〜3 時間 |
| 10 | [プラグイン](07-plugins/) | 上級 | 2 時間 |

**[完全学習ロードマップ ->](LEARNING-ROADMAP.md)**

---

## 15 分で始める

> **インストールに関する注記**：v2.1.113 以降、Claude Code はプラットフォーム別のネイティブバイナリ（macOS / Linux / Windows）として配布される。`npm install -g @anthropic-ai/claude-code` も引き続き利用可能で、初回利用時にネイティブバイナリがオプション依存関係としてダウンロードされる。v2.1.116 以降、ダウンロード元は `https://downloads.claude.ai/claude-code-releases` であり、企業プロキシではこのホストを許可リストに加える必要がある。

```bash
# 1. ガイドをクローン
git clone https://github.com/luongnv89/claude-howto.git
cd claude-howto

# 2. 最初のスラッシュコマンドをコピー
mkdir -p /path/to/your-project/.claude/commands
cp 01-slash-commands/optimize.md /path/to/your-project/.claude/commands/

# 3. 試す — Claude Code で次を入力:
# /optimize

# 4. 次に進みたければ、プロジェクトメモリを設定:
cp 02-memory/project-CLAUDE.md /path/to/your-project/CLAUDE.md

# 5. スキルをインストール:
cp -r 03-skills/code-review ~/.claude/skills/
```

フルセットアップが必要なら、**1 時間で必要な設定** はこちら。

```bash
# スラッシュコマンド (15 分)
cp 01-slash-commands/*.md .claude/commands/

# プロジェクトメモリ (15 分)
cp 02-memory/project-CLAUDE.md ./CLAUDE.md

# スキルをインストール (15 分)
cp -r 03-skills/code-review ~/.claude/skills/

# 週末ゴール: フック、サブエージェント、MCP、プラグインを追加
# ガイド付きセットアップは学習パスに従う
```

**[完全インストールリファレンスを見る](#15-分で始める)**

---

## 何が作れるか

| ユースケース | 組み合わせる機能 |
|----------|------------------------|
| **自動コードレビュー** | スラッシュコマンド + サブエージェント + メモリ + MCP |
| **チームオンボーディング** | メモリ + スラッシュコマンド + プラグイン |
| **CI/CD 自動化** | CLI リファレンス + フック + バックグラウンドタスク |
| **ドキュメント生成** | スキル + サブエージェント + プラグイン |
| **セキュリティ監査** | サブエージェント + スキル + フック（読み取り専用モード） |
| **DevOps パイプライン** | プラグイン + MCP + フック + バックグラウンドタスク |
| **複雑なリファクタリング** | チェックポイント + プランニングモード + フック |

---

## FAQ

**無料か？**
そう。MIT ライセンスで永遠に無料。個人プロジェクト、業務、チームで自由に使える。ライセンス表記の同梱以外に制約はない。

**メンテナンスされているか？**
積極的に。本ガイドは Claude Code のリリースごとに同期される。現行バージョンは v2.1.119（2026 年 4 月）で、Claude Code 2.1+ と互換。

**公式ドキュメントとの違いは？**
公式ドキュメントは機能リファレンスである。本ガイドは図、本番品質テンプレート、段階的な学習パスを備えたチュートリアルである。両者は補完関係にある。学ぶときはここから始め、具体的な仕様が必要なときに公式を参照するとよい。

**全部進めるのにどれくらいかかるか？**
完全パスで 11〜13 時間。ただし 15 分で即座に価値が得られる。スラッシュコマンドのテンプレートをコピーして試すだけでよい。

**Claude Sonnet / Haiku / Opus と一緒に使えるか？**
使える。すべてのテンプレートは Claude Sonnet 4.6、Claude Opus 4.7、Claude Haiku 4.5 で動作する。

**コントリビュートできるか？**
もちろん。ガイドラインは [CONTRIBUTING.md](CONTRIBUTING.md) を参照。新しい例、バグ修正、ドキュメント改善、コミュニティテンプレートを歓迎する。

**オフラインで読めるか？**
読める。`uv run scripts/build_epub.py` を実行すれば、すべてのコンテンツとレンダリング済みの図を含む EPUB 電子書籍が生成される。

---

## 今日から Claude Code をマスターし始める

すでに Claude Code はインストール済みのはず。あとは使いこなし方を知るだけで、生産性が 10 倍になる。本ガイドはそこに到達する構造化されたパス、視覚的な解説、コピペで使えるテンプレートを提供する。

MIT ライセンス。永遠に無料。クローンして、フォークして、自分のものにしてほしい。

**[学習パスを始める ->](LEARNING-ROADMAP.md)** | **[機能カタログを見る](CATALOG.md)** | **[15 分で始める](#15-分で始める)**

---

<details>
<summary>クイックナビゲーション — 全機能</summary>

| 機能 | 説明 | フォルダ |
|---------|-------------|--------|
| **機能カタログ** | インストールコマンド付き完全リファレンス | [CATALOG.md](CATALOG.md) |
| **スラッシュコマンド** | ユーザーが実行するショートカット | [01-slash-commands/](01-slash-commands/) |
| **メモリ** | 永続的なコンテキスト | [02-memory/](02-memory/) |
| **スキル** | 再利用可能な機能 | [03-skills/](03-skills/) |
| **サブエージェント** | 専門特化した AI アシスタント | [04-subagents/](04-subagents/) |
| **MCP プロトコル** | 外部ツールアクセス | [05-mcp/](05-mcp/) |
| **フック** | イベント駆動の自動化 | [06-hooks/](06-hooks/) |
| **プラグイン** | バンドルされた機能 | [07-plugins/](07-plugins/) |
| **チェックポイント** | セッションのスナップショットと巻き戻し | [08-checkpoints/](08-checkpoints/) |
| **高度な機能** | プランニング、思考、バックグラウンドタスク | [09-advanced-features/](09-advanced-features/) |
| **CLI リファレンス** | コマンド、フラグ、オプション | [10-cli/](10-cli/) |
| **ブログ記事** | 実際の利用例 | [Blog Posts](https://medium.com/@luongnv89) |

</details>

<details>
<summary>機能比較</summary>

| 機能 | 起動方法 | 永続性 | 適している用途 |
|---------|-----------|------------|----------|
| **スラッシュコマンド** | 手動 (`/cmd`) | セッション内のみ | クイックショートカット |
| **メモリ** | 自動ロード | セッション横断 | 長期的な学習 |
| **スキル** | 自動起動 | ファイルシステム | 自動化ワークフロー |
| **サブエージェント** | 自動委譲 | コンテキスト分離 | タスク分散 |
| **MCP プロトコル** | 自動問い合わせ | リアルタイム | ライブデータアクセス |
| **フック** | イベントトリガー | 設定値で永続化 | 自動化と検証 |
| **プラグイン** | 1 コマンド | 全機能を含む | 完全なソリューション |
| **チェックポイント** | 手動 / 自動 | セッション単位 | 安全な実験 |
| **プランニングモード** | 手動 / 自動 | 計画フェーズ | 複雑な実装 |
| **バックグラウンドタスク** | 手動 | タスク存続期間 | 長時間処理 |
| **CLI リファレンス** | ターミナルコマンド | セッション / スクリプト | 自動化とスクリプト |

</details>

<details>
<summary>インストール早見表</summary>

```bash
# Slash Commands
cp 01-slash-commands/*.md .claude/commands/

# Memory
cp 02-memory/project-CLAUDE.md ./CLAUDE.md

# Skills
cp -r 03-skills/code-review ~/.claude/skills/

# Subagents
cp 04-subagents/*.md .claude/agents/

# MCP
export GITHUB_TOKEN="token"
claude mcp add github -- npx -y @modelcontextprotocol/server-github

# Hooks
mkdir -p ~/.claude/hooks
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh

# Plugins
/plugin install pr-review

# Checkpoints (自動有効、設定で調整)
# 08-checkpoints/README.md を参照

# Advanced Features (設定で調整)
# 09-advanced-features/config-examples.json を参照

# CLI Reference (インストール不要)
# 利用例は 10-cli/README.md を参照
```

</details>

<details>
<summary>01. スラッシュコマンド</summary>

**配置場所**：[01-slash-commands/](01-slash-commands/)

**概要**：Markdown ファイルとして保存される、ユーザーが実行するショートカット

**例**：
- `optimize.md` — コード最適化分析
- `pr.md` — プルリクエスト準備
- `generate-api-docs.md` — API ドキュメント生成

**インストール**：
```bash
cp 01-slash-commands/*.md /path/to/project/.claude/commands/
```

**使い方**：
```
/optimize
/pr
/generate-api-docs
```

**詳しく学ぶ**：[Discovering Claude Code Slash Commands](https://medium.com/@luongnv89/discovering-claude-code-slash-commands-cdc17f0dfb29)

</details>

<details>
<summary>02. メモリ</summary>

**配置場所**：[02-memory/](02-memory/)

**概要**：セッションをまたいで保持される永続的なコンテキスト

**例**：
- `project-CLAUDE.md` — チーム共通のプロジェクト規約
- `directory-api-CLAUDE.md` — ディレクトリ固有のルール
- `personal-CLAUDE.md` — 個人の好み

**インストール**：
```bash
# プロジェクトメモリ
cp 02-memory/project-CLAUDE.md /path/to/project/CLAUDE.md

# ディレクトリメモリ
cp 02-memory/directory-api-CLAUDE.md /path/to/project/src/api/CLAUDE.md

# 個人メモリ
cp 02-memory/personal-CLAUDE.md ~/.claude/CLAUDE.md
```

**使い方**：Claude が自動的に読み込む

</details>

<details>
<summary>03. スキル</summary>

**配置場所**：[03-skills/](03-skills/)

**概要**：指示書とスクリプトを備えた、再利用可能で自動起動される機能

**例**：
- `code-review/` — スクリプトつきの包括的なコードレビュー
- `brand-voice/` — ブランドボイスの一貫性チェッカー
- `doc-generator/` — API ドキュメント生成

**インストール**：
```bash
# 個人スキル
cp -r 03-skills/code-review ~/.claude/skills/

# プロジェクトスキル
cp -r 03-skills/code-review /path/to/project/.claude/skills/
```

**使い方**：関連する場面で自動的に起動される

</details>

<details>
<summary>04. サブエージェント</summary>

**配置場所**：[04-subagents/](04-subagents/)

**概要**：分離されたコンテキストとカスタムプロンプトを持つ、専門特化した AI アシスタント

**例**：
- `code-reviewer.md` — 包括的なコード品質分析
- `test-engineer.md` — テスト戦略とカバレッジ
- `documentation-writer.md` — 技術ドキュメント作成
- `secure-reviewer.md` — セキュリティ重視のレビュー（読み取り専用）
- `implementation-agent.md` — 機能の完全実装

**インストール**：
```bash
cp 04-subagents/*.md /path/to/project/.claude/agents/
```

**使い方**：メインエージェントが自動的に委譲する

</details>

<details>
<summary>05. MCP プロトコル</summary>

**配置場所**：[05-mcp/](05-mcp/)

**概要**：外部ツールや API にアクセスするための Model Context Protocol

**例**：
- `github-mcp.json` — GitHub 連携
- `database-mcp.json` — データベースクエリ
- `filesystem-mcp.json` — ファイル操作
- `multi-mcp.json` — 複数の MCP サーバ

**インストール**：
```bash
# 環境変数を設定
export GITHUB_TOKEN="your_token"
export DATABASE_URL="postgresql://..."

# CLI で MCP サーバを追加
claude mcp add github -- npx -y @modelcontextprotocol/server-github

# またはプロジェクト .mcp.json に手動追加 (例は 05-mcp/ を参照)
```

**使い方**：設定後、MCP ツールは自動的に Claude から利用可能になる

</details>

<details>
<summary>06. フック</summary>

**配置場所**：[06-hooks/](06-hooks/)

**概要**：Claude Code のイベントに応じて自動実行されるイベント駆動シェルコマンド

**例**：
- `format-code.sh` — 書き込み前にコードを自動整形
- `pre-commit.sh` — コミット前にテストを実行
- `security-scan.sh` — セキュリティ問題のスキャン
- `log-bash.sh` — すべての bash コマンドをログに記録
- `validate-prompt.sh` — ユーザープロンプトを検証
- `notify-team.sh` — イベント発生時の通知送信

**インストール**：
```bash
mkdir -p ~/.claude/hooks
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh
```

`~/.claude/settings.json` でフックを設定する：
```json
{
  "hooks": {
    "PreToolUse": [{
      "matcher": "Write",
      "hooks": ["~/.claude/hooks/format-code.sh"]
    }],
    "PostToolUse": [{
      "matcher": "Write",
      "hooks": ["~/.claude/hooks/security-scan.sh"]
    }]
  }
}
```

**使い方**：イベント発生時にフックが自動実行される

**フックの種類**（5 系統、28 イベント）：
- **ツール系フック**：`PreToolUse`、`PostToolUse`、`PostToolUseFailure`、`PermissionRequest`
- **セッション系フック**：`SessionStart`、`SessionEnd`、`Stop`、`StopFailure`、`SubagentStart`、`SubagentStop`
- **タスク系フック**：`UserPromptSubmit`、`TaskCompleted`、`TaskCreated`、`TeammateIdle`
- **ライフサイクル系フック**：`ConfigChange`、`CwdChanged`、`FileChanged`、`PreCompact`、`PostCompact`、`WorktreeCreate`、`WorktreeRemove`、`Notification`、`InstructionsLoaded`、`Elicitation`、`ElicitationResult`

</details>

<details>
<summary>07. プラグイン</summary>

**配置場所**：[07-plugins/](07-plugins/)

**概要**：コマンド、エージェント、MCP、フックをまとめたバンドル

**例**：
- `pr-review/` — 完全な PR レビューワークフロー
- `devops-automation/` — デプロイと監視
- `documentation/` — ドキュメント生成

**インストール**：
```bash
/plugin install pr-review
/plugin install devops-automation
/plugin install documentation
```

**使い方**：バンドルされたスラッシュコマンドや機能を利用する

</details>

<details>
<summary>08. チェックポイントと巻き戻し</summary>

**配置場所**：[08-checkpoints/](08-checkpoints/)

**概要**：会話の状態を保存し、過去地点に巻き戻して別のアプローチを試す機能

**主要概念**：
- **チェックポイント**：会話状態のスナップショット
- **巻き戻し**：以前のチェックポイントへ戻る
- **分岐点**：同じチェックポイントから複数のアプローチを試す

**使い方**：
```
# チェックポイントはユーザープロンプトのたびに自動作成される
# 巻き戻しは Esc を 2 回押すか、次を実行:
/rewind

# 5 つの選択肢から選ぶ:
# 1. コードと会話を復元
# 2. 会話のみ復元
# 3. コードのみ復元
# 4. ここから要約
# 5. やめる
```

**ユースケース**：
- 複数の実装アプローチを試す
- ミスからのリカバリ
- 安全な実験
- 代替案の比較
- 異なる設計の A/B テスト

</details>

<details>
<summary>09. 高度な機能</summary>

**配置場所**：[09-advanced-features/](09-advanced-features/)

**概要**：複雑なワークフローと自動化のための高度な機能

**含まれる機能**：
- **プランニングモード** — コーディング前に詳細な実装計画を作成
- **拡張思考（Extended Thinking）** — 複雑な問題に対する深い推論（`Alt+T` / `Option+T` で切り替え）
- **バックグラウンドタスク** — ブロックなしに長時間処理を実行
- **権限モード** — `default`、`acceptEdits`、`plan`、`dontAsk`、`bypassPermissions`
- **ヘッドレスモード** — CI/CD で Claude Code を実行：`claude -p "Run tests and generate report"`
- **セッション管理** — `/resume`、`/rename`、`/fork`、`claude -c`、`claude -r`
- **設定** — `~/.claude/settings.json` で挙動をカスタマイズ

完全な設定例は [config-examples.json](09-advanced-features/config-examples.json) を参照。

</details>

<details>
<summary>10. CLI リファレンス</summary>

**配置場所**：[10-cli/](10-cli/)

**概要**：Claude Code のコマンドラインインターフェース完全リファレンス

**簡単な例**：
```bash
# 対話モード
claude "explain this project"

# 印字モード (非対話)
claude -p "review this code"

# ファイル内容を処理
cat error.log | claude -p "explain this error"

# スクリプト向け JSON 出力
claude -p --output-format json "list functions"

# セッション再開
claude -r "feature-auth" "continue implementation"
```

**ユースケース**：CI/CD パイプライン統合、スクリプト自動化、バッチ処理、複数セッションのワークフロー、カスタムエージェント設定

</details>

<details>
<summary>ワークフロー例</summary>

### 完全なコードレビューワークフロー

```markdown
# 利用機能: スラッシュコマンド + サブエージェント + メモリ + MCP

User: /review-pr

Claude:
1. プロジェクトメモリ (コーディング規約) を読み込む
2. GitHub MCP 経由で PR を取得
3. code-reviewer サブエージェントに委譲
4. test-engineer サブエージェントに委譲
5. 知見を統合
6. 包括的なレビューを提供
```

### ドキュメント自動生成

```markdown
# 利用機能: スキル + サブエージェント + メモリ

User: "auth モジュールの API ドキュメントを生成して"

Claude:
1. プロジェクトメモリ (ドキュメント規約) を読み込む
2. ドキュメント生成リクエストを検知
3. doc-generator スキルを自動起動
4. api-documenter サブエージェントに委譲
5. 例つきの包括的なドキュメントを作成
```

### DevOps デプロイ

```markdown
# 利用機能: プラグイン + MCP + フック

User: /deploy production

Claude:
1. デプロイ前フックを実行 (環境を検証)
2. deployment-specialist サブエージェントに委譲
3. Kubernetes MCP 経由でデプロイ実行
4. 進捗を監視
5. デプロイ後フックを実行 (ヘルスチェック)
6. ステータスを報告
```

</details>

<details>
<summary>ディレクトリ構造</summary>

```
├── 01-slash-commands/
│   ├── optimize.md
│   ├── pr.md
│   ├── generate-api-docs.md
│   └── README.md
├── 02-memory/
│   ├── project-CLAUDE.md
│   ├── directory-api-CLAUDE.md
│   ├── personal-CLAUDE.md
│   └── README.md
├── 03-skills/
│   ├── code-review/
│   │   ├── SKILL.md
│   │   ├── scripts/
│   │   └── templates/
│   ├── brand-voice/
│   │   ├── SKILL.md
│   │   └── templates/
│   ├── doc-generator/
│   │   ├── SKILL.md
│   │   └── generate-docs.py
│   └── README.md
├── 04-subagents/
│   ├── code-reviewer.md
│   ├── test-engineer.md
│   ├── documentation-writer.md
│   ├── secure-reviewer.md
│   ├── implementation-agent.md
│   └── README.md
├── 05-mcp/
│   ├── github-mcp.json
│   ├── database-mcp.json
│   ├── filesystem-mcp.json
│   ├── multi-mcp.json
│   └── README.md
├── 06-hooks/
│   ├── format-code.sh
│   ├── pre-commit.sh
│   ├── security-scan.sh
│   ├── log-bash.sh
│   ├── validate-prompt.sh
│   ├── notify-team.sh
│   └── README.md
├── 07-plugins/
│   ├── pr-review/
│   ├── devops-automation/
│   ├── documentation/
│   └── README.md
├── 08-checkpoints/
│   ├── checkpoint-examples.md
│   └── README.md
├── 09-advanced-features/
│   ├── config-examples.json
│   ├── planning-mode-examples.md
│   └── README.md
├── 10-cli/
│   └── README.md
└── README.md (このファイル)
```

</details>

<details>
<summary>ベストプラクティス</summary>

### 推奨事項
- スラッシュコマンドからシンプルに始める
- 機能を段階的に追加する
- メモリにチーム規約を入れる
- 設定はまずローカルで試す
- カスタム実装をドキュメント化する
- プロジェクト設定をバージョン管理する
- プラグインをチームで共有する

### 避けるべきこと
- 重複した機能を作らない
- 認証情報をハードコードしない
- ドキュメント化を省略しない
- 単純なタスクを過度に複雑にしない
- セキュリティのベストプラクティスを無視しない
- 機密データをコミットしない

</details>

<details>
<summary>トラブルシューティング</summary>

### 機能が読み込まれない
1. ファイルの配置場所と命名を確認
2. YAML フロントマターの構文を確認
3. ファイル権限を確認
4. Claude Code のバージョン互換性を確認

### MCP 接続失敗
1. 環境変数を確認
2. MCP サーバのインストールを確認
3. 認証情報をテスト
4. ネットワーク接続を確認

### サブエージェントに委譲されない
1. ツール権限を確認
2. エージェント説明文の明確さを確認
3. タスクの複雑度を確認
4. エージェント単体でテスト

</details>

<details>
<summary>テスト</summary>

このプロジェクトには包括的な自動テストが含まれる。

- **ユニットテスト**：pytest を使った Python テスト（Python 3.10、3.11、3.12）
- **コード品質**：Ruff によるリンティングとフォーマット
- **セキュリティ**：Bandit による脆弱性スキャン
- **型チェック**：mypy による静的型解析
- **ビルド検証**：EPUB 生成のテスト
- **カバレッジ計測**：Codecov 統合

```bash
# 開発依存関係をインストール
uv pip install -r requirements-dev.txt

# 全ユニットテストを実行
pytest scripts/tests/ -v

# カバレッジレポートつきでテスト実行
pytest scripts/tests/ -v --cov=scripts --cov-report=html

# コード品質チェック
ruff check scripts/
ruff format --check scripts/

# セキュリティスキャン
bandit -c pyproject.toml -r scripts/ --exclude scripts/tests/

# 型チェック
mypy scripts/ --ignore-missing-imports
```

`main`/`develop` への push および `main` への PR で自動的にテストが実行される。詳細は [TESTING.md](../.github/TESTING.md) を参照。

</details>

<details>
<summary>EPUB 生成</summary>

本ガイドをオフラインで読みたい場合は EPUB 電子書籍を生成する。

```bash
uv run scripts/build_epub.py
```

これによりレンダリング済み Mermaid 図を含む全コンテンツの `claude-howto-guide.epub` が作成される。

詳細なオプションは [scripts/README.md](../scripts/README.md) を参照。

</details>

<details>
<summary>コントリビュート</summary>

問題を見つけた、もしくは例を提供したい場合は歓迎する。

**詳細なガイドラインは [CONTRIBUTING.md](CONTRIBUTING.md) を参照：**
- コントリビュートの種類（例、ドキュメント、機能、バグ、フィードバック）
- 開発環境のセットアップ方法
- ディレクトリ構造とコンテンツ追加方法
- 執筆ガイドラインとベストプラクティス
- コミットおよび PR プロセス

**コミュニティ標準：**
- [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) — メンバー同士の接し方
- [SECURITY.md](SECURITY.md) — セキュリティポリシーと脆弱性報告

### セキュリティ問題の報告

セキュリティ脆弱性を発見した場合は、責任ある形で報告してほしい。

1. **GitHub のプライベート脆弱性報告を使う**：https://github.com/luongnv89/claude-howto/security/advisories
2. **または** [.github/SECURITY_REPORTING.md](../.github/SECURITY_REPORTING.md) で詳細手順を読む
3. セキュリティ脆弱性については **公開 issue を立てない**

クイックスタート：
1. リポジトリをフォークしてクローン
2. 内容が分かるブランチ名を作る（`add/feature-name`、`fix/bug`、`docs/improvement` など）
3. ガイドラインに沿って変更を加える
4. 明確な説明をつけてプルリクエストを送る

**助けが必要なら？** issue かディスカッションを立てれば、プロセスを案内する。

</details>

<details>
<summary>追加リソース</summary>

- [Claude Code Documentation](https://code.claude.com/docs/en/overview)
- [MCP Protocol Specification](https://modelcontextprotocol.io)
- [Skills Repository](https://github.com/luongnv89/skills) — すぐ使えるスキル集
- [Anthropic Cookbook](https://github.com/anthropics/anthropic-cookbook)
- [Boris Cherny's Claude Code Workflow](https://x.com/bcherny/status/2007179832300581177) — Claude Code の制作者が体系化したワークフローを共有：並列エージェント、共有 CLAUDE.md、プランニングモード、スラッシュコマンド、サブエージェント、自律的長時間セッションのための検証フック。

</details>

---

## コントリビュート

コントリビュートを歓迎する。始め方の詳細は [Contributing Guide](CONTRIBUTING.md) を参照。

---

## ライセンス

MIT License — [LICENSE](../LICENSE) を参照。利用、変更、再配布は自由。唯一の条件はライセンス表記の同梱である。

---

**最終更新**：2026 年 4 月 24 日
**Claude Code バージョン**：2.1.119
**情報源**：
- https://code.claude.com/docs/en/overview
- https://code.claude.com/docs/en/changelog
- https://github.com/anthropics/claude-code/releases/tag/v2.1.119
- https://github.com/anthropics/claude-code/releases/tag/v2.1.113
**互換モデル**：Claude Sonnet 4.6、Claude Opus 4.7、Claude Haiku 4.5
