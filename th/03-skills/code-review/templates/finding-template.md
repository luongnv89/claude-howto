<!-- i18n-source: 03-skills/code-review/templates/finding-template.md -->
<!-- i18n-date: 2026-05-09 -->
# template การบันทึกผลการตรวจสอบโค้ด

ใช้ template นี้เมื่อบันทึกปัญหาแต่ละรายการที่พบในระหว่างการตรวจสอบโค้ด

---

## ปัญหา: [ชื่อปัญหา]

### Severity
- [ ] Critical (บล็อกการ deploy)
- [ ] High (ควรแก้ไขก่อน merge)
- [ ] Medium (ควรแก้ไขเร็วๆ นี้)
- [ ] Low (ดีถ้าแก้ไขได้)

### หมวดหมู่
- [ ] ความปลอดภัย (Security)
- [ ] ประสิทธิภาพ (Performance)
- [ ] คุณภาพโค้ด (Code Quality)
- [ ] ความสามารถในการบำรุงรักษา (Maintainability)
- [ ] การทดสอบ (Testing)
- [ ] Design Pattern
- [ ] เอกสาร (Documentation)

### ตำแหน่ง
**ไฟล์:** `src/components/UserCard.tsx`

**บรรทัด:** 45-52

**Function/Method:** `renderUserDetails()`

### คำอธิบายปัญหา

**อะไร:** อธิบายว่าปัญหาคืออะไร

**ทำไมถึงสำคัญ:** อธิบายผลกระทบและเหตุผลที่ต้องแก้ไข

**พฤติกรรมปัจจุบัน:** แสดงโค้ดหรือพฤติกรรมที่มีปัญหา

**พฤติกรรมที่คาดหวัง:** อธิบายว่าควรเกิดอะไรขึ้นแทน

### ตัวอย่างโค้ด

#### ปัจจุบัน (มีปัญหา)

```typescript
// แสดงปัญหา N+1 query
const users = fetchUsers();
users.forEach(user => {
  const posts = fetchUserPosts(user.id); // Query ต่อผู้ใช้!
  renderUserPosts(posts);
});
```

#### การแก้ไขที่แนะนำ

```typescript
// เพิ่มประสิทธิภาพด้วย JOIN query
const usersWithPosts = fetchUsersWithPosts();
usersWithPosts.forEach(({ user, posts }) => {
  renderUserPosts(posts);
});
```

### การวิเคราะห์ผลกระทบ

| ด้าน | ผลกระทบ | Severity |
|--------|--------|----------|
| ประสิทธิภาพ | query มากกว่า 100 รายการสำหรับผู้ใช้ 20 คน | High |
| ประสบการณ์ผู้ใช้ | โหลดหน้าช้า | High |
| Scalability | พังเมื่อขนาดใหญ่ขึ้น | Critical |
| ความสามารถในการบำรุงรักษา | debug ยาก | Medium |

### ปัญหาที่เกี่ยวข้อง

- ปัญหาคล้ายกันใน `AdminUserList.tsx` บรรทัด 120
- PR ที่เกี่ยวข้อง: #456
- Issue ที่เกี่ยวข้อง: #789

### แหล่งข้อมูลเพิ่มเติม

- [N+1 Query Problem](https://en.wikipedia.org/wiki/N%2B1_problem)
- [Database Join Documentation](https://docs.example.com/joins)

### หมายเหตุผู้ตรวจสอบ

- pattern นี้พบบ่อยใน codebase นี้
- พิจารณาเพิ่มสิ่งนี้ใน code style guide
- อาจคุ้มค่าที่จะสร้าง helper function

### การตอบสนองของผู้เขียน (สำหรับข้อเสนอแนะ)

*ให้ผู้เขียนโค้ดกรอกข้อมูล:*

- [ ] ดำเนินการแก้ไขใน commit: `abc123`
- [ ] สถานะการแก้ไข: เสร็จสมบูรณ์ / กำลังดำเนินการ / ต้องการการหารือ
- [ ] คำถามหรือข้อกังวล: (อธิบาย)

---

## สถิติการค้นพบ (สำหรับผู้ตรวจสอบ)

เมื่อตรวจสอบการค้นพบหลายรายการ ให้ติดตาม:

- **จำนวนปัญหาทั้งหมดที่พบ:** X
- **Critical:** X
- **High:** X
- **Medium:** X
- **Low:** X

**คำแนะนำ:** ✅ อนุมัติ / ⚠️ ขอการเปลี่ยนแปลง / 🔄 ต้องการการหารือ

**คุณภาพโค้ดโดยรวม:** 1-5 ดาว
