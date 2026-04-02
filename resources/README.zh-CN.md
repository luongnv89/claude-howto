<picture>
  <source media="(prefers-color-scheme: dark)" srcset="logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="logos/claude-howto-logo.svg">
</picture>

# Claude How To - 品牌资源

Claude How To 项目的完整品牌资源集合：logo、icon 与 favicon。所有资源采用 V3.0 设计：**带代码括号（`>`）的指南针**，象征“在代码世界中被引导前进”。配色为 Black/White/Gray + Bright Green（#22C55E）点缀。

## 目录结构

```text
resources/
├── logos/
│   ├── claude-howto-logo.svg       # 主 Logo - 浅色模式 (520×120px)
│   └── claude-howto-logo-dark.svg  # 主 Logo - 深色模式 (520×120px)
├── icons/
│   ├── claude-howto-icon.svg       # App 图标 - 浅色模式 (256×256px)
│   └── claude-howto-icon-dark.svg  # App 图标 - 深色模式 (256×256px)
└── favicons/
    ├── favicon-16.svg              # Favicon - 16×16px
    ├── favicon-32.svg              # Favicon - 32×32px（主）
    ├── favicon-64.svg              # Favicon - 64×64px
    ├── favicon-128.svg             # Favicon - 128×128px
    └── favicon-256.svg             # Favicon - 256×256px
```

`assets/logo/` 下的附加资源：

```text
assets/logo/
├── logo-full.svg       # 图标 + 字标（横向）
├── logo-mark.svg       # 仅指南针符号（120×120px）
├── logo-wordmark.svg   # 仅文字
├── logo-icon.svg       # App 图标（512×512，圆角）
├── favicon.svg         # 16×16 优化版
├── logo-white.svg      # 深色背景白色版本
└── logo-black.svg      # 黑色单色版本
```

## 资源概览

### 设计概念（V3.0）

**Compass with Code Bracket** —— 引导与代码的结合：
- **Compass Ring** = 导航、定位方向
- **North Needle（Green）** = 学习路径上的方向与进度
- **South Needle（Black）** = 稳定基础
- **`>` Bracket** = 终端提示符、代码、CLI 语境
- **Tick Marks** = 精确与结构化学习

### Logos

**文件：**
- `logos/claude-howto-logo.svg`（浅色）
- `logos/claude-howto-logo-dark.svg`（深色）

**规格：**
- **尺寸**：520×120 px
- **用途**：主品牌头图（含字标）
- **使用场景**：
  - 网站 Header
  - README 徽章区
  - 营销素材
  - 印刷物料
- **格式**：SVG（可无限缩放）
- **模式**：Light（白底）与 Dark（#0A0A0A 背景）

### Icons

**文件：**
- `icons/claude-howto-icon.svg`（浅色）
- `icons/claude-howto-icon-dark.svg`（深色）

**规格：**
- **尺寸**：256×256 px
- **用途**：应用图标、头像、缩略图
- **使用场景**：
  - App 图标
  - 个人/团队头像
  - 社交媒体缩略图
  - 文档标题图标
- **格式**：SVG（可无限缩放）
- **模式**：Light 与 Dark

**设计元素：**
- 带主次刻度的指南针环
- 绿色北针（方向/引导）
- 黑色南针（基础/稳定）
- 中心 `>` 代码括号（终端/CLI）
- 绿色中心点强调

### Favicons

面向 Web 的多尺寸优化：

| File | Size | DPI | Usage |
|------|------|-----|-------|
| `favicon-16.svg` | 16×16 px | 1x | 旧浏览器标签页 |
| `favicon-32.svg` | 32×32 px | 1x | 标准浏览器 favicon |
| `favicon-64.svg` | 64×64 px | 1x-2x | 高 DPI 显示 |
| `favicon-128.svg` | 128×128 px | 2x | Apple touch、书签 |
| `favicon-256.svg` | 256×256 px | 4x | 现代浏览器、PWA 图标 |

**优化说明：**
- 16px：仅保留外环、指针、chevron 等最小几何
- 32px：加入主方向刻度
- 64px+：展示完整细节（含次刻度）
- 与主图标保持视觉一致
- SVG 保证任意尺寸锐利显示

## HTML 集成

### 基础 Favicon 配置

