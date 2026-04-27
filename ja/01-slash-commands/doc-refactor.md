<!-- i18n-source: 01-slash-commands/doc-refactor.md -->
<!-- i18n-source-sha: 7f2e773 -->
<!-- i18n-date: 2026-04-27 -->

---
name: Documentation Refactor
description: プロジェクトドキュメントを再構成して明瞭性とアクセシビリティを高める
tags: documentation, refactoring, organization
---

# ドキュメントリファクタリング

プロジェクトの種類に合わせてドキュメント構造をリファクタリングする:

1. **プロジェクトを分析**: 種類（ライブラリ／API／Web アプリ／CLI／マイクロサービス）、アーキテクチャ、ユーザーペルソナを特定する
2. **ドキュメントを集約**: 技術ドキュメントを `docs/` に移動し、適切な相互参照を整える
3. **ルート README.md**: 概要、クイックスタート、モジュール／コンポーネントのサマリ、ライセンス、連絡先を含むエントリーポイントとして整理する
4. **コンポーネント別ドキュメント**: モジュール／パッケージ／サービス単位の README ファイルを追加し、セットアップとテスト手順を記載する
5. **`docs/` を関連カテゴリで整理する**:
   - Architecture、API Reference、Database、Design、Troubleshooting、Deployment、Contributing（プロジェクトの必要に応じて調整）
6. **ガイドを作成する**（該当するものを選ぶ）:
   - User Guide: アプリケーションのエンドユーザー向けドキュメント
   - API Documentation: API のエンドポイント、認証、サンプル
   - Development Guide: セットアップ、テスト、コントリビューションのワークフロー
   - Deployment Guide: サービス／アプリの本番デプロイ
7. **すべての図に Mermaid を使う**（アーキテクチャ、フロー、スキーマ）

ドキュメントは簡潔に、流し読みしやすく、プロジェクトの種類に即した内容に保つ。

---
**Last Updated**: April 9, 2026
