<!-- i18n-source: CHANGELOG.md -->
<!-- i18n-source-sha: cf92e8e -->
<!-- i18n-date: 2026-04-27 -->

# 変更履歴

## v2.1.112 — 2026-04-16

### ハイライト

- すべての英語チュートリアルを Claude Code v2.1.112 および新しい Opus 4.7 モデル（`claude-opus-4-7`）に同期。Opus 4.7 でデフォルトとなる新しい `xhigh` エフォートレベル（`high` と `max` の中間）、2 つの新しい組み込みスラッシュコマンド（`/ultrareview`、`/less-permission-prompts`）、Opus 4.7 の Max サブスクライバー向けに `--enable-auto-mode` を不要としたオートモード、Windows の PowerShell ツール、「Auto（ターミナルに合わせる）」テーマ、およびプロンプト名で命名されるプランファイルを反映。18 件の英語ドキュメントのフッターを Claude Code v2.1.112 に更新。@Luong NGUYEN

### 機能

- 全モジュール、ルートドキュメント、サンプル、リファレンスにわたるウクライナ語（uk）ローカライズを完全追加（039dde2）@Evgenij I

### バグ修正

- pre-tool-check.sh フックのプロトコルバグを修正（bce7cf8）@yarlinghe
- CI を通すため不正な mermaid サンプルをテキストブロックに変更（b8a7b1f）@Evgenij I
- ウクライナ語版 claude_concepts_guide.md の目次における CP1251 エンコード問題を修正（d970cc6）@Evgenij I
- スタブのウクライナ語 README を完全翻訳に置き換え、壊れたアンカーを修正（f6d73e2）@Evgenij I
- 全フッターの Claude Code バージョンを 2.1.97 に統一（63a1416）@Luong NGUYEN
- 2026-04-09 のドキュメント正確性アップデートを適用（e015f39）@Luong NGUYEN

### ドキュメント

- Claude Code v2.1.112 に同期（Opus 4.7、`xhigh` エフォート、`/ultrareview`、`/less-permission-prompts`、PowerShell ツール、Auto-match-terminal テーマ）@Luong NGUYEN
- Claude Code v2.1.110 に同期（TUI、プッシュ通知、セッションリキャップ）（15f0085）@Luong NGUYEN
- Claude Code v2.1.101 に同期（`/team-onboarding`、`/ultraplan`、Monitor ツール）（2deba3a）@Luong NGUYEN
- ベトナム語ドキュメントを英語ソースに同期（561c6cb）@Thiên Toán
- 全ファイルの Last Updated 日付と Claude Code バージョンを更新（7f2e773）@Luong NGUYEN
- 言語切替えにウクライナ語へのリンクを追加（9c224ff）@Luong NGUYEN
- コントリビューターセクションを削除（f07313d）@Luong NGUYEN
- GitHub メトリクスを 21,800+ stars、2,585+ forks に更新（4f55374）@Luong NGUYEN

**Full Changelog**: https://github.com/luongnv89/claude-howto/compare/v2.3.0...v2.1.112

---

## v2.3.0 — 2026-04-07

### 機能

- 言語ごとの EPUB アーティファクトをビルド・公開（90e9c30）@Thiên Toán
- 不足していた pre-tool-check.sh フックを 06-hooks に追加（b511ed1）@JiayuWang
- zh/ ディレクトリに中国語翻訳を追加（89e89d4）@Luong NGUYEN
- performance-optimizer サブエージェントと dependency-check フックを追加（f53d080）@qk

### バグ修正

- Windows Git Bash 互換性 + stdin JSON プロトコル（2cbb10c）@Luong NGUYEN
- 08-checkpoints の autoCheckpoint 設定ドキュメントを修正（749c79f）@JiayuWang
- プレースホルダー置換の代わりに SVG 画像を埋め込み（1b16709）@Thiên Toán
- memory README におけるネストされたコードフェンスのレンダリングを修正（ce24423）@Zhaoshan Duan
- squash merge により失われたレビュー修正を再適用（34259ca）@Luong NGUYEN
- フックスクリプトを Windows Git Bash 互換にし、stdin JSON プロトコルを使用（107153d）@binyu li

### ドキュメント

