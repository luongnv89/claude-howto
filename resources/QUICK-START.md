# 快速入門 - 品牌素材

## 複製素材至您的專案

```bash
# 複製所有資源至您的網頁專案
cp -r resources/ /path/to/your/website/

# 或僅複製 favicons 用於網頁
cp resources/favicons/* /path/to/your/website/public/
```

## 加入 HTML（複製貼上）

```html
<!-- Favicons -->
<link rel="icon" type="image/svg+xml" href="/resources/favicons/favicon-32.svg" sizes="32x32">
<link rel="icon" type="image/svg+xml" href="/resources/favicons/favicon-16.svg" sizes="16x16">
<link rel="apple-touch-icon" href="/resources/favicons/favicon-128.svg">
<link rel="icon" type="image/svg+xml" href="/resources/favicons/favicon-256.svg" sizes="256x256">
<meta name="theme-color" content="#000000">
```

## 在 Markdown/文件中使用

```markdown
# Claude How To

![Claude How To Logo](resources/logos/claude-howto-logo.svg)

![Icon](resources/icons/claude-howto-icon.svg)
```

## 建議尺寸

| 用途 | 尺寸 | 檔案 |
|---------|------|------|
| 網站標頭 | 520×120 | `logos/claude-howto-logo.svg` |
| 應用程式圖示 | 256×256 | `icons/claude-howto-icon.svg` |
| 瀏覽器分頁 | 32×32 | `favicons/favicon-32.svg` |
| 手機主螢幕 | 128×128 | `favicons/favicon-128.svg` |
| 桌面應用程式 | 256×256 | `favicons/favicon-256.svg` |
| 小頭像 | 64×64 | `favicons/favicon-64.svg` |

## 色彩值

```css
/* 在您的 CSS 中使用 */
--color-primary: #000000;
--color-secondary: #6B7280;
--color-accent: #22C55E;
--color-bg-light: #FFFFFF;
--color-bg-dark: #0A0A0A;
```

## 圖示設計意涵

**指南針搭配程式碼括號**：
- 指南針環 = 導覽、結構化的學習路徑
- 綠色北針 = 方向、進度、引導
- 黑色南針 = 根基、穩固基礎
- `>` 括號 = 終端機提示、程式碼、CLI 脈絡
- 刻度標記 = 精確、結構化步驟

這象徵著「在清晰的引導下找到程式碼的方向。」

## 何時使用什麼

### 網站
- **標頭**：Logo（`logos/claude-howto-logo.svg`）
- **Favicon**：32px（`favicons/favicon-32.svg`）
- **社群預覽**：圖示（`icons/claude-howto-icon.svg`）

### GitHub
- **README 徽章**：圖示（`icons/claude-howto-icon.svg`）64-128px
- **儲存庫頭像**：圖示（`icons/claude-howto-icon.svg`）

### 社群媒體
- **大頭貼**：圖示（`icons/claude-howto-icon.svg`）
- **橫幅**：Logo（`logos/claude-howto-logo.svg`）
- **縮圖**：圖示 256×256px

### 文件
- **章節標頭**：Logo 或圖示（縮放至合適大小）
- **導覽圖示**：Favicon（32-64px）

---

請參閱 [README.md](README.md) 取得完整文件。
