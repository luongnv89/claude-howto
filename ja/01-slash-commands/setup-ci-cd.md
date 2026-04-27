<!-- i18n-source: 01-slash-commands/setup-ci-cd.md -->
<!-- i18n-source-sha: 7f2e773 -->
<!-- i18n-date: 2026-04-27 -->

---
name: Setup CI/CD Pipeline
description: 品質保証のための pre-commit フックと GitHub Actions を導入する
tags: ci-cd, devops, automation
---

# CI/CD パイプラインのセットアップ

プロジェクトの種類に応じて、包括的な DevOps の品質ゲートを導入する:

1. **プロジェクトを分析**: 言語、フレームワーク、ビルドシステム、既存ツールを検出する
2. **言語別ツールで pre-commit フックを設定する**:
   - フォーマッタ: Prettier／Black／gofmt／rustfmt など
   - リンタ: ESLint／Ruff／golangci-lint／Clippy など
   - セキュリティ: Bandit／gosec／cargo-audit／npm audit など
   - 型チェック: TypeScript／mypy／flow（該当する場合）
   - テスト: 関連するテストスイートを実行する
3. **GitHub Actions ワークフローを作成する**（.github/workflows/）:
   - push／PR 時に pre-commit と同じチェックを実行する
   - 複数バージョン／プラットフォームのマトリクス（該当する場合）
   - ビルドとテストの検証
   - デプロイ手順（必要な場合）
4. **パイプラインを検証する**: ローカルで動作確認し、テスト用 PR を作成し、全チェックの通過を確認する

無料・オープンソースのツールを使う。既存の設定を尊重する。実行時間は短く保つ。

---
**Last Updated**: April 9, 2026
