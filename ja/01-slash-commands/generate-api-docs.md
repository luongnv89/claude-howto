<!-- i18n-source: 01-slash-commands/generate-api-docs.md -->
<!-- i18n-source-sha: 7f2e773 -->
<!-- i18n-date: 2026-04-27 -->

---
description: ソースコードから網羅的な API ドキュメントを生成する
---

# API ドキュメント生成

次の手順で API ドキュメントを生成する:

1. `/src/api/` 配下の全ファイルをスキャンする
2. 関数シグネチャと JSDoc コメントを抽出する
3. エンドポイント／モジュール単位で整理する
4. サンプル付きの Markdown を作成する
5. リクエスト／レスポンスのスキーマを含める
6. エラーに関するドキュメントを追加する

出力形式:
- `/docs/api.md` に Markdown ファイルとして出力
- 全エンドポイントについて curl のサンプルを含める
- TypeScript の型定義を追加する

---
**Last Updated**: April 9, 2026
