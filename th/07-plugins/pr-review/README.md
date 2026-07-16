<!-- i18n-source: 07-plugins/pr-review/README.md -->
<!-- i18n-date: 2026-05-09 -->
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../../resources/logos/claude-howto-logo.svg">
</picture>

# PR Review Plugin

workflow การตรวจสอบ PR อย่างครบวงจร พร้อมการตรวจสอบความปลอดภัย testing และเอกสาร

## คุณสมบัติ

✅ การวิเคราะห์ความปลอดภัย
✅ การตรวจสอบ coverage ของ test
✅ การตรวจสอบเอกสาร
✅ การประเมินคุณภาพโค้ด
✅ การวิเคราะห์ผลกระทบด้านประสิทธิภาพ

## การติดตั้ง

```bash
/plugin install pr-review
```

## สิ่งที่รวมอยู่

### Slash Commands
- `/review-pr` — การตรวจสอบ PR อย่างครอบคลุม
- `/check-security` — การตรวจสอบเชิงความปลอดภัย
- `/check-tests` — การวิเคราะห์ coverage ของ test

### Subagents
- `security-reviewer` — การตรวจจับช่องโหว่ด้านความปลอดภัย
- `test-checker` — การวิเคราะห์ coverage ของ test
- `performance-analyzer` — การประเมินผลกระทบด้านประสิทธิภาพ

### MCP Servers
- การเชื่อมต่อ GitHub สำหรับข้อมูล PR

### Hooks
- `pre-review.js` — การตรวจสอบก่อนดำเนินการ review

## การใช้งาน

### การตรวจสอบ PR พื้นฐาน
```
/review-pr
```

### การตรวจสอบความปลอดภัยเท่านั้น
```
/check-security
```

### การตรวจสอบ coverage ของ test
```
/check-tests
```

## ข้อกำหนด

- Claude Code 1.0+
- การเข้าถึง GitHub
- Git repository

## การตั้งค่า

ตั้งค่า GitHub token:
```bash
export GITHUB_TOKEN="your_github_token"
```

## ตัวอย่าง Workflow

```
User: /review-pr

Claude:
1. รัน pre-review hook (ตรวจสอบ git repo)
2. ดึงข้อมูล PR ผ่าน GitHub MCP
3. มอบหมายการตรวจสอบความปลอดภัยให้ security-reviewer subagent
4. มอบหมายการทดสอบให้ test-checker subagent
5. มอบหมายการวิเคราะห์ประสิทธิภาพให้ performance-analyzer subagent
6. รวบรวมผลการค้นพบทั้งหมด
7. จัดทำรายงานการตรวจสอบอย่างครอบคลุม

Result:
✅ Security: ไม่พบปัญหาสำคัญ
⚠️  Testing: Coverage อยู่ที่ 65% แนะนำให้ถึง 80%+
✅ Performance: ไม่มีผลกระทบสำคัญ
📝 Recommendations: เพิ่ม test สำหรับ edge case
```

---

**Last Updated**: May 6, 2026
**Claude Code Version**: 2.1.131
**Sources**:
- https://code.claude.com/docs/en/plugins
- https://github.com/anthropics/claude-code/releases/tag/v2.1.131
**Compatible Models**: Claude Sonnet 4.6, Claude Opus 4.7, Claude Haiku 4.5
