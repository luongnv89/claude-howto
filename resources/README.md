<picture>
  <source media="(prefers-color-scheme: dark)" srcset="logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="logos/claude-howto-logo.svg">
</picture>

# Claude How To - 品牌素材

Claude How To 專案的完整 Logo、圖示和 favicon 集合。所有素材使用 V3.0 設計：指南針搭配程式碼括號（`>`）符號，代表程式碼導覽的引導 — 使用黑色/白色/灰色色調搭配亮綠色（#22C55E）強調色。

## 目錄結構

```
resources/
├── logos/
│   ├── claude-howto-logo.svg       # 主 Logo - 淺色模式 (520×120px)
│   └── claude-howto-logo-dark.svg  # 主 Logo - 深色模式 (520×120px)
├── icons/
│   ├── claude-howto-icon.svg       # 應用程式圖示 - 淺色模式 (256×256px)
│   └── claude-howto-icon-dark.svg  # 應用程式圖示 - 深色模式 (256×256px)
└── favicons/
    ├── favicon-16.svg              # Favicon - 16×16px
    ├── favicon-32.svg              # Favicon - 32×32px（主要）
    ├── favicon-64.svg              # Favicon - 64×64px
    ├── favicon-128.svg             # Favicon - 128×128px
    └── favicon-256.svg             # Favicon - 256×256px
```

`assets/logo/` 中的額外素材：
```
assets/logo/
├── logo-full.svg       # 標誌 + 文字標誌（水平）
├── logo-mark.svg       # 僅指南針符號 (120×120px)
├── logo-wordmark.svg   # 僅文字
├── logo-icon.svg       # 應用程式圖示 (512×512，圓角)
├── favicon.svg         # 16×16 最佳化
├── logo-white.svg      # 白色版本用於深色背景
└── logo-black.svg      # 黑色單色版本
```

## 素材概覽

### 設計概念（V3.0）

**指南針搭配程式碼括號** — 引導遇上程式碼：
- **指南針環** = 導覽、找到方向
- **北針（綠色）** = 方向、學習路徑上的進度
- **南針（黑色）** = 根基、穩固基礎
- **`>` 括號** = 終端機提示、程式碼、CLI 脈絡
- **刻度標記** = 精確、結構化學習

### Logo

**檔案**：
- `logos/claude-howto-logo.svg`（淺色模式）
- `logos/claude-howto-logo-dark.svg`（深色模式）

**規格**：
- **尺寸**：520×120 px
- **用途**：主要標頭/品牌 logo，含文字標誌
- **使用場景**：
  - 網站標頭
  - README 徽章
  - 行銷素材
  - 印刷品
- **格式**：SVG（完全可縮放）
- **模式**：淺色（白色背景）& 深色（#0A0A0A 背景）

### 圖示

**檔案**：
- `icons/claude-howto-icon.svg`（淺色模式）
- `icons/claude-howto-icon-dark.svg`（深色模式）

**規格**：
- **尺寸**：256×256 px
- **用途**：應用程式圖示、頭像、縮圖
- **使用場景**：
  - 應用程式圖示
  - 個人頭像
  - 社群媒體縮圖
  - 文件標頭
- **格式**：SVG（完全可縮放）
- **模式**：淺色（白色背景）& 深色（#0A0A0A 背景）

**設計元素**：
- 含主方位和副方位刻度標記的指南針環
- 綠色北針（方向/引導）
- 黑色南針（基礎）
- 中心的 `>` 程式碼括號（終端機/CLI）
- 綠色中心點強調

### Favicon

針對網頁使用最佳化的多種尺寸版本：

| 檔案 | 尺寸 | DPI | 用途 |
|------|------|-----|-------|
| `favicon-16.svg` | 16×16 px | 1x | 瀏覽器分頁（舊版瀏覽器） |
| `favicon-32.svg` | 32×32 px | 1x | 標準瀏覽器 favicon |
| `favicon-64.svg` | 64×64 px | 1x-2x | 高 DPI 顯示器 |
| `favicon-128.svg` | 128×128 px | 2x | Apple 觸控圖示、書籤 |
| `favicon-256.svg` | 256×256 px | 4x | 現代瀏覽器、PWA 圖示 |

**最佳化說明**：
- 16px：極簡幾何 — 僅環形、指針、箭頭
- 32px：新增主方位刻度標記
- 64px+：含副方位刻度的完整細節
- 所有版本與主圖示保持視覺一致性
- SVG 格式確保任何尺寸的清晰顯示

## HTML 整合

### 基本 Favicon 設定

