<picture>
  <source media="(prefers-color-scheme: dark)" srcset="logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="logos/claude-howto-logo.svg">
</picture>

# Claude How To - 品牌资源

这是 Claude How To 项目的完整品牌资源集合，包括 logo、图标和 favicon。所有资源都采用 V3.0 设计：一个带有代码括号（`>`）符号的指南针，象征在代码中引导前进，整体使用黑/白/灰配色，并以亮绿色（`#22C55E`）作为强调色。

## 目录结构

```
resources/
├── logos/
│   ├── claude-howto-logo.svg       # 主 logo - 浅色模式 (520×120px)
│   └── claude-howto-logo-dark.svg  # 主 logo - 深色模式 (520×120px)
├── icons/
│   ├── claude-howto-icon.svg       # 应用图标 - 浅色模式 (256×256px)
│   └── claude-howto-icon-dark.svg  # 应用图标 - 深色模式 (256×256px)
└── favicons/
    ├── favicon-16.svg              # Favicon - 16×16px
    ├── favicon-32.svg              # Favicon - 32×32px（主用）
    ├── favicon-64.svg              # Favicon - 64×64px
    ├── favicon-128.svg             # Favicon - 128×128px
    └── favicon-256.svg             # Favicon - 256×256px
```

`assets/logo/` 下还有额外资源：
```
assets/logo/
├── logo-full.svg       # 图形标记 + 品牌字样（横向）
├── logo-mark.svg       # 仅指南针符号 (120×120px)
├── logo-wordmark.svg   # 仅文字
├── logo-icon.svg       # 应用图标 (512×512，圆角)
├── favicon.svg         # 16×16 优化版
├── logo-white.svg      # 适用于深色背景的白色版本
└── logo-black.svg      # 黑色单色版本
```

## 资源概览

### 设计概念（V3.0）

**指南针 + 代码括号**，代表“导航遇见代码”：
- **指南针环** = 导航、找到方向
- **北针（绿色）** = 方向、学习路径上的进展
- **南针（黑色）** = 扎实基础、稳固根基
- **`>` 括号** = 终端提示符、代码、CLI 场景
- **刻度线** = 精准、结构化学习

### Logo

**文件**：
- `logos/claude-howto-logo.svg`（浅色模式）
- `logos/claude-howto-logo-dark.svg`（深色模式）

**规格**：
- **尺寸**：520×120 px
- **用途**：主标题/品牌 logo，带品牌字样
- **使用场景**：
  - 网站页眉
  - README 徽章
  - 营销素材
  - 印刷物料
- **格式**：SVG（可无限缩放）
- **模式**：浅色（白色背景）与深色（#0A0A0A 背景）

### 图标

**文件**：
- `icons/claude-howto-icon.svg`（浅色模式）
- `icons/claude-howto-icon-dark.svg`（深色模式）

**规格**：
- **尺寸**：256×256 px
- **用途**：应用图标、头像、缩略图
- **使用场景**：
  - App 图标
  - 个人头像
  - 社交媒体缩略图
  - 文档页眉
- **格式**：SVG（可无限缩放）
- **模式**：浅色（白色背景）与深色（#0A0A0A 背景）

**设计元素**：
- 带方位和中间方位刻度的指南针环
- 绿色北针（方向/引导）
- 黑色南针（基础）
- 中央 `>` 代码括号（终端/CLI）
- 绿色中心点强调

### Favicon

为网页使用提供了多种尺寸的优化版本：

| 文件 | 尺寸 | DPI | 用途 |
|------|------|-----|------|
| `favicon-16.svg` | 16×16 px | 1x | 浏览器标签页（旧浏览器） |
| `favicon-32.svg` | 32×32 px | 1x | 标准浏览器 favicon |
| `favicon-64.svg` | 64×64 px | 1x-2x | 高 DPI 显示器 |
| `favicon-128.svg` | 128×128 px | 2x | Apple touch icon、书签 |
| `favicon-256.svg` | 256×256 px | 4x | 现代浏览器、PWA 图标 |

**优化说明**：
- 16px：最小几何元素，仅保留环、指针和箭头
- 32px：增加方位刻度
- 64px 以上：完整细节与中间方位刻度
- 全部版本都保持与主图标一致的视觉效果
- SVG 格式保证任意尺寸下都清晰锐利

