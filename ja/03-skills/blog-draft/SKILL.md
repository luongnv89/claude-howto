<!-- i18n-source: 03-skills/blog-draft/SKILL.md -->
<!-- i18n-source-sha: f396788 -->
<!-- i18n-date: 2026-04-27 -->

---
name: blog-draft
description: アイデアとリソースからブログ記事の下書きを作成する。ブログ記事の執筆、リサーチからのコンテンツ作成、記事の下書き作成時に使用する。リサーチ、ブレインストーミング、アウトライン作成、バージョン管理付きの反復的な下書き作成を案内する。
---

## ユーザー入力

```text
$ARGUMENTS
```

進める前にユーザー入力を**必ず**考慮する。ユーザーは以下を提供すべきである。
- **Idea/Topic**: ブログ記事の主要なコンセプトやテーマ
- **Resources**: URL、ファイル、リサーチ用の参考情報（任意だが推奨）
- **Target audience**: ブログ記事の対象読者（任意）
- **Tone/Style**: フォーマル、カジュアル、技術的、など（任意）

**重要**: ユーザーが**既存のブログ記事**の更新を要求している場合、ステップ 0-8 をスキップして直接**ステップ 9**から開始する。まず既存の下書きファイルを読み、その後で反復プロセスを進める。

## 実行フロー

以下のステップを順次実行する。**ステップをスキップしたり、指示された箇所でユーザー承認なしに進めたりしてはならない。**

### Step 0: プロジェクトフォルダの作成

1. 次の形式でフォルダ名を生成する: `YYYY-MM-DD-short-topic-name`
   - 今日の日付を使用
   - トピックから短く URL フレンドリーなスラッグを作成（小文字、ハイフン、最大 5 単語）

2. フォルダ構造を作成:
   ```
   blog-posts/
   └── YYYY-MM-DD-short-topic-name/
       └── resources/
   ```

3. 進める前にフォルダ作成をユーザーに確認する。

### Step 1: リサーチとリソース収集

1. ブログ記事ディレクトリ内に `resources/` サブフォルダを作成

2. 提供された各リソースに対して:
   - **URLs**: 取得して主要情報を `resources/` にマークダウンファイルとして保存
   - **Files**: 読み込んで `resources/` に要約
   - **Topics**: ウェブ検索を使用して最新情報を収集

3. 各リソースについて、`resources/` に要約ファイルを作成:
   - `resources/source-1-[short-name].md`
   - `resources/source-2-[short-name].md`
   - など

4. 各要約には以下を含める:
   ```markdown
   # Source: [Title/URL]

   ## Key Points
   - Point 1
   - Point 2

   ## Relevant Quotes/Data
   - Quote or statistic 1
   - Quote or statistic 2

   ## How This Relates to Topic
   関連性の簡潔な説明
   ```

5. リサーチの要約をユーザーに提示する。

### Step 2: ブレインストーミングと明確化

1. アイデアとリサーチしたリソースに基づき、以下を提示:
   - リサーチから特定された**主要テーマ**
   - ブログ記事の**取りうる切り口**
   - カバーすべき**重要ポイント**
   - 明確化が必要な情報の**ギャップ**

2. 明確化のための質問:
   - 読者に持って帰ってほしい主要なテイクアウェイは何か？
   - リサーチの中で特に強調したい点はあるか？
   - 目標の長さは？（short: 500-800 words、medium: 1000-1500、long: 2000+）
   - 除外したい点はあるか？

3. **進める前にユーザー応答を待つ。**

### Step 3: アウトライン提案

1. 以下を含む構造化されたアウトラインを作成:

   ```markdown
   # Blog Post Outline: [Title]

   ## Meta Information
   - **Target Audience**: [who]
   - **Tone**: [style]
   - **Target Length**: [word count]
   - **Main Takeaway**: [key message]

   ## Proposed Structure

   ### Hook/Introduction
   - Opening hook idea
   - Context setting
   - Thesis statement

   ### Section 1: [Title]
   - Key point A
   - Key point B
   - Supporting evidence from [source]

   ### Section 2: [Title]
   - Key point A
   - Key point B

   [全セクションについて続ける...]

   ### Conclusion
   - Summary of key points
   - Call to action or final thought

   ## Sources to Cite
   - Source 1
   - Source 2
   ```

2. アウトラインをユーザーに提示し、**承認または修正を求める**。

### Step 4: 承認されたアウトラインの保存

1. ユーザーがアウトラインを承認したら、ブログ記事フォルダ内の `OUTLINE.md` に保存する。

2. アウトラインが保存されたことを確認する。

### Step 5: アウトラインのコミット（git リポジトリの場合）

1. カレントディレクトリが git リポジトリかどうか確認する。

2. はいの場合:
   - 新しいファイル（ブログ記事フォルダ、resources、OUTLINE.md）をステージング
   - 次のメッセージでコミットを作成: `docs: Add outline for blog post - [topic-name]`
   - リモートへプッシュ