- 全チュートリアルを Claude Code 最新ドキュメント（2026 年 4 月）に同期（72d3b01）@Luong NGUYEN
- 言語切替えに中国語へのリンクを追加（6cbaa4d）@Luong NGUYEN
- 英語とベトナム語の言語切替えを追加（100c45e）@Luong NGUYEN
- GitHub #1 Trending バッジを追加（0ca8c37）@Luong NGUYEN
- コンテキストゾーン監視のための cc-context-stats を導入（d41b335）@Luong NGUYEN
- luongnv89/skills コレクションと luongnv89/asm スキルマネージャを導入（7e3c0b6）@Luong NGUYEN
- README の統計情報を最新の GitHub メトリクス（5,900+ stars、690+ forks）に更新（5001525）@Luong NGUYEN
- README の統計情報を最新の GitHub メトリクス（3,900+ stars、460+ forks）に更新（9cb92d6）@Luong NGUYEN

### リファクタリング

- Kroki HTTP 依存をローカルの mmdc レンダリングに置き換え（e76bbe4）@Luong NGUYEN
- 品質チェックを pre-commit に前倒しし、CI を 2 回目のパスとする（6d1e0ae）@Luong NGUYEN
- オートモードの権限ベースラインを絞り込み（2790fb2）@Luong NGUYEN
- auto-adapt フックをワンタイム権限セットアップスクリプトに置き換え（995a5d6）@Luong NGUYEN

### その他

- 品質ゲートのシフトレフト — pre-commit に mypy を追加し、CI 失敗を修正（699fb39）@Luong NGUYEN
- ベトナム語（Tiếng Việt）ローカライズを追加（a70777e）@Thiên Toán

**Full Changelog**: https://github.com/luongnv89/claude-howto/compare/v2.2.0...v2.3.0

---

## v2.2.0 — 2026-03-26

### ドキュメント

- 全チュートリアルとリファレンスを Claude Code v2.1.84 に同期（f78c094）@luongnv89
  - スラッシュコマンドを 55+ 個の組み込み + 5 個のバンドルスキルに更新、3 個を非推奨としてマーク
  - フックイベントを 18 から 25 に拡張、`agent` フックタイプを追加（4 タイプに）
  - Auto Mode、Channels、Voice Dictation を高度な機能に追加
  - スキル frontmatter に `effort`、`shell` フィールドを追加；エージェントに `initialPrompt`、`disallowedTools` フィールドを追加
  - WebSocket MCP トランスポート、エリシテーション、2KB ツール上限を追加
  - プラグインの LSP サポート、`userConfig`、`${CLAUDE_PLUGIN_DATA}` を追加
  - 全リファレンスドキュメント（CATALOG、QUICK_REFERENCE、LEARNING-ROADMAP、INDEX）を更新
- README をランディングページ構成のガイドに書き直し（32a0776）@luongnv89

### バグ修正

- CI 準拠のため不足していた cSpell 単語と README セクションを追加（93f9d51）@luongnv89
- cSpell 辞書に `Sandboxing` を追加（b80ce6f）@luongnv89

**Full Changelog**: https://github.com/luongnv89/claude-howto/compare/v2.1.1...v2.2.0

---

## v2.1.1 — 2026-03-13

### バグ修正

- CI のリンクチェックで失敗するデッドマーケットプレイスリンクを削除（3fdf0d6）@luongnv89
- cSpell 辞書に `sandboxed` と `pycache` を追加（dc64618）@luongnv89

**Full Changelog**: https://github.com/luongnv89/claude-howto/compare/v2.1.0...v2.1.1

---

## v2.1.0 — 2026-03-13

### 機能

- セルフアセスメントとレッスンクイズスキルによる適応学習パスを追加（1ef46cd）@luongnv89
  - `/self-assessment` — 10 個の機能領域にわたる対話型習熟度クイズと個別最適化された学習パス
  - `/lesson-quiz [lesson]` — 8〜10 問の的を絞った質問によるレッスンごとの知識チェック

### バグ修正

- 壊れた URL、非推奨化、古いリファレンスを更新（8fe4520）@luongnv89
- リソースおよび self-assessment スキル内の壊れたリンクを修正（7a05863）@luongnv89
- concepts ガイドのネストされたコードブロックにチルダフェンスを使用（5f82719）@VikalpP
- cSpell 辞書に不足していた単語を追加（8df7572）@luongnv89

### ドキュメント

