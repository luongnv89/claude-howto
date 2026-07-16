<!-- i18n-source: clean-code-rules.md -->
<!-- i18n-date: 2026-05-09 -->

# กฎ Clean Code สำหรับการสร้างโค้ดด้วย AI

กฎเหล่านี้เป็นแนวทางสำหรับการสร้างโค้ดที่มีคุณภาพระดับมืออาชีพและสามารถบำรุงรักษาได้

## การตั้งชื่อที่มีความหมาย
- ใช้ชื่อที่แสดงเจตนาอธิบายว่าสิ่งนั้นมีอยู่เพื่ออะไร
- หลีกเลี่ยงข้อมูลที่ทำให้เข้าใจผิดและความแตกต่างที่ไม่มีความหมาย (เช่น `data`, `info`, `manager`)
- ใช้ชื่อที่ออกเสียงได้และค้นหาได้
- ชื่อ class: คำนาม (เช่น `UserAccount`, `PaymentProcessor`)
- ชื่อ method: คำกริยา (เช่น `calculateTotal`, `sendEmail`)
- หลีกเลี่ยงการใช้ตัวย่อและการเข้ารหัส (Hungarian notation, prefixes)

## ฟังก์ชัน
- รักษาฟังก์ชันให้สั้น (อุดมคติคือน้อยกว่า 20 บรรทัด)
- ทำสิ่งเดียวเท่านั้น — Single Responsibility Principle
- ระดับ abstraction หนึ่งระดับต่อฟังก์ชัน
- จำกัด arguments: อุดมคติ 0-2 ตัว, สูงสุด 3 ตัว, หลีกเลี่ยง flag arguments
- ไม่มี side effects — ฟังก์ชันควรทำตามที่ชื่อบอก
- แยกคำสั่ง (เปลี่ยนสถานะ) จากคำถาม (คืนข้อมูล)
- ชอบ exceptions มากกว่า error codes

## ความคิดเห็น
- โค้ดควรอธิบายตัวเองได้ — หลีกเลี่ยงความคิดเห็นเมื่อเป็นไปได้
- ความคิดเห็นที่ดี: ข้อมูลทางกฎหมาย, คำเตือน, TODOs, เอกสาร public API
- ความคิดเห็นที่ไม่ดี: ซ้ำซ้อน, ทำให้เข้าใจผิด, หรืออธิบายโค้ดที่ไม่ดี
- ห้ามคอมเมนต์โค้ดออก — ลบมัน (version control รักษาประวัติ)
- ถ้าต้องการความคิดเห็น ให้พิจารณา refactoring โค้ดแทน

## การจัดรูปแบบ
- รักษาไฟล์ให้เล็กและมุ่งเน้น
- การจัดรูปแบบแนวตั้ง: แนวคิดที่เกี่ยวข้องใกล้กัน, บรรทัดว่างแยกแนวคิด
- การจัดรูปแบบแนวนอน: จำกัดความยาวบรรทัด (80-120 ตัวอักษร)
- ใช้การเยื้องและสไตล์ทีมที่สอดคล้องกัน
- จัดกลุ่มฟังก์ชันที่เกี่ยวข้องเข้าด้วยกัน

## Objects และโครงสร้างข้อมูล
- Objects: ซ่อนข้อมูลไว้ใน abstractions, เปิดเผยพฤติกรรมผ่าน methods
- โครงสร้างข้อมูล: เปิดเผยข้อมูล, มีพฤติกรรมน้อยที่สุด
- Law of Demeter: คุยกับเพื่อนทันทีเท่านั้น, หลีกเลี่ยง `a.getB().getC().doSomething()`
- ห้ามเปิดเผยโครงสร้างภายในผ่าน getters/setters อย่างไม่ตั้งใจ

## การจัดการข้อผิดพลาด
- ใช้ exceptions ไม่ใช่ return codes หรือ error flags
- เขียน `try-catch-finally` ก่อนเมื่อโค้ดอาจล้มเหลว
- ให้ context ใน exception messages
- ห้าม return `null` — คืน empty collections หรือใช้ Optional/Maybe
- ห้ามส่ง `null` เป็น arguments

