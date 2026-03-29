# 測試指南

本文件描述 Claude How To 的測試基礎設施。

## 概覽

本專案使用 GitHub Actions 在每次推送和 pull request 時自動執行測試。測試涵蓋：

- **單元測試**：使用 pytest 的 Python 測試
- **程式碼品質**：使用 Ruff 進行 linting 和格式化
- **安全性**：使用 Bandit 進行漏洞掃描
- **型別檢查**：使用 mypy 進行靜態型別分析
- **建置驗證**：EPUB 產生測試

## 本機執行測試

### 先決條件

```bash
# 安裝 uv（快速 Python 套件管理器）
pip install uv

# 或在 macOS 上使用 Homebrew
brew install uv
```

### 設定環境

```bash
# 複製儲存庫
git clone https://github.com/luongnv89/claude-howto.git
cd claude-howto

# 建立虛擬環境
uv venv

# 啟動
source .venv/bin/activate  # macOS/Linux
# 或
.venv\Scripts\activate     # Windows

# 安裝開發依賴項
uv pip install -r requirements-dev.txt
```

### 執行測試

```bash
# 執行所有單元測試
pytest scripts/tests/ -v

# 執行測試並附帶覆蓋率
pytest scripts/tests/ -v --cov=scripts --cov-report=html

# 執行特定測試檔案
pytest scripts/tests/test_build_epub.py -v

# 執行特定測試函式
pytest scripts/tests/test_build_epub.py::test_function_name -v

# 以監視模式執行測試（需要 pytest-watch）
ptw scripts/tests/
```

### 執行 Linting

```bash
# 檢查程式碼格式
ruff format --check scripts/

# 自動修復格式問題
ruff format scripts/

# 執行 linter
ruff check scripts/

# 自動修復 linter 問題
ruff check --fix scripts/
```

### 執行安全掃描

```bash
# 執行 Bandit 安全掃描
bandit -c pyproject.toml -r scripts/ --exclude scripts/tests/

# 產生 JSON 報告
bandit -c pyproject.toml -r scripts/ --exclude scripts/tests/ -f json -o bandit-report.json
```

### 執行型別檢查

```bash
# 使用 mypy 檢查型別
mypy scripts/ --ignore-missing-imports --no-implicit-optional
```

## GitHub Actions 工作流程

### 觸發條件

- **推送**到 `main` 或 `develop` 分支（當 scripts 有變更時）
- **Pull Request** 到 `main`（當 scripts 有變更時）
- 手動觸發工作流程

### 工作項目

#### 1. 單元測試（pytest）

- **執行環境**：Ubuntu 最新版
- **Python 版本**：3.10、3.11、3.12
- **執行內容**：
  - 從 `requirements-dev.txt` 安裝依賴項
  - 執行 pytest 並附帶覆蓋率報告
  - 上傳覆蓋率至 Codecov
  - 歸檔測試結果和覆蓋率 HTML

**結果**：若任何測試失敗，工作流程失敗（關鍵）

#### 2. 程式碼品質（Ruff）

- **執行環境**：Ubuntu 最新版
- **Python 版本**：3.11
- **執行內容**：
  - 使用 `ruff format` 檢查程式碼格式
  - 使用 `ruff check` 執行 linter
  - 回報問題但不使工作流程失敗

**結果**：非阻擋性（僅警告）

#### 3. 安全掃描（Bandit）

- **執行環境**：Ubuntu 最新版
- **Python 版本**：3.11
- **執行內容**：
  - 掃描安全漏洞
  - 產生 JSON 報告
  - 上傳報告作為 artifact

**結果**：非阻擋性（僅警告）

#### 4. 型別檢查（mypy）

- **執行環境**：Ubuntu 最新版
- **Python 版本**：3.11
- **執行內容**：
  - 執行靜態型別分析
  - 回報型別不匹配
  - 幫助及早發現錯誤

**結果**：非阻擋性（僅警告）

#### 5. 建置 EPUB

- **執行環境**：Ubuntu 最新版
- **依賴**：pytest、lint、security（全部須通過）
- **執行內容**：
  - 使用 `scripts/build_epub.py` 建置 EPUB 檔案
  - 驗證 EPUB 成功建立
  - 上傳 EPUB 作為 artifact

**結果**：若建置失敗，工作流程失敗（關鍵）

#### 6. 摘要

