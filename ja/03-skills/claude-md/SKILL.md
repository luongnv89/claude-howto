<!-- i18n-source: 03-skills/claude-md/SKILL.md -->
<!-- i18n-source-sha: f78c094 -->
<!-- i18n-date: 2026-04-27 -->
---
name: claude-md
description: Create or update CLAUDE.md files following best practices for optimal AI agent onboarding
---

## ユーザー入力

```text
$ARGUMENTS
```

ユーザー入力が空でない場合、進める前に **必ず** 内容を考慮すること。ユーザーは以下を指定する場合がある:
- `create` - 新しい CLAUDE.md をゼロから作成
- `update` - 既存 CLAUDE.md を改善
- `audit` - 現在の CLAUDE.md の品質を分析しレポート
- 作成・更新する具体的なパス（例: ディレクトリ固有命令向けの `src/api/CLAUDE.md`）

## 基本原則

**LLM はステートレス**: CLAUDE.md は、すべての会話に自動的に含まれる唯一のファイルである。コードベースに対する AI エージェントの主要なオンボーディングドキュメントとして機能する。

### ゴールデンルール

1. **少ないほど良い**: フロンティア LLM は約 150〜200 個の命令に従える。Claude Code のシステムプロンプトはすでに約 50 個を使用している。CLAUDE.md は焦点を絞り簡潔に保つこと。

2. **普遍的な適用性**: あらゆるセッションに関係する情報のみを含める。タスク固有の命令は別ファイルに置く。

3. **Claude をリンターとして使わない**: スタイルガイドラインはコンテキストを膨張させ命令の遵守を低下させる。代わりに決定論的なツール（prettier, eslint など）を使う。

4. **絶対に自動生成しない**: CLAUDE.md は AI ハーネスにおける最も影響力の高いポイントである。慎重に手作業で作り上げること。

## 実行フロー

### 1. プロジェクト分析

まず現在のプロジェクト状態を分析する:

1. 既存の CLAUDE.md ファイルを確認:
   - ルートレベル: `./CLAUDE.md` または `.claude/CLAUDE.md`
   - ディレクトリ固有: `**/CLAUDE.md`
   - グローバルユーザー設定: `~/.claude/CLAUDE.md`

2. プロジェクト構造を特定:
   - 技術スタック（言語、フレームワーク）
   - プロジェクト種別（モノレポ、単一アプリ、ライブラリ）
   - 開発ツール（パッケージマネージャー、ビルドシステム、テストランナー）

3. 既存ドキュメントをレビュー:
   - README.md
   - CONTRIBUTING.md
   - package.json, pyproject.toml, Cargo.toml など

### 2. コンテンツ戦略（WHAT, WHY, HOW）

CLAUDE.md を 3 つの観点で構成する:

#### WHAT - 技術と構造
- 技術スタックの概要
- プロジェクトの編成（モノレポでは特に重要）
- 主要ディレクトリとその目的

#### WHY - 目的と背景
- プロジェクトが何をするか
- なぜ特定の設計判断が下されたのか
- 各主要コンポーネントが何を担当するか

#### HOW - ワークフローと規約
- 開発ワークフロー（bun と node、pip と uv など）
- テスト手順とコマンド
- 検証およびビルド手段
- 重要な「ハマりどころ」や明示されない要件

### 3. プログレッシブディスクロージャ戦略

大規模プロジェクトでは `agent_docs/` フォルダの作成を推奨する:

```
agent_docs/
  |- building_the_project.md
  |- running_tests.md
  |- code_conventions.md
  |- architecture_decisions.md
```

CLAUDE.md からは以下のような命令でこれらのファイルを参照する:
```markdown
For detailed build instructions, refer to `agent_docs/building_the_project.md`
```

**重要**: 古くなるコンテキストを避けるため、コードスニペットではなく `file:line` 参照を用いる。

### 4. 品質制約

CLAUDE.md を作成・更新する際:

