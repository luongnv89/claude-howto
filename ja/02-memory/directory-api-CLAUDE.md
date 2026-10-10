<!-- i18n-source: 02-memory/directory-api-CLAUDE.md -->
<!-- i18n-source-sha: 7f2e773 -->
<!-- i18n-date: 2026-04-27 -->

# API モジュール標準

このファイルは /src/api/ 配下のすべてに対し、ルートの CLAUDE.md を補完する。メモリファイルは
連結されるものであり、上書きされるわけではない。ルートの CLAUDE.md は引き続き適用され、
Claude Code はこのサブツリー内のファイルを読む、書く、または編集するときに本ファイルをオンデマンドで読み込む。

## API 固有の標準

### リクエスト検証
- スキーマ検証には Zod を使う
- 入力は必ず検証する
- 検証エラー時は 400 を返す
- フィールド単位のエラー詳細を含める

### 認証
- すべてのエンドポイントで JWT トークンを必須とする
- トークンは Authorization ヘッダに付ける
- トークンの有効期限は 24 時間
- リフレッシュトークン機構を実装する

### レスポンス形式

すべてのレスポンスは次の構造に従う:

```json
{
  "success": true,
  "data": { /* actual data */ },
  "timestamp": "2025-11-06T10:30:00Z",
  "version": "1.0"
}
```

エラーレスポンス:
```json
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "User message",
    "details": { /* field errors */ }
  },
  "timestamp": "2025-11-06T10:30:00Z"
}
```

### ページネーション
- カーソルベースページネーションを使う（オフセット方式は使わない）
- `hasMore` の真偽値を含める
- 1 ページの最大サイズは 100 まで
- デフォルトのページサイズ: 20

### レート制限
- 認証済みユーザー: 1 時間あたり 1000 リクエスト
- 公開エンドポイント: 1 時間あたり 100 リクエスト
- 上限超過時は 429 を返す
- retry-after ヘッダを付ける

### キャッシュ
- セッションキャッシュには Redis を使う
- キャッシュ期間: デフォルト 5 分
- 書き込み操作時に無効化する
- キャッシュキーにリソース種別のタグを付ける

---
**最終更新**: 2026 年 10 月 10 日
**Claude Code バージョン**: 2.1.296
**Sources**:
- https://code.claude.com/docs/en/memory
- https://github.com/anthropics/claude-code/releases/tag/v2.1.288
- https://github.com/anthropics/claude-code/releases/tag/v2.1.293
