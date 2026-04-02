# Claude How To - 设计系统

## 视觉识别

### 图标设计概念：Compass with Code Bracket

Claude How To 图标采用**带 `>` 代码括号的指南针**，表示“在代码实践中获得方向引导”：

```text
     N (green)
     ▲
     │
W ───>─── E     Compass = Guidance/Direction
     │          > Bracket = Code/Terminal/CLI
     ▼
     S (black)
```

这带来：
- **高识别度**：第一眼就传达“代码导航指南”
- **符号语义明确**：指南针=找方向；`>`=代码/终端
- **可扩展性强**：16px 到 512px 都可用
- **品牌统一**：符合开发者工具的克制审美

---

## 色彩系统

### 色板

| Color | Hex | RGB | Usage |
|-------|-----|-----|-------|
| Black (Primary) | `#000000` | 0, 0, 0 | 主描边、文本、南针 |
| White (Background) | `#FFFFFF` | 255, 255, 255 | 浅色背景 |
| Gray (Secondary) | `#6B7280` | 107, 114, 128 | 次刻度、辅助文本 |
| Bright Green (Accent) | `#22C55E` | 34, 197, 94 | 北针、中心点、强调线 |
| Near Black (Dark BG) | `#0A0A0A` | 10, 10, 10 | 深色背景 |

### 对比度（WCAG）

- Black on White：**21:1** AAA
- Gray on White：**4.6:1** AA
- Green on White：**3.2:1**（仅装饰，不用于正文）
- White on Dark：**19.5:1** AAA

### 强调色规则

**Bright Green（#22C55E）仅用于强调：**
- 指南针北针
- 中心点
- 强调下划线/边框
- 不用作背景色
- 不用于正文文本

---

## 字体系统

### Logo 字体
- **Family**：Inter, SF Pro Display, -apple-system, Segoe UI, sans-serif
- **“Claude”**：42px，700（bold），Black
- **“How-To”**：32px，500（medium），Gray（#6B7280）
- **Subtitle**：10px，500，Gray，字距 1.5px，全大写

### 界面字体
- **Family**：Inter, SF Pro, 系统 sans-serif
- **Weight**：400-600
- **Style**：清晰、易读

---

## 图标细节

### 指南针规格

指南针图形由以下几何元素组成：

```text
Element             | Stroke/Fill    | Color
--------------------|----------------|------------------
Outer ring          | 3px stroke     | Black / White (dark mode)
North tick          | 2.5px stroke   | Black / White (dark mode)
Other cardinal ticks| 2px stroke     | Gray / White 50% (dark mode)
Intercardinal ticks | 1.5px stroke   | Gray / White 40% (dark mode)
North needle        | filled polygon | #22C55E (always green)
South needle        | filled polygon | Black / White (dark mode)
> bracket           | 3px stroke     | Black / White (dark mode)
Center dot          | filled circle  | #22C55E (always green)
```

### 尺寸层级

```text
16px  → 仅外环 + 指针 + chevron（极简）
32px  → 增加主方向刻度
64px  → 增加次方向刻度
128px → 完整细节且保持锐利
256px → 最大细节与更粗描边
```

---

## 尺寸规范

### Logo 尺寸

- **最小**：200px 宽（Web）
- **推荐**：520px（原生尺寸）
- **最大**：无限制（矢量）
- **比例**：约 4.3:1

### Icon 尺寸

- **最小**：16px（favicon）
- **推荐**：64-256px（App、头像）
- **最大**：无限制（矢量）
- **比例**：1:1（正方形）

---

## 间距与对齐

### Logo 留白

```text
┌─────────────────────────────────────┐
│                                     │
│        Clear Space Minimum          │
│         (logo height / 2)           │
│                                     │
│    [COMPASS]  Claude                │
│               How-To                │
│                                     │
└─────────────────────────────────────┘
```

### Icon 中心点

所有 icon 以画布中心对齐：
- 256px 画布中心：128×128
- 128px 画布中心：64×64

---

## 可访问性

### 色彩可读性
- 所有文本满足 WCAG AA（至少 4.5:1）
- 绿色仅用于装饰，不承载关键信息
- 不依赖红绿区分语义

### 可缩放性
- SVG 在任意尺寸都清晰
- 16px 仍可辨识核心图形
- 根据尺寸逐级展示细节

---

## 应用示例

### Web Header
- 尺寸：520×120px logo
- 文件：`logos/claude-howto-logo.svg`
- 背景：White 或 #0A0A0A
- 留白：至少 20px

### App Icon
- 尺寸：256×256px
- 文件：`icons/claude-howto-icon.svg`
- 背景：White 或 Dark
- 用途：应用快捷方式、头像

### 浏览器 Favicon
- 尺寸：32px（主），16px（兜底）
- 文件：`favicons/favicon-32.svg`
- 格式：SVG

### 社交媒体
- 头像：256×256 icon
- 横幅：520×120 logo（居中）

### 文档
- 章节标题：缩放 logo
- 小节图标：64×64 favicon
- 行内图标：32×32 favicon

---

## 文件格式细节

### SVG 结构

全部 SVG 均为扁平设计：
- 无渐变（仅纯色）
- 无滤镜（无 blur/glow/shadow）
- 干净 stroke/fill 几何
- 通过 viewBox 响应式缩放
- 可读、可维护代码

### 跨浏览器兼容

- Chrome/Edge：完全支持
- Firefox：完全支持
- Safari：完全支持
- iOS Safari：完全支持
- 现代浏览器：全部支持

---

## 自定义

### 更换强调色

若要创建其他强调色版本：

1. 将 `#22C55E` 替换为目标色
2. 确保装饰元素对比度仍 ≥ 3:1
3. 保持黑白灰结构不变

### 缩放

```css
svg {
  width: 256px;
  height: 256px;
}
```

SVG 会依据 viewBox 自动缩放，无需额外 transform。

---

## 版本管理

建议通过 git 跟踪设计变更：
- SVG 作为文本文件直接版本化
- 设计更新时打版本 tag
- 提交时同步维护 `DESIGN-SYSTEM.md`

---

**Last Updated**: February 2026
**Design System Version**: 3.0
