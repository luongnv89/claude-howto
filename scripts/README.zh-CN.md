<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# EPUB 构建脚本

从 Claude How-To 的 markdown 文件构建 EPUB 电子书。

## 功能

- 按目录结构组织章节（01-slash-commands、02-memory 等）
- 通过 Kroki.io API 将 Mermaid 图渲染为 PNG
- 异步并发拉取（并行渲染所有图）
- 使用项目 logo 生成封面图
- 将内部 markdown 链接转换为 EPUB 章节引用
- 严格错误模式：任一图渲染失败即构建失败

## 环境要求

- Python 3.10+
- [uv](https://github.com/astral-sh/uv)
- 可访问网络（用于 Mermaid 渲染）

## 快速开始

```bash
# 最简单方式：uv 自动处理依赖
uv run scripts/build_epub.py
```

## 开发环境

```bash
# 创建虚拟环境
uv venv

# 激活并安装依赖
source .venv/bin/activate
uv pip install -r requirements-dev.txt

# 运行测试
pytest scripts/tests/ -v

# 运行脚本
python scripts/build_epub.py
```

## 命令行参数

```text
usage: build_epub.py [-h] [--root ROOT] [--output OUTPUT] [--verbose]
                     [--timeout TIMEOUT] [--max-concurrent MAX_CONCURRENT]

options:
  -h, --help            show this help message and exit
  --root, -r ROOT       Root directory (default: repo root)
  --output, -o OUTPUT   Output path (default: claude-howto-guide.epub)
  --verbose, -v         Enable verbose logging
  --timeout TIMEOUT     API timeout in seconds (default: 30)
  --max-concurrent N    Max concurrent requests (default: 10)
```

## 示例

```bash
# 输出详细日志
uv run scripts/build_epub.py --verbose

# 自定义输出位置
uv run scripts/build_epub.py --output ~/Desktop/claude-guide.epub

# 限制并发请求（遇到限流时）
uv run scripts/build_epub.py --max-concurrent 5
```

## 输出结果

会在仓库根目录生成 `claude-howto-guide.epub`。

EPUB 包含：
- 使用项目 logo 的封面
- 分层目录结构
- 所有 markdown 内容转换后的 EPUB 兼容 HTML
- Mermaid 图对应 PNG 图片

## 运行测试

```bash
# 使用虚拟环境
source .venv/bin/activate
pytest scripts/tests/ -v

# 或直接使用 uv
uv run --with pytest --with pytest-asyncio \
    --with ebooklib --with markdown --with beautifulsoup4 \
    --with httpx --with pillow --with tenacity \
    pytest scripts/tests/ -v
```

## 依赖

通过 PEP 723 行内脚本元数据管理：

| Package | Purpose |
|---------|---------|
| `ebooklib` | EPUB 生成 |
| `markdown` | Markdown 转 HTML |
| `beautifulsoup4` | HTML 解析 |
| `httpx` | 异步 HTTP 客户端 |
| `pillow` | 封面图生成 |
| `tenacity` | 重试机制 |

## 故障排查

**网络错误导致构建失败**：检查网络连接与 Kroki.io 状态，可尝试 `--timeout 60`。

**请求被限流**：通过 `--max-concurrent 3` 降低并发数。

**缺少 logo**：若找不到 `claude-howto-logo.png`，脚本会退化为仅文本封面。
