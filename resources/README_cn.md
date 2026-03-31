<picture>
  <source media="(prefers-color-scheme: dark)" srcset="logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="logos/claude-howto-logo.svg">
</picture>

# Claude How To - 品牌资源

Claude How To 项目的完整 Logo、图标和 Favicon 合集。所有资源采用 V3.0 设计：指南针与代码括号（`>`）符号，代表在代码中有指引地导航——使用黑/白/灰调色板搭配亮绿色（#22C55E）强调色。

## 目录结构

```
resources/
├── logos/
│   ├── claude-howto-logo.svg       # 主 Logo - 浅色模式（520×120px）
│   └── claude-howto-logo-dark.svg  # 主 Logo - 深色模式（520×120px）
├── icons/
│   ├── claude-howto-icon.svg       # 应用图标 - 浅色模式（256×256px）
│   └── claude-howto-icon-dark.svg  # 应用图标 - 深色模式（256×256px）
└── favicons/
    ├── favicon-16.svg              # Favicon - 16×16px
    ├── favicon-32.svg              # Favicon - 32×32px（主要）
    ├── favicon-64.svg              # Favicon - 64×64px
    ├── favicon-128.svg             # Favicon - 128×128px
    └── favicon-256.svg             # Favicon - 256×256px
```

`assets/logo/` 中的附加资源：
```
assets/logo/
├── logo-full.svg       # 标志 + 文字标（水平）
├── logo-mark.svg       # 仅指南针符号（120×120px）
├── logo-wordmark.svg   # 仅文字
├── logo-icon.svg       # 应用图标（512×512，圆角）
├── favicon.svg         # 16×16 优化版
├── logo-white.svg      # 深色背景用白色版本
└── logo-black.svg      # 黑色单色版本
```

## 资源概览

### 设计理念（V3.0）

**指南针与代码括号** — 引导与代码的结合：
- **指南针圆环** = 导航，找到自己的路
- **北针（绿色）** = 方向，学习路径上的进步
- **南针（黑色）** = 根基，坚实的基础
- **`>` 括号** = 终端提示符、代码、CLI 语境
- **刻度标记** = 精确性，结构化学习

### Logo

**文件**：
- `logos/claude-howto-logo.svg`（浅色模式）
- `logos/claude-howto-logo-dark.svg`（深色模式）

**规格**：
- **尺寸**：520×120 px
- **用途**：带文字标的主头部/品牌 Logo
- **使用场景**：
  - 网站头部
  - README 徽章
  - 营销材料
  - 印刷材料
- **格式**：SVG（完全可缩放）
- **模式**：浅色（白色背景）& 深色（#0A0A0A 背景）

### 图标

**文件**：
- `icons/claude-howto-icon.svg`（浅色模式）
- `icons/claude-howto-icon-dark.svg`（深色模式）

**规格**：
- **尺寸**：256×256 px
- **用途**：应用图标、头像、缩略图
- **使用场景**：
  - 应用图标
  - 个人头像
  - 社交媒体缩略图
  - 文档头部
- **格式**：SVG（完全可缩放）
- **模式**：浅色（白色背景）& 深色（#0A0A0A 背景）

**设计元素**：
- 带基本方位和斜向刻度标记的指南针圆环
- 绿色北针（方向/引导）
- 黑色南针（基础）
- 居中的 `>` 代码括号（终端/CLI）
- 绿色中心点强调色

### Favicon

多种尺寸的 Web 优化版本：

| 文件 | 尺寸 | DPI | 使用场景 |
|------|------|-----|-------|
| `favicon-16.svg` | 16×16 px | 1x | 浏览器标签页（旧版浏览器） |
| `favicon-32.svg` | 32×32 px | 1x | 标准浏览器 favicon |
| `favicon-64.svg` | 64×64 px | 1x-2x | 高 DPI 显示屏 |
| `favicon-128.svg` | 128×128 px | 2x | Apple 触摸图标、书签 |
| `favicon-256.svg` | 256×256 px | 4x | 现代浏览器、PWA 图标 |

**优化说明**：
- 16px：最简几何形状——圆环、指针、箭头符号
- 32px：添加基本方位刻度标记
- 64px+：包含斜向刻度的完整细节
- 所有尺寸与主图标保持视觉一致
- SVG 格式确保任意尺寸下均清晰显示

## HTML 集成

### 基本 Favicon 设置

