<!-- i18n-source: 02-memory/directory-api-CLAUDE.md -->
<!-- i18n-date: 2026-05-09 -->
# มาตรฐานโมดูล API

ไฟล์นี้แทนที่ CLAUDE.md ระดับรากสำหรับทุกอย่างใน /src/api/

## มาตรฐานเฉพาะ API

### การตรวจสอบคำขอ (Request Validation)
- ใช้ Zod สำหรับการตรวจสอบ schema
- ตรวจสอบ input ทุกครั้ง
- ส่งคืน 400 พร้อมข้อมูลข้อผิดพลาดในการตรวจสอบ
- รวมรายละเอียดข้อผิดพลาดในระดับ field

### การยืนยันตัวตน (Authentication)
- ทุก endpoint ต้องใช้ JWT token
- Token อยู่ใน Authorization header
- Token หมดอายุหลังจาก 24 ชั่วโมง
- ใช้กลไก refresh token

### รูปแบบการตอบกลับ (Response Format)

ทุกการตอบกลับต้องเป็นไปตามโครงสร้างนี้:

```json
{
  "success": true,
  "data": { /* ข้อมูลจริง */ },
  "timestamp": "2025-11-06T10:30:00Z",
  "version": "1.0"
}
```

การตอบกลับเมื่อเกิดข้อผิดพลาด:
```json
{
  "success": false,
  "error": {
    "code": "VALIDATION_ERROR",
    "message": "ข้อความสำหรับผู้ใช้",
    "details": { /* รายละเอียดข้อผิดพลาดแต่ละ field */ }
  },
  "timestamp": "2025-11-06T10:30:00Z"
}
```

### การแบ่งหน้า (Pagination)
- ใช้ cursor-based pagination (ไม่ใช้ offset)
- รวม boolean `hasMore`
- จำกัดขนาดหน้าสูงสุดที่ 100
- ขนาดหน้าเริ่มต้น: 20

### การจำกัดอัตราคำขอ (Rate Limiting)
- 1000 คำขอต่อชั่วโมงสำหรับผู้ใช้ที่ยืนยันตัวตนแล้ว
- 100 คำขอต่อชั่วโมงสำหรับ endpoint สาธารณะ
- ส่งคืน 429 เมื่อเกินขีดจำกัด
- รวม retry-after header

### การแคช (Caching)
- ใช้ Redis สำหรับการแคช session
- ระยะเวลาแคชเริ่มต้น: 5 นาที
- ยกเลิกการแคชเมื่อมีการเขียนข้อมูล
- ติดแท็ก cache key ด้วยประเภทของทรัพยากร

---
**อัปเดตล่าสุด**: 9 เมษายน 2569
