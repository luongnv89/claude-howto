<!-- i18n-source: 08-checkpoints/README.md -->
<!-- i18n-source-sha: d17d515 -->
<!-- i18n-date: 2026-04-27 -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../../resources/logos/claude-howto-logo.svg">
</picture>

# チェックポイントと巻き戻し

チェックポイントは、Claude Code セッションの会話状態を保存し、過去の地点へ巻き戻すための機能である。複数のアプローチを比較したい場合、ミスから復旧したい場合、代替案を見比べたい場合に大きな威力を発揮する。

## 概観

チェックポイントを使うと、会話状態を保存して過去の地点に戻れるため、安全に試行錯誤と複数アプローチの探索ができる。チェックポイントは会話状態のスナップショットであり、以下を含む：
- やり取りされた全メッセージ
- 加えられたファイル変更
- ツール使用履歴
- セッションコンテキスト

別アプローチの試行、ミスからの復旧、代替案の比較といった場面で威力を発揮する。

## 主要な概念

| 概念 | 説明 |
|------|------|
| **Checkpoint（チェックポイント）** | メッセージ・ファイル・コンテキストを含む会話状態のスナップショット |
| **Rewind（巻き戻し）** | 過去のチェックポイントへ戻り、それ以降の変更を破棄する操作 |
| **Branch Point（分岐点）** | 複数のアプローチを試すための起点となるチェックポイント |

## チェックポイントへのアクセス

チェックポイントへアクセス・管理する主な方法は 2 つある。

### キーボードショートカット
`Esc` キーを 2 回（`Esc` + `Esc`）押すと、チェックポイントインターフェイスが開き、保存済みチェックポイントを参照できる。

### スラッシュコマンド
すばやくアクセスしたい場合は `/rewind` コマンド（エイリアス：`/checkpoint`）を使う：

```bash
# 巻き戻しインターフェイスを開く
/rewind

# またはエイリアスを利用
/checkpoint
```

## 巻き戻しオプション

巻き戻しを実行すると、5 つのオプションメニューが表示される：

1. **Restore code and conversation** -- 指定したチェックポイントの状態にファイルとメッセージの両方を戻す
2. **Restore conversation** -- メッセージのみ巻き戻し、現在のコードはそのまま残す
3. **Restore code** -- ファイル変更のみ戻し、会話履歴は完全に維持する
4. **Summarize from here** -- そこ以降の会話を AI 生成のサマリに圧縮し、コンテキストウィンドウを解放する。選択点より前のメッセージはそのまま残る。ディスク上のファイルは変更されない。元のメッセージはセッショントランスクリプトに保存される。サマリを特定のトピックに絞るための指示を任意で与えられる。
5. **Never mind** -- 操作をキャンセルし、現在の状態に戻る

> **注意**: 会話を復元または要約した後、選択したメッセージの元のプロンプトが入力欄に復元され、再送信や編集ができる状態になる。

## 自動チェックポイント

Claude Code は自動でチェックポイントを作成する：

- **ユーザーの入力ごと** - 入力のたびに新しいチェックポイントが生成される
- **セッション間で保持** - 別セッションを跨いでもチェックポイントは残る
- **自動クリーンアップ** - 30 日経過したチェックポイントは自動削除される

これにより、数分前から数日前まで、会話のどの時点へも巻き戻せる。

## ユースケース

| シナリオ | ワークフロー |
|----------|-------------|
| **アプローチの探索** | 保存 → 案 A を試す → 保存 → 巻き戻し → 案 B を試す → 比較 |
| **安全なリファクタリング** | 保存 → リファクタリング → テスト → 失敗なら巻き戻し |
| **A/B テスト** | 保存 → 設計 A → 保存 → 巻き戻し → 設計 B → 比較 |
| **ミスからの復旧** | 問題に気づく → 直前の良好な状態へ巻き戻し |

## チェックポイントの利用

### 一覧表示と巻き戻し

`Esc` を 2 回押すか `/rewind` を実行するとチェックポイントブラウザが開く。タイムスタンプ付きの一覧から好きなチェックポイントを選ぶと、その状態に巻き戻る。

### チェックポイントの詳細

各チェックポイントには以下が表示される：
- 作成時のタイムスタンプ
- 変更されたファイル
- 会話内のメッセージ数
- 使用されたツール

## 実用例

### 例 1: 別アプローチを試す

