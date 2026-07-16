<!-- i18n-source: 03-skills/code-review/templates/review-checklist.md -->
<!-- i18n-date: 2026-05-09 -->
# checklist การตรวจสอบโค้ด

## checklist ความปลอดภัย
- [ ] ไม่มี credentials หรือ secret ที่ hardcode
- [ ] มีการตรวจสอบ input ทุก user input
- [ ] ป้องกัน SQL injection (parameterized query)
- [ ] ป้องกัน CSRF บน operation ที่เปลี่ยนแปลงสถานะ
- [ ] ป้องกัน XSS ด้วยการ escape ที่เหมาะสม
- [ ] มีการตรวจสอบ authentication บน protected endpoint
- [ ] มีการตรวจสอบ authorization บนทรัพยากร
- [ ] การ hash รหัสผ่านที่ปลอดภัย (bcrypt, argon2)
- [ ] ไม่มีข้อมูลที่ละเอียดอ่อนใน log
- [ ] บังคับใช้ HTTPS

## checklist ประสิทธิภาพ
- [ ] ไม่มี N+1 query
- [ ] ใช้ index ที่เหมาะสม
- [ ] มีการ caching ในจุดที่เป็นประโยชน์
- [ ] ไม่มี blocking operation บน main thread
- [ ] ใช้ async/await อย่างถูกต้อง
- [ ] paginate ชุดข้อมูลขนาดใหญ่
- [ ] มี connection pool สำหรับฐานข้อมูล
- [ ] regular expression ได้รับการเพิ่มประสิทธิภาพ
- [ ] ไม่มีการสร้าง object ที่ไม่จำเป็น
- [ ] ป้องกัน memory leak

## checklist คุณภาพ
- [ ] function น้อยกว่า 50 บรรทัด
- [ ] ชื่อตัวแปรชัดเจน
- [ ] ไม่มีโค้ดซ้ำ
- [ ] มีการจัดการ error ที่เหมาะสม
- [ ] คอมเมนต์อธิบาย "ทำไม" ไม่ใช่ "ทำอะไร"
- [ ] ไม่มี console.log ใน production
- [ ] มีการตรวจสอบ type (TypeScript/JSDoc)
- [ ] ปฏิบัติตามหลัก SOLID
- [ ] ใช้ design pattern อย่างถูกต้อง
- [ ] โค้ดอธิบายตัวเองได้

## checklist การทดสอบ
- [ ] มี unit test
- [ ] ครอบคลุม edge case
- [ ] ทดสอบ error scenario
- [ ] มี integration test
- [ ] ความครอบคลุมมากกว่า 80%
- [ ] ไม่มี flaky test
- [ ] mock dependency ภายนอก
- [ ] ชื่อ test ชัดเจน
