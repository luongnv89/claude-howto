<!-- i18n-source: 01-slash-commands/unit-test-expand.md -->
<!-- i18n-source-sha: 7f2e773 -->
<!-- i18n-date: 2026-04-27 -->

---
name: Expand Unit Tests
description: 未テストの分岐やエッジケースを狙ってテストカバレッジを高める
tags: testing, coverage, unit-tests
---

# ユニットテストの拡充

プロジェクトのテストフレームワークに合わせて、既存のユニットテストを拡充する:

1. **カバレッジを分析**: カバレッジレポートを実行し、未テストの分岐、エッジケース、低カバレッジ領域を特定する
2. **ギャップを特定**: コードを見直し、論理分岐、エラー経路、境界条件、null／空入力を確認する
3. **プロジェクトのフレームワークでテストを書く**:
   - Jest／Vitest／Mocha（JavaScript／TypeScript）
   - pytest／unittest（Python）
   - Go testing／testify（Go）
   - Rust のテストフレームワーク（Rust）
4. **特定のシナリオを狙う**:
   - エラーハンドリングと例外
   - 境界値（最小／最大、空、null）
   - エッジケース・コーナーケース
   - 状態遷移と副作用
5. **改善を確認**: 再度カバレッジを計測し、計測可能な向上を確認する

新しく追加したテストコードのみを提示する。既存のテストパターンと命名規則に従う。

---
**Last Updated**: April 9, 2026
