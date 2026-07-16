<!-- i18n-source: 08-checkpoints/checkpoint-examples.md -->
<!-- i18n-date: 2026-05-08 -->

# ตัวอย่าง Checkpoint

ตัวอย่างจากสถานการณ์จริงของการใช้ checkpoints อย่างมีประสิทธิภาพใน Claude Code

หมายเหตุ: Checkpoints ถูกสร้างโดยอัตโนมัติพร้อมกับทุก prompt ของผู้ใช้ คุณไม่จำเป็นต้องบันทึกด้วยตนเอง หากต้องการ rewind ให้กด `Esc` สองครั้ง (`Esc+Esc`) หรือใช้ `/rewind` เพื่อเปิด checkpoint browser

## ตัวอย่างที่ 1: การโยกย้ายฐานข้อมูล

### สถานการณ์
คุณต้องโยกย้ายจาก MySQL ไปยัง PostgreSQL แต่ต้องการสำรวจทั้งแนวทางการโยกย้ายโดยตรงและแนวทาง dual-write แบบค่อยเป็นค่อยไป

### ขั้นตอนการทำงาน

```
ผู้ใช้: มาใช้งานการโยกย้ายโดยตรงจาก MySQL ไปยัง PostgreSQL กัน
      [สร้าง Checkpoint A โดยอัตโนมัติ]

Claude: ฉันจะใช้งานการโยกย้ายโดยตรง...
[เปลี่ยน database driver อัปเดต queries แก้ไข schema]

ผู้ใช้: รันการทดสอบ
      [สร้าง Checkpoint B โดยอัตโนมัติ]

Claude: กำลังรันการทดสอบ...
❌ การทดสอบ 15 รายการล้มเหลว - ปัญหา connection pool

ผู้ใช้: แนวทางนี้มีปัญหา มาลอง dual-write pattern แทน
[ผู้ใช้กด Esc+Esc เลือก Checkpoint A เลือก "Restore code and conversation"]

ผู้ใช้: ตอนนี้ใช้งาน dual-write pattern ที่เขียนไปยังทั้งสองฐานข้อมูล

Claude: ฉันจะใช้งาน dual-write migration...
[ใช้งาน dual-write layer กลยุทธ์การโยกย้ายแบบค่อยเป็นค่อยไป]

ผู้ใช้: รันการทดสอบ

Claude: กำลังรันการทดสอบ...
✅ การทดสอบทั้งหมดผ่าน

ผู้ใช้: แนวทาง dual-write ปลอดภัยกว่าอย่างชัดเจน มา commit กัน
```

## ตัวอย่างที่ 2: การปรับประสิทธิภาพ

### สถานการณ์
มีกลยุทธ์การปรับประสิทธิภาพหลายอย่างที่ต้องลอง

### ขั้นตอนการทำงาน

