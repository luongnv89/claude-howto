<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../../resources/logos/claude-howto-logo.svg">
</picture>

# 构建脚本

这个目录包含两个生成器，把教程的 Markdown 文件转换成可分发的格式：

- [**EPUB 构建器**](#epub-构建脚本) — `build_epub.py`
- [**静态网站构建器**](#静态网站构建器) — `build_website.py`

两者都把 `.md` 文件当作唯一的事实来源——修改 Markdown 后重新运行
对应脚本即可重新生成输出。

---

# EPUB 构建脚本

把 Claude How-To 的 Markdown 文件构建成 EPUB 电子书。

## 功能

- 按目录结构组织章节（01-slash-commands、02-memory 等）
- 用 [Pele](https://github.com/obsidianmd/pele) 把 Mermaid 图表渲染成 SVG 图片（由 Node.js 运行的固定版本包）；CSS 变量会被展平为白底纯色，保证所有 EPUB 阅读器都能正常显示
- 相同的图表只渲染一次，结果在多个章节间复用
- 用项目 logo 生成封面图片
- 把内部 Markdown 链接转换成 EPUB 章节引用
- 严格错误模式——任何一个图表渲染失败都会使构建失败

## 需求

- Python 3.10+
- [uv](https://github.com/astral-sh/uv)
- `PATH` 中需要有 Node.js >= 20，用于渲染 Mermaid 图表。固定版本的 Pele 包在首次运行时下载（仅需联网一次），经 sha256 校验后缓存在 `scripts/.vendor-cache/pele/`

## 快速开始

最简单的方式是直接让 `uv` 帮你处理依赖：

```bash
uv run scripts/build_epub.py
```

## 开发环境

如果你要修改脚本本身，可以先创建虚拟环境，再安装开发依赖。

```bash
# 创建虚拟环境
uv venv

# 激活并安装依赖
source .venv/bin/activate
uv pip install -r scripts/requirements-dev.txt

# 运行测试
pytest scripts/tests/ -v

# 运行脚本
python scripts/build_epub.py
```

## 命令行选项

```
usage: build_epub.py [-h] [--root ROOT] [--output OUTPUT] [--verbose]
                     [--lang {en,vi,zh,ja,ko,fa}]

options:
  -h, --help            show this help message and exit
  --root, -r ROOT       Root directory (default: repo root)
  --output, -o OUTPUT   Output path (default: claude-howto-guide.epub)
  --verbose, -v         Enable verbose logging
  --lang {en,vi,zh,ja,ko,fa}  Language to build (default: en)
```

## 示例

```bash
# 带详细输出构建
uv run scripts/build_epub.py --verbose

# 指定输出位置
uv run scripts/build_epub.py --output ~/Desktop/claude-guide.epub

# 构建翻译版本
uv run scripts/build_epub.py --lang vi
```

## 输出

在仓库根目录生成 `claude-howto-guide.epub`。

EPUB 包含：
- 带项目 logo 的封面图片
- 嵌套分区的目录
- 所有 Markdown 内容转换成的 EPUB 兼容 HTML
- 渲染成 SVG 图片的 Mermaid 图表

## 运行测试

```bash
# 使用虚拟环境
source .venv/bin/activate
pytest scripts/tests/ -v

# 或者直接用 uv
uv run --with pytest --with pytest-asyncio \
    --with ebooklib --with markdown --with beautifulsoup4 \
    --with pillow \
    pytest scripts/tests/ -v
```

## 依赖

通过 PEP 723 内联脚本元数据管理：

| 包 | 用途 |
|---------|---------|
| `ebooklib` | 生成 EPUB |
| `markdown` | Markdown 转 HTML |
| `beautifulsoup4` | 解析 HTML |
| `pillow` | 生成封面图片 |

## 故障排查

**构建失败并提示 `Pele is unavailable`**：安装 Node.js >= 20，并确认 `node` 在 `PATH` 中（`node --version`）。

**Pele 包下载或校验失败**：首次构建会从 cdn.jsdelivr.net 下载固定版本的 Pele 包，并对每个文件做 sha256 校验。离线或处于代理环境时，先在有网络的机器上跑一次构建；之后的构建会使用 `scripts/.vendor-cache/pele/<版本>/` 里的缓存。校验不匹配说明下载被篡改或截断：删除对应目录后重新构建。

**缺少 logo**：找不到 `claude-howto-logo.png` 时，脚本会生成纯文字封面。

---

# 静态网站构建器

从 EPUB 构建所用的同一批 Markdown 文件生成一个优雅、移动端友好的静态网站。网站只是渲染出来的视图；`.md` 文件仍然是唯一的事实来源。

## 功能

- 每个 Markdown 源文件对应一个 HTML 页面——内部 `.md` 链接会被改写成站点上的对应页面
- 对仓库中非 Markdown 文件（模板、脚本、JSON）的引用会变成 GitHub blob 链接，在 github.com 上打开源文件
- Mermaid 图表在客户端用 Pele（`pele.global.js`）渲染，由构建出的站点自行提供（运行时不依赖 CDN）；图表跟随深色模式切换
- Tailwind CSS 用独立 CLI（Go 二进制，无需 Node.js）编译，并由构建出的站点提供——响应式布局，带侧边栏导航、页内目录、深色模式切换和上一页/下一页导航
- Inter + JetBrains Mono 字体与 CSS 一起自托管——页面加载时不发起任何第三方请求
- 与 EPUB 课程顺序保持一致（`01-` … `10-` 加顶层文档）
- 以纯静态文件方式即可托管——为部署到 GitHub Pages 而设计

## 快速开始

```bash
# 把英文网站构建到 ./site/
uv run scripts/build_website.py

# 本地预览
python -m http.server --directory site 8080
# 然后打开 http://localhost:8080
```

## 命令行选项

```
usage: build_website.py [-h] [--root ROOT] [--output OUTPUT]
                        [--lang {en,vi,zh,ja,uk,ko,fa}] [--repo-url REPO_URL]
                        [--branch BRANCH] [--verbose]

options:
  --root, -r ROOT       Source root (default: repo root)
  --output, -o OUTPUT   Output directory (default: <repo>/site)
  --lang LANG           Language to build: en | vi | zh | ja | uk | ko | fa
  --repo-url URL        GitHub repo for blob links (default: luongnv89/claude-howto)
  --branch BRANCH       Branch for blob links (default: main)
  --verbose, -v         Enable verbose logging
```

## GitHub Pages 部署

仓库自带工作流 `.github/workflows/pages.yml`：每次推送到 `main`（且任何 `.md` 或生成器文件有变化）时构建站点，并通过 `actions/deploy-pages` 发布。在仓库设置的 GitHub Pages 中把 **Source** 设为 **GitHub Actions** 即可启用。

## 架构

`build_website.py` 复用 `build_epub.py` 的章节排序逻辑，并在
`scripts/website_templates/` 下提供 HTML 模板：

- `page.html.j2` — 每页的 Jinja2 模板，含侧边栏导航、目录、上一页/下一页
- `tailwind.config.js`、`tailwind.input.css` — Tailwind 独立 CLI 的配置和入口 CSS；CLI 扫描构建出的 HTML，只产出实际用到的工具类，生成 `site/assets/tailwind.css`
- `site.css` — 少量站点专用样式和 Pygments 主题

Tailwind CLI 二进制、Pele 包和字体文件在首次构建时下载到
`scripts/.vendor-cache/`（已 gitignore）——见
`scripts/vendor_assets.py`。

标题锚点使用 `check_cross_references.heading_to_anchor` 中的完全相同的算法生成，因此 pre-commit 钩子校验过的 `#anchor` 链接在渲染后的站点上都能正确跳转。