## Classes
- Classes ขนาดเล็ก: วัดด้วยความรับผิดชอบ ไม่ใช่จำนวนบรรทัด
- Single Responsibility Principle: เหตุผลเดียวในการเปลี่ยนแปลง
- High cohesion: ตัวแปร class ถูกใช้โดย methods หลายตัว
- Low coupling: dependencies น้อยที่สุดระหว่าง classes
- Open/Closed Principle: เปิดสำหรับการขยาย, ปิดสำหรับการแก้ไข

## Unit Tests
- Fast, Independent, Repeatable, Self-validating, Timely (F.I.R.S.T.)
- หนึ่ง assert ต่อ test (หรือหนึ่งแนวคิด)
- คุณภาพโค้ด test เทียบเท่าโค้ด production
- ชื่อ test ที่อ่านได้ซึ่งอธิบายสิ่งที่กำลังทดสอบ
- รูปแบบ Arrange-Act-Assert

## หลักการคุณภาพโค้ด
- **DRY (Don't Repeat Yourself)**: ไม่มีการซ้ำซ้อน
- **YAGNI (You Aren't Gonna Need It)**: ไม่สร้างสำหรับอนาคตสมมติ
- **KISS (Keep It Simple)**: หลีกเลี่ยงความซับซ้อนที่ไม่จำเป็น
- **Boy Scout Rule**: ปล่อยโค้ดให้สะอาดกว่าที่พบ

## Code Smells ที่ควรหลีกเลี่ยง
- ฟังก์ชันหรือ classes ยาวเกินไป
- โค้ดที่ซ้ำซ้อน
- โค้ดที่ตายแล้ว (ตัวแปร, ฟังก์ชัน, parameters ที่ไม่ได้ใช้)
- Feature envy (method ที่สนใจ class อื่นมากกว่า)
- Inappropriate intimacy (classes ที่รู้เรื่องกันมากเกินไป)
- รายการ parameters ยาวเกินไป
- Primitive obsession (ใช้ primitives แทน small objects มากเกินไป)
- คำสั่ง Switch/case (พิจารณา polymorphism)
- Temporary fields (ตัวแปร class ที่ใช้เป็นบางครั้ง)

## Concurrency
- แยกโค้ด concurrent ออกจากโค้ดอื่น
- จำกัดขอบเขตของข้อมูล synchronized/locked
- ใช้ thread-safe collections
- รักษาส่วน synchronized ให้เล็ก
- รู้จัก execution models และ primitives

## การออกแบบระบบ
- แยกการก่อสร้างออกจากการใช้งาน (dependency injection)
- ใช้ factories, builders สำหรับการสร้าง object ที่ซับซ้อน
- โปรแกรมไปยัง interfaces ไม่ใช่ implementations
- ชอบ composition มากกว่า inheritance
- ใช้ design patterns เมื่อทำให้ง่ายขึ้น ไม่ใช่เพื่อแสดงความสามารถ

## การ Refactoring
- Refactor อย่างต่อเนื่อง ไม่ใช่ในชุดใหญ่
- ต้องมี tests ที่ผ่านก่อนและหลังเสมอ
- ขั้นตอนเล็ก: การเปลี่ยนแปลงหนึ่งครั้งต่อครั้ง
- การ refactoring ทั่วไป: Extract Method, Rename, Move, Inline

## เอกสาร
- โค้ดที่อธิบายตัวเองได้ > ความคิดเห็น > เอกสารภายนอก
- Public APIs ต้องการเอกสารที่ชัดเจน
- รวมตัวอย่างในเอกสาร
- รักษาเอกสารให้ใกล้กับโค้ด (อุดมคติคืออยู่ในโค้ด)

---

**ปรัชญาหลัก**: โค้ดถูกอ่านมากกว่าที่เขียน 10 เท่า ปรับปรุงเพื่อความสามารถในการอ่านและการบำรุงรักษา ไม่ใช่ความชาญฉลาด

---
**อัปเดตล่าสุด**: 9 เมษายน 2026