```
ผู้ใช้: มาปรับเวลาตอบสนองของ API ให้ดีขึ้น ปัจจุบัน: 450ms
      [สร้าง Checkpoint "Baseline" โดยอัตโนมัติ]

Claude: ฉันจะเพิ่ม database query caching...
[ใช้งาน Redis caching]

ผู้ใช้: รันการทดสอบประสิทธิภาพ

Claude: ผลลัพธ์: เวลาตอบสนองเฉลี่ย 280ms (ปรับปรุง 38%)

ผู้ใช้: ลองแนวทางอื่น
[ผู้ใช้กด Esc+Esc เลือก checkpoint "Baseline" เลือก "Restore code and conversation"]

ผู้ใช้: ลองปรับ database query แทน

Claude: ฉันจะปรับ database queries...
[เพิ่ม indexes ปรับ N+1 queries]

ผู้ใช้: รันการทดสอบประสิทธิภาพ

Claude: ผลลัพธ์: เวลาตอบสนองเฉลี่ย 180ms (ปรับปรุง 60%)

ผู้ใช้: ลองแนวทางที่สามด้วย
[ผู้ใช้กด Esc+Esc เลือก checkpoint "Baseline" เลือก "Restore code and conversation"]

ผู้ใช้: ลอง response compression และ CDN

Claude: ฉันจะเพิ่ม compression และ CDN...
[ใช้งาน gzip ตั้งค่า CDN]

ผู้ใช้: รันการทดสอบประสิทธิภาพ

Claude: ผลลัพธ์: เวลาตอบสนองเฉลี่ย 320ms (ปรับปรุง 29%)

ผู้ใช้: การปรับ query ดีที่สุด ขอย้อนกลับและรวมกับ caching
[ผู้ใช้กด Esc+Esc เลือก checkpoint หลังการปรับ query เลือก "Restore code and conversation"]

ผู้ใช้: ตอนนี้เพิ่ม Redis caching บน queries ที่ปรับแล้ว

Claude: [เพิ่ม Redis caching บน queries ที่ปรับแล้ว]

ผู้ใช้: รันการทดสอบประสิทธิภาพ

Claude: ผลลัพธ์: เวลาตอบสนองเฉลี่ย 95ms (ปรับปรุง 79%) 🎉

ผู้ใช้: สมบูรณ์แบบ! นี่คือผู้ชนะ มา commit กัน
```

## ตัวอย่างที่ 3: การวนซ้ำ UI/UX

### สถานการณ์
ลองเลย์เอาต์ต่างๆ สำหรับ dashboard

### ขั้นตอนการทำงาน

```
ผู้ใช้: มาออกแบบ dashboard ใหม่ด้วยเลย์เอาต์ sidebar
      [สร้าง Checkpoint "Start" โดยอัตโนมัติ]

Claude: [ใช้งานเลย์เอาต์ sidebar]

ผู้ใช้: แสดง screenshot ให้ดูหน่อย

Claude: [แสดง screenshot]

ผู้ใช้: sidebar รู้สึกแคบเกินไป มาลอง top navigation แทน
[ผู้ใช้กด Esc+Esc เลือก checkpoint "Start" เลือก "Restore code and conversation"]

ผู้ใช้: ลองเลย์เอาต์ top navigation

Claude: [ใช้งาน top navigation]

ผู้ใช้: แสดง screenshot ให้ดูหน่อย

Claude: [แสดง screenshot]

ผู้ใช้: ดีขึ้น แต่ลองเลย์เอาต์ card-based grid บ้าง
[ผู้ใช้กด Esc+Esc เลือก checkpoint "Start" เลือก "Restore code and conversation"]

ผู้ใช้: ลองเลย์เอาต์ card-based grid

Claude: [ใช้งาน card grid]

ผู้ใช้: แสดง screenshot ให้ดูหน่อย

Claude: [แสดง screenshot]

ผู้ใช้: ดีมาก! แต่รวม top nav กับ card grid ได้ไหม?
[ผู้ใช้กด Esc+Esc เลือก checkpoint หลัง card grid เลือก "Restore code and conversation"]

ผู้ใช้: เพิ่ม top navigation ให้กับ card grid layout

Claude: [เพิ่ม top navigation ให้กับ card grid]

ผู้ใช้: สมบูรณ์แบบ! นี่คือการออกแบบสุดท้าย
```

## ตัวอย่างที่ 4: เซสชันการ Debugging

### สถานการณ์
ค้นหาข้อบกพร่องที่ยุ่งยากด้วยหลายสมมติฐาน

### ขั้นตอนการทำงาน

