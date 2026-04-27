<!-- i18n-source: 09-advanced-features/README.md -->
<!-- i18n-source-sha: a7a0ea2 -->
<!-- i18n-date: 2026-04-27 -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# 高度な機能

Claude Code の高度な機能を網羅的に解説するガイド。プランニングモード、拡張思考、オートモード、バックグラウンドタスク、権限モード、プリントモード（非対話モード）、セッション管理、対話機能、チャンネル、音声入力、リモートコントロール、Web セッション、デスクトップアプリ、タスクリスト、プロンプト候補、Git ワークツリー、サンドボックス、マネージド設定、設定ファイルなどを扱う。

## 目次

1. [概要](#概要)
2. [プランニングモード](#プランニングモード)
3. [Ultraplan（クラウドでのプラン作成）](#ultraplanクラウドでのプラン作成)
4. [拡張思考](#拡張思考)
5. [オートモード](#オートモード)
6. [バックグラウンドタスク](#バックグラウンドタスク)
7. [Monitor ツール（イベント駆動ストリーム）](#monitor-ツールイベント駆動ストリーム)
8. [スケジュールタスク](#スケジュールタスク)
9. [権限モード](#権限モード)
10. [ヘッドレスモード](#ヘッドレスモード)
11. [セッション管理](#セッション管理)
12. [対話機能](#対話機能)
13. [TUI モード（フルスクリーン）](#tui-モードフルスクリーン)
14. [音声入力](#音声入力)
15. [チャンネル](#チャンネル)
16. [Chrome 連携](#chrome-連携)
17. [リモートコントロール](#リモートコントロール)
18. [Web セッション](#web-セッション)
19. [デスクトップアプリ](#デスクトップアプリ)
20. [タスクリスト](#タスクリスト)
21. [プロンプト候補](#プロンプト候補)
22. [Git ワークツリー](#git-ワークツリー)
23. [サンドボックス](#サンドボックス)
24. [マネージド設定（エンタープライズ）](#マネージド設定エンタープライズ)
25. [設定とコンフィグ](#設定とコンフィグ)
26. [エージェントチーム](#エージェントチーム)
27. [ベストプラクティス](#ベストプラクティス)
28. [追加リソース](#追加リソース)

---

## 概要

Claude Code の高度な機能は、プランニング、推論、自動化、制御の各仕組みでコア機能を拡張する。これらの機能により、複雑な開発タスク、コードレビュー、自動化、複数セッション管理に対応した高度なワークフローを実現できる。

**主な高度な機能：**
- **プランニングモード**：コーディング前に詳細な実装計画を作成する
- **拡張思考**：複雑な問題に対する深い推論を行う
- **オートモード**：バックグラウンドの安全分類器が各アクションを実行前にレビューする（Research Preview）
- **バックグラウンドタスク**：会話をブロックせずに長時間処理を実行する
- **権限モード**：Claude が実行可能な操作を制御する（`default`、`acceptEdits`、`plan`、`auto`、`dontAsk`、`bypassPermissions`）
- **プリントモード**：自動化や CI/CD のために Claude Code を非対話で実行する（`claude -p`）
- **セッション管理**：複数の作業セッションを管理する
- **対話機能**：キーボードショートカット、複数行入力、コマンド履歴
- **音声入力**：プッシュ・トゥ・トークによる音声入力（20 言語の STT 対応）
- **チャンネル**：MCP サーバが実行中セッションにメッセージをプッシュする（Research Preview）
- **リモートコントロール**：Claude.ai または Claude アプリから Claude Code を操作する
- **Web セッション**：claude.ai/code 上でブラウザから Claude Code を実行する
- **デスクトップアプリ**：視覚的な diff レビューと複数セッション対応のスタンドアロンアプリ
- **タスクリスト**：コンテキストコンパクション後も維持される永続的なタスク追跡
- **プロンプト候補**：コンテキストに応じたスマートなコマンド候補表示
- **Git ワークツリー**：並列作業のための隔離されたワークツリーブランチ
- **サンドボックス**：OS レベルのファイルシステムとネットワーク隔離
- **マネージド設定**：plist、レジストリ、マネージドファイルによるエンタープライズ展開
- **設定**：JSON 設定ファイルで挙動をカスタマイズする

---

## プランニングモード

プランニングモードでは、複雑なタスクを実装する前に Claude が思考を巡らせ、レビューと承認が可能な詳細な計画を作成できる。

### プランニングモードとは

プランニングモードは 2 段階のアプローチである：
1. **計画フェーズ**：Claude がタスクを分析し、詳細な実装計画を作成する
2. **実装フェーズ**：承認後、Claude が計画を実行する

### プランニングモードを使うべきとき

✅ プランニングモードが向くケース：
- 複雑な複数ファイルにまたがるリファクタリング
- 新機能の実装
- アーキテクチャ変更
- データベースマイグレーション
- 大規模な API 再設計

❌ プランニングモードが向かないケース：
- 単純なバグ修正
- フォーマット変更
- 単一ファイルの編集
- 簡単な質問

### プランニングモードの起動

**スラッシュコマンド：**
```bash
/plan Implement user authentication system
```

**CLI フラグ：**
```bash
claude --permission-mode plan
```

**デフォルトとして設定：**
```json
{
  "permissions": {
    "defaultMode": "plan"
  }
}
```

**キーボードショートカット：**
- `Shift + Tab` — 権限モードを切り替える（プランモードを含む）
- `Alt + M` — 権限モードを切り替える（Windows/Linux）

### プランニングモードのメリット

- **構造化された実装アプローチ**：実装ステップを詳細に分解する
- **レビューと承認**：実行前に計画を承認または調整できる
- **リスクの特定**：実装前に潜在的な問題を洗い出す
- **明確なフェーズ分け**：実装フェーズとマイルストーンを整理する

### 例：機能実装

```
User: /plan Add a real-time notification system

Claude: I'll create a plan for implementing real-time notifications.

## Implementation Plan

### Phase 1: Infrastructure Setup
1. Install WebSocket libraries (socket.io)
2. Set up WebSocket server
3. Configure connection management

### Phase 2: Backend Implementation
4. Create notification service
5. Implement notification queue
6. Add database schema for notifications
7. Create API endpoints

### Phase 3: Frontend Integration
8. Set up WebSocket client
9. Create notification UI components
10. Implement notification state management
11. Add notification permissions

### Phase 4: Testing & Deployment
12. Write unit tests
13. Write integration tests
14. Update documentation
15. Deploy to staging

Estimated time: 3-4 hours
Files to modify: 12
New files to create: 8

Ready to proceed? (yes/no/modify plan)

User: yes

Claude: [Begins implementation following the plan]
```

### 計画の修正

```
User: Modify the plan - skip the queue for now, we'll add it later

Claude: Updated plan:
[Shows modified plan with queue removed]

User: Looks good, proceed

Claude: [Implements modified plan]
```

### プランニングモードの設定

プランニングモードは CLI フラグまたはスラッシュコマンドで起動する：

```bash
# CLI でプランモードを起動
claude --permission-mode plan

# または REPL 内で /plan スラッシュコマンドを使う
/plan Implement user authentication system
```

**プラン用のモデルエイリアス：** `opusplan` をモデルエイリアスとして使うと、プランニングに Opus、実行に Sonnet を使い分けられる：

```bash
claude --model opusplan "design and implement the new API"
```

**外部エディタで計画を編集：** `Ctrl+G` を押すと、現在の計画を外部エディタで開いて詳細に修正できる。

> **v2.1.112 アップデート：** 計画ファイルがランダムな単語ではなく、生成元プロンプトに基づいた名前で保存されるようになり、閲覧と再利用が容易になった。

---

## Ultraplan（クラウドでのプラン作成）

> **v2.1.101 で新登場：** Ultraplan は初回起動時に Claude Code on the web のクラウド環境を自動作成するようになり、手動セットアップやコンテナ起動の待ち時間なしでドラフト作成を始められる。

> **注：** Ultraplan は Research Preview であり、Claude Code v2.1.91 以降が必要である。

`/ultraplan` は、ローカル CLI からプランニングタスクを Claude Code on the web のセッション（プランモード）に引き渡す。Claude がクラウドで計画を作成している間、ターミナルは別の作業に使え、ブラウザでドラフトをレビューしてから、同じクラウドセッションで実行するか、ターミナルにテレポートして実行するかを選べる。

### Ultraplan を使うべきとき

- ターミナルより豊かなレビュー環境が欲しいとき：インラインコメント、絵文字リアクション、アウトラインのサイドバー、永続的な履歴を活用できる。
- ローカルでコーディングを続けながら、ハンズオフでドラフトを進めたいとき：クラウドセッションがリポジトリを調査し計画を書き、CLI をブロックしない。
- 実行前にステークホルダーのレビューが必要なとき：共有可能な Web URL がターミナルのスクロール内容を貼り付けるより便利。

### 必要要件

- Claude Code on the web アカウント
- GitHub リポジトリ（クラウドセッションが実コードに対してドラフト作成するためにクローンする）
- Amazon Bedrock、Google Cloud Vertex AI、Microsoft Foundry では **利用不可**

### 起動方法 3 種

- **コマンド：** `/ultraplan <prompt>` — 明示的に呼び出す。
- **キーワード：** 通常のプロンプトに `ultraplan` を含めると、Claude がリクエストをクラウドにルーティングする。
- **ローカル計画から：** Claude がローカルで計画を作成した後、承認ダイアログで「No, refine with Ultraplan on Claude Code on the web」を選ぶと、より深い調査のためにドラフトを引き渡せる。

### 利用例

```bash
/ultraplan migrate the auth service from sessions to JWTs
```

Claude が応答してクラウド環境を起動し（v2.1.101 以降は初回実行時に自動作成）、ブラウザで開けるセッションリンクを返す。

### ステータス表示

| ステータス | 意味 |
|---|---|
| `◇ ultraplan` | Claude がコードベースを調査し、計画をドラフト中 |
| `◇ ultraplan needs your input` | Claude が確認質問を持っている。セッションリンクを開いて応答する |
| `◆ ultraplan ready` | 計画がブラウザでレビュー可能になった |

### 実行オプション

計画が完成すると、実行経路は 2 つある。ブラウザで計画を承認して同じクラウドセッションで実行する場合、Claude がリモートで変更を実装し、Web UI からプルリクエストを開く。あるいは「Approve plan and teleport back to terminal」を選んでローカルで実装する。ターミナルテレポートのダイアログでは 3 つの選択肢が表示される：

- **Implement here** — 現在のターミナルセッションで承認済み計画を実行する。
- **Start new session** — 同じ作業ディレクトリで新規セッションを開いて実行する。
- **Cancel** — 計画をファイルに保存し、後で再開できるようにする。

> **警告：** Ultraplan を開始するとリモートコントロールは切断される。両機能とも claude.ai/code インターフェースを共有しているため、同時に有効化できるのは一方のみである。

---

## 拡張思考

拡張思考により、Claude は複雑な問題について、解を提示する前により多くの時間をかけて推論できる。

### 拡張思考とは

拡張思考は意図的なステップバイステップの推論プロセスで、Claude は次を行う：
- 複雑な問題の分解
- 複数のアプローチの検討
- トレードオフの評価
- エッジケースの推論

### 拡張思考の起動

**キーボードショートカット：**
- `Option + T`（macOS）／ `Alt + T`（Windows/Linux）— 拡張思考を切り替える

**自動起動：**
- 全モデル（Opus 4.7、Sonnet 4.6、Haiku 4.5）でデフォルト有効
- Opus 4.7：適応的推論で努力度レベルを指定可能：`low`（○）、`medium`（◐）、`high`（●）、`xhigh`（Opus 4.7 限定、Opus 4.7 のローンチ以降 Claude Code でデフォルト、2026-04-16）、`max`。Opus 4.6 と Sonnet 4.6 も `low`、`medium`、`high`、`max` をサポートする（`xhigh` なし）。Opus 4.7 はネイティブで 1M トークンのコンテキストウィンドウを持つ（1M コンテキスト対応は v2.1.117 で導入された。それ以前は `/context` が Opus 4.7 を 200K ウィンドウとして誤計算し、早期の自動コンパクションを引き起こしていた）。
- Pro/Max サブスクライバの Opus 4.6 / Sonnet 4.6：v2.1.117 でデフォルト努力度が `medium` から `high` に引き上げられた。
- その他のモデル：固定バジェット（最大 31,999 トークン）

**設定方法：**
- 切り替え：`Alt+T` / `Option+T`、または `/config` から
- 推論内容を表示：`Ctrl+O`（verbose モード）
- 努力度を設定：`/effort` コマンドまたは `--effort` フラグ

**カスタムバジェット：**
```bash
export MAX_THINKING_TOKENS=1024
```

**努力度レベル**（Opus 4.7、Opus 4.6、Sonnet 4.6 でサポート）：
```bash
export CLAUDE_CODE_EFFORT_LEVEL=xhigh   # low (○), medium (◐), high (●), xhigh (Opus 4.7 only, default), or max
```

**CLI フラグ：**
```bash
claude --effort high "complex architectural review"
```

**スラッシュコマンド：**
```
/effort high
```

> **注：** プロンプトに「ultrathink」というキーワードを含めると深い推論モードが起動する。努力度レベル `low`、`medium`、`high`、`max` は Opus 4.7、Opus 4.6、Sonnet 4.6 でサポートされる。`xhigh`（Opus 4.7 でのデフォルト）は Opus 4.7 専用である。

### 拡張思考のメリット

- **深い推論**：複雑な問題に対してより多くの時間をかけて思考する
- **より良いアーキテクチャ判断**：包括的な評価に基づいて情報に基づく選択ができる
- **エッジケースの考慮**：起こりうる問題やシナリオを丁寧に検討する
- **徹底的な分析**：複雑な問題解決への構造化されたアプローチ

### 例：アーキテクチャ判断

```
User: /think Should we use microservices or a monolith for our e-commerce platform?

Claude: Let me think through this architectural decision carefully...

<extended_thinking>
## Context Analysis
- Team size: 5 developers
- Expected traffic: 10k daily users initially
- Need to scale to 100k+ users
- Limited DevOps resources
- 6-month timeline to MVP

## Approach 1: Microservices
Pros:
+ Independent scaling
+ Technology flexibility
+ Team independence
+ Fault isolation

Cons:
- Operational complexity
- Network overhead
- Distributed tracing needed
- Requires DevOps expertise
- Slower initial development

## Approach 2: Monolith
Pros:
+ Simpler deployment
+ Faster initial development
+ Easier debugging
+ Lower operational overhead
+ Single codebase

Cons:
- Scaling challenges later
- All-or-nothing deployments
- Technology lock-in
- Potential for tight coupling

## Decision Factors
1. Team size (5 devs) → Favors monolith
2. DevOps resources (limited) → Favors monolith
3. Timeline (6 months) → Favors monolith
4. Future scale (100k users) → Achievable with monolith + caching
5. Complexity budget → Limited

## Recommendation
Start with a **modular monolith**:
- Single deployment unit
- Clear module boundaries
- Clean interfaces between modules
- Prepare for future extraction to microservices if needed

This gives you:
✓ Fast initial development
✓ Low operational complexity
✓ Option to extract services later
✓ Clear architecture

Migration path: When you reach 50k+ users or specific modules need independent scaling, extract those modules into microservices.
</extended_thinking>

**Recommendation**: Implement a modular monolith with clean module boundaries.

This approach balances your current constraints (team size, timeline, DevOps resources) with future scalability needs. You can migrate specific modules to microservices later when there's a clear business need.
```

### 拡張思考の設定

拡張思考は環境変数、キーボードショートカット、CLI フラグで制御する：

```bash
# 思考トークンのバジェットを設定
export MAX_THINKING_TOKENS=16000

# 努力度レベルを設定 (Opus 4.7, Opus 4.6, Sonnet 4.6): low (○), medium (◐), high (●), xhigh (Opus 4.7 only, default), or max
export CLAUDE_CODE_EFFORT_LEVEL=xhigh
```

セッション中に切り替える場合は `Alt+T` / `Option+T`、努力度の設定は `/effort`、その他の設定は `/config` を使う。

---

## オートモード

オートモードは Research Preview の権限モード（2026 年 3 月）で、バックグラウンドの安全分類器が各アクションを実行前にレビューする。Claude が自律的に作業しつつ、危険な操作はブロックできる。

### 必要要件

- **プラン：** Team、Enterprise、または API（Pro や Max プランでは利用不可）
- **モデル：** Claude Sonnet 4.6 または Opus 4.7
- **プロバイダ：** Anthropic API のみ（Bedrock、Vertex、Foundry では非対応）
- **分類器：** Claude Sonnet 4.6 上で動作する（追加のトークンコストが発生）

### オートモードの有効化

```bash
# Unlock auto mode with CLI flag (no longer required for Max subscribers on Opus 4.7 — access it directly)
claude --enable-auto-mode

# Then cycle to it with Shift+Tab in the REPL
```

> **v2.1.112 アップデート：** オートモードに `--enable-auto-mode` フラグは不要になった。Max サブスクライバは Opus 4.7 で直接アクセスできる。

または、デフォルトの権限モードとして設定する：

```bash
claude --permission-mode auto
```

設定ファイルで指定する：
```json
{
  "permissions": {
    "defaultMode": "auto"
  }
}
```

### 分類器の動作

バックグラウンド分類器は次の決定順で各アクションを評価する：

1. **許可／拒否ルール** — 明示的な権限ルールが最初にチェックされる
2. **読み取り専用／編集の自動承認** — ファイル読み取りと編集は自動的に通過する
3. **分類器** — バックグラウンド分類器がアクションをレビューする
4. **フォールバック** — 連続 3 回または合計 20 回のブロック後、プロンプト確認に切り替わる

### デフォルトでブロックされる操作

オートモードはデフォルトで以下をブロックする：

| ブロック対象 | 例 |
|----------------|---------|
| パイプ経由のシェルインストール | `curl \| bash` |
| 機密データの外部送信 | API キーや認証情報のネットワーク送信 |
| 本番デプロイ | 本番を対象とするデプロイコマンド |
| 一括削除 | 大規模ディレクトリでの `rm -rf` |
| IAM の変更 | 権限とロールの変更 |
| main への強制プッシュ | `git push --force origin main` |

### デフォルトで許可される操作

| 許可対象 | 例 |
|----------------|---------|
| ローカルファイル操作 | プロジェクトファイルの読み書きと編集 |
| 宣言された依存関係のインストール | マニフェスト経由の `npm install`、`pip install` |
| 読み取り専用 HTTP | ドキュメント取得のための `curl` |
| 現在のブランチへのプッシュ | `git push origin feature-branch` |

### オートモードの設定

**デフォルトルールを JSON で出力：**
```bash
claude auto-mode defaults
```

**信頼インフラの設定：** エンタープライズ展開向けに `autoMode.environment` マネージド設定を使う。これにより、管理者は信頼できる CI/CD 環境、デプロイ先、インフラパターンを定義できる。

#### `"$defaults"` で既定値を拡張する（v2.1.118）

v2.1.118 以降、`autoMode.allow`、`autoMode.soft_deny`、`autoMode.environment` は `"$defaults"` トークンを受け付ける。これにより、組み込みリストを置き換えるのではなく、ルールを **追加** できる。v2.1.118 より前では、ユーザー定義の配列が無告知で組み込み設定を上書きしていた。

**変更前（組み込みを置き換える — v2.1.118 より前の挙動）：**

```json
{
  "autoMode": {
    "allow": ["Bash(gh pr list:*)"]
  }
}
```

**変更後（組み込みを拡張する — v2.1.118 以降）：**

```json
{
  "autoMode": {
    "allow": ["$defaults", "Bash(gh pr list:*)"],
    "soft_deny": ["$defaults", "Bash(kubectl delete:*)"],
    "environment": ["$defaults", "trusted-ci.internal"]
  }
}
```

組織やプロジェクト固有の追加を重ねつつ、出荷時のベースラインルールを維持したいときは `"$defaults"` を使う。

### フォールバックの動作

分類器の判断が不確実な場合、オートモードはユーザーへのプロンプト確認にフォールバックする：
- **連続 3 回** の分類器ブロック後
- セッション内で **合計 20 回** の分類器ブロック後

これにより、分類器が確信を持って承認できない場合でも、ユーザーは常に制御を保持できる。

### オートモード相当の権限を投入する（Team プラン不要）

Team プランを持っていない場合、またはバックグラウンド分類器なしでよりシンプルなアプローチを取りたい場合は、`~/.claude/settings.json` に保守的なベースラインの安全な権限ルールを投入できる。スクリプトはまず読み取り専用とローカル検査のルールから始まり、編集、テスト、ローカル Git 書き込み、パッケージインストール、GitHub 書き込み操作などはオプトインで有効化する。

**ファイル：** `09-advanced-features/setup-auto-mode-permissions.py`

```bash
# Preview what would be added (no changes written)
python3 09-advanced-features/setup-auto-mode-permissions.py --dry-run

# Apply the conservative baseline
python3 09-advanced-features/setup-auto-mode-permissions.py

# Add more capability only when you need it
python3 09-advanced-features/setup-auto-mode-permissions.py --include-edits --include-tests
python3 09-advanced-features/setup-auto-mode-permissions.py --include-git-write --include-packages
```

このスクリプトは以下のカテゴリにわたるルールを追加する：

| カテゴリ | 例 |
|----------|---------|
| コア読み取り専用ツール | `Read(*)`、`Glob(*)`、`Grep(*)`、`Agent(*)`、`WebSearch(*)`、`WebFetch(*)` |
| ローカル検査 | `Bash(git status:*)`、`Bash(git log:*)`、`Bash(git diff:*)`、`Bash(cat:*)` |
| オプションの編集 | `Edit(*)`、`Write(*)`、`NotebookEdit(*)` |
| オプションのテスト／ビルド | `Bash(pytest:*)`、`Bash(python3 -m pytest:*)`、`Bash(cargo test:*)` |
| オプションの Git 書き込み | `Bash(git add:*)`、`Bash(git commit:*)`、`Bash(git stash:*)` |
| Git（ローカル書き込み） | `Bash(git add:*)`、`Bash(git commit:*)`、`Bash(git checkout:*)` |
| パッケージマネージャ | `Bash(npm install:*)`、`Bash(pip install:*)`、`Bash(cargo build:*)` |
| ビルドとテスト | `Bash(make:*)`、`Bash(pytest:*)`、`Bash(go test:*)` |
| よく使うシェル | `Bash(ls:*)`、`Bash(cat:*)`、`Bash(find:*)`、`Bash(cp:*)`、`Bash(mv:*)` |
| GitHub CLI | `Bash(gh pr view:*)`、`Bash(gh pr create:*)`、`Bash(gh issue list:*)` |

危険な操作（`rm -rf`、`sudo`、強制プッシュ、`DROP TABLE`、`terraform destroy` など）は意図的に除外されている。スクリプトは冪等であり、2 回実行してもルールは重複しない。

---

## バックグラウンドタスク

バックグラウンドタスクにより、長時間処理を会話をブロックせずに実行できる。

### バックグラウンドタスクとは

バックグラウンドタスクは作業を継続しつつ非同期で実行される：
- 長時間のテストスイート
- ビルドプロセス
- データベースマイグレーション
- デプロイスクリプト
- 解析ツール

**基本的な使い方：**
```bash
User: Run tests in background

Claude: Started task bg-1234

/task list           # Show all tasks
/task status bg-1234 # Check progress
/task show bg-1234   # View output
/task cancel bg-1234 # Cancel task
```

### バックグラウンドタスクの起動

```
User: Run the full test suite in the background

Claude: Starting tests in background (task-id: bg-1234)
You can continue working while tests run.

[You can continue the conversation]

User: Meanwhile, let's refactor the auth module

Claude: [Works on auth module while tests run in background]

[Later, when tests complete]

Claude: 📢 Background task bg-1234 completed:
✅ 245 tests passed
❌ 3 tests failed
View results: /task show bg-1234
```

### バックグラウンドタスクの管理

**実行中タスクの一覧：**
```
User: /task list

Active background tasks:
1. [bg-1234] Running tests (50% complete, 2min remaining)
2. [bg-1235] Building Docker image (25% complete, 8min remaining)
3. [bg-1236] Deploying to staging (90% complete, 30sec remaining)
```

**タスクの状態確認：**
```
User: /task status bg-1234

Task bg-1234: Running tests
Status: In progress
Progress: 120/245 tests (49%)
Started: 2025-11-08 10:30:15
Estimated completion: 2025-11-08 10:34:22
```

**タスク出力の表示：**
```
User: /task show bg-1234

[Shows live output from the test run]
```

**タスクのキャンセル：**
```
User: /task cancel bg-1234

Cancelled background task bg-1234
```

### 例：並列開発

```
User: Run the build in the background

Claude: Starting build... (task-id: bg-5001)

User: Also run the linter in background

Claude: Starting linter... (task-id: bg-5002)

User: While those run, let's implement the new API endpoint

Claude: [Implements API endpoint while build and linter run]

[10 minutes later]

Claude: 📢 Build completed successfully (bg-5001)
📢 Linter found 12 issues (bg-5002)

User: Show me the linter issues

Claude: [Shows linter output from bg-5002]
```

### 設定

```json
{
  "backgroundTasks": {
    "enabled": true,
    "maxConcurrentTasks": 5,
    "notifyOnCompletion": true,
    "autoCleanup": true,
    "logOutput": true
  }
}
```

---

## Monitor ツール（イベント駆動ストリーム）

> **v2.1.98 で新登場：** Monitor ツールは Claude がバックグラウンドコマンドの stdout を監視し、マッチするイベントが現れた瞬間に反応できるようにする。長時間プロセスの待機にポーリングループや `sleep` を使う必要がなくなる。

Monitor は stdout に書き込む任意のシェルコマンドにアタッチする。コマンドからの stdout 行ごとに通知が発生し、セッションがウェイクする。Claude がコマンドを指定し、ハーネスが出力をストリーミングしてイベント発生時に配信する。基盤プロセスの起動については関連する [バックグラウンドタスク](#バックグラウンドタスク) のセクションを参照。

### なぜ重要か

`/loop` や `sleep` でポーリングすると、何も変わっていなくてもサイクルごとに API ラウンドトリップを 1 回消費してしまう。Monitor はイベントが発生するまで沈黙を守り、コマンドが静かな間は **トークン消費ゼロ** で待機する。イベントが発生した瞬間に Claude は反応する — 次のポーリングティックを待つ遅延がない。数分以上動作する処理にはポーリングループより安価かつ高速である。

### よくある 2 つのパターン

**ストリームフィルタ** は長時間動作するソースからの連続出力を監視する。コマンドは永続的に動作し、マッチする行ごとにイベントとなる。

```bash
tail -f /var/log/app.log | grep --line-buffered "ERROR"
```

**ポーリング・アンド・エミットフィルタ** はソースを定期的にチェックし、変化があったときだけ出力する。ネイティブストリームを持たない API、データベースなどで使う。

```bash
last=$(date -u +%Y-%m-%dT%H:%M:%SZ)
while true; do
  gh api "repos/owner/repo/issues/123/comments?since=$last" || true
  last=$(date -u +%Y-%m-%dT%H:%M:%SZ)
  sleep 30
done
```

### 具体例

「dev サーバを起動してエラーを監視して」と頼むと、Claude はサーバをバックグラウンドタスクとして起動し、Monitor フィルタ（`tail -F server.log | grep --line-buffered -E "ERROR|FATAL"`）をアタッチする。セッションは静かになる。ログにエラー行が現れた瞬間、Claude は目覚めてエラーを読み、反応できる — サーバ再起動、バグ修正、ユーザーへの通知のいずれも、ユーザーが状況確認に来なくても可能になる。

> **警告：** `grep` にパイプするときは **必ず** `grep --line-buffered` を使う。これがないと grep は stdout を 4KB チャンクでバッファリングし、低トラフィックのストリームでは数分の遅延が生じることがある。これは Monitor が実運用で壊れる最大の原因である。フィルタが本来鳴るはずなのに沈黙している場合、まず `--line-buffered` フラグを確認すること。

---

## スケジュールタスク

スケジュールタスクを使うと、定期スケジュールで自動的にプロンプトを実行したり、1 回だけのリマインダーとして実行したりできる。タスクはセッションスコープ — Claude Code が動作している間だけ実行され、セッション終了時にクリアされる。v2.1.72 以降で利用可能。

### `/loop` コマンド

```bash
# Explicit interval
/loop 5m check if the deployment finished

# Natural language
/loop check build status every 30 minutes
```

正確なスケジューリングのため、標準 5 フィールドの cron 式もサポートされる。

### 1 回限りのリマインダー

特定の時刻に 1 回だけ実行するリマインダーを設定できる：

```
remind me at 3pm to push the release branch
in 45 minutes, run the integration tests
```

### スケジュールタスクの管理

| ツール | 説明 |
|------|-------------|
| `CronCreate` | 新規スケジュールタスクを作成する |
| `CronList` | アクティブなスケジュールタスクを一覧表示する |
| `CronDelete` | スケジュールタスクを削除する |

**制限と挙動：**
- セッションあたり最大 **50 個のスケジュールタスク**
- セッションスコープ — セッション終了時にクリアされる
- 定期タスクは **3 日後** に自動失効する
- タスクは Claude Code の動作中のみ実行される — 取りこぼしの追加実行はない

### 挙動の詳細

| 項目 | 詳細 |
|--------|--------|
| **定期実行のジッタ** | 間隔の最大 10%（最大 15 分） |
| **1 回限りのジッタ** | :00／:30 境界で最大 90 秒 |
| **取りこぼし** | キャッチアップなし — Claude Code が動いていなければスキップされる |
| **永続化** | 再起動をまたいで保持されない |

### クラウドスケジュールタスク

`/schedule` を使うと、Anthropic のインフラ上で動作するクラウドスケジュールタスクを作成できる：

```
/schedule daily at 9am run the test suite and report failures
```

クラウドスケジュールタスクは再起動をまたいで永続化され、Claude Code をローカルで動かす必要はない。

### スケジュールタスクの無効化

```bash
export CLAUDE_CODE_DISABLE_CRON=1
```

### 例：デプロイの監視

```
/loop 5m check the deployment status of the staging environment.
        If the deploy succeeded, notify me and stop looping.
        If it failed, show the error logs.
```

> **ヒント：** スケジュールタスクはセッションスコープである。再起動後も生き残る永続的な自動化には、CI/CD パイプライン、GitHub Actions、デスクトップアプリのスケジュールタスクを使う。

---

## 権限モード

権限モードは、明示的な承認なしに Claude が実行できる操作を制御する。

### 利用可能な権限モード

| モード | 挙動 |
|---|---|
| `default` | ファイル読み取りのみ。それ以外の操作は確認を求める |
| `acceptEdits` | ファイル読み取りと編集を許可。コマンドは確認を求める |
| `plan` | ファイル読み取りのみ（リサーチモード、編集なし） |
| `auto` | バックグラウンドの安全分類器のチェック付きで全操作を許可（Research Preview） |
| `bypassPermissions` | 全操作、権限チェックなし（危険） |
| `dontAsk` | 事前承認済みツールのみ実行、その他はすべて拒否 |

CLI では `Shift+Tab` でモードを切り替える。デフォルトは `--permission-mode` フラグまたは `permissions.defaultMode` 設定で指定する。

### 起動方法

**キーボードショートカット：**
```bash
Shift + Tab  # Cycle through all 6 modes
```

**スラッシュコマンド：**
```bash
/plan                  # Enter plan mode
```

**CLI フラグ：**
```bash
claude --permission-mode plan
claude --permission-mode auto
```

**設定：**
```json
{
  "permissions": {
    "defaultMode": "auto"
  }
}
```

### 権限モードの例

#### Default モード
Claude は重要な操作の前に確認を求める：

```
User: Fix the bug in auth.ts

Claude: I need to modify src/auth.ts to fix the bug.
The change will update the password validation logic.

Approve this change? (yes/no/show)
```

#### Plan モード
実行前に実装計画をレビューする：

```
User: /plan Implement user authentication system

Claude: I'll create a plan for implementing authentication.

## Implementation Plan
[Detailed plan with phases and steps]

Ready to proceed? (yes/no/modify)
```

#### Accept Edits モード
ファイル変更を自動承認する：

```
User: acceptEdits
User: Fix the bug in auth.ts

Claude: [Makes changes without asking]
```

### ユースケース

**コードレビュー：**
```
User: claude --permission-mode plan
User: Review this PR and suggest improvements

Claude: [Reads code, provides feedback, but cannot modify]
```

**ペアプログラミング：**
```
User: claude --permission-mode default
User: Let's implement the feature together

Claude: [Asks for approval before each change]
```

**自動化タスク：**
```
User: claude --permission-mode acceptEdits
User: Fix all linting issues in the codebase

Claude: [Auto-accepts file edits without asking]
```

---

## ヘッドレスモード

プリントモード（`claude -p`）により Claude Code を対話入力なしで実行できる。自動化や CI/CD に最適である。これは非対話モードであり、旧来の `--headless` フラグを置き換える。

### プリントモードとは

プリントモードでは次が可能になる：
- スクリプトの自動実行
- CI/CD 統合
- バッチ処理
- スケジュールタスク

### プリントモードでの実行（非対話）

```bash
# Run specific task
claude -p "Run all tests"

# Process piped content
cat error.log | claude -p "Analyze these errors"

# CI/CD integration (GitHub Actions)
- name: AI Code Review
  run: claude -p "Review PR"
```

### プリントモードのその他の使用例

```bash
# Run a specific task with output capture
claude -p "Run all tests and generate coverage report"

# With structured output
claude -p --output-format json "Analyze code quality"

# With input from stdin
echo "Analyze code quality" | claude -p "explain this"
```

### 例：CI/CD 統合

**GitHub Actions：**
```yaml
# .github/workflows/code-review.yml
name: AI Code Review

on: [pull_request]

jobs:
  review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Install Claude Code
        run: npm install -g @anthropic-ai/claude-code

      - name: Run Claude Code Review
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        run: |
          claude -p --output-format json \
            --max-turns 3 \
            "Review this PR for:
            - Code quality issues
            - Security vulnerabilities
            - Performance concerns
            - Test coverage
            Output results as JSON" > review.json

      - name: Post Review Comment
        uses: actions/github-script@v7
        with:
          script: |
            const fs = require('fs');
            const review = JSON.parse(fs.readFileSync('review.json', 'utf8'));
            github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: JSON.stringify(review, null, 2)
            });
```

### プリントモードの設定

プリントモード（`claude -p`）は自動化向けにいくつかのフラグをサポートする：

```bash
# Limit autonomous turns
claude -p --max-turns 5 "refactor this module"

# Structured JSON output
claude -p --output-format json "analyze this codebase"

# With schema validation
claude -p --json-schema '{"type":"object","properties":{"issues":{"type":"array"}}}' \
  "find bugs in this code"

# Disable session persistence
claude -p --no-session-persistence "one-off analysis"
```

---

## セッション管理

複数の Claude Code セッションを効果的に管理する。

### セッション管理コマンド

| コマンド | 説明 |
|---------|-------------|
| `/resume` | ID または名前で会話を再開する |
| `/rename` | 現在のセッションに名前を付ける |
| `/fork` | 現在のセッションを新規ブランチとしてフォークする |
| `claude -c` | 直近の会話を継続する |
| `claude -r "session"` | 名前または ID でセッションを再開する |

### セッションの再開

**直近の会話を継続：**
```bash
claude -c
```

**名前付きセッションの再開：**
```bash
claude -r "auth-refactor" "finish this PR"
```

**現在のセッションを名前付きにする**（REPL 内）：
```
/rename auth-refactor
```

### セッションのフォーク

別アプローチを試したいが元のセッションを失いたくないとき、セッションをフォークする：

```
/fork
```

CLI からも実行できる：
```bash
claude --resume auth-refactor --fork-session "try OAuth instead"
```

### セッションの永続化

セッションは自動保存され、いつでも再開できる：

```bash
# Continue last conversation
claude -c

# Resume specific session by name or ID
claude -r "auth-refactor"

# Resume and fork for experimentation
claude --resume auth-refactor --fork-session "alternative approach"
```

### セッションリキャップ（v2.1.108）

しばらく離れた後にセッションへ戻ると、Claude は何が達成されたかを簡潔に振り返れる。テレメトリが無効化されているユーザー（Bedrock、Vertex、Foundry ユーザー）ではデフォルトで有効である。

**リキャップ動作の制御：**

```bash
/recap                                 # manually trigger a recap
/config                                # toggle auto-recap on/off
```

または環境変数で：
```bash
CLAUDE_CODE_ENABLE_AWAY_SUMMARY=0 claude   # disable recap
CLAUDE_CODE_ENABLE_AWAY_SUMMARY=1 claude   # force enable recap
```

---

## 対話機能

### キーボードショートカット

Claude Code は効率向上のためキーボードショートカットをサポートする。公式ドキュメントの完全リファレンス：

| ショートカット | 説明 |
|----------|-------------|
| `Ctrl+C` | 入力／生成のキャンセル |
| `Ctrl+D` | Claude Code を終了 |
| `Ctrl+G` | 計画を外部エディタで編集 |
| `Ctrl+L` | ターミナル画面のクリア |
| `Ctrl+O` | 詳細出力の切り替え（推論を表示） |
| `Ctrl+R` | 履歴の逆方向検索 |
| `Ctrl+T` | タスクリストビューの切り替え |
| `Ctrl+B` | 実行中タスクをバックグラウンド化 |
| `Esc+Esc` | コード／会話の巻き戻し |
| `Shift+Tab` / `Alt+M` | 権限モードの切り替え |
| `Option+P` / `Alt+P` | モデルの切り替え |
| `Option+T` / `Alt+T` | 拡張思考の切り替え |

**行編集（標準 readline ショートカット）：**

| ショートカット | 動作 |
|----------|--------|
| `Ctrl + A` | 行頭へ移動 |
| `Ctrl + E` | 行末へ移動 |
| `Ctrl + K` | 行末まで切り取り |
| `Ctrl + U` | 行頭まで切り取り |
| `Ctrl + W` | 後方の単語を削除 |
| `Ctrl + Y` | ペースト（ヤンク） |
| `Tab` | 自動補完 |
| `↑ / ↓` | コマンド履歴 |

### キーバインドのカスタマイズ

`/keybindings` を実行するとカスタムキーボードショートカットを作成できる。コマンドは `~/.claude/keybindings.json` を編集用に開く（v2.1.18 以降）。

**設定形式：**

```json
{
  "$schema": "https://www.schemastore.org/claude-code-keybindings.json",
  "bindings": [
    {
      "context": "Chat",
      "bindings": {
        "ctrl+e": "chat:externalEditor",
        "ctrl+u": null,
        "ctrl+k ctrl+s": "chat:stash"
      }
    },
    {
      "context": "Confirmation",
      "bindings": {
        "ctrl+a": "confirmation:yes"
      }
    }
  ]
}
```

バインドを `null` に設定するとデフォルトのショートカットを解除できる。

### 利用可能なコンテキスト

キーバインドは特定の UI コンテキストにスコープされる：

| コンテキスト | 主な動作 |
|---------|-------------|
| **Chat** | `submit`、`cancel`、`cycleMode`、`modelPicker`、`thinkingToggle`、`undo`、`externalEditor`、`stash`、`imagePaste` |
| **Confirmation** | `yes`、`no`、`previous`、`next`、`nextField`、`cycleMode`、`toggleExplanation` |
| **Global** | `interrupt`、`exit`、`toggleTodos`、`toggleTranscript` |
| **Autocomplete** | `accept`、`dismiss`、`next`、`previous` |
| **HistorySearch** | `search`、`previous`、`next` |
| **Settings** | コンテキスト固有の設定ナビゲーション |
| **Tabs** | タブの切り替えと管理 |
| **Help** | ヘルプパネルのナビゲーション |

`Transcript`、`Task`、`ThemePicker`、`Attachments`、`Footer`、`MessageSelector`、`DiffDialog`、`ModelPicker`、`Select` を含め、合計 18 のコンテキストがある。

### コードのサポート

キーバインドはコード（複数キーの組み合わせ）をサポートする：

```
"ctrl+k ctrl+s"   → Two-key sequence: press ctrl+k, then ctrl+s
"ctrl+shift+p"    → Simultaneous modifier keys
```

**キー記法：**
- **修飾キー：** `ctrl`、`alt`（または `opt`）、`shift`、`meta`（または `cmd`）
- **大文字は Shift を含意：** `K` は `shift+k` と等価
- **特殊キー：** `escape`、`enter`、`return`、`tab`、`space`、`backspace`、`delete`、矢印キー

### 予約キーと競合キー

| キー | 状態 | 備考 |
|-----|--------|-------|
| `Ctrl+C` | 予約 | リバインド不可（割り込み） |
| `Ctrl+D` | 予約 | リバインド不可（終了） |
| `Ctrl+B` | ターミナル競合 | tmux のプレフィックスキー |
| `Ctrl+A` | ターミナル競合 | GNU Screen のプレフィックスキー |
| `Ctrl+Z` | ターミナル競合 | プロセスサスペンド |

> **ヒント：** ショートカットが効かない場合、ターミナルエミュレータやマルチプレクサとの競合を確認すること。

### タブ補完

Claude Code はインテリジェントなタブ補完を提供する：

```
User: /rew<TAB>
→ /rewind

User: /plu<TAB>
→ /plugin

User: /plugin <TAB>
→ /plugin install
→ /plugin enable
→ /plugin disable
```

### コマンド履歴

過去のコマンドにアクセスする：

```
User: <↑>  # Previous command
User: <↓>  # Next command
User: Ctrl+R  # Search history

(reverse-i-search)`test': run all tests
```

### 複数行入力

複雑なクエリには複数行モードを使う：

```bash
User: \
> Long complex prompt
> spanning multiple lines
> \end
```

**例：**

```
User: \
> Implement a user authentication system
> with the following requirements:
> - JWT tokens
> - Email verification
> - Password reset
> - 2FA support
> \end

Claude: [Processes the multi-line request]
```

### インライン編集

送信前にコマンドを編集できる：

```
User: Deploy to prodcution<Backspace><Backspace>uction

[Edit in-place before sending]
```

### Vim モード

テキスト編集に Vi/Vim キーバインドを有効化する：

**起動：**
- `/config` で有効化（「Editor / Vim mode」を切り替え）するか、`~/.claude/settings.json` に `editorMode: "vim"` を設定する。スタンドアロンの `/vim` スラッシュコマンドは削除された（[issue #43370](https://github.com/anthropics/claude-code/issues/43370) を参照）。Vim モードは設定駆動になった。
- モード切り替え：NORMAL は `Esc`、INSERT は `i/a/o`、VISUAL は `v`、VISUAL-LINE は `V`（v2.1.118 以降）

**ナビゲーションキー：**
- `h` / `l` — 左／右へ移動
- `j` / `k` — 下／上へ移動
- `w` / `b` / `e` — 単語単位で移動
- `0` / `$` — 行頭／行末へ移動
- `gg` / `G` — テキストの先頭／末尾へジャンプ

**テキストオブジェクト：**
- `iw` / `aw` — inner / around 単語
- `i"` / `a"` — inner / around 引用文字列
- `i(` / `a(` — inner / around 括弧

**ビジュアルモード（v2.1.118 以降）：**

| キー | モード | 挙動 |
|-----|------|----------|
| `v` | Visual | 文字単位の選択。視覚的フィードバック付き。モーションキーで拡張する |
| `V` | Visual-line | 行単位の選択。常に行全体を選択する |
| `y` | Yank | 現在のビジュアル選択をコピー |
| `d` / `x` | Delete | 現在のビジュアル選択を削除 |
| `c` | Change | 選択を削除して INSERT モードへ |
| `Esc` | Exit | NORMAL モードへ戻る |

ビジュアル選択は入力フィールド内でハイライトされ、操作確定前にヤンク／削除／変更の対象を正確に確認できる。

### Bash モード

`!` プレフィックスでシェルコマンドを直接実行する：

```bash
! npm test
! git status
! cat src/index.js
```

コンテキストを切り替えずに素早くコマンドを実行したいときに使う。

---

## TUI モード（フルスクリーン）

> **v2.1.110 で新登場**

TUI（Text User Interface）モードは Claude Code をちらつきのない出力でフルスクリーン表示する。tmux や iTerm2 の分割ペインなどのターミナルマルチプレクサに最適である。

### TUI モードの有効化

`/tui` コマンドで切り替えるか、`--tui` フラグで起動する：

```bash
/tui          # toggle from within a session
claude --tui  # start directly in TUI mode
```

### 設定

| 設定 | 説明 | デフォルト |
|---------|-------------|---------|
| `autoScrollEnabled` | 最新メッセージへ自動スクロール | `true` |

`/config` または `settings.json` から自動スクロールを無効化する：

```json
{
  "autoScrollEnabled": false
}
```

### フォーカスビュー

`/focus` コマンドはフォーカスビューを切り替える — 最も関連性の高い出力だけを表示する集中モードである。`Ctrl+O` は通常表示と詳細トランスクリプト表示の切り替えのみを行うようになった（フォーカスビューは `/focus`）。

---

## 音声入力

音声入力は Claude Code でプッシュ・トゥ・トークの音声入力を提供し、タイピングではなくプロンプトを話して入力できるようにする。

### 音声入力の起動

```
/voice
```

### 機能

| 機能 | 説明 |
|---------|-------------|
| **プッシュ・トゥ・トーク** | キーを押している間録音し、離すと送信する |
| **20 言語対応** | 音声テキスト変換が 20 言語をサポート |
| **カスタムキーバインド** | `/keybindings` でプッシュ・トゥ・トークキーを設定 |
| **アカウント要件** | STT 処理に Claude.ai アカウントが必要 |

### 設定

キーバインド設定ファイル（`/keybindings`）でプッシュ・トゥ・トークのキーバインドをカスタマイズする。音声入力は Claude.ai アカウントを使って音声テキスト変換を行う。

---

## チャンネル

チャンネルは Research Preview の機能で、MCP サーバ経由で外部サービスのイベントを実行中の Claude Code セッションにプッシュする。Telegram、Discord、iMessage、任意の Webhook をソースとして利用でき、ポーリングなしで Claude がリアルタイム通知に反応できる。

### チャンネルの購読

```bash
# Subscribe to channel plugins at startup
claude --channels discord,telegram

# Subscribe to multiple sources
claude --channels discord,telegram,imessage,webhooks
```

### サポート対象の連携

| 連携 | 説明 |
|-------------|-------------|
| **Discord** | セッション内で Discord メッセージを受信して応答する |
| **Telegram** | セッション内で Telegram メッセージを受信して応答する |
| **iMessage** | セッション内で iMessage 通知を受信する |
| **Webhooks** | 任意の Webhook ソースからイベントを受信する |

### 設定

起動時に `--channels` フラグでチャンネルを設定する。エンタープライズ展開では、許可するチャンネルプラグインを制御するマネージド設定を使う：

```json
{
  "allowedChannelPlugins": ["discord", "telegram"]
}
```

`allowedChannelPlugins` マネージド設定は、組織全体で許可されるチャンネルプラグインを制御する。

### 仕組み

1. MCP サーバが外部サービスに接続するチャンネルプラグインとして動作する
2. 受信メッセージとイベントがアクティブな Claude Code セッションへプッシュされる
3. Claude はセッションのコンテキスト内でメッセージを読んで応答できる
4. チャンネルプラグインは `allowedChannelPlugins` マネージド設定で承認が必要
5. ポーリング不要 — イベントはリアルタイムでプッシュされる

---

## Chrome 連携

Chrome 連携は、Claude Code を Chrome または Microsoft Edge ブラウザに接続し、ライブな Web 自動化とデバッグを行う機能である。これは v2.0.73 以降で利用可能なベータ機能である（Edge サポートは v1.0.36 以降で追加）。

### Chrome 連携の有効化

**起動時：**

```bash
claude --chrome      # Enable Chrome connection
claude --no-chrome   # Disable Chrome connection
```

**セッション内：**

```
/chrome
```

「Enabled by default」を選択すると、今後すべてのセッションで Chrome 連携が有効になる。Claude Code はブラウザのログイン状態を共有するため、認証済み Web アプリと対話できる。

### 機能

| 機能 | 説明 |
|------------|-------------|
| **ライブデバッグ** | コンソールログの読み取り、DOM 要素の検査、JavaScript のリアルタイムデバッグ |
| **デザイン検証** | レンダリングされたページとデザインモックアップを比較 |
| **フォーム検証** | フォーム送信、入力検証、エラーハンドリングをテスト |
| **Web アプリのテスト** | 認証済みアプリ（Gmail、Google Docs、Notion など）と対話 |
| **データ抽出** | Web ページのコンテンツをスクレイプして処理 |
| **セッション録画** | ブラウザ操作を GIF ファイルとして録画 |

### サイト単位の権限

Chrome 拡張機能はサイトごとのアクセスを管理する。拡張機能のポップアップから、特定サイトへのアクセスをいつでも許可・取り消しできる。Claude Code は明示的に許可されたサイトとのみ対話する。

### 仕組み

Claude Code は表示されたウィンドウ内でブラウザを操作する — 操作の様子をリアルタイムで観察できる。ブラウザがログインページや CAPTCHA に遭遇すると、Claude は一時停止して手動対応を待つ。

### 既知の制限

- **ブラウザ対応：** Chrome と Edge のみ — Brave、Arc、その他の Chromium ブラウザは非対応
- **WSL：** Windows Subsystem for Linux では利用不可
- **サードパーティプロバイダ：** Bedrock、Vertex、Foundry の API プロバイダでは非対応
- **サービスワーカーのアイドル：** 長時間セッション中に Chrome 拡張機能のサービスワーカーがアイドル状態になることがある

> **ヒント：** Chrome 連携はベータ機能である。今後のリリースでブラウザサポートが拡大する可能性がある。

---

## リモートコントロール

リモートコントロールにより、ローカルで動作中の Claude Code セッションをスマートフォン、タブレット、任意のブラウザから継続できる。ローカルセッションはマシン上で動き続ける — クラウドへ移動するものは何もない。Pro、Max、Team、Enterprise プランで利用可能（v2.1.51 以降）。

### リモートコントロールの開始

**CLI から：**

```bash
# Start with default session name
claude remote-control

# Start with a custom name
claude remote-control --name "Auth Refactor"
```

**セッション内から：**

```
/remote-control
/remote-control "Auth Refactor"
```

**利用可能なフラグ：**

| フラグ | 説明 |
|------|-------------|
| `--name "title"` | 識別しやすいセッションタイトル |
| `--verbose` | 詳細な接続ログを表示 |
| `--sandbox` | ファイルシステムとネットワークの隔離を有効化 |
| `--no-sandbox` | サンドボックスを無効化（デフォルト） |

### セッションへの接続

別デバイスから接続する 3 つの方法：

1. **セッション URL** — セッション開始時にターミナルに出力される。任意のブラウザで開ける
2. **QR コード** — 開始後 `spacebar` を押すとスキャン可能な QR コードが表示される
3. **名前で検索** — claude.ai/code または Claude モバイルアプリ（iOS/Android）でセッションを参照

### セキュリティ

- マシン上で **インバウンドポートを開かない**
- **アウトバウンド HTTPS のみ**（TLS 経由）
- **スコープ付き認証情報** — 短命で狭くスコープされた複数のトークン
- **セッション分離** — 各リモートセッションは独立

### リモートコントロール vs Claude Code on the web

| 観点 | リモートコントロール | Claude Code on Web |
|--------|---------------|-------------------|
| **実行場所** | マシン上で動作 | Anthropic クラウド上で動作 |
| **ローカルツール** | ローカル MCP サーバ、ファイル、CLI へのフルアクセス | ローカル依存なし |
| **ユースケース** | 別デバイスからローカル作業を継続 | 任意のブラウザで新規開始 |

### 制限

- Claude Code インスタンスごとにリモートセッションは 1 つ
- ホストマシンのターミナルを開いたままにする必要がある
- ネットワーク到達不能時は約 10 分でセッションがタイムアウト

### ユースケース

- デスクから離れた場所からモバイルデバイスやタブレットで Claude Code を操作する
- ローカルツール実行を保ちつつ、より豊かな claude.ai UI を使う
- 完全なローカル開発環境とともに外出先で素早くコードレビュー

### プッシュ通知（v2.1.110）

リモートコントロールがアクティブで、`/config` で「Push when Claude decides」が有効になっている場合、Claude はモバイルプッシュ通知を送信できる — 例えば長時間タスクの完了時や入力が必要なときなど。

有効化方法：
1. リモートコントロールを起動：`/remote-control` または `claude --rc`
2. `/config` を開いて **Push when Claude decides** を有効化

プッシュ通知には Claude サブスクリプションと Claude モバイルアプリが必要である。

---

## Web セッション

Web セッションでは、claude.ai/code 上のブラウザで直接 Claude Code を実行したり、CLI から Web セッションを作成したりできる。

### Web セッションの作成

```bash
# Create a new web session from the CLI
claude --remote "implement the new API endpoints"
```

これにより claude.ai 上で Claude Code セッションが開始され、任意のブラウザからアクセスできる。

### Web セッションをローカルで再開

Web で開始したセッションをローカルで継続したい場合：

```bash
# Resume a web session in the local terminal
claude --teleport
```

または対話 REPL 内で：
```
/teleport
```

### ユースケース

- 1 台のマシンで作業を始め、別のマシンで継続する
- セッション URL をチームメンバーと共有する
- 視覚的な diff レビューには Web UI を使い、実行はターミナルに切り替える

---

## デスクトップアプリ

Claude Code デスクトップアプリは、視覚的な diff レビュー、並列セッション、統合コネクタを備えたスタンドアロンアプリケーションである。macOS と Windows で利用可能（Pro、Max、Team、Enterprise プラン）。

### インストール

[claude.ai](https://claude.ai) からプラットフォームに合わせてダウンロードする：
- **macOS：** ユニバーサルビルド（Apple Silicon と Intel）
- **Windows：** x64 と ARM64 のインストーラを利用可能

セットアップ手順は [Desktop Quickstart](https://code.claude.com/docs/en/desktop-quickstart) を参照。

### CLI からの引き渡し

現在の CLI セッションをデスクトップアプリに転送する：

```
/desktop
```

### コア機能

| 機能 | 説明 |
|---------|-------------|
| **Diff ビュー** | ファイルごとの視覚的レビューとインラインコメント。Claude はコメントを読んで修正する |
| **アプリプレビュー** | dev サーバを自動起動し、組み込みブラウザでライブ検証 |
| **PR 監視** | GitHub CLI 連携。CI 失敗の自動修正、チェック完了時の自動マージ |
| **並列セッション** | サイドバーで複数セッションを管理。Git ワークツリーで自動的に隔離 |
| **スケジュールタスク** | 定期タスク（時次、日次、平日、週次）。アプリが開いている間に実行 |
| **リッチレンダリング** | コード、Markdown、図表のレンダリングとシンタックスハイライト |

### アプリプレビューの設定

`.claude/launch.json` で dev サーバの動作を設定する：

```json
{
  "command": "npm run dev",
  "port": 3000,
  "readyPattern": "ready on",
  "persistCookies": true
}
```

### コネクタ

外部サービスを接続してより豊かなコンテキストを得る：

| コネクタ | 機能 |
|-----------|------------|
| **GitHub** | PR 監視、Issue トラッキング、コードレビュー |
| **Slack** | 通知、チャンネルコンテキスト |
| **Linear** | Issue トラッキング、スプリント管理 |
| **Notion** | ドキュメント、ナレッジベースアクセス |
| **Asana** | タスク管理、プロジェクト追跡 |
| **Calendar** | スケジュール認識、ミーティングコンテキスト |

> **注：** コネクタはリモート（クラウド）セッションでは利用不可。

### リモートと SSH セッション

- **リモートセッション：** Anthropic のクラウドインフラで動作。アプリを閉じても継続する。claude.ai/code または Claude モバイルアプリからアクセス可能
- **SSH セッション：** SSH 経由でリモートマシンに接続し、リモートのファイルシステムとツールへのフルアクセスを得る。Claude Code をリモートマシンにインストールする必要がある

### デスクトップでの権限モード

デスクトップアプリは CLI と同じ 4 つの権限モードをサポートする：

| モード | 挙動 |
|------|----------|
| **Ask permissions**（デフォルト） | すべての編集とコマンドをレビューして承認 |
| **Auto accept edits** | ファイル編集は自動承認、コマンドは手動承認 |
| **Plan mode** | 変更前にアプローチをレビュー |
| **Bypass permissions** | 自動実行（サンドボックス限定、管理者制御） |

### エンタープライズ機能

- **管理コンソール：** 組織のコードタブアクセスと権限設定を制御
- **MDM 展開：** macOS は MDM、Windows は MSIX で展開
- **SSO 統合：** 組織メンバーにシングルサインオンを必須にする
- **マネージド設定：** チーム設定とモデルの可用性を一元管理

---

## タスクリスト

タスクリスト機能はコンテキストコンパクション（コンテキストウィンドウに収めるため会話履歴がトリミングされること）を生き延びる永続的なタスク追跡を提供する。

### タスクリストの切り替え

セッション中に `Ctrl+T` を押すとタスクリストビューを切り替えられる。

### 永続的なタスク

タスクはコンテキストコンパクションをまたいで永続化されるため、長時間の作業項目が会話コンテキストのトリミング時に失われない。複雑で多段階の実装に特に有用である。

### 名前付きタスクディレクトリ

`CLAUDE_CODE_TASK_LIST_ID` 環境変数を使うと、複数セッションで共有される名前付きタスクディレクトリを作成できる：

```bash
export CLAUDE_CODE_TASK_LIST_ID=my-project-sprint-3
```

これにより複数セッションが同じタスクリストを共有でき、チームワークフローや複数セッションプロジェクトに有用である。

---

## プロンプト候補

プロンプト候補は、Git 履歴と現在の会話コンテキストに基づき、グレーアウトされた例示コマンドを表示する。

### 仕組み

- 候補は入力プロンプトの下にグレーアウトされたテキストとして表示される
- `Tab` を押すと候補を受け入れる
- `Enter` を押すと受け入れて即座に送信する
- 候補はコンテキストを認識し、Git 履歴と会話状態から導出される

### プロンプト候補の無効化

```bash
export CLAUDE_CODE_ENABLE_PROMPT_SUGGESTION=false
```

---

## Git ワークツリー

Git ワークツリーにより、隔離されたワークツリーで Claude Code を起動できる。スタッシュやブランチ切り替えなしに、異なるブランチでの並列作業が可能になる。

### ワークツリーで起動

```bash
# Start Claude Code in an isolated worktree
claude --worktree
# or
claude -w
```

### ワークツリーの保存場所

ワークツリーは以下に作成される：
```
<repo>/.claude/worktrees/<name>
```

### モノレポ向けスパースチェックアウト

`worktree.sparsePaths` 設定でモノレポにスパースチェックアウトを行い、ディスク使用量とクローン時間を削減できる：

```json
{
  "worktree": {
    "sparsePaths": ["packages/my-package", "shared/"]
  }
}
```

### ワークツリーのツールとフック

| 項目 | 説明 |
|------|-------------|
| `ExitWorktree` | 現在のワークツリーを終了してクリーンアップするツール |
| `WorktreeCreate` | ワークツリー作成時に発火するフックイベント |
| `WorktreeRemove` | ワークツリー削除時に発火するフックイベント |

### 自動クリーンアップ

ワークツリーで変更が行われていない場合、セッション終了時に自動でクリーンアップされる。

### ユースケース

- メインブランチを触らずに機能ブランチで作業する
- 作業ディレクトリに影響を与えずにテストを隔離実行する
- 使い捨て環境で実験的な変更を試す
- モノレポで特定パッケージをスパースチェックアウトして起動を高速化する

---

## サンドボックス

サンドボックスは、Claude Code が実行する Bash コマンドに OS レベルのファイルシステムとネットワーク隔離を提供する。これは権限ルールを補完し、追加のセキュリティレイヤーを提供する。

### サンドボックスの有効化

**スラッシュコマンド：**
```
/sandbox
```

**CLI フラグ：**
```bash
claude --sandbox       # Enable sandboxing
claude --no-sandbox    # Disable sandboxing
```

### 設定項目

| 設定 | 説明 |
|---------|-------------|
| `sandbox.enabled` | サンドボックスを有効化／無効化 |
| `sandbox.failIfUnavailable` | サンドボックスを起動できない場合に失敗させる |
| `sandbox.filesystem.allowWrite` | 書き込みを許可するパス |
| `sandbox.filesystem.allowRead` | 読み取りを許可するパス |
| `sandbox.filesystem.denyRead` | 読み取りを拒否するパス |
| `sandbox.network.allowedDomains` | Bash 起動プロセスからアクセスを許可するドメイン（`*.` ワイルドカード対応） |
| `sandbox.network.deniedDomains` | `allowedDomains` のワイルドカードで許可されてもブロックするドメイン（v2.1.113 以降） |
| `sandbox.enableWeakerNetworkIsolation` | macOS で弱いネットワーク隔離を有効化 |

`deniedDomains` が広いワイルドカードを上書きする例（v2.1.113 以降）：

```json
{
  "sandbox": {
    "network": {
      "allowedDomains": ["*.example.com"],
      "deniedDomains": ["evil.example.com"]
    }
  }
}
```

ワイルドカードによって `example.com` 上のすべてが通過するが、`deniedDomains` で個別指定したホストはブロックされる。

### 設定例

```json
{
  "sandbox": {
    "enabled": true,
    "failIfUnavailable": true,
    "filesystem": {
      "allowWrite": ["/Users/me/project"],
      "allowRead": ["/Users/me/project", "/usr/local/lib"],
      "denyRead": ["/Users/me/.ssh", "/Users/me/.aws"]
    },
    "enableWeakerNetworkIsolation": true
  }
}
```

### 仕組み

- Bash コマンドはファイルシステムアクセスを制限したサンドボックス環境で動作する
- ネットワークアクセスを隔離して意図しない外部接続を防げる
- 多層防御のため権限ルールと併用できる
- macOS では `sandbox.enableWeakerNetworkIsolation` でネットワーク制限を行う（macOS では完全なネットワーク隔離は利用不可）

### ユースケース

- 信頼できないコードや生成コードを安全に実行する
- プロジェクト外ファイルへの誤った変更を防ぐ
- 自動化タスク中のネットワークアクセスを制限する

---

## マネージド設定（エンタープライズ）

マネージド設定により、エンタープライズ管理者がプラットフォームネイティブの管理ツールを使って組織全体で Claude Code 設定を展開できる。

### 展開方法

| プラットフォーム | 方法 | 対応バージョン |
|----------|--------|-------|
| macOS | マネージド plist ファイル（MDM） | v2.1.51 以降 |
| Windows | Windows レジストリ | v2.1.51 以降 |
| クロスプラットフォーム | マネージド設定ファイル | v2.1.51 以降 |
| クロスプラットフォーム | マネージドドロップイン（`managed-settings.d/` ディレクトリ） | v2.1.83 以降 |

### マネージドドロップイン

v2.1.83 以降、管理者は複数のマネージド設定ファイルを `managed-settings.d/` ディレクトリに配置できる。ファイルはアルファベット順にマージされ、チーム横断のモジュラー設定が可能になる：

```
~/.claude/managed-settings.d/
  00-org-defaults.json
  10-team-policies.json
  20-project-overrides.json
```

### 利用可能なマネージド設定

| 設定 | 説明 |
|---------|-------------|
| `disableBypassPermissionsMode` | ユーザーによる bypass permissions の有効化を防ぐ |
| `availableModels` | ユーザーが選択可能なモデルを制限する |
| `allowedChannelPlugins` | 許可するチャンネルプラグインを制御する |
| `autoMode.environment` | オートモードの信頼インフラを設定する |
| `wslInheritsWindowsSettings` | Windows/WSL 限定（v2.1.118 以降）：`true` の場合、WSL 内で動作する Claude Code が Windows ホストのマネージド設定を継承し、Registry/MDM で展開された企業ポリシーが Windows シェルと WSL シェルで均一に適用される |
| カスタムポリシー | 組織固有の権限とツールポリシー |

### 例：macOS Plist

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
  "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>disableBypassPermissionsMode</key>
  <true/>
  <key>availableModels</key>
  <array>
    <string>claude-sonnet-4-6</string>
    <string>claude-haiku-4-5</string>
  </array>
</dict>
</plist>
```

---

## 設定とコンフィグ

### 設定ファイルの場所

1. **グローバル設定：** `~/.claude/config.json`
2. **プロジェクト設定：** `./.claude/config.json`
3. **ユーザー設定：** `~/.config/claude-code/settings.json`

### 完全な設定例

**コア高度機能の設定：**

```json
{
  "permissions": {
    "mode": "default"
  },
  "hooks": {
    "PreToolUse:Edit": "eslint --fix ${file_path}",
    "PostToolUse:Write": "~/.claude/hooks/security-scan.sh"
  },
  "mcp": {
    "enabled": true,
    "servers": {
      "github": {
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-github"]
      }
    }
  }
}
```

**拡張設定例：**

```json
{
  "permissions": {
    "mode": "default",
    "allowedTools": ["Bash(git log:*)", "Read"],
    "disallowedTools": ["Bash(rm -rf:*)"]
  },

  "hooks": {
    "PreToolUse": [{ "matcher": "Edit", "hooks": ["eslint --fix ${file_path}"] }],
    "PostToolUse": [{ "matcher": "Write", "hooks": ["~/.claude/hooks/security-scan.sh"] }],
    "Stop": [{ "hooks": ["~/.claude/hooks/notify.sh"] }]
  },

  "mcp": {
    "enabled": true,
    "servers": {
      "github": {
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-github"],
        "env": {
          "GITHUB_TOKEN": "${GITHUB_TOKEN}"
        }
      }
    }
  }
}
```

### 環境変数

設定を環境変数で上書きする：

```bash
# Model selection
export ANTHROPIC_MODEL=claude-opus-4-7
export ANTHROPIC_DEFAULT_OPUS_MODEL=claude-opus-4-7
export ANTHROPIC_DEFAULT_SONNET_MODEL=claude-sonnet-4-6
export ANTHROPIC_DEFAULT_HAIKU_MODEL=claude-haiku-4-5

# API configuration
export ANTHROPIC_API_KEY=sk-ant-...

# Thinking configuration
export MAX_THINKING_TOKENS=16000
export CLAUDE_CODE_EFFORT_LEVEL=xhigh   # low, medium, high, xhigh (Opus 4.7 only, default), or max (supported on Opus 4.7, Opus 4.6, Sonnet 4.6)

# Feature toggles
export CLAUDE_CODE_DISABLE_AUTO_MEMORY=true
export CLAUDE_CODE_DISABLE_BACKGROUND_TASKS=true
export CLAUDE_CODE_DISABLE_CRON=1
export CLAUDE_CODE_DISABLE_GIT_INSTRUCTIONS=true
export CLAUDE_CODE_DISABLE_TERMINAL_TITLE=true
export CLAUDE_CODE_DISABLE_1M_CONTEXT=true
export CLAUDE_CODE_DISABLE_NONSTREAMING_FALLBACK=true
export CLAUDE_CODE_ENABLE_PROMPT_SUGGESTION=false
export CLAUDE_CODE_ENABLE_TASKS=true
export CLAUDE_CODE_SIMPLE=true              # Set by --bare flag

# MCP configuration
export MAX_MCP_OUTPUT_TOKENS=50000
export ENABLE_TOOL_SEARCH=true

# Prompt caching
export ENABLE_PROMPT_CACHING_1H=1      # Use 1-hour prompt cache TTL (default is 5 min)

# Task management
export CLAUDE_CODE_TASK_LIST_ID=my-project-tasks

# Agent teams (experimental)
export CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1

# Subagent and plugin configuration
export CLAUDE_CODE_SUBAGENT_MODEL=sonnet
export CLAUDE_CODE_PLUGIN_SEED_DIR=./my-plugins
export CLAUDE_CODE_NEW_INIT=1

# Subprocess and streaming
export CLAUDE_CODE_SUBPROCESS_ENV_SCRUB="SECRET_KEY,DB_PASSWORD"
export CLAUDE_AUTOCOMPACT_PCT_OVERRIDE=80
export CLAUDE_STREAM_IDLE_TIMEOUT_MS=30000
export ANTHROPIC_CUSTOM_MODEL_OPTION=my-custom-model
export SLASH_COMMAND_TOOL_CHAR_BUDGET=50000
```

> **v2.1.108：** `ENABLE_PROMPT_CACHING_1H=1` — デフォルトの 5 分 TTL ではなく 1 時間のプロンプトキャッシュ TTL を使用する。安定した長時間セッションでキャッシュミスを削減する。

### 設定管理コマンド

```
User: /config
[Opens interactive configuration menu]
```

`/config` コマンドは以下のような設定をトグルする対話メニューを提供する：
- 拡張思考のオン／オフ
- 詳細出力
- 権限モード
- モデル選択

### プロジェクト単位の設定

プロジェクトに `.claude/config.json` を作成する：

```json
{
  "hooks": {
    "PreToolUse": [{ "matcher": "Bash", "hooks": ["npm test && npm run lint"] }]
  },
  "permissions": {
    "mode": "default"
  },
  "mcp": {
    "servers": {
      "project-db": {
        "command": "mcp-postgres",
        "env": {
          "DATABASE_URL": "${PROJECT_DB_URL}"
        }
      }
    }
  }
}
```

---

## エージェントチーム

エージェントチームは複数の Claude Code インスタンスがタスクで協業できる実験的機能である。デフォルトでは無効化されている。

### エージェントチームの有効化

環境変数または設定で有効化する：

```bash
# Environment variable
export CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1
```

または設定 JSON に追加する：

```json
{
  "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"
}
```

### エージェントチームの仕組み

- **チームリード** が全体タスクを調整し、サブタスクをチームメイトに委譲する
- **チームメイト** はそれぞれ独自のコンテキストウィンドウを持ち、独立して作業する
- **共有タスクリスト** によりチームメンバー間の自己調整が可能になる
- サブエージェント定義（`.claude/agents/` または `--agents` フラグ）でチームメイトの役割と専門性を定義する

### 表示モード

エージェントチームは `--teammate-mode` フラグで設定する 2 つの表示モードをサポートする：

| モード | 説明 |
|------|-------------|
| `in-process`（デフォルト） | チームメイトが同じターミナルプロセス内で動作する |
| `tmux` | 各チームメイトが専用の分割ペインを持つ（tmux または iTerm2 が必要） |
| `auto` | 最適な表示モードを自動選択する |

```bash
# Use tmux split panes for teammate display
claude --teammate-mode tmux

# Explicitly use in-process mode
claude --teammate-mode in-process
```

### ユースケース

- 異なるチームメイトが異なるモジュールを担当する大規模リファクタリング
- 並列のコードレビューと実装
- コードベース横断的な複数ファイル変更の調整

> **注：** エージェントチームは実験的機能であり、今後のリリースで変更される可能性がある。完全なリファレンスは [code.claude.com/docs/en/agent-teams](https://code.claude.com/docs/en/agent-teams) を参照。

---

## ベストプラクティス

### プランニングモード
- ✅ 複雑な複数ステップタスクに使う
- ✅ 承認前に計画をレビューする
- ✅ 必要に応じて計画を修正する
- ❌ 単純なタスクには使わない

### 拡張思考
- ✅ アーキテクチャ判断に使う
- ✅ 複雑な問題解決に使う
- ✅ 思考プロセスをレビューする
- ❌ 単純なクエリには使わない

### バックグラウンドタスク
- ✅ 長時間実行操作に使う
- ✅ タスクの進捗を監視する
- ✅ タスクの失敗を適切に処理する
- ❌ 同時タスクを多すぎるほど起動しない

### 権限
- ✅ コードレビューには `plan`（読み取り専用）を使う
- ✅ 対話的開発には `default` を使う
- ✅ 自動化ワークフローには `acceptEdits` を使う
- ✅ セーフティガードレール付きの自律作業には `auto` を使う
- ✅ どうしても必要でない限り `bypassPermissions` を使わない

### セッション
- ✅ 異なるタスクには別々のセッションを使う
- ✅ 重要なセッション状態を保存する
- ✅ 古いセッションをクリーンアップする
- ❌ 1 つのセッションに無関係な作業を混在させない

---

## 追加リソース

Claude Code および関連機能の詳細：

- [Official Interactive Mode Documentation](https://code.claude.com/docs/en/interactive-mode)
- [Official Headless Mode Documentation](https://code.claude.com/docs/en/headless)
- [CLI Reference](https://code.claude.com/docs/en/cli-reference)
- [Checkpoints Guide](../08-checkpoints/) — セッション管理と巻き戻し
- [Slash Commands](../01-slash-commands/) — コマンドリファレンス
- [Memory Guide](../02-memory/) — 永続コンテキスト
- [Skills Guide](../03-skills/) — 自律機能
- [Subagents Guide](../04-subagents/) — タスク委譲実行
- [MCP Guide](../05-mcp/) — 外部データアクセス
- [Hooks Guide](../06-hooks/) — イベント駆動自動化
- [Plugins Guide](../07-plugins/) — バンドル拡張
- [Official Scheduled Tasks Documentation](https://code.claude.com/docs/en/scheduled-tasks)
- [Official Chrome Integration Documentation](https://code.claude.com/docs/en/chrome)
- [Official Remote Control Documentation](https://code.claude.com/docs/en/remote-control)
- [Official Keybindings Documentation](https://code.claude.com/docs/en/keybindings)
- [Official Desktop App Documentation](https://code.claude.com/docs/en/desktop)
- [Official Agent Teams Documentation](https://code.claude.com/docs/en/agent-teams)

---

**最終更新：** 2026 年 4 月 24 日
**Claude Code バージョン：** 2.1.119
**情報源：**
- https://code.claude.com/docs/en/permission-modes
- https://code.claude.com/docs/en/interactive-mode
- https://code.claude.com/docs/en/settings
- https://www.anthropic.com/news/claude-opus-4-7
- https://github.com/anthropics/claude-code/releases/tag/v2.1.117
- https://github.com/anthropics/claude-code/releases/tag/v2.1.118

**互換モデル：** Claude Sonnet 4.6、Claude Opus 4.7、Claude Haiku 4.5
