# 脚本

用于生成 EPUB 电子书和管理 Kimi Code HowTo 指南内容的脚本集合。

## EPUB 生成

主要脚本是 `build_epub.py`，它将整个指南编译成可下载的 EPUB 电子书。

### 用法

```bash
# 生成 EPUB
uv run scripts/build_epub.py

# 输出
# Creates: claude-howto-guide.epub
```

### 功能

- 将所有 Markdown 内容编译为单个 EPUB
- 包含渲染的 Mermaid 图表
- 保持导航结构
- 优化离线阅读

## 要求

- Python 3.10+
- uv 包管理器
- 依赖项列在 `pyproject.toml` 中

## 安装

```bash
# 安装开发依赖
uv pip install -r requirements-dev.txt
```

## 测试

```bash
# 运行测试
pytest scripts/tests/ -v

# 运行带覆盖率的测试
pytest scripts/tests/ -v --cov=scripts --cov-report=html
```

## 额外工具

此文件夹中的其他实用程序：
- 验证脚本
- 构建工具
- 维护脚本

有关详细使用信息，请参阅主指南。