```
ผู้ใช้: มี memory leak ในแอปพลิเคชัน
      [สร้าง Checkpoint "Before debugging" โดยอัตโนมัติ]

Claude: ให้ฉันตรวจสอบ...
[วิเคราะห์โค้ด]

ผู้ใช้: คิดว่าอยู่ที่ event listeners มาแก้ไขดูกัน

Claude: [แก้ไข event listener cleanup]

ผู้ใช้: รัน memory profiler

Claude: ยังมี memory leak อยู่ — event listeners ไม่ใช่สาเหตุ

ผู้ใช้: ขอย้อนกลับและลองสมมติฐานอื่น
[ผู้ใช้กด Esc+Esc เลือก checkpoint "Before debugging" เลือก "Restore code and conversation"]

ผู้ใช้: บางทีอาจเป็น database connections?

Claude: [ใช้งานการแก้ไข connection pooling]

ผู้ใช้: รัน memory profiler

Claude: ยังมี leak อยู่ — ไม่ใช่ connections เช่นกัน

ผู้ใช้: ขอย้อนกลับและลองมุมมองอื่น
[ผู้ใช้กด Esc+Esc เลือก checkpoint "Before debugging" เลือก "Restore code and conversation"]

ผู้ใช้: มาตรวจสอบ circular references กัน

Claude: [ค้นพบและแก้ไข circular references ใน cache]

ผู้ใช้: รัน memory profiler

Claude: ✅ Memory leak แก้ไขแล้ว! Circular references ใน caching layer เป็นสาเหตุ

ผู้ใช้: ยอดเยี่ยม! มา commit การแก้ไขนี้กัน
```

## ตัวอย่างที่ 5: วิวัฒนาการการออกแบบ API

### สถานการณ์
ออกแบบ REST API ด้วยการวนซ้ำหลายครั้ง

### ขั้นตอนการทำงาน

```
ผู้ใช้: สร้าง REST API สำหรับแพลตฟอร์ม blog ของเรา
      [สร้าง Checkpoint "Before API design" โดยอัตโนมัติ]

Claude: [สร้าง basic CRUD API]

ผู้ใช้: มันเรียบง่ายเกินไป มาเพิ่ม pagination และ filtering กัน

Claude: [เพิ่ม pagination และ filtering]

ผู้ใช้: เราต้องการความสัมพันธ์ระหว่าง resource ที่ดีขึ้น

Claude: [ใช้งาน HATEOAS links]

ผู้ใช้: จริงๆ แล้วลอง GraphQL แทน REST ดีกว่า
[ผู้ใช้กด Esc+Esc เลือก checkpoint "Before API design" เลือก "Restore code and conversation"]

ผู้ใช้: ใช้งาน GraphQL API สำหรับแพลตฟอร์ม blog แทน

Claude: [ใช้งาน GraphQL API]

ผู้ใช้: คิดว่า REST เหมาะกับ use case ของเรามากกว่า
[ผู้ใช้กด Esc+Esc เลือก checkpoint หลัง HATEOAS เลือก "Restore code and conversation"]

ผู้ใช้: มาสรุปแนวทาง REST กัน
```

## ตัวอย่างที่ 6: การจัดการ Configuration

### สถานการณ์
ทดสอบแนวทาง configuration ต่างๆ

### ขั้นตอนการทำงาน

```
ผู้ใช้: ย้าย configuration ไปยัง environment variables
      [สร้าง Checkpoint "Original config" โดยอัตโนมัติ]

Claude: [ใช้งาน env var configuration]

ผู้ใช้: ทดสอบใน development

Claude: ทำงานได้ในเครื่อง แต่มีปัญหา deployment ใน production

ผู้ใช้: ลองแนวทางอื่น
[ผู้ใช้กด Esc+Esc เลือก checkpoint "Original config" เลือก "Restore code and conversation"]

ผู้ใช้: ลองแนวทาง config file พร้อม validation

Claude: [ใช้งาน YAML config พร้อม JSON schema validation]

ผู้ใช้: ทดสอบใน development

Claude: ✅ ทำงานได้ดี มี validation errors ที่ดี

ผู้ใช้: รองรับ env vars สำหรับค่าที่ sensitive ได้ไหม?

Claude: [เพิ่ม env var override สำหรับ secrets]

ผู้ใช้: ทดสอบ deployment

Claude: ✅ ทุก environment ทำงานได้ถูกต้อง

ผู้ใช้: สมบูรณ์แบบ! พร้อมสำหรับ production แล้ว
```

