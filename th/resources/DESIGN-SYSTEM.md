<!-- i18n-source: resources/DESIGN-SYSTEM.md -->
<!-- i18n-date: 2026-07-15 -->

# Claude How To - Design System

## เอกลักษณ์ Visual

### แนวคิดการออกแบบ Icon: เข็มทิศพร้อม Code Bracket

Icon ของ Claude How To ใช้ **เข็มทิศพร้อม `>` code bracket** เพื่อแสดงถึงการนำทางผ่านโค้ดอย่างมีคำแนะนำ:

```
     N (green)
     ▲
     │
W ───>─── E     Compass = Guidance/Direction
     │          > Bracket = Code/Terminal/CLI
     ▼
     S (black)
```

สิ่งนี้สร้าง:
- **ความชัดเจน Visual**: สื่อสารถึง "คู่มือนำทางโค้ด" ได้ทันที
- **ความหมายเชิงสัญลักษณ์**: เข็มทิศ = การหาทิศทาง; `>` = โค้ด/terminal
- **Scalability**: ใช้งานได้ในทุกขนาดตั้งแต่ 16px ถึง 512px
- **การสอดคล้องกับแบรนด์**: เข้ากับ aesthetic ของเครื่องมือสำหรับนักพัฒนาด้วย palette ที่เรียบง่าย

---

## ระบบสี

### Palette

| สี | Hex | RGB | การใช้งาน |
|----|-----|-----|----------|
| Black (Primary) | `#000000` | 0, 0, 0 | Stroke หลัก, ข้อความ, เข็มใต้ |
| White (Background) | `#FFFFFF` | 255, 255, 255 | พื้นหลัง Light mode |
| Gray (Secondary) | `#6B7280` | 107, 114, 128 | เส้น tick รอง, ข้อความรอง |
| Bright Green (Accent) | `#22C55E` | 34, 197, 94 | เข็มเหนือ, center dot, เส้นเน้น |
| Near Black (Dark BG) | `#0A0A0A` | 10, 10, 10 | พื้นหลัง Dark mode |

### อัตราส่วน Contrast (WCAG)

- Black บน White: **21:1** AAA
- Gray บน White: **4.6:1** AA
- Green บน White: **3.2:1** (decorative เท่านั้น, ไม่ใช้สำหรับข้อความ)
- White บน Dark: **19.5:1** AAA

### กฎสำหรับสี Accent

