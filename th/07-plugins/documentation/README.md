<!-- i18n-source: 07-plugins/documentation/README.md -->
<!-- i18n-date: 2026-05-09 -->
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../../resources/logos/claude-howto-logo.svg">
</picture>

# Documentation Plugin

การสร้างและบำรุงรักษาเอกสารที่ครบวงจรสำหรับโปรเจกต์ของคุณ

## ฟีเจอร์

✅ การสร้างเอกสาร API
✅ การสร้างและอัปเดต README
✅ การซิงค์เอกสาร
✅ การปรับปรุง code comment
✅ การสร้างตัวอย่าง

## การติดตั้ง

```bash
/plugin install documentation
```

## สิ่งที่รวมอยู่

### Slash Commands
- `/generate-api-docs` - สร้างเอกสาร API
- `/generate-readme` - สร้างหรืออัปเดต README
- `/sync-docs` - ซิงค์เอกสารกับการเปลี่ยนแปลงโค้ด
- `/validate-docs` - ตรวจสอบเอกสาร

### Subagents
- `api-documenter` - ผู้เชี่ยวชาญด้านเอกสาร API
- `code-commentator` - การปรับปรุง code comment
- `example-generator` - การสร้างตัวอย่างโค้ด

### Templates
- `api-endpoint.md` - template เอกสาร API endpoint
- `function-docs.md` - template เอกสาร function
- `adr-template.md` - template Architecture Decision Record

### MCP Servers
- GitHub integration สำหรับการซิงค์เอกสาร

## การใช้งาน

### สร้างเอกสาร API
```
/generate-api-docs
```

### สร้าง README
```
/generate-readme
```

### ซิงค์เอกสาร
```
/sync-docs
```

### ตรวจสอบเอกสาร
```
/validate-docs
```

## ข้อกำหนด

- Claude Code 1.0+
- GitHub access (ตัวเลือก)

## ตัวอย่าง Workflow

```
ผู้ใช้: /generate-api-docs

Claude:
1. สแกน API endpoint ทั้งหมดใน /src/api/
2. มอบหมายให้ subagent api-documenter
3. ดึง function signature และ JSDoc
4. จัดระเบียบตาม module/endpoint
5. ใช้ template api-endpoint.md
6. สร้างเอกสาร markdown ที่ครบถ้วน
7. รวมตัวอย่าง curl, JavaScript และ Python

ผลลัพธ์:
✅ สร้างเอกสาร API แล้ว
📄 ไฟล์ที่สร้าง:
   - docs/api/users.md
   - docs/api/auth.md
   - docs/api/products.md
📊 ความครอบคลุม: 23/23 endpoint ได้รับการจัดทำเอกสาร
```

## การใช้งาน Templates

### API Endpoint Template
ใช้สำหรับจัดทำเอกสาร REST API endpoint พร้อมตัวอย่างครบถ้วน

### Function Documentation Template
ใช้สำหรับจัดทำเอกสาร function/method แต่ละรายการ

### ADR Template
ใช้สำหรับบันทึกการตัดสินใจทางสถาปัตยกรรม

## การกำหนดค่า

ตั้งค่า GitHub token สำหรับการซิงค์เอกสาร:
```bash
export GITHUB_TOKEN="your_github_token"
```

## แนวทางปฏิบัติที่ดีที่สุด

- เก็บเอกสารไว้ใกล้กับโค้ด
- อัปเดตเอกสารพร้อมกับการเปลี่ยนแปลงโค้ด
- รวมตัวอย่างเชิงปฏิบัติ
- ตรวจสอบความถูกต้องสม่ำเสมอ
- ใช้ template เพื่อความสอดคล้อง

---

**อัปเดตล่าสุด**: 6 พฤษภาคม 2026
**Claude Code Version**: 2.1.131
**แหล่งที่มา**:
- https://code.claude.com/docs/en/plugins
- https://github.com/anthropics/claude-code/releases/tag/v2.1.131
**Compatible Models**: Claude Sonnet 4.6, Claude Opus 4.7, Claude Haiku 4.5