## ตัวอย่างที่ 7: กลยุทธ์การทดสอบ

### สถานการณ์
ใช้งานการทดสอบแบบครอบคลุม

### ขั้นตอนการทำงาน

```
ผู้ใช้: เพิ่ม unit tests สำหรับ auth module
      [สร้าง Checkpoint โดยอัตโนมัติ]

Claude: [เพิ่ม Jest unit tests]

ผู้ใช้: รันการทดสอบ

Claude: การทดสอบ 45 รายการผ่าน coverage 78%

ผู้ใช้: เพิ่ม integration tests ด้วย

Claude: [เพิ่ม integration tests]

ผู้ใช้: รันการทดสอบ

Claude: การทดสอบ 89 รายการผ่าน coverage 92% แต่การทดสอบช้า (3 นาที)

ผู้ใช้: การทดสอบช้าเกินไป มาปรับให้เร็วขึ้น

Claude: [ปรับ test setup เพิ่ม parallel execution]

ผู้ใช้: รันการทดสอบ

Claude: การทดสอบ 89 รายการผ่าน coverage 92% 35 วินาที ✅

ผู้ใช้: ดีมาก! ตอนนี้เพิ่ม E2E tests สำหรับ critical paths

Claude: [เพิ่ม Playwright E2E tests]

ผู้ใช้: รันการทดสอบทั้งหมด

Claude: การทดสอบ 112 รายการผ่าน coverage 94% 2 นาที

ผู้ใช้: สมดุลระหว่าง coverage และความเร็วสมบูรณ์แบบ!
```

## ตัวอย่างที่ 8: การใช้ Summarize from Checkpoint

### สถานการณ์
หลังจากเซสชัน debugging ที่ยาวนาน คุณต้องการย่อการสนทนาในขณะที่ยังคงบริบทไว้

### ขั้นตอนการทำงาน

```
ผู้ใช้: [หลังจากข้อความ debugging และการสำรวจกว่า 20 ข้อความ]

[ผู้ใช้กด Esc+Esc เลือก checkpoint ต้นๆ เลือก "Summarize from here"]
[อาจระบุคำสั่งเพิ่มเติม: "เน้นที่สิ่งที่เราลองและสิ่งที่ได้ผล"]

Claude: [สร้างสรุปของการสนทนาจากจุดนั้นเป็นต้นไป]
[ข้อความต้นฉบับยังคงอยู่ใน transcript]
[สรุปแทนที่การสนทนาที่มองเห็น ลดการใช้ context window]

ผู้ใช้: ตอนนี้มาดำเนินต่อด้วยแนวทางที่ได้ผล
```

## ข้อสรุปสำคัญ

1. **Checkpoints อัตโนมัติ**: ทุก prompt ของผู้ใช้สร้าง checkpoint — ไม่ต้องบันทึกด้วยตนเอง
2. **ใช้ Esc+Esc หรือ /rewind**: สองวิธีในการเข้าถึง checkpoint browser
3. **เลือกตัวเลือก restore ที่เหมาะสม**: กู้คืนโค้ด, การสนทนา, ทั้งสอง, หรือสรุป ขึ้นอยู่กับความต้องการ
4. **ไม่ต้องกลัวการทดลอง**: Checkpoints ทำให้การลองเปลี่ยนแปลงครั้งใหญ่ปลอดภัย
5. **ใช้ร่วมกับ git**: ใช้ checkpoints สำหรับการสำรวจ git สำหรับงานที่สรุปแล้ว
6. **สรุปเซสชันที่ยาวนาน**: ใช้ "Summarize from here" เพื่อให้การสนทนาจัดการได้

---
**อัปเดตล่าสุด**: 6 พฤษภาคม 2026
**Claude Code Version**: 2.1.131
**แหล่งข้อมูล**:
- https://code.claude.com/docs/en/checkpointing
- https://code.claude.com/docs/en/changelog
