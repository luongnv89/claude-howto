<!-- i18n-source: .github/TESTING.md -->
<!-- i18n-source-sha: 728bd50 -->
<!-- i18n-date: 2026-04-27 -->
# テストガイド

本ドキュメントは Claude How To のテスト基盤について説明する。

## 概要

本プロジェクトは GitHub Actions を使い、すべてのプッシュとプルリクエストで自動的にテストを実行する。テスト内容：

- **ユニットテスト**: pytest による Python テスト
- **コード品質**: Ruff によるリンティングとフォーマット
- **セキュリティ**: Bandit による脆弱性スキャン
- **型チェック**: mypy による静的型解析
- **ビルド検証**: EPUB 生成テスト

## ローカルでテストを実行する

### 前提条件

```bash
# Install uv (fast Python package manager)
pip install uv

# Or on macOS with Homebrew
brew install uv
```

### 環境セットアップ

```bash
# Clone the repository
git clone https://github.com/luongnv89/claude-howto.git
cd claude-howto

# Create virtual environment
uv venv

# Activate it
source .venv/bin/activate  # macOS/Linux
# or
.venv\Scripts\activate     # Windows

# Install development dependencies
uv pip install -r requirements-dev.txt
```

### テスト実行

```bash
# Run all unit tests
pytest scripts/tests/ -v

# Run tests with coverage
pytest scripts/tests/ -v --cov=scripts --cov-report=html

# Run specific test file
pytest scripts/tests/test_build_epub.py -v

# Run specific test function
pytest scripts/tests/test_build_epub.py::test_function_name -v

# Run tests in watch mode (requires pytest-watch)
ptw scripts/tests/
```

### リンティング実行

```bash
# Check code formatting
ruff format --check scripts/

# Auto-fix formatting issues
ruff format scripts/

# Run linter
ruff check scripts/

# Auto-fix linter issues
ruff check --fix scripts/
```

### セキュリティスキャン実行

```bash
# Run Bandit security scan
bandit -c pyproject.toml -r scripts/ --exclude scripts/tests/

# Generate JSON report
bandit -c pyproject.toml -r scripts/ --exclude scripts/tests/ -f json -o bandit-report.json
```

### 型チェック実行

```bash
# Check types with mypy
mypy scripts/ --ignore-missing-imports --no-implicit-optional
```

## GitHub Actions ワークフロー

### トリガー

- `main` または `develop` ブランチへの **プッシュ**（scripts が変更されたとき）
- `main` への **プルリクエスト**（scripts が変更されたとき）
- 手動の workflow dispatch

### ジョブ

#### 1. ユニットテスト（pytest）

- **実行環境**: Ubuntu latest
- **Python バージョン**: 3.10、3.11、3.12
- **内容**:
  - `requirements-dev.txt` から依存関係をインストール
  - カバレッジレポート付きで pytest を実行
  - カバレッジを Codecov へアップロード
  - テスト結果とカバレッジ HTML をアーカイブ

**結果**: テストが 1 つでも失敗するとワークフロー失敗（クリティカル）

#### 2. コード品質（Ruff）

- **実行環境**: Ubuntu latest
- **Python バージョン**: 3.11
- **内容**:
  - `ruff format` でコードフォーマットを確認
  - `ruff check` でリンターを実行
  - 問題を報告するがワークフローは失敗させない

**結果**: ノンブロッキング（警告のみ）

#### 3. セキュリティスキャン（Bandit）

- **実行環境**: Ubuntu latest
- **Python バージョン**: 3.11
- **内容**:
  - セキュリティ脆弱性をスキャン
  - JSON レポートを生成
  - レポートをアーティファクトとしてアップロード

**結果**: ノンブロッキング（警告のみ）

#### 4. 型チェック（mypy）

- **実行環境**: Ubuntu latest
- **Python バージョン**: 3.11
- **内容**:
  - 静的型解析を実行
  - 型不一致を報告
  - 早期にバグを検出する助けになる

**結果**: ノンブロッキング（警告のみ）

#### 5. EPUB ビルド

- **実行環境**: Ubuntu latest
- **依存ジョブ**: pytest、lint、security（すべてパスする必要がある）
- **内容**:
  - `scripts/build_epub.py` を使い EPUB ファイルをビルド
  - EPUB が正常に生成されたか検証
  - EPUB をアーティファクトとしてアップロード

**結果**: ビルドが失敗するとワークフロー失敗（クリティカル）

#### 6. サマリ

- **実行環境**: Ubuntu latest
- **依存ジョブ**: 上記すべて
- **内容**:
  - ワークフローサマリを生成
  - すべてのアーティファクトを一覧表示
  - 全体ステータスを報告

## テストの書き方

### テスト構造

テストは `scripts/tests/` 配下に `test_*.py` のような名前で配置する：