```html
<!-- Browser favicon -->
<link rel="icon" type="image/svg+xml" href="/resources/favicons/favicon-32.svg">
<link rel="icon" type="image/svg+xml" href="/resources/favicons/favicon-16.svg" sizes="16x16">

<!-- Apple touch icon (mobile home screen) -->
<link rel="apple-touch-icon" href="/resources/favicons/favicon-128.svg">

<!-- PWA & modern browsers -->
<link rel="icon" type="image/svg+xml" href="/resources/favicons/favicon-256.svg" sizes="256x256">
```

### 完整配置示例

```html
<head>
  <!-- Primary favicon -->
  <link rel="icon" type="image/svg+xml" href="/resources/favicons/favicon-32.svg" sizes="32x32">
  <link rel="icon" type="image/svg+xml" href="/resources/favicons/favicon-16.svg" sizes="16x16">

  <!-- Apple touch icon -->
  <link rel="apple-touch-icon" href="/resources/favicons/favicon-128.svg">

  <!-- PWA icons -->
  <link rel="icon" type="image/svg+xml" href="/resources/favicons/favicon-256.svg" sizes="256x256">

  <!-- Android -->
  <link rel="shortcut icon" href="/resources/favicons/favicon-256.svg">

  <!-- PWA manifest reference (if using manifest.json) -->
  <meta name="theme-color" content="#000000">
</head>
```

## 色板

### 主色
- **Black**: `#000000`（主文本、描边、南针）
- **White**: `#FFFFFF`（浅色背景）
- **Gray**: `#6B7280`（辅助文本、次刻度）

### 强调色
- **Bright Green**: `#22C55E`（北针、中心点、强调线）

### 深色模式
- **Background**: `#0A0A0A`

### CSS Variables

```css
--color-primary: #000000;
--color-secondary: #6B7280;
--color-accent: #22C55E;
--color-bg-light: #FFFFFF;
--color-bg-dark: #0A0A0A;
```

### Tailwind 配置示例

```js
colors: {
  brand: {
    primary: '#000000',
    secondary: '#6B7280',
    accent: '#22C55E',
  }
}
```

### 使用原则
- 黑色用于主文本与结构元素
- 灰色用于辅助元素
- 绿色仅用于强调（指针、点、线）
- 不要使用绿色作为大面积背景
- 对比度遵循 WCAG AA（至少 4.5:1）

## 设计指南

### Logo 使用
- 建议放置在白色或 #0A0A0A 背景
- 等比缩放
- 保留最小留白（至少 Logo 高度的 1/2）
- 根据背景选择 light/dark 版本

### Icon 使用
- 推荐标准尺寸：16、32、64、128、256px
- 保持指南针比例
- 等比缩放

### Favicon 使用
- 按场景选择尺寸
- 16-32px：浏览器标签/书签
- 64px：站点图标
- 128px+：移动端主屏图标

## SVG 优化

所有 SVG 均为扁平化设计（无渐变、无滤镜）：
- 干净描边几何
- 无内嵌位图
- 路径已优化
- 响应式 viewBox

Web 优化示例：

```bash
svgo --config='{
  "js2svg": {
    "indent": 2
  },
  "plugins": [
    "convertStyleToAttrs",
    "removeRasterImages"
  ]
}' input.svg -o output.svg
```

## PNG 转换

面向旧浏览器可将 SVG 转 PNG：

```bash
# ImageMagick
convert -density 300 -background none favicon-256.svg favicon-256.png

# Inkscape
inkscape -D -z --file=favicon-256.svg --export-png=favicon-256.png
```

## 可访问性

- 高对比（WCAG AA，最小 4.5:1）
- 几何形状在小尺寸仍可识别
- SVG 矢量可缩放
- 图标无文字依赖（文字在字标中单独提供）
- 不依赖红绿配色表达语义

## Attribution

这些资源属于 Claude How To 项目。

**License**：MIT（见项目 LICENSE）

## 版本历史

- **v3.0**（2026-02）：指南针 + 代码括号设计，Black/White/Gray + Green 点缀
- **v2.0**（2026-01）：Claude 风格 12 射线 starburst + emerald 色板
- **v1.0**（2026-01）：原始六边形进阶图标方案

---

**Last Updated**：February 2026
**Current Version**：3.0 (Compass-Bracket)
**All Assets**：生产可用 SVG，完全可缩放，符合 WCAG AA
