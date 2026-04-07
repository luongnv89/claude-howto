# 测试指南

本文档说明 Claude How To 的测试基础设施。

## 概览

项目使用 GitHub Actions 在每次 push 和 pull request 时自动运行测试。测试覆盖：

- **单元测试**：使用 pytest 的 Python 测试
- **代码质量**：使用 Ruff 做 lint 和格式化
- **安全**：使用 Bandit 做漏洞扫描
- **类型检查**：使用 mypy 做静态类型分析
- **构建验证**：EPUB 生成测试

## 在本地运行测试

### 前置条件

```bash
# 安装 uv（快速 Python 包管理器）
pip install uv

# 或者在 macOS 上使用 Homebrew
brew install uv
```

### 配置环境

```bash
# 克隆仓库
git clone https://github.com/luongnv89/claude-howto.git
cd claude-howto

# 创建虚拟环境
uv venv

# 激活虚拟环境
source .venv/bin/activate  # macOS/Linux
# 或者
.venv\Scripts\activate     # Windows

# 安装开发依赖
uv pip install -r requirements-dev.txt
```

### 运行测试

```bash
# 运行所有单元测试
pytest scripts/tests/ -v

# 运行带覆盖率的测试
pytest scripts/tests/ -v --cov=scripts --cov-report=html

# 运行指定测试文件
pytest scripts/tests/test_build_epub.py -v

# 运行指定测试函数
pytest scripts/tests/test_build_epub.py::test_function_name -v

# 以 watch 模式运行测试（需要 pytest-watch）
ptw scripts/tests/
```

### 运行 lint

```bash
# 检查代码格式
ruff format --check scripts/

# 自动修复格式问题
ruff format scripts/

# 运行 lint
ruff check scripts/

# 自动修复 lint 问题
ruff check --fix scripts/
```

### 运行安全扫描

```bash
# 运行 Bandit 安全扫描
bandit -c pyproject.toml -r scripts/ --exclude scripts/tests/

# 生成 JSON 报告
bandit -c pyproject.toml -r scripts/ --exclude scripts/tests/ -f json -o bandit-report.json
```

### 运行类型检查

```bash
# 使用 mypy 检查类型
mypy scripts/ --ignore-missing-imports --no-implicit-optional
```

## GitHub Actions 工作流

### 触发条件

- 推送到 `main` 或 `develop` 分支（当 `scripts` 有变更时）
- 向 `main` 提交 Pull Request（当 `scripts` 有变更时）
- 手动触发 workflow

### 作业

#### 1. 单元测试（pytest）

- **运行环境**：Ubuntu latest
- **Python 版本**：3.10、3.11、3.12
- **执行内容**：
  - 从 `requirements-dev.txt` 安装依赖
  - 运行 pytest 并生成覆盖率报告
  - 将覆盖率上传到 Codecov
  - 归档测试结果和 HTML 覆盖率报告

**结果**：如果任何测试失败，工作流失败（关键）

#### 2. 代码质量（Ruff）

- **运行环境**：Ubuntu latest
- **Python 版本**：3.11
- **执行内容**：
  - 使用 `ruff format` 检查格式
  - 使用 `ruff check` 运行 lint
  - 报告问题，但不会让整个工作流失败

**结果**：非阻塞（仅警告）

#### 3. 安全扫描（Bandit）

- **运行环境**：Ubuntu latest
- **Python 版本**：3.11
- **执行内容**：
  - 扫描安全漏洞
  - 生成 JSON 报告
  - 将报告作为 artifact 上传

**结果**：非阻塞（仅警告）

#### 4. 类型检查（mypy）

- **运行环境**：Ubuntu latest
- **Python 版本**：3.11
- **执行内容**：
  - 执行静态类型分析
  - 报告类型不匹配
  - 帮助尽早发现 bug

**结果**：非阻塞（仅警告）

#### 5. 构建 EPUB

- **运行环境**：Ubuntu latest
- **依赖**：pytest、lint、安全扫描（都必须通过）
- **执行内容**：
  - 使用 `scripts/build_epub.py` 构建 EPUB
  - 验证 EPUB 是否成功生成
  - 将 EPUB 作为 artifact 上传

**结果**：如果构建失败，工作流失败（关键）

#### 6. 总结

- **运行环境**：Ubuntu latest
- **依赖**：所有其他作业
- **执行内容**：
  - 生成工作流总结
  - 列出所有 artifacts
  - 汇总总体状态

## 编写测试

### 测试结构

测试应放在 `scripts/tests/` 中，文件名形如 `test_*.py`：

