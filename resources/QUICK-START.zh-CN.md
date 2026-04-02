# Quick Start - 品牌资源

## 将资源复制到你的项目

```bash
# 将全部 resources 复制到你的网站项目
cp -r resources/ /path/to/your/website/

# 或者仅复制网页 favicon
cp resources/favicons/* /path/to/your/website/public/
```

## 添加到 HTML（可直接复制）

```html
<!-- Favicons -->
<link rel="icon" type="image/svg+xml" href="/resources/favicons/favicon-32.svg" sizes="32x32">
<link rel="icon" type="image/svg+xml" href="/resources/favicons/favicon-16.svg" sizes="16x16">
<link rel="apple-touch-icon" href="/resources/favicons/favicon-128.svg">
<link rel="icon" type="image/svg+xml" href="/resources/favicons/favicon-256.svg" sizes="256x256">
<meta name="theme-color" content="#000000">
```

## 在 Markdown/文档中使用

```markdown
# Claude How To

![Claude How To Logo](resources/logos/claude-howto-logo.svg)

![Icon](resources/icons/claude-howto-icon.svg)
```

## 推荐尺寸

| Purpose | Size | File |
|---------|------|------|
| Website header | 520×120 | `logos/claude-howto-logo.svg` |
| App icon | 256×256 | `icons/claude-howto-icon.svg` |
| Browser tab | 32×32 | `favicons/favicon-32.svg` |
| Mobile home screen | 128×128 | `favicons/favicon-128.svg` |
| Desktop app | 256×256 | `favicons/favicon-256.svg` |
| Small avatar | 64×64 | `favicons/favicon-64.svg` |

## 颜色值

```css
/* 在你的 CSS 中使用 */
--color-primary: #000000;
--color-secondary: #6B7280;
--color-accent: #22C55E;
--color-bg-light: #FFFFFF;
--color-bg-dark: #0A0A0A;
```

## 图标设计含义

**Compass with Code Bracket**：
- 指南针外环 = 导航、结构化学习路径
- 绿色北针 = 方向、进度、引导
- 黑色南针 = 扎实基础、稳定落地
- `>` 符号 = 终端提示符、代码、CLI 语境
- 刻度线 = 精确与结构化步骤

核心寓意：**在清晰引导中找到代码实践方向**。

## 不同场景怎么用

### 网站
- **Header**：Logo（`logos/claude-howto-logo.svg`）
- **Favicon**：32px（`favicons/favicon-32.svg`）
- **社交分享图**：Icon（`icons/claude-howto-icon.svg`）

### GitHub
- **README 徽章图标**：Icon（`icons/claude-howto-icon.svg`），64-128px
- **仓库头像**：Icon（`icons/claude-howto-icon.svg`）

### 社交媒体
- **头像**：Icon（`icons/claude-howto-icon.svg`）
- **横幅**：Logo（`logos/claude-howto-logo.svg`）
- **缩略图**：256×256 的 Icon

### 文档
- **章节标题**：Logo 或 Icon（按版式缩放）
- **导航图标**：Favicon（32-64px）

---

完整说明见 [README.md](README.zh-CN.md)。
