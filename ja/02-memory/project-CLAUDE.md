<!-- i18n-source: 02-memory/project-CLAUDE.md -->
<!-- i18n-source-sha: 7f2e773 -->
<!-- i18n-date: 2026-04-27 -->

# プロジェクト設定

## プロジェクト概要
- **名称**: E コマースプラットフォーム
- **技術スタック**: Node.js、PostgreSQL、React 18、Docker
- **チーム規模**: 開発者 5 名
- **デッドライン**: 2025 年第 4 四半期

## アーキテクチャ
@docs/architecture.md
@docs/api-standards.md
@docs/database-schema.md

## 開発標準

### コードスタイル
- フォーマットには Prettier を使う
- ESLint（airbnb config）を使う
- 1 行の最大長: 100 文字
- インデント: スペース 2 個

### 命名規則
- **ファイル**: kebab-case（user-controller.js）
- **クラス**: PascalCase（UserService）
- **関数／変数**: camelCase（getUserById）
- **定数**: UPPER_SNAKE_CASE（API_BASE_URL）
- **データベーステーブル**: snake_case（user_accounts）

### Git ワークフロー
- ブランチ名: `feature/description` または `fix/description`
- コミットメッセージ: Conventional Commits に従う
- マージ前に PR が必要
- すべての CI/CD チェックを通す
- 最低 1 名の承認が必要

### テスト要件
- コードカバレッジ最低 80%
- すべての主要パスにテストが必要
- ユニットテストには Jest を使う
- E2E テストには Cypress を使う
- テストファイル名: `*.test.ts` または `*.spec.ts`

### API 標準
- RESTful エンドポイントのみ
- リクエスト／レスポンスは JSON
- HTTP ステータスコードを正しく使う
- API はバージョン付きエンドポイント: `/api/v1/`
- 全エンドポイントに例付きドキュメントを用意する

### データベース
- スキーマ変更にはマイグレーションを使う
- 認証情報をハードコードしない
- コネクションプーリングを使う
- 開発環境ではクエリログを有効化する
- 定期的なバックアップを必須とする

### デプロイ
- Docker ベースのデプロイ
- Kubernetes によるオーケストレーション
- Blue-Green デプロイ戦略
- 失敗時は自動ロールバック
- データベースマイグレーションはデプロイ前に実行する

## よく使うコマンド

| コマンド | 用途 |
|---------|------|
| `npm run dev` | 開発サーバを起動 |
| `npm test` | テストスイートを実行 |
| `npm run lint` | コードスタイルを確認 |
| `npm run build` | 本番向けビルド |
| `npm run migrate` | データベースマイグレーションを実行 |

## チーム連絡先
- Tech Lead: Sarah Chen (@sarah.chen)
- Product Manager: Mike Johnson (@mike.j)
- DevOps: Alex Kim (@alex.k)

## 既知の問題と回避策
- ピーク時、PostgreSQL のコネクションプールが 20 に制限される
- 回避策: クエリのキューイングを実装する
- Safari 14 で async generator の互換性問題
- 回避策: Babel トランスパイラを使う

## 関連プロジェクト
- Analytics Dashboard: `/projects/analytics`
- Mobile App: `/projects/mobile`
- Admin Panel: `/projects/admin`

---
**Last Updated**: April 9, 2026