```html
<!-- 瀏覽器 favicon -->
<link rel="icon" type="image/svg+xml" href="/resources/favicons/favicon-32.svg">
<link rel="icon" type="image/svg+xml" href="/resources/favicons/favicon-16.svg" sizes="16x16">

<!-- Apple 觸控圖示（手機主螢幕） -->
<link rel="apple-touch-icon" href="/resources/favicons/favicon-128.svg">

<!-- PWA & 現代瀏覽器 -->
<link rel="icon" type="image/svg+xml" href="/resources/favicons/favicon-256.svg" sizes="256x256">
```

### 完整設定

```html
<head>
  <!-- 主要 favicon -->
  <link rel="icon" type="image/svg+xml" href="/resources/favicons/favicon-32.svg" sizes="32x32">
  <link rel="icon" type="image/svg+xml" href="/resources/favicons/favicon-16.svg" sizes="16x16">

  <!-- Apple 觸控圖示 -->
  <link rel="apple-touch-icon" href="/resources/favicons/favicon-128.svg">

  <!-- PWA 圖示 -->
  <link rel="icon" type="image/svg+xml" href="/resources/favicons/favicon-256.svg" sizes="256x256">

  <!-- Android -->
  <link rel="shortcut icon" href="/resources/favicons/favicon-256.svg">

  <!-- PWA manifest 參考（若使用 manifest.json） -->
  <meta name="theme-color" content="#000000">
</head>
```

## 色彩方案

### 主要色彩
- **黑色**：`#000000`（主要文字、筆畫、南針）
- **白色**：`#FFFFFF`（淺色背景）
- **灰色**：`#6B7280`（次要文字、次要刻度標記）

### 強調色
- **亮綠色**：`#22C55E`（北針、中心點、強調線 — 僅用於強調，絕不作為背景）

### 深色模式
- **背景**：`#0A0A0A`（近黑色）

### CSS 變數
```css
--color-primary: #000000;
--color-secondary: #6B7280;
--color-accent: #22C55E;
--color-bg-light: #FFFFFF;
--color-bg-dark: #0A0A0A;
```

### Tailwind 設定
```js
colors: {
  brand: {
    primary: '#000000',
    secondary: '#6B7280',
    accent: '#22C55E',
  }
}
```

### 使用指南
- 使用黑色作為主要文字和結構元素
- 使用灰色作為次要/輔助元素
- 綠色**僅**用於強調 — 指針、圓點、強調線
- 絕不使用綠色作為背景色
- 維持 WCAG AA 對比度（最低 4.5:1）

## 設計指南

### Logo 使用
- 在白色或深色（#0A0A0A）背景上使用
- 等比例縮放
- 在 logo 周圍包含淨空區域（最小值：logo 高度 / 2）
- 為適當的背景使用提供的淺色/深色變體

### 圖示使用
- 使用標準尺寸：16、32、64、128、256px
- 維持指南針比例
- 等比例縮放

### Favicon 使用
- 為場景使用適當的尺寸
- 16-32px：瀏覽器分頁、書籤
- 64px：Favicon 網站圖示
- 128px+：Apple/Android 主螢幕

## SVG 最佳化

所有 SVG 檔案為扁平設計，無漸層或濾鏡：
- 乾淨的基於筆畫的幾何
- 無嵌入點陣圖
- 最佳化路徑
- 響應式 viewBox

網頁最佳化：
```bash
# 壓縮 SVG 同時維持品質
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

## PNG 轉換

將 SVG 轉換為 PNG 以支援舊版瀏覽器：

```bash
# 使用 ImageMagick
convert -density 300 -background none favicon-256.svg favicon-256.png

# 使用 Inkscape
inkscape -D -z --file=favicon-256.svg --export-png=favicon-256.png
```

## 無障礙

- 高對比度色彩比例（符合 WCAG AA — 最低 4.5:1）
- 在所有尺寸都可辨識的乾淨幾何形狀
- 可縮放的向量格式
- 圖示中無文字（文字在文字標誌中另外加入）
- 不依賴紅綠色彩傳達意義

## 授權

這些素材是 Claude How To 專案的一部分。

**授權**：MIT（見專案 LICENSE 檔案）

## 版本歷程

- **v3.0**（2026 年 2 月）：指南針-括號設計，含黑色/白色/灰色 + 綠色強調色方案
- **v2.0**（2026 年 1 月）：Claude 風格的 12 射線星形設計，含翡翠色方案
- **v1.0**（2026 年 1 月）：原始六邊形漸進式圖示設計

---

**最後更新**：2026 年 2 月
**目前版本**：3.0（指南針-括號）
**所有素材**：可用於生產的 SVG，完全可縮放，符合 WCAG AA 無障礙標準