```
User: Let's add a caching layer to the API

Claude: I'll add Redis caching to your API endpoints...
[Makes changes at checkpoint A]

User: Actually, let's try in-memory caching instead

Claude: I'll rewind to explore a different approach...
[User presses Esc+Esc and rewinds to checkpoint A]
[Implements in-memory caching at checkpoint B]

User: Now I can compare both approaches
```

### 例 2: ミスからの復旧

```
User: Refactor the authentication module to use JWT

Claude: I'll refactor the authentication module...
[Makes extensive changes]

User: Wait, that broke the OAuth integration. Let's go back.

Claude: I'll help you rewind to before the refactoring...
[User presses Esc+Esc and selects the checkpoint before the refactor]

User: Let's try a more conservative approach this time
```

### 例 3: 安全な試行錯誤

```
User: Let's try rewriting this in a functional style
[Creates checkpoint before experiment]

Claude: [Makes experimental changes]

User: The tests are failing. Let's rewind.
[User presses Esc+Esc and rewinds to the checkpoint]

Claude: I've rewound the changes. Let's try a different approach.
```

### 例 4: アプローチの分岐

```
User: I want to compare two database designs
[Takes note of checkpoint - call it "Start"]

Claude: I'll create the first design...
[Implements Schema A]

User: Now let me go back and try the second approach
[User presses Esc+Esc and rewinds to "Start"]

Claude: Now I'll implement Schema B...
[Implements Schema B]

User: Great! Now I have both schemas to choose from
```

## チェックポイントの保持期間

Claude Code はチェックポイントを自動管理する：

- ユーザー入力ごとにチェックポイントが自動作成される
- 古いチェックポイントは最大 30 日まで保持される
- ストレージが無限に増えないよう自動でクリーンアップされる

## ワークフローパターン

### 探索のための分岐戦略

複数アプローチを試すとき：

```
1. 初期実装 → チェックポイント A
2. アプローチ 1 を試す → チェックポイント B
3. チェックポイント A に巻き戻し
4. アプローチ 2 を試す → チェックポイント C
5. B と C の結果を比較
6. 最良案を選んで継続
```

### 安全なリファクタリングのパターン

大きな変更を加えるとき：

```
1. 現状 → チェックポイント（自動）
2. リファクタリング開始
3. テスト実行
4. 成功 → 続行
5. 失敗 → 巻き戻して別案を試す
```

## ベストプラクティス

チェックポイントは自動作成されるため、状態保存を意識せず作業に集中できる。ただし以下のポイントは押さえておくとよい。

### チェックポイントを効果的に使う

✅ **やる:**
- 巻き戻し前に利用可能なチェックポイントを確認する
- 別方向を試したいときに巻き戻しを使う
- 複数アプローチの比較用にチェックポイントを残す
- 各巻き戻しオプション（コードと会話の復元、会話のみ復元、コードのみ復元、要約）の挙動を理解する

❌ **やらない:**
- コード保全をチェックポイントだけに頼る
- ファイルシステムへの外部変更まで追跡されると思い込む
- git コミットの代わりにチェックポイントを使う

## 設定

チェックポイントは Claude Code の組み込み機能で、有効化のための設定は不要である。ユーザー入力のたびにチェックポイントが自動生成される。

チェックポイントに関連する唯一の設定は `cleanupPeriodDays` で、セッションとチェックポイントの保持期間を制御する：

```json
{
  "cleanupPeriodDays": 30
}
```

- `cleanupPeriodDays`: セッション履歴とチェックポイントの保持日数（デフォルト: `30`）

> **v2.1.117 のアップデート**: `cleanupPeriodDays` がチェックポイントだけでなく、ディスク上の 4 種類のキャッシュの保持期間を統合的に制御するようになった：
>
> - セッションチェックポイント
> - `~/.claude/tasks/` — 永続的なタスクリスト
> - `~/.claude/shell-snapshots/` — 取得済みのシェル環境スナップショット
> - `~/.claude/backups/` — 設定ファイル / CLAUDE.md の循環バックアップ
>
> 1 つの設定で 4 つのディレクトリが同じ日数で一律に整理される。

## 制限事項

チェックポイントには次の制限がある：

- **bash コマンドによる変更は追跡されない** - `rm`、`mv`、`cp` などのファイルシステム操作はチェックポイントに含まれない
- **外部の変更は追跡されない** - エディタやターミナルなど Claude Code の外で行った変更は捕捉されない
- **バージョン管理の代わりにはならない** - 永続的で監査可能な変更には git を使う