```python
# scripts/tests/test_example.py
import pytest
from scripts.example_module import some_function

def test_basic_functionality():
    """Test that some_function works correctly."""
    result = some_function("input")
    assert result == "expected_output"

def test_error_handling():
    """Test that some_function handles errors gracefully."""
    with pytest.raises(ValueError):
        some_function("invalid_input")

@pytest.mark.asyncio
async def test_async_function():
    """Test async functions."""
    result = await async_function()
    assert result is not None
```

### テストのベストプラクティス

- **記述的な名前を使う**: `test_function_returns_correct_value()`
- **テスト 1 つにつきアサート 1 つ**（可能な限り）: 失敗のデバッグが容易
- **再利用可能なセットアップにフィクスチャを使う**: `scripts/tests/conftest.py` を参照
- **外部サービスをモックする**: `unittest.mock` または `pytest-mock` を使う
- **エッジケースをテストする**: 空入力、None 値、エラー
- **テストを高速に保つ**: sleep() と外部 I/O を避ける
- **pytest マーカーを使う**: 遅いテストには `@pytest.mark.slow`

### フィクスチャ

共通フィクスチャは `scripts/tests/conftest.py` に定義する：

```python
# Use fixtures in your tests
def test_something(tmp_path):
    """tmp_path fixture provides temporary directory."""
    test_file = tmp_path / "test.txt"
    test_file.write_text("content")
    assert test_file.read_text() == "content"
```

## カバレッジレポート

### ローカルカバレッジ

```bash
# Generate coverage report
pytest scripts/tests/ --cov=scripts --cov-report=html

# Open the coverage report in your browser
open htmlcov/index.html
```

### カバレッジ目標

- **最低カバレッジ**: 80%
- **ブランチカバレッジ**: 有効
- **重点領域**: コア機能とエラー経路

## pre-commit フック

本プロジェクトは pre-commit フックでコミット前に自動チェックを実行する：

```bash
# Install pre-commit hooks
pre-commit install

# Run hooks manually
pre-commit run --all-files

# Skip hooks for a commit (not recommended)
git commit --no-verify
```

`.pre-commit-config.yaml` で設定済みのフック：
- Ruff フォーマッター
- Ruff リンター
- Bandit セキュリティスキャナ
- YAML 検証
- ファイルサイズチェック
- マージコンフリクト検出

## トラブルシューティング

### ローカルでパスするが CI で失敗する

よくある原因：
1. **Python バージョンの違い**: CI は 3.10、3.11、3.12 を使う
2. **依存関係の不足**: `requirements-dev.txt` を更新する
3. **プラットフォーム差異**: パス区切り、環境変数
4. **不安定なテスト**: タイミングや順序に依存するテスト

解決策：
```bash
# Test with the same Python versions
uv python install 3.10 3.11 3.12

# Test with clean environment
rm -rf .venv
uv venv
uv pip install -r requirements-dev.txt
pytest scripts/tests/
```

### Bandit が誤検知を出す

セキュリティ警告の中には誤検知がある場合もある。`pyproject.toml` で設定する：

```toml
[tool.bandit]
exclude_dirs = ["scripts/tests"]
skips = ["B101"]  # Skip assert_used warning
```

### 型チェックが厳しすぎる

特定ファイルで型チェックを緩める：

```python
# Add at the top of file
# type: ignore

# Or for specific lines
some_dynamic_code()  # type: ignore
```

## 継続的インテグレーションのベストプラクティス

1. **テストを高速に保つ**: 各テストは 1 秒以内で完了する
2. **外部 API をテストしない**: 外部サービスをモックする
3. **隔離してテストする**: 各テストは独立しているべき
4. **明確なアサートを使う**: `assert x` ではなく `assert x == 5`
5. **非同期テストを扱う**: `@pytest.mark.asyncio` を使う
6. **レポートを生成する**: カバレッジ、セキュリティ、型チェック

## リソース

- [pytest Documentation](https://docs.pytest.org/)
- [Ruff Documentation](https://docs.astral.sh/ruff/)
- [Bandit Documentation](https://bandit.readthedocs.io/)
- [mypy Documentation](https://mypy.readthedocs.io/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)

## テストへの貢献

PR を提出する際：

1. 新機能には **テストを書く**
2. **ローカルでテストを実行**: `pytest scripts/tests/ -v`
3. **カバレッジを確認**: `pytest scripts/tests/ --cov=scripts`
4. **リンティングを実行**: `ruff check scripts/`
5. **セキュリティスキャン**: `bandit -r scripts/ --exclude scripts/tests/`
6. テストが変わる場合は **ドキュメントを更新**

すべての PR にはテストが必要！🧪

---

テストに関する質問や問題は、GitHub Issue または Discussion を開いてほしい。
