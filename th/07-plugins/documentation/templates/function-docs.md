<!-- i18n-source: 07-plugins/documentation/templates/function-docs.md -->
<!-- i18n-date: 2026-05-09 -->
# Function: `functionName`

## คำอธิบาย
คำอธิบายสั้น ๆ ว่า function ทำอะไร

## Signature
```typescript
function functionName(param1: Type1, param2: Type2): ReturnType
```

## พารามิเตอร์

| พารามิเตอร์ | ประเภท | จำเป็น | คำอธิบาย |
|-----------|------|----------|-------------|
| param1 | Type1 | ใช่ | คำอธิบาย param1 |
| param2 | Type2 | ไม่ | คำอธิบาย param2 |

## ค่าที่คืน
**ประเภท**: `ReturnType`

คำอธิบายสิ่งที่คืน

## ข้อยกเว้น
- `Error`: เมื่อมีการให้ input ที่ไม่ถูกต้อง
- `TypeError`: เมื่อมีการส่งประเภทที่ผิด

## ตัวอย่าง

### การใช้งานพื้นฐาน
```typescript
const result = functionName('value1', 'value2');
console.log(result);
```

### การใช้งานขั้นสูง
```typescript
const result = functionName(
  complexParam1,
  { option: true }
);
```

## หมายเหตุ
- หมายเหตุหรือคำเตือนเพิ่มเติม
- ข้อพิจารณาด้านประสิทธิภาพ
- แนวทางปฏิบัติที่ดีที่สุด

## ดูเพิ่มเติม
- [Function ที่เกี่ยวข้อง](#)
- [เอกสาร API](#)
