<!-- i18n-source: TRANSLATION_NOTES.md -->
<!-- i18n-date: 2026-05-08 -->

# บันทึกการแปลภาษาไทย

# Thai Translation Notes & Style Guide

> **สำคัญ:** เอกสารนี้กำหนดหลักการและคำศัพท์สำหรับการแปล Claude Code Documentation เป็นภาษาไทย ผู้แปลทุกคนต้องอ่านก่อนเริ่มงาน

## หลักการแปลพื้นฐาน

- **รูปแบบภาษา:** ภาษาไทยเชิงวิชาการ เป็นทางการ เหมาะกับ GitHub technical documentation
- **รูปประโยค:** ใช้กริยาตรง เช่น "คำสั่งนี้ทำงาน..." ไม่ใช่ "คำสั่งนี้จะทำงาน..."
- **ห้ามใช้:** "ครับ" "ค่ะ" "พูดง่ายๆ" หรือสำนวนภาษาพูด
- **โค้ด:** คงไว้ทุกบรรทัด ห้ามแปล แปลได้เฉพาะ comment ในโค้ด
- **Mermaid:** ทุกอย่างในบล็อก ```mermaid คงไว้หมด ไม่แปล

---

## อภิธานศัพท์เทคนิค

คำศัพท์ที่ใช้สม่ำเสมอในทุกไฟล์:

| English | ภาษาไทย | หมายเหตุ |
|---------|---------|---------|
| slash command | slash command | คงเป็นภาษาอังกฤษ (ชื่อฟีเจอร์) |
| hook | hook | คงเป็นภาษาอังกฤษ (ชื่อฟีเจอร์) |
| skill | skill | คงเป็นภาษาอังกฤษ (ชื่อฟีเจอร์) |
| subagent | subagent | คงเป็นภาษาอังกฤษ (ชื่อฟีเจอร์) |
| agent | agent | คงเป็นภาษาอังกฤษ |
| memory | memory | คงเป็นภาษาอังกฤษ (ชื่อฟีเจอร์) |
| checkpoint | checkpoint | คงเป็นภาษาอังกฤษ (ชื่อฟีเจอร์) |
| plugin | plugin | คงเป็นภาษาอังกฤษ (ชื่อฟีเจอร์) |
| pull request / PR | pull request / PR | คงเป็นภาษาอังกฤษ (คำศัพท์ Git) |
| commit | commit | คงเป็นภาษาอังกฤษ (คำศัพท์ Git) |
| branch | branch | คงเป็นภาษาอังกฤษ (คำศัพท์ Git) |
| merge | merge | คงเป็นภาษาอังกฤษ (คำศัพท์ Git) |
| MCP (Model Context Protocol) | MCP | คงเป็นภาษาอังกฤษ (ชื่อโปรโตคอล) |
| CLAUDE.md | CLAUDE.md | คงเป็นภาษาอังกฤษ (ชื่อไฟล์) |
| SKILL.md | SKILL.md | คงเป็นภาษาอังกฤษ (ชื่อไฟล์) |
| workflow | workflow | คงเป็นภาษาอังกฤษ |
| pipeline | pipeline | คงเป็นภาษาอังกฤษ |
| sandbox | sandbox | คงเป็นภาษาอังกฤษ |
| template | template | คงเป็นภาษาอังกฤษ |
| boilerplate | boilerplate | คงเป็นภาษาอังกฤษ |
| deployment | deployment | คงเป็นภาษาอังกฤษ |
| refactoring | refactoring | คงเป็นภาษาอังกฤษ |
| debugging | debugging | คงเป็นภาษาอังกฤษ |
| linting | linting | คงเป็นภาษาอังกฤษ |
| token | token | คงเป็นภาษาอังกฤษ |
| context window | context window | คงเป็นภาษาอังกฤษ |
| frontmatter | frontmatter | คงเป็นภาษาอังกฤษ |
| API | API | คงเป็นภาษาอังกฤษ |
| CLI | CLI | คงเป็นภาษาอังกฤษ |
| CI/CD | CI/CD | คงเป็นภาษาอังกฤษ |
| repository | repository | คงเป็นภาษาอังกฤษ |
| worktree | worktree | คงเป็นภาษาอังกฤษ (คำศัพท์ Git) |
| Sonnet, Opus, Haiku | Sonnet, Opus, Haiku | คงเป็นภาษาอังกฤษ (ชื่อ model) |
| feature | ฟีเจอร์ | แปลได้ |
| developer | นักพัฒนา | แปลได้ |
| documentation | เอกสาร | แปลได้ |
| configuration | การกำหนดค่า | แปลได้ |
| settings | การตั้งค่า | แปลได้ |
| environment variable | ตัวแปรสภาพแวดล้อม | แปลได้ |
| command | คำสั่ง | แปลได้ |
| output | ผลลัพธ์ | แปลได้ |
| best practice | แนวปฏิบัติที่ดี | แปลได้ |
| use case | กรณีการใช้งาน | แปลได้ |
| user | ผู้ใช้ | แปลได้ |

---

## กฎที่ต้องปฏิบัติตาม

1. **code blocks** (```) คงไว้ทุกบรรทัด ห้ามแปลโค้ด แปลได้เฉพาะ comment ในโค้ด
2. **Mermaid diagram** ทุกอย่างในบล็อก ```mermaid คงไว้หมด ไม่แปล
3. **file path, URL, badge/shield URL** คงไว้ทั้งหมด
4. **ชื่อ function, variable, class** ในโค้ดคงไว้
5. **commit message format** (feat:, fix:, docs:) คงไว้
6. **CLI output examples** คงไว้
7. **Mermaid labels** คงเป็นภาษาอังกฤษ
8. **ตาราง** รักษาโครงสร้างไว้ แปลเฉพาะข้อความในเซลล์ที่เป็น prose
9. **internal links** ปรับให้ชี้ไปที่โครงสร้างไฟล์ที่ถูกต้อง
10. **badge/shield** ทั้งหมดใน README.md คงไว้ไม่แปล
11. เพิ่ม **i18n frontmatter** ที่ต้นไฟล์ทุกไฟล์

---

## แนวทางการเขียนประโยค

### ประโยคบรรยาย
- ใช้: "คำสั่งนี้ทำงานโดย..."
- ไม่ใช้: "คำสั่งนี้จะทำงานโดย..."

### คำสั่งแนะนำ
- ใช้: "ติดตั้งด้วยคำสั่ง", "สร้างไฟล์", "เพิ่มการกำหนดค่า"
- ไม่ใช้: "คุณควรติดตั้ง", "ลองสร้างไฟล์"

### การอธิบายฟีเจอร์
- ใช้: "ฟีเจอร์นี้ช่วยให้นักพัฒนา..."
- ไม่ใช้: "ฟีเจอร์นี้จะช่วยให้คุณ..."

---

**อัปเดตล่าสุด:** 2026-05-08
**ภาษาต้นฉบับ:** English
**ผู้รับผิดชอบ:** Community contributors