- フェーズ 5 QA — ドキュメント全体の整合性、URL、用語を修正（00bbe4c）@luongnv89
- フェーズ 3〜4 完了 — 新機能のカバレッジとリファレンスドキュメントの更新（132de29）@luongnv89
- MCP コンテキスト肥大化セクションに MCPorter ランタイムを追加（ef52705）@luongnv89
- 6 つのガイドに不足していたコマンド、機能、設定を追加（4bc8f15）@luongnv89
- 既存リポジトリ規約に基づくスタイルガイドを追加（84141d0）@luongnv89
- ガイド比較表に self-assessment 行を追加（8fe0c96）@luongnv89
- PR #7 のため VikalpP をコントリビューターリストに追加（d5b4350）@luongnv89
- self-assessment と lesson-quiz スキルへの参照を README とロードマップに追加（d5a6106）@luongnv89

### 新規コントリビュータ

- @VikalpP が #7 で初コントリビュート

**Full Changelog**: https://github.com/luongnv89/claude-howto/compare/v2.0.0...v2.1.0

---

## v2.0.0 — 2026-02-01

### 機能

- 全ドキュメントを Claude Code 2026 年 2 月の機能に同期（487c96d）
  - 10 個のチュートリアルディレクトリと 7 個のリファレンスドキュメントにまたがる 26 ファイルを更新
  - **Auto Memory**（プロジェクトごとの永続的な学習）のドキュメントを追加
  - **Remote Control**、**Web Sessions**、**Desktop App** のドキュメントを追加
  - **Agent Teams**（実験的なマルチエージェント協調）のドキュメントを追加
  - **MCP OAuth 2.0**、**Tool Search**、**Claude.ai Connectors** のドキュメントを追加
  - サブエージェントの **Persistent Memory** と **Worktree Isolation** のドキュメントを追加
  - **Background Subagents**、**Task List**、**Prompt Suggestions** のドキュメントを追加
  - **Sandboxing** と **Managed Settings**（Enterprise）のドキュメントを追加
  - **HTTP Hooks** と 7 個の新しいフックイベントのドキュメントを追加
  - **Plugin Settings**、**LSP Servers**、Marketplace アップデートのドキュメントを追加
  - **Summarize from Checkpoint** リワインドオプションのドキュメントを追加
  - 17 個の新スラッシュコマンド（`/fork`、`/desktop`、`/teleport`、`/tasks`、`/fast` など）をドキュメント化
  - 新しい CLI フラグ（`--worktree`、`--from-pr`、`--remote`、`--teleport`、`--teammate-mode` など）をドキュメント化
  - オートメモリ、エフォートレベル、エージェントチームなどに関する新しい環境変数をドキュメント化

### デザイン

- ロゴをコンパス・ブラケットマークと最小限のパレットに刷新（20779db）

### バグ修正 / 訂正

- モデル名を更新：Sonnet 4.5 → **Sonnet 4.6**、Opus 4.5 → **Opus 4.6**
- 権限モード名を修正：架空の「Unrestricted/Confirm/Read-only」を実在する `default`/`acceptEdits`/`plan`/`dontAsk`/`bypassPermissions` に置換
- フックイベントを修正：架空の `PreCommit`/`PostCommit`/`PrePush` を削除し、実在のイベント（`SubagentStart`、`WorktreeCreate`、`ConfigChange` など）を追加
- CLI 構文を修正：`claude-code --headless` を `claude -p`（print mode）に置換
- チェックポイントコマンドを修正：架空の `/checkpoint save/list/rewind/diff` を実在の `Esc+Esc` / `/rewind` インターフェースに置換
- セッション管理を修正：架空の `/session list/new/switch/save` を実在の `/resume`/`/rename`/`/fork` に置換
- プラグインマニフェスト形式を修正：`plugin.yaml` → `.claude-plugin/plugin.json`
- MCP 設定パスを修正：`~/.claude/mcp.json` → `.mcp.json`（プロジェクト）/ `~/.claude.json`（ユーザー）
- ドキュメント URL を修正：`docs.claude.com` → `docs.anthropic.com`；架空の `plugins.claude.com` を削除
- 複数ファイルにわたる架空の設定フィールドを削除
- 全ファイルの "Last Updated" 日付を 2026 年 2 月に更新

**Full Changelog**: https://github.com/luongnv89/claude-howto/compare/20779db...v2.0.0
