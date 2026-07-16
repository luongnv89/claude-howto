<!-- i18n-source: resources/QUICK-START.md -->
<!-- i18n-date: 2026-05-09 -->

# เริ่มต้นอย่างรวดเร็ว - Brand Assets

## คัดลอก Asset ไปยังโปรเจกต์ของคุณ

```bash
# คัดลอก resource ทั้งหมดไปยัง web project
cp -r resources/ /path/to/your/website/

# หรือเฉพาะ favicon สำหรับเว็บ
cp resources/favicons/* /path/to/your/website/public/
```

## เพิ่มใน HTML (คัดลอกและวาง)

```html
<!-- Favicons -->
<link rel="icon" type="image/svg+xml" href="/resources/favicons/favicon-32.svg" sizes="32x32">
<link rel="icon" type="image/svg+xml" href="/resources/favicons/favicon-16.svg" sizes="16x16">
<link rel="apple-touch-icon" href="/resources/favicons/favicon-128.svg">
<link rel="icon" type="image/svg+xml" href="/resources/favicons/favicon-256.svg" sizes="256x256">
<meta name="theme-color" content="#000000">
```

## ใช้งานใน Markdown/เอกสาร

```markdown
# Claude How To

![Claude How To Logo](resources/logos/claude-howto-logo.svg)

![Icon](resources/icons/claude-howto-icon.svg)
```

## ขนาดที่แนะนำ

| วัตถุประสงค์ | ขนาด | ไฟล์ |
|-------------|------|------|
| Website header | 520×120 | `logos/claude-howto-logo.svg` |
| App icon | 256×256 | `icons/claude-howto-icon.svg` |
| Browser tab | 32×32 | `favicons/favicon-32.svg` |
| Mobile home screen | 128×128 | `favicons/favicon-128.svg` |
| Desktop app | 256×256 | `favicons/favicon-256.svg` |
| Small avatar | 64×64 | `favicons/favicon-64.svg` |

## ค่าสี

```css
/* ใช้ใน CSS */
--color-primary: #000000;
--color-secondary: #6B7280;
--color-accent: #22C55E;
--color-bg-light: #FFFFFF;
--color-bg-dark: #0A0A0A;
```

## ความหมายของการออกแบบ Icon

**เข็มทิศพร้อม Code Bracket**:
- วงเข็มทิศ = Navigation, เส้นทางการเรียนรู้ที่มีโครงสร้าง
- เข็มเหนือสีเขียว = ทิศทาง, ความก้าวหน้า, การนำทาง
- เข็มใต้สีดำ = ความมั่นคง, รากฐานที่แข็งแกร่ง
- `>` bracket = Terminal prompt, โค้ด, บริบท CLI
- เส้น Tick = ความแม่นยำ, ขั้นตอนที่มีโครงสร้าง

นี่คือสัญลักษณ์ของ "การหาทิศทางผ่านโค้ดด้วยการนำทางที่ชัดเจน"

## จะใช้อะไรที่ไหน

### เว็บไซต์
- **Header**: Logo (`logos/claude-howto-logo.svg`)
- **Favicon**: 32px (`favicons/favicon-32.svg`)
- **Social preview**: Icon (`icons/claude-howto-icon.svg`)

### GitHub
- **README badge**: Icon (`icons/claude-howto-icon.svg`) ที่ 64–128px
- **Repository avatar**: Icon (`icons/claude-howto-icon.svg`)

### Social Media
- **Profile picture**: Icon (`icons/claude-howto-icon.svg`)
- **Banner**: Logo (`logos/claude-howto-logo.svg`)
- **Thumbnail**: Icon ที่ 256×256px

### เอกสาร
- **Chapter header**: Logo หรือ icon (ปรับขนาดให้พอดี)
- **Navigation icon**: Favicon (32–64px)

---

ดู [README.md](README.md) สำหรับเอกสารฉบับสมบูรณ์