3. git リポジトリでない場合は、このステップをスキップしユーザーに伝える。

### Step 6: 下書き作成

1. 承認されたアウトラインに基づき、ブログ記事の下書き全文を作成する。

2. OUTLINE.md の構造に厳密に従う。

3. 含めるもの:
   - フック付きの魅力的な導入
   - 明確なセクション見出し
   - リサーチからの裏付けとなる証拠と例
   - セクション間の滑らかな遷移
   - テイクアウェイのある力強い結論
   - **Citations**: すべての比較、統計、データポイント、事実主張は元のソースを必ず引用すること

4. 下書きをブログ記事フォルダ内に `draft-v0.1.md` として保存する。

5. フォーマット:
   ```markdown
   # [Blog Post Title]

   *[Optional: subtitle or tagline]*

   [インライン引用付きの本文...]

   ---

   ## References
   - [1] Source 1 Title - URL or Citation
   - [2] Source 2 Title - URL or Citation
   - [3] Source 3 Title - URL or Citation
   ```

6. **引用要件**:
   - すべてのデータポイント、統計、比較にはインライン引用を必ず付ける
   - [1]、[2] などの番号引用、または [Source Name] のような名前付き引用を使用
   - 引用を末尾の References セクションへリンクする
   - 例: "Studies show that 65% of developers prefer TypeScript [1]"
   - 例: "React outperforms Vue in rendering speed by 20% [React Benchmarks 2024]"

### Step 7: 下書きのコミット（git リポジトリの場合）

1. git リポジトリかどうか確認する。

2. はいの場合:
   - 下書きファイルをステージング
   - 次のメッセージでコミットを作成: `docs: Add draft v0.1 for blog post - [topic-name]`
   - リモートへプッシュ

3. git リポジトリでない場合は、スキップしてユーザーに伝える。

### Step 8: レビュー用に下書きを提示

1. 下書きの内容をユーザーに提示する。

2. フィードバックを求める:
   - 全体の印象は？
   - 拡張または削減が必要なセクションは？
   - トーン調整は必要か？
   - 不足している情報は？
   - 具体的な編集や書き直しは？

3. **ユーザー応答を待つ。**

### Step 9: 反復または最終化

**ユーザーが変更を要求した場合:**
1. すべての要望を記録する
2. 以下の調整を加えてステップ 6 へ戻る:
   - バージョン番号を増加（v0.2、v0.3 など）
   - すべてのフィードバックを反映
   - `draft-v[X.Y].md` として保存
   - ステップ 7-8 を繰り返す

**ユーザーが承認した場合:**
1. 最終下書きのバージョンを確認
2. ユーザーが要求すれば任意で `final.md` にリネーム
3. ブログ記事作成プロセスを要約:
   - 作成したバージョンの総数
   - バージョン間の主要な変更
   - 最終ワード数
   - 作成したファイル

## バージョン追跡

すべての下書きは段階的なバージョン番号付きで保持する:
- `draft-v0.1.md` - 初回下書き
- `draft-v0.2.md` - 1 回目のフィードバック反映後
- `draft-v0.3.md` - 2 回目のフィードバック反映後
- など

これによりブログ記事の進化を追跡し、必要に応じて差し戻すことができる。

## 出力ファイル構造

```
blog-posts/
└── YYYY-MM-DD-topic-name/
    ├── resources/
    │   ├── source-1-name.md
    │   ├── source-2-name.md
    │   └── ...
    ├── OUTLINE.md
    ├── draft-v0.1.md
    ├── draft-v0.2.md (反復した場合)
    └── draft-v0.3.md (さらに反復した場合)
```

## 品質のためのヒント

- **Hook**: 質問、意外な事実、共感できるシナリオで始める
- **Flow**: 各段落は次の段落と接続させる
- **Evidence**: リサーチデータで主張を裏付ける
- **Citations**: 以下については必ずソースを引用する:
  - すべての統計とデータポイント（例: "According to [Source], 75% of..."）
  - 製品、サービス、アプローチ間の比較（例: "X performs 2x faster than Y [Source]"）
  - 市場トレンド、リサーチ結果、ベンチマークについての事実主張
  - 形式: [Source Name] または [Author, Year] のインライン引用を使用
- **Voice**: 全体を通じて一貫したトーンを保つ
- **Length**: 目標ワード数を尊重
- **Readability**: 短い段落、適切な箇所での箇条書きを使用
- **CTA**: 明確な CTA または考えさせる問いで終える

## 注意事項

- 指定されたチェックポイントでは必ずユーザー承認を待つ
- 履歴のためすべての下書きバージョンを保持する
- URL が提供された場合は最新情報のためウェブ検索を使用する
- リソースが不十分な場合はユーザーに追加を求めるか、追加リサーチを提案する
- 対象読者（技術系、一般、ビジネスなど）に応じてトーンを適応させる
