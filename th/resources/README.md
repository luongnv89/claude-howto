<!-- i18n-source: resources/README.md -->
<!-- i18n-date: 2026-07-15 -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="logos/claude-howto-logo.svg">
</picture>

# Claude How To - Brand Assets

ชุดครบถ้วนของ logo, icon, และ favicon สำหรับโปรเจกต์ Claude How To ทุก asset ใช้การออกแบบ V3.0: เข็มทิศพร้อมสัญลักษณ์ code bracket (`>`) สื่อถึงการนำทางผ่านโค้ดอย่างมีคำแนะนำ โดยใช้ palette สี Black/White/Gray พร้อมสี Bright Green (#22C55E) เป็นสีเน้น

## โครงสร้าง Directory

```
resources/
├── logos/
│   ├── claude-howto-logo.svg       # Main logo - Light mode (520×120px)
│   └── claude-howto-logo-dark.svg  # Main logo - Dark mode (520×120px)
├── icons/
│   ├── claude-howto-icon.svg       # App icon - Light mode (256×256px)
│   └── claude-howto-icon-dark.svg  # App icon - Dark mode (256×256px)
└── favicons/
    ├── favicon-16.svg              # Favicon - 16×16px
    ├── favicon-32.svg              # Favicon - 32×32px (primary)
    ├── favicon-64.svg              # Favicon - 64×64px
    ├── favicon-128.svg             # Favicon - 128×128px
    └── favicon-256.svg             # Favicon - 256×256px
```

Asset เพิ่มเติมใน `assets/logo/`:
```
assets/logo/
├── logo-full.svg       # Mark + wordmark (แนวนอน)
├── logo-mark.svg       # สัญลักษณ์เข็มทิศอย่างเดียว (120×120px)
├── logo-wordmark.svg   # ข้อความอย่างเดียว
├── logo-icon.svg       # App icon (512×512, มุมมน)
├── favicon.svg         # Optimized 16×16
├── logo-white.svg      # เวอร์ชันสีขาวสำหรับพื้นหลังมืด
└── logo-black.svg      # เวอร์ชัน monochrome สีดำ
```

## ภาพรวม Asset

### แนวคิดการออกแบบ (V3.0)

**เข็มทิศพร้อม Code Bracket** — การนำทางผสานกับโค้ด:
- **วงเข็มทิศ** = Navigation, การหาทิศทางของคุณ
- **เข็มเหนือ (สีเขียว)** = ทิศทาง, ความก้าวหน้าในเส้นทางการเรียนรู้
- **เข็มใต้ (สีดำ)** = ความมั่นคง, รากฐานที่แข็งแกร่ง
- **`>` Bracket** = Terminal prompt, โค้ด, บริบท CLI
- **เส้น Tick** = ความแม่นยำ, การเรียนรู้อย่างมีโครงสร้าง

### Logo

**ไฟล์**:
- `logos/claude-howto-logo.svg` (Light mode)
- `logos/claude-howto-logo-dark.svg` (Dark mode)

**ข้อกำหนด**:
- **ขนาด**: 520×120 px
- **วัตถุประสงค์**: Logo header/branding หลักพร้อม wordmark
- **การใช้งาน**:
  - Header เว็บไซต์
  - README badge
  - สื่อการตลาด
  - สื่อสิ่งพิมพ์
- **รูปแบบ**: SVG (ปรับขนาดได้อย่างสมบูรณ์)
- **โหมด**: Light (พื้นหลังสีขาว) และ Dark (พื้นหลัง #0A0A0A)

### Icon

**ไฟล์**:
- `icons/claude-howto-icon.svg` (Light mode)
- `icons/claude-howto-icon-dark.svg` (Dark mode)

**ข้อกำหนด**:
- **ขนาด**: 256×256 px
- **วัตถุประสงค์**: App icon, avatar, thumbnail
- **การใช้งาน**:
  - App icon
  - Profile avatar
  - Social media thumbnail
  - เอกสาร header
- **รูปแบบ**: SVG (ปรับขนาดได้อย่างสมบูรณ์)
- **โหมด**: Light (พื้นหลังสีขาว) และ Dark (พื้นหลัง #0A0A0A)

**องค์ประกอบการออกแบบ**:
- วงเข็มทิศพร้อมเส้น tick แบบ cardinal และ intercardinal
- เข็มเหนือสีเขียว (ทิศทาง/คำแนะนำ)
- เข็มใต้สีดำ (รากฐาน)
- `>` code bracket ตรงกลาง (terminal/CLI)
- จุดตรงกลางสีเขียวเป็นสีเน้น

### Favicon

เวอร์ชัน optimized หลายขนาดสำหรับการใช้งานบนเว็บ:

| ไฟล์ | ขนาด | DPI | การใช้งาน |
|------|------|-----|----------|
| `favicon-16.svg` | 16×16 px | 1x | Browser tab (เบราว์เซอร์เก่า) |
| `favicon-32.svg` | 32×32 px | 1x | Favicon เบราว์เซอร์มาตรฐาน |
| `favicon-64.svg` | 64×64 px | 1x-2x | จอแสดงผล High-DPI |
| `favicon-128.svg` | 128×128 px | 2x | Apple touch icon, bookmark |
| `favicon-256.svg` | 256×256 px | 4x | เบราว์เซอร์สมัยใหม่, PWA icon |

**หมายเหตุการ Optimize**:
- 16px: เรขาคณิตขั้นต่ำ — วง, เข็ม, chevron เท่านั้น
- 32px: เพิ่มเส้น tick แบบ cardinal
- 64px+: รายละเอียดครบถ้วนพร้อมเส้น tick แบบ intercardinal
- ทุกขนาดคงความสอดคล้องทาง visual กับ icon หลัก
- รูปแบบ SVG รับประกันการแสดงผลที่คมชัดในทุกขนาด

## การรวมเข้ากับ HTML

### การตั้งค่า Favicon พื้นฐาน

```html
<!-- Browser favicon -->
<link rel="icon" type="image/svg+xml" href="/resources/favicons/favicon-32.svg">
<link rel="icon" type="image/svg+xml" href="/resources/favicons/favicon-16.svg" sizes="16x16">

<!-- Apple touch icon (mobile home screen) -->
<link rel="apple-touch-icon" href="/resources/favicons/favicon-128.svg">

<!-- PWA & modern browsers -->
<link rel="icon" type="image/svg+xml" href="/resources/favicons/favicon-256.svg" sizes="256x256">
```

### การตั้งค่าแบบครบถ้วน

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

## Color Palette

### สีหลัก
- **Black**: `#000000` (ข้อความหลัก, stroke, เข็มใต้)
- **White**: `#FFFFFF` (พื้นหลัง Light)
- **Gray**: `#6B7280` (ข้อความรอง, เส้น tick รอง)

### สีเน้น
- **Bright Green**: `#22C55E` (เข็มเหนือ, center dot, เส้นเน้น — ใช้เป็น highlight เท่านั้น ไม่ใช้เป็นพื้นหลัง)

### Dark Mode
- **พื้นหลัง**: `#0A0A0A` (เกือบดำ)

### CSS Variables
```css
--color-primary: #000000;
--color-secondary: #6B7280;
--color-accent: #22C55E;
--color-bg-light: #FFFFFF;
--color-bg-dark: #0A0A0A;
```

### Tailwind Config
```js
colors: {
  brand: {
    primary: '#000000',
    secondary: '#6B7280',
    accent: '#22C55E',
  }
}
```

### หลักเกณฑ์การใช้งาน
- ใช้สีดำสำหรับข้อความหลักและองค์ประกอบเชิงโครงสร้าง
- ใช้สีเทาสำหรับองค์ประกอบรอง/องค์ประกอบสนับสนุน
- ใช้สีเขียว **เฉพาะ** สำหรับ highlight — เข็ม, จุด, เส้นเน้น
- ห้ามใช้สีเขียวเป็นสีพื้นหลัง
- คงอัตราส่วน contrast ระดับ WCAG AA (ขั้นต่ำ 4.5:1)

## หลักเกณฑ์การออกแบบ

### การใช้งาน Logo
- ใช้บนพื้นหลังสีขาวหรือมืด (#0A0A0A)
- ปรับขนาดตามสัดส่วน
- เว้น clear space รอบ logo (ขั้นต่ำ: ความสูง logo / 2)
- ใช้เวอร์ชัน light/dark ที่ให้มาให้เหมาะสมกับพื้นหลัง

### การใช้งาน Icon
- ใช้ที่ขนาดมาตรฐาน: 16, 32, 64, 128, 256px
- คงสัดส่วนของเข็มทิศ
- ปรับขนาดตามสัดส่วน

### การใช้งาน Favicon
- ใช้ขนาดที่เหมาะสมกับบริบท
- 16-32px: Browser tab, bookmark
- 64px: Favicon site icon
- 128px+: หน้าจอ home ของ Apple/Android

## การ Optimize SVG

ไฟล์ SVG ทั้งหมดเป็นการออกแบบแบบ flat โดยไม่มี gradient หรือ filter:
- เรขาคณิตแบบ stroke ที่สะอาด
- ไม่มี raster ฝังอยู่
- Path ที่ optimize แล้ว
- viewBox แบบ responsive

สำหรับการ optimize บนเว็บ:
```bash
# Compress SVG while maintaining quality
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

## การแปลง PNG

เพื่อแปลง SVG เป็น PNG สำหรับรองรับเบราว์เซอร์เก่า:

```bash
# Using ImageMagick
convert -density 300 -background none favicon-256.svg favicon-256.png

# Using Inkscape
inkscape -D -z --file=favicon-256.svg --export-png=favicon-256.png
```

## Accessibility

- อัตราส่วนสี contrast สูง (WCAG AA compliant — ขั้นต่ำ 4.5:1)
- รูปทรงเรขาคณิตที่สะอาดและจดจำได้ในทุกขนาด
- รูปแบบ vector ที่ปรับขนาดได้
- ไม่มีข้อความใน icon (ข้อความเพิ่มแยกต่างหากใน wordmark)
- ไม่มีการพึ่งพาสีแดง-เขียวในการสื่อความหมาย

## การระบุที่มา

Asset เหล่านี้เป็นส่วนหนึ่งของโปรเจกต์ Claude How To

**License**: MIT (ดูไฟล์ LICENSE ของโปรเจกต์)

## ประวัติเวอร์ชัน

- **v3.0** (กุมภาพันธ์ 2026): การออกแบบ Compass-bracket พร้อม palette Black/White/Gray + Green accent
- **v2.0** (มกราคม 2026): การออกแบบ 12-ray starburst แบบ Claude พร้อม palette emerald
- **v1.0** (มกราคม 2026): การออกแบบ icon แบบ hexagon-based ดั้งเดิม

---

**อัปเดตล่าสุด**: กุมภาพันธ์ 2026  
**เวอร์ชันปัจจุบัน**: 3.0 (Compass-Bracket)  
**ทุก Asset**: SVG พร้อมใช้งานระดับ production, ปรับขนาดได้อย่างสมบูรณ์, ผ่านมาตรฐาน WCAG AA