1. **目標の長さ**: 300 行以下（理想は 100 行以下）
2. **スタイルルールなし**: lint やフォーマットの命令は除く
3. **タスク固有命令なし**: 別ファイルへ移す
4. **コードスニペットなし**: ファイル参照を用いる
5. **冗長情報なし**: package.json や README にあるものを繰り返さない

### 5. 必須セクション

良く構成された CLAUDE.md には以下を含めるべきである:

```markdown
# Project Name

Brief one-line description.

## Tech Stack
- Primary language and version
- Key frameworks/libraries
- Database/storage (if any)

## Project Structure
[Only for monorepos or complex structures]
- `apps/` - Application entry points
- `packages/` - Shared libraries

## Development Commands
- Install: `command`
- Test: `command`
- Build: `command`

## Critical Conventions
[Only non-obvious, high-impact conventions]
- Convention 1 with brief explanation
- Convention 2 with brief explanation

## Known Issues / Gotchas
[Things that consistently trip up developers]
- Issue 1
- Issue 2
```

### 6. 避けるべきアンチパターン

**含めてはいけないもの:**
- コードスタイルガイドライン（リンターを使う）
- Claude の使い方に関するドキュメント
- 自明なパターンへの長い説明
- コピー＆ペーストされたコード例
- 一般的なベストプラクティス（"write clean code"）
- 特定タスク向けの命令
- 自動生成された内容
- 大量の TODO リスト

### 7. 検証チェックリスト

最終化前に確認:

- [ ] 300 行以下（できれば 100 行以下）
- [ ] すべての行があらゆるセッションに適用される
- [ ] スタイルやフォーマットのルールがない
- [ ] コードスニペットがない（ファイル参照を使う）
- [ ] コマンドが動作することを検証済み
- [ ] 複雑なプロジェクトでプログレッシブディスクロージャを利用
- [ ] 重要なハマりどころがドキュメント化されている
- [ ] README.md と内容が重複していない

## 出力形式

### `create` または既定の場合:

1. プロジェクトを分析する
2. 上記の構造に従って CLAUDE.md の草案を作る
3. 草案をレビュー用に提示する
4. 承認後、適切な場所へ書き込む

### `update` の場合:

1. 既存 CLAUDE.md を読む
2. ベストプラクティスに照らして監査する
3. 以下を特定する:
   - 削除する内容（スタイルルール、コードスニペット、タスク固有）
   - 凝縮する内容
   - 不足している必須情報
4. 変更内容をレビュー用に提示する
5. 承認後、変更を適用する

### `audit` の場合:

1. 既存 CLAUDE.md を読む
2. 以下を含むレポートを生成する:
   - 現在の行数と目標値
   - 普遍的に適用可能なコンテンツの割合
   - 検出されたアンチパターンの一覧
   - 改善のための推奨
3. ファイルを変更しない、レポートのみを行う

## AGENTS.md の取り扱い

ユーザーが AGENTS.md の作成・更新を求めた場合:

AGENTS.md は専門エージェントの振る舞いを定義するために用いられる。プロジェクトコンテキスト用の CLAUDE.md と異なり、AGENTS.md では以下を定義する:
- カスタムエージェントの役割と能力
- エージェント固有の命令と制約
- マルチエージェントシナリオのワークフロー定義

同様の原則を適用する:
- 焦点を絞り簡潔に保つ
- プログレッシブディスクロージャを用いる
- 内容を埋め込むのではなく外部ドキュメントを参照する

## 注意事項

- コマンドを含める前に必ず動作確認する
- 迷ったら省略する。少ないほど良い
- システムリマインダーは Claude に対して CLAUDE.md は「関係があるかどうかわからない」と告げている。ノイズが多いほど無視されやすい
- モノレポは明確な WHAT/WHY/HOW 構造の恩恵が最も大きい
- ディレクトリ固有の CLAUDE.md ファイルはさらに焦点を絞るべきである