**Bright Green (#22C55E) สงวนไว้สำหรับ highlight เท่านั้น:**
- เข็มเหนือของเข็มทิศ
- Center dot
- Accent underline/border
- ห้ามใช้เป็น background color
- ห้ามใช้สำหรับ body text

---

## Typography

### Logo Font
- **Family**: Inter, SF Pro Display, -apple-system, Segoe UI, sans-serif
- **"Claude"**: 42px, weight 700 (bold), Black
- **"How-To"**: 32px, weight 500 (medium), Gray (#6B7280)
- **Subtitle**: 10px, weight 500, Gray, letter-spacing 1.5px, uppercase

### Interface Font
- **Family**: Inter, SF Pro, system fonts (sans-serif)
- **Weight**: 400-600
- **สไตล์**: สะอาด, อ่านง่าย

---

## รายละเอียด Icon

### ข้อกำหนดเข็มทิศ

Compass mark สร้างขึ้นจาก element เชิงเรขาคณิตเหล่านี้:

```
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

### การเพิ่มขึ้นตามขนาด

```
16px  → Ring + needles + chevron only (minimal)
32px  → Adds cardinal tick marks
64px  → Adds intercardinal tick marks
128px → Full detail, all elements crisp
256px → Maximum detail, thick strokes
```

---

## หลักเกณฑ์ขนาด

### ขนาด Logo

- **ขั้นต่ำ**: 200px ความกว้าง (สำหรับเว็บ)
- **แนะนำ**: 520px (ขนาด native)
- **สูงสุด**: ไม่จำกัด (รูปแบบ vector)
- **Aspect Ratio**: ~4.3:1 (กว้าง:สูง)

### ขนาด Icon

- **ขั้นต่ำ**: 16px (favicon)
- **แนะนำ**: 64-256px (app, avatar)
- **สูงสุด**: ไม่จำกัด (รูปแบบ vector)
- **Aspect Ratio**: 1:1 (สี่เหลี่ยมจัตุรัส)

---

## Spacing & Alignment

### ระยะห่าง Logo

```
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

### จุดกึ่งกลาง Icon

Icon ทุกตัวจัดกึ่งกลางที่จุดกลางของ canvas:
- 128×128 สำหรับ canvas 256px
- 64×64 สำหรับ canvas 128px
- รักษาการจัดแนวให้ตรงกับ UI element อื่น

---

## Accessibility

### Contrast ของสี
- ข้อความทั้งหมดผ่านมาตรฐาน WCAG AA (ขั้นต่ำ 4.5:1)
- สีเขียว accent เป็น decorative ไม่ใช่ informational
- ไม่มีการพึ่งพาสีแดง-เขียวในการสื่อความหมาย

### Scalability
- รูปแบบ vector ให้ความคมชัดในทุกขนาด
- รูปทรงเรขาคณิตยังคงจดจำได้ที่ขนาด 16px
- รายละเอียดเพิ่มขึ้นตามขนาดที่มี

---

## ตัวอย่างการใช้งาน

### Web Header
- ขนาด: logo 520×120px
- ไฟล์: `logos/claude-howto-logo.svg`
- Background: White หรือ dark (#0A0A0A)
- Padding: ขั้นต่ำ 20px

### App Icon
- ขนาด: 256×256px
- ไฟล์: `icons/claude-howto-icon.svg`
- Background: White หรือ dark
- การใช้งาน: App shortcut, avatar

### Browser Favicon
- ขนาด: 32px (primary), 16px (fallback)
- ไฟล์: `favicons/favicon-32.svg`
- รูปแบบ: SVG เพื่อการแสดงผลที่คมชัด

### Social Media
- Profile: icon 256×256px
- Banner: logo 520×120px (จัดกึ่งกลาง)

### เอกสาร
- Chapter Header: logo ปรับขนาดให้พอดี
- Section Icon: favicon 64×64px
- Inline: favicon 32×32px

---

## รายละเอียดรูปแบบไฟล์

### โครงสร้าง SVG

ไฟล์ SVG ทั้งหมดเป็น flat design:
- ไม่มี gradient (สีทึบเท่านั้น)
- ไม่มี filter effect (ไม่มี blur, glow, หรือ shadow)
- รูปทรง stroke และ fill ที่สะอาด
- ViewBox สำหรับ responsive scaling
- โค้ดที่อ่านง่าย มี comment

### ความเข้ากันได้ข้ามเบราว์เซอร์

- Chrome/Edge: รองรับเต็มรูปแบบ
- Firefox: รองรับเต็มรูปแบบ
- Safari: รองรับเต็มรูปแบบ
- iOS Safari: รองรับเต็มรูปแบบ
- เบราว์เซอร์สมัยใหม่ทั้งหมด: รองรับเต็มรูปแบบ

---

## การปรับแต่ง

### การเปลี่ยนสี Accent

เพื่อสร้าง variant ที่มีสี accent ต่างออกไป:

1. แทนที่ `#22C55E` ทุกตำแหน่งด้วยสี accent ของคุณ
2. ตรวจสอบให้อัตราส่วน contrast อยู่เหนือ 3:1 สำหรับ decorative element
3. คงโครงสร้างสี black/white/gray ไว้ไม่เปลี่ยนแปลง

### การปรับขนาด

```css
svg {
  width: 256px;
  height: 256px;
}
```

SVG ปรับขนาดโดยอัตโนมัติผ่าน viewBox — ไม่จำเป็นต้องใช้ transform

---

## Version Control

ติดตามการเปลี่ยนแปลงการออกแบบใน git:
- Version ไฟล์ SVG ตามปกติ (เป็นไฟล์ text)
- Tag release ที่มีการเปลี่ยนแปลงการออกแบบ
- รวม DESIGN-SYSTEM.md ไว้ใน commit

---

**อัปเดตล่าสุด**: กุมภาพันธ์ 2026
**เวอร์ชัน Design System**: 3.0