## トラブルシューティング

### チェックポイントが見つからない

**問題**: 期待したチェックポイントが存在しない

**対処法**:
- チェックポイントが消去されていないか確認する
- ディスク容量を確認する
- `cleanupPeriodDays` を十分大きくする（デフォルト: 30 日）

### 巻き戻しに失敗する

**問題**: チェックポイントへ巻き戻せない

**対処法**:
- 未コミットの変更が衝突していないか確認する
- チェックポイントが破損していないか確認する
- 別のチェックポイントへ戻すことを試す

## Git との連携

チェックポイントは git を補完するが、置き換えるものではない：

| 項目 | Git | チェックポイント |
|------|-----|----------------|
| 範囲 | ファイルシステム | 会話 + ファイル |
| 永続性 | 永続的 | セッション単位 |
| 粒度 | コミット単位 | 任意の地点 |
| 速度 | 比較的遅い | 即時 |
| 共有 | 可 | 限定的 |

両者を組み合わせて使う：
1. 試行錯誤にはチェックポイントを使う
2. 確定した変更には git コミットを使う
3. git 操作の前にチェックポイントを作成する
4. 良好なチェックポイントの状態を git にコミットする

## クイックスタートガイド

### 基本ワークフロー

1. **普通に作業する** - Claude Code が自動でチェックポイントを作成
2. **戻りたくなったら** - `Esc` を 2 回押すか `/rewind` を使う
3. **チェックポイントを選ぶ** - リストから巻き戻し先を選択
4. **復元対象を選ぶ** - コードと会話、会話のみ、コードのみ、要約、キャンセルから選択
5. **作業を続ける** - 選んだ時点に戻った状態で再開

### キーボードショートカット

- **`Esc` + `Esc`** - チェックポイントブラウザを開く
- **`/rewind`** - チェックポイントへの別アクセス手段
- **`/checkpoint`** - `/rewind` のエイリアス

## いつ巻き戻すかを知る：コンテキスト監視

チェックポイントで戻ることはできるが、*いつ*戻るべきかをどう判断するか。会話が長くなるにつれて Claude のコンテキストウィンドウは消費され、モデル品質は静かに劣化する。気づかないうちに半盲状態のモデルからコードを受け取っているかもしれない。

**[cc-context-stats](https://github.com/luongnv89/cc-context-stats)** は、Claude Code のステータスバーにリアルタイムの **コンテキストゾーン** を追加してこの問題を解決する。コンテキストウィンドウのどの位置にいるかを追跡し、**Plan**（緑、計画とコーディングが安全）から **Code**（黄、新しい計画は始めない）、**Dump**（橙、まとめて巻き戻す）まで段階表示する。ゾーンが切り替わったら、劣化した出力で押し切らずチェックポイントから新しく始めるべきタイミングだとわかる。

## 関連概念

- **[高度な機能](../09-advanced-features/)** - プランニングモードやその他の高度な機能
- **[メモリ管理](../02-memory/)** - 会話履歴とコンテキストの管理
- **[スラッシュコマンド](../01-slash-commands/)** - ユーザーが起動するショートカット
- **[フック](../06-hooks/)** - イベント駆動の自動化
- **[プラグイン](../07-plugins/)** - バンドルされた拡張パッケージ

## 追加リソース

- [チェックポイント公式ドキュメント](https://code.claude.com/docs/en/checkpointing)
- [高度な機能ガイド](../09-advanced-features/) - 拡張思考などの機能

## まとめ

チェックポイントは Claude Code の自動機能で、作業を失う恐れなく安全にさまざまなアプローチを試せる。ユーザー入力のたびに新しいチェックポイントが作られるため、セッションのどの時点へも戻れる。

主な利点：
- 複数アプローチを恐れずに試せる
- ミスからすばやく復旧できる
- 異なる解決案を並べて比較できる
- バージョン管理と安全に組み合わせられる

注意：チェックポイントは git の代わりにはならない。試行錯誤にはチェックポイント、永続的なコード変更には git を使う。

---

**最終更新**: 2026 年 4 月 24 日
**Claude Code バージョン**: 2.1.119
**出典**:
- https://code.claude.com/docs/en/checkpointing
- https://code.claude.com/docs/en/settings
- https://github.com/anthropics/claude-code/releases/tag/v2.1.117
**対応モデル**: Claude Sonnet 4.6、Claude Opus 4.7、Claude Haiku 4.5