```html
<!-- 浏览器 favicon -->
<link rel="icon" type="image/svg+xml" href="/resources/favicons/favicon-32.svg">
<link rel="icon" type="image/svg+xml" href="/resources/favicons/favicon-16.svg" sizes="16x16">

<!-- Apple 触摸图标（移动端主屏幕） -->
<link rel="apple-touch-icon" href="/resources/favicons/favicon-128.svg">

<!-- PWA 及现代浏览器 -->
<link rel="icon" type="image/svg+xml" href="/resources/favicons/favicon-256.svg" sizes="256x256">
```

### 完整设置

```html
<head>
  <!-- 主 favicon -->
  <link rel="icon" type="image/svg+xml" href="/resources/favicons/favicon-32.svg" sizes="32x32">
  <link rel="icon" type="image/svg+xml" href="/resources/favicons/favicon-16.svg" sizes="16x16">

  <!-- Apple 触摸图标 -->
  <link rel="apple-touch-icon" href="/resources/favicons/favicon-128.svg">

  <!-- PWA 图标 -->
  <link rel="icon" type="image/svg+xml" href="/resources/favicons/favicon-256.svg" sizes="256x256">

  <!-- Android -->
  <link rel="shortcut icon" href="/resources/favicons/favicon-256.svg">

  <!-- PWA manifest 引用（如果使用 manifest.json） -->
  <meta name="theme-color" content="#000000">
</head>
```

## 色彩方案

### 主色
- **黑色**：`#000000`（主要文字、描边、南针）
- **白色**：`#FFFFFF`（浅色背景）
- **灰色**：`#6B7280`（次要文字、小刻度标记）

### 强调色
- **亮绿色**：`#22C55E`（北针、中心点、强调线——仅用于高亮，不作背景色）

### 深色模式
- **背景**：`#0A0A0A`（近黑色）

### CSS 变量
```css
--color-primary: #000000;
--color-secondary: #6B7280;
--color-accent: #22C55E;
--color-bg-light: #FFFFFF;
--color-bg-dark: #0A0A0A;
```

### Tailwind 配置
```js
colors: {
  brand: {
    primary: '#000000',
    secondary: '#6B7280',
    accent: '#22C55E',
  }
}
```

### 使用规范
- 黑色用于主要文字和结构元素
- 灰色用于次要/辅助元素
- 绿色**仅**用于高亮——指针、点、强调线
- 不要将绿色用作背景色
- 保持 WCAG AA 对比度（最低 4.5:1）

## 设计规范

### Logo 使用规范
- 在白色或深色（#0A0A0A）背景上使用
- 按比例缩放
- Logo 周围保留净空（最小：Logo 高度 / 2）
- 根据背景选择合适的浅色/深色变体

### 图标使用规范
- 使用标准尺寸：16、32、64、128、256px
- 保持指南针比例
- 按比例缩放

### Favicon 使用规范
- 根据使用场景选择合适尺寸
- 16-32px：浏览器标签页、书签
- 64px：网站图标
- 128px+：Apple/Android 主屏幕

## SVG 优化

所有 SVG 文件为扁平设计，无渐变或滤镜：
- 简洁的描边几何形状
- 无嵌入栅格图像
- 优化的路径
- 响应式 viewBox

Web 优化：
```bash
# 在保持质量的同时压缩 SVG
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

为兼容旧版浏览器，将 SVG 转换为 PNG：

```bash
# 使用 ImageMagick
convert -density 300 -background none favicon-256.svg favicon-256.png

# 使用 Inkscape
inkscape -D -z --file=favicon-256.svg --export-png=favicon-256.png
```

## 无障碍访问

- 高对比度颜色比（符合 WCAG AA——最低 4.5:1）
- 在任何尺寸下均可辨认的简洁几何形状
- 可缩放矢量格式
- 图标中无文字（文字单独添加在文字标中）
- 含义不依赖红绿色区分

## 版权声明

这些资源是 Claude How To 项目的一部分。

**许可证**：MIT（详见项目 LICENSE 文件）

## 版本历史

- **v3.0**（2026 年 2 月）：指南针-括号设计，黑/白/灰 + 绿色强调色方案
- **v2.0**（2026 年 1 月）：Claude 风格的 12 射线星形设计，翡翠绿色方案
- **v1.0**（2026 年 1 月）：原始六边形进度图标设计

---

**最后更新**：2026 年 2 月
**当前版本**：3.0（指南针-括号）
**所有资源**：生产就绪 SVG，完全可缩放，符合 WCAG AA 无障碍标准
