<!-- i18n-source: 02-memory/project-CLAUDE.md -->
<!-- i18n-date: 2026-05-09 -->
# การกำหนดค่าโปรเจกต์

## ภาพรวมโปรเจกต์
- **ชื่อ**: E-commerce Platform
- **Tech Stack**: Node.js, PostgreSQL, React 18, Docker
- **ขนาดทีม**: นักพัฒนา 5 คน
- **กำหนดส่ง**: Q4 2025

## สถาปัตยกรรม (Architecture)
@docs/architecture.md
@docs/api-standards.md
@docs/database-schema.md

## มาตรฐานการพัฒนา

### รูปแบบโค้ด (Code Style)
- ใช้ Prettier สำหรับการจัดรูปแบบ
- ใช้ ESLint with airbnb config
- ความยาวบรรทัดสูงสุด: 100 ตัวอักษร
- ใช้การเยื้อง 2 space

### รูปแบบการตั้งชื่อ (Naming Conventions)
- **Files**: kebab-case (user-controller.js)
- **Classes**: PascalCase (UserService)
- **Functions/Variables**: camelCase (getUserById)
- **Constants**: UPPER_SNAKE_CASE (API_BASE_URL)
- **Database Tables**: snake_case (user_accounts)

### Git Workflow
- ชื่อ branch: `feature/description` หรือ `fix/description`
- ข้อความ commit: ตาม conventional commits
- ต้องมี PR ก่อน merge
- ต้องผ่านการตรวจสอบ CI/CD ทั้งหมด
- ต้องได้รับอนุมัติอย่างน้อย 1 คน

### ข้อกำหนดด้านการทดสอบ (Testing Requirements)
- ความครอบคลุม code อย่างน้อย 80%
- ทุก critical path ต้องมี test
- ใช้ Jest สำหรับ unit test
- ใช้ Cypress สำหรับ E2E test
- ชื่อไฟล์ test: `*.test.ts` หรือ `*.spec.ts`

### มาตรฐาน API
- RESTful endpoints เท่านั้น
- JSON request/response
- ใช้ HTTP status code อย่างถูกต้อง
- กำหนดเวอร์ชัน API endpoint: `/api/v1/`
- จัดทำเอกสารทุก endpoint พร้อมตัวอย่าง

### ฐานข้อมูล (Database)
- ใช้ migration สำหรับการเปลี่ยน schema
- ห้าม hardcode credentials
- ใช้ connection pooling
- เปิด query logging ใน development
- ต้องสำรองข้อมูลเป็นประจำ

### การ deploy
- deploy แบบ Docker-based
- orchestration ด้วย Kubernetes
- กลยุทธ์ Blue-green deployment
- rollback อัตโนมัติเมื่อเกิดความล้มเหลว
- database migration รันก่อน deploy

## คำสั่งที่ใช้บ่อย

| คำสั่ง | วัตถุประสงค์ |
|---------|---------|
| `npm run dev` | เริ่ม development server |
| `npm test` | รัน test suite |
| `npm run lint` | ตรวจสอบ code style |
| `npm run build` | build สำหรับ production |
| `npm run migrate` | รัน database migration |

## ผู้ติดต่อในทีม
- Tech Lead: Sarah Chen (@sarah.chen)
- Product Manager: Mike Johnson (@mike.j)
- DevOps: Alex Kim (@alex.k)

## ปัญหาที่ทราบและวิธีแก้ไข
- PostgreSQL connection pooling จำกัดที่ 20 ในช่วงเวลา peak
- วิธีแก้: ใช้ query queuing
- Safari 14 มีปัญหากับ async generators
- วิธีแก้: ใช้ Babel transpiler

## โปรเจกต์ที่เกี่ยวข้อง
- Analytics Dashboard: `/projects/analytics`
- Mobile App: `/projects/mobile`
- Admin Panel: `/projects/admin`

---
**อัปเดตล่าสุด**: 9 เมษายน 2569