- **執行環境**：Ubuntu 最新版
- **依賴**：所有其他工作項目
- **執行內容**：
  - 產生工作流程摘要
  - 列出所有 artifacts
  - 回報總體狀態

## 撰寫測試

### 測試結構

測試應放在 `scripts/tests/` 中，檔名格式為 `test_*.py`：

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

### 測試最佳實踐

- **使用描述性名稱**：`test_function_returns_correct_value()`
- **每個測試一個斷言**（盡可能）：更容易除錯失敗
- **使用 fixtures** 進行可重用的設定：見 `scripts/tests/conftest.py`
- **模擬外部服務**：使用 `unittest.mock` 或 `pytest-mock`
- **測試邊界情況**：空輸入、None 值、錯誤
- **保持測試快速**：避免 sleep() 和外部 I/O
- **使用 pytest markers**：`@pytest.mark.slow` 用於慢速測試

### Fixtures

常用 fixtures 定義在 `scripts/tests/conftest.py`：

```python
# 在測試中使用 fixtures
def test_something(tmp_path):
    """tmp_path fixture provides temporary directory."""
    test_file = tmp_path / "test.txt"
    test_file.write_text("content")
    assert test_file.read_text() == "content"
```

## 覆蓋率報告

### 本機覆蓋率

```bash
# 產生覆蓋率報告
pytest scripts/tests/ --cov=scripts --cov-report=html

# 在瀏覽器中開啟覆蓋率報告
open htmlcov/index.html
```

### 覆蓋率目標

- **最低覆蓋率**：80%
- **分支覆蓋率**：已啟用
- **重點領域**：核心功能和錯誤路徑

## Pre-commit Hooks

本專案使用 pre-commit hooks 在提交前自動執行檢查：

```bash
# 安裝 pre-commit hooks
pre-commit install

# 手動執行 hooks
pre-commit run --all-files

# 跳過 hooks 進行提交（不建議）
git commit --no-verify
```

在 `.pre-commit-config.yaml` 中設定的 hooks：
- Ruff 格式化工具
- Ruff linter
- Bandit 安全掃描器
- YAML 驗證
- 檔案大小檢查
- 合併衝突偵測

## 疑難排解

### 測試在本機通過但在 CI 失敗

常見原因：
1. **Python 版本差異**：CI 使用 3.10、3.11、3.12
2. **缺少依賴項**：更新 `requirements-dev.txt`
3. **平台差異**：路徑分隔符、環境變數
4. **不穩定的測試**：依賴時序或順序的測試

解決方案：
```bash
# 使用相同的 Python 版本測試
uv python install 3.10 3.11 3.12

# 使用乾淨的環境測試
rm -rf .venv
uv venv
uv pip install -r requirements-dev.txt
pytest scripts/tests/
```

### Bandit 回報誤報

部分安全警告可能是誤報。在 `pyproject.toml` 中設定：

```toml
[tool.bandit]
exclude_dirs = ["scripts/tests"]
skips = ["B101"]  # 跳過 assert_used 警告
```

### 型別檢查過於嚴格

放寬特定檔案的型別檢查：

```python
# 在檔案頂部新增
# type: ignore

# 或針對特定行
some_dynamic_code()  # type: ignore
```

## 持續整合最佳實踐

1. **保持測試快速**：每個測試應在 <1 秒內完成
2. **不要測試外部 API**：模擬外部服務
3. **隔離測試**：每個測試應獨立
4. **使用清晰的斷言**：`assert x == 5` 而非 `assert x`
5. **處理非同步測試**：使用 `@pytest.mark.asyncio`
6. **產生報告**：覆蓋率、安全性、型別檢查

## 資源

- [pytest 文件](https://docs.pytest.org/)
- [Ruff 文件](https://docs.astral.sh/ruff/)
- [Bandit 文件](https://bandit.readthedocs.io/)
- [mypy 文件](https://mypy.readthedocs.io/)
- [GitHub Actions 文件](https://docs.github.com/en/actions)

## 貢獻測試

提交 PR 時：

1. **為新功能撰寫測試**
2. **在本機執行測試**：`pytest scripts/tests/ -v`
3. **檢查覆蓋率**：`pytest scripts/tests/ --cov=scripts`
4. **執行 linting**：`ruff check scripts/`
5. **安全掃描**：`bandit -r scripts/ --exclude scripts/tests/`
6. 若測試有變更，**更新文件**

所有 PR 都需要測試！

---

如有測試相關問題，請開啟 GitHub issue 或 discussion。
