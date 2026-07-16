<!-- i18n-source: 07-plugins/devops-automation/README.md -->
<!-- i18n-date: 2026-05-09 -->
<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../../resources/logos/claude-howto-logo.svg">
</picture>

# DevOps Automation Plugin

DevOps automation ที่ครบวงจรสำหรับ deployment การตรวจสอบ และการตอบสนองต่อ incident

## ฟีเจอร์

✅ Deployment อัตโนมัติ
✅ ขั้นตอน rollback
✅ การตรวจสอบสุขภาพระบบ
✅ workflow การตอบสนองต่อ incident
✅ Kubernetes integration

## การติดตั้ง

```bash
/plugin install devops-automation
```

## สิ่งที่รวมอยู่

### Slash Commands
- `/deploy` - Deploy ไปยัง production หรือ staging
- `/rollback` - Rollback เป็นเวอร์ชันก่อนหน้า
- `/status` - ตรวจสอบสุขภาพระบบ
- `/incident` - จัดการ incident ใน production

### Subagents
- `deployment-specialist` - การดำเนินการ deployment
- `incident-commander` - การประสานงาน incident
- `alert-analyzer` - การวิเคราะห์สุขภาพระบบ

### MCP Servers
- Kubernetes integration

### Scripts
- `deploy.sh` - Deployment automation
- `rollback.sh` - Rollback automation
- `health-check.sh` - ยูทิลิตีตรวจสอบสุขภาพ

### Hooks
- `pre-deploy.js` - การตรวจสอบก่อน deployment
- `post-deploy.js` - งานหลัง deployment

## การใช้งาน

### Deploy ไปยัง Staging
```
/deploy staging
```

### Deploy ไปยัง Production
```
/deploy production
```

### Rollback
```
/rollback production
```

### ตรวจสอบสถานะ
```
/status
```

### จัดการ Incident
```
/incident
```

## ข้อกำหนด

- Claude Code 1.0+
- Kubernetes CLI (kubectl)
- กำหนดค่า cluster access แล้ว

## การกำหนดค่า

ตั้งค่า Kubernetes config:
```bash
export KUBECONFIG=~/.kube/config
```

## ตัวอย่าง Workflow

```
ผู้ใช้: /deploy production

Claude:
1. รัน hook pre-deploy (ตรวจสอบ kubectl และการเชื่อมต่อ cluster)
2. มอบหมายให้ subagent deployment-specialist
3. รันสคริปต์ deploy.sh
4. ตรวจสอบความคืบหน้า deployment ผ่าน Kubernetes MCP
5. รัน hook post-deploy (รอ pod พร้อม ทำ smoke test)
6. ให้ deployment summary

ผลลัพธ์:
✅ Deployment เสร็จสมบูรณ์
📦 เวอร์ชัน: v2.1.0
🚀 Pods: 3/3 พร้อม
⏱️  เวลา: 2 นาที 34 วินาที
```

---

**อัปเดตล่าสุด**: 6 พฤษภาคม 2026
**Claude Code Version**: 2.1.131
**แหล่งที่มา**:
- https://code.claude.com/docs/en/plugins
- https://github.com/anthropics/claude-code/releases/tag/v2.1.131
**Compatible Models**: Claude Sonnet 4.6, Claude Opus 4.7, Claude Haiku 4.5