```python
# scripts/tests/test_example.py
import pytest
from scripts.example_module import some_function

def test_basic_functionality():
    """测试 some_function 是否正常工作。"""
    result = some_function("input")
    assert result == "expected_output"

def test_error_handling():
    """测试 some_function 是否能优雅处理错误。"""
    with pytest.raises(ValueError):
        some_function("invalid_input")

@pytest.mark.asyncio
async def test_async_function():
    """测试异步函数。"""
    result = await async_function()
    assert result is not None
```

### 测试最佳实践

- **使用有描述性的名称**：例如 `test_function_returns_correct_value()`
- **尽量每个测试只做一个断言**：更容易排查失败原因
- **使用 fixture** 复用初始化逻辑：见 `scripts/tests/conftest.py`
- **Mock 外部服务**：使用 `unittest.mock` 或 `pytest-mock`
- **测试边界情况**：空输入、None 值、错误情况
- **保持测试快速**：避免 `sleep()` 和外部 I/O
- **使用 pytest 标记**：例如 `@pytest.mark.slow` 标记慢测试

### Fixtures

常用 fixture 定义在 `scripts/tests/conftest.py`：

```python
# 在测试中使用 fixture
def test_something(tmp_path):
    """tmp_path fixture 提供临时目录。"""
    test_file = tmp_path / "test.txt"
    test_file.write_text("content")
    assert test_file.read_text() == "content"
```

## 覆盖率报告

### 本地覆盖率

```bash
# 生成覆盖率报告
pytest scripts/tests/ --cov=scripts --cov-report=html

# 在浏览器中打开覆盖率报告
open htmlcov/index.html
```

### 覆盖率目标

- **最低覆盖率**：80%
- **分支覆盖率**：启用
- **重点区域**：核心功能和错误路径

## Pre-commit Hooks

项目使用 pre-commit hooks 在每次提交前自动运行检查：

```bash
# 安装 pre-commit hooks
pre-commit install

# 手动运行 hooks
pre-commit run --all-files

# 跳过某次提交的 hooks（不推荐）
git commit --no-verify
```

在 `.pre-commit-config.yaml` 中配置的 hooks：
- Ruff formatter
- Ruff linter
- Bandit security scanner
- YAML validation
- 文件大小检查
- 合并冲突检测

## 排障

### 本地测试通过，但 CI 失败

常见原因：
1. **Python 版本差异**：CI 使用 3.10、3.11、3.12
2. **依赖缺失**：更新 `requirements-dev.txt`
3. **平台差异**：路径分隔符、环境变量
4. **测试不稳定**：依赖时序或执行顺序的测试

解决方案：
```bash
# 使用相同的 Python 版本测试
uv python install 3.10 3.11 3.12

# 使用干净环境测试
rm -rf .venv
uv venv
uv pip install -r requirements-dev.txt
pytest scripts/tests/
```

### Bandit 报告误报

某些安全警告可能是误报。可在 `pyproject.toml` 中配置：

```toml
[tool.bandit]
exclude_dirs = ["scripts/tests"]
skips = ["B101"]  # 跳过 assert_used 警告
```

### 类型检查太严格

对特定文件放宽类型检查：

```python
# 放在文件顶部
# type: ignore

# 或者针对特定行
some_dynamic_code()  # type: ignore
```

## 持续集成最佳实践

1. **保持测试快速**：每个测试最好在 1 秒内完成
2. **不要测试外部 API**：用 mock 替代外部服务
3. **测试要隔离**：每个测试都应独立
4. **断言要清晰**：写 `assert x == 5`，不要写 `assert x`
5. **处理异步测试**：使用 `@pytest.mark.asyncio`
6. **生成报告**：覆盖率、安全扫描、类型检查

## 资源

- [pytest Documentation](https://docs.pytest.org/)
- [Ruff Documentation](https://docs.astral.sh/ruff/)
- [Bandit Documentation](https://bandit.readthedocs.io/)
- [mypy Documentation](https://mypy.readthedocs.io/)
- [GitHub Actions Documentation](https://docs.github.com/en/actions)

## 贡献测试

提交 PR 时：

1. **为新功能编写测试**
2. **本地运行测试**：`pytest scripts/tests/ -v`
3. **检查覆盖率**：`pytest scripts/tests/ --cov=scripts`
4. **运行 lint**：`ruff check scripts/`
5. **安全扫描**：`bandit -r scripts/ --exclude scripts/tests/`
6. **如果测试变化，更新文档**

所有 PR 都必须包含测试！🧪

---

如果你对测试有问题或疑问，请在 GitHub 上创建 issue 或 discussion。