## HTML 集成

### 基础 Favicon 配置

```html
<!-- 浏览器 favicon -->
<link rel="icon" type="image/svg+xml" href="/resources/favicons/favicon-32.svg">
<link rel="icon" type="image/svg+xml" href="/resources/favicons/favicon-16.svg" sizes="16x16">

<!-- Apple touch icon（移动端桌面图标） -->
<link rel="apple-touch-icon" href="/resources/favicons/favicon-128.svg">

<!-- PWA 与现代浏览器 -->
<link rel="icon" type="image/svg+xml" href="/resources/favicons/favicon-256.svg" sizes="256x256">
```

### 完整配置

```html
<head>
  <!-- 主 favicon -->
  <link rel="icon" type="image/svg+xml" href="/resources/favicons/favicon-32.svg" sizes="32x32">
  <link rel="icon" type="image/svg+xml" href="/resources/favicons/favicon-16.svg" sizes="16x16">

  <!-- Apple touch icon -->
  <link rel="apple-touch-icon" href="/resources/favicons/favicon-128.svg">

  <!-- PWA 图标 -->
  <link rel="icon" type="image/svg+xml" href="/resources/favicons/favicon-256.svg" sizes="256x256">

  <!-- Android -->
  <link rel="shortcut icon" href="/resources/favicons/favicon-256.svg">

  <!-- PWA manifest 引用（如果使用 manifest.json） -->
  <meta name="theme-color" content="#000000">
</head>
```

## 颜色方案

### 主色
- **黑色**：`#000000`（主文本、线条、南针）
- **白色**：`#FFFFFF`（浅色背景）
- **灰色**：`#6B7280`（次级文本、次要刻度）

### 强调色
- **亮绿色**：`#22C55E`（北针、中心点、强调线条，只用于高亮，绝不作为背景）

### 深色模式
- **背景**：`#0A0A0A`（接近黑色）

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
- 主文本和结构元素使用黑色
- 次级/辅助元素使用灰色
- 绿色**仅**用于高亮，例如指针、点和强调线
- 不要把绿色用作背景色
- 保持 WCAG AA 对比度（最低 4.5:1）

## 设计规范

### Logo 使用
- 用于白色或深色（#0A0A0A）背景
- 按比例缩放
- Logo 四周保留足够留白（最小值：logo 高度 / 2）
- 根据背景选择对应的浅色/深色版本

### 图标使用
- 适用于标准尺寸：16、32、64、128、256px
- 保持指南针比例
- 按比例缩放

### Favicon 使用
- 根据场景选用合适尺寸
- 16-32px：浏览器标签页、书签
- 64px：站点图标
- 128px 以上：Apple/Android 桌面图标

## SVG 优化

所有 SVG 文件都采用扁平设计，没有渐变和滤镜：
- 干净的基于描边的几何结构
- 不嵌入位图
- 路径已优化
- 使用响应式 `viewBox`

网页优化示例：
```bash
# 压缩 SVG，同时保持质量
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

如果你需要为旧浏览器支持转换成 PNG：

```bash
# 使用 ImageMagick
convert -density 300 -background none favicon-256.svg favicon-256.png

# 使用 Inkscape
inkscape -D -z --file=favicon-256.svg --export-png=favicon-256.png
```

## 无障碍性

- 高对比度颜色比例（符合 WCAG AA，最低 4.5:1）
- 几何形状清晰，在各种尺寸下都容易识别
- 矢量格式，可无限缩放
- 图标中不使用文字（文字由单独的 wordmark 承担）
- 不依赖红绿配色表达含义

## 署名

这些资源属于 Claude How To 项目。

**许可证**：MIT（见项目 LICENSE 文件）

## 版本历史

- **v3.0**（2026 年 2 月）：指南针 + 括号设计，黑/白/灰 + 绿色强调色
- **v2.0**（2026 年 1 月）：受 Claude 启发的 12 芒星爆发式设计，祖母绿配色
- **v1.0**（2026 年 1 月）：最初基于六边形的进度图标设计

---

**最后更新**：2026 年 2 月
**当前版本**：3.0（指南针 + 括号）
**全部资源**：可直接用于生产环境的 SVG，支持无限缩放，符合 WCAG AA 无障碍标准
