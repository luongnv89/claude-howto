<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../../../resources/logos/claude-howto-logo.svg">
</picture>

# پلاگین خودکارسازی DevOps

خودکارسازی کامل DevOps برای استقرار، مانیتورینگ و پاسخ به حوادث.

## امکانات

✅ استقرار خودکار
✅ رویه‌های بازگشت (rollback)
✅ مانیتورینگ سلامت سیستم
✅ گردش‌کار پاسخ به حوادث
✅ یکپارچه‌سازی Kubernetes

## نصب

```bash
claude --plugin-dir ./07-plugins/devops-automation
```

## محتویات

### دستورات Slash
- `/deploy` - استقرار در محیط تولید یا staging
- `/rollback` - بازگشت به نسخه قبلی
- `/status` - بررسی سلامت سیستم
- `/incident` - مدیریت حوادث تولید

### subagentها
- `deployment-specialist` - عملیات استقرار
- `incident-commander` - هماهنگی حوادث
- `alert-analyzer` - تحلیل سلامت سیستم

### سرورهای MCP
- یکپارچه‌سازی Kubernetes

### اسکریپت‌ها
- `deploy.sh` - خودکارسازی استقرار
- `rollback.sh` - خودکارسازی بازگشت
- `health-check.sh` - ابزارهای بررسی سلامت

### هوک‌ها
- `pre-deploy.js` - اعتبارسنجی پیش از استقرار
- `post-deploy.js` - وظایف پس از استقرار

## استفاده

### استقرار در staging
```
/deploy staging
```

### استقرار در تولید
```
/deploy production
```

### بازگشت
```
/rollback production
```

### بررسی وضعیت
```
/status
```

### مدیریت حادثه
```
/incident
```

## نیازمندی‌ها

- Claude Code 2.1+
- Kubernetes CLI (kubectl)
- دسترسی کلاستر پیکربندی‌شده

## پیکربندی

پیکربندی Kubernetes خود را تنظیم کنید:
```bash
export KUBECONFIG=~/.kube/config
```

## گردش‌کار نمونه

```
کاربر: /deploy production

Claude:
۱. اجرای هوک pre-deploy (اعتبارسنجی kubectl، اتصال کلاستر)
۲. واگذاری به subagent deployment-specialist
۳. اجرای اسکریپت deploy.sh
۴. مانیتورینگ پیشرفت استقرار از طریق Kubernetes MCP
۵. اجرای هوک post-deploy (انتظار برای podها، تست‌های smoke)
۶. ارائه خلاصه استقرار

نتیجه:
✅ استقرار کامل شد
📦 نسخه: v2.1.0
🚀 Podها: ۳/۳ آماده
⏱️  زمان: ۲m 34s
```

---

**آخرین به‌روزرسانی**: ۱۸ اکتبر ۲۰۲۶
**نسخه Claude Code**: 2.1.302
**منابع**:
- https://code.claude.com/docs/en/plugins
- https://github.com/anthropics/claude-code/releases/tag/v2.1.131
- https://github.com/anthropics/claude-code/releases/tag/v2.1.138
- https://code.claude.com/docs/en/model-config
- https://code.claude.com/docs/en/plugins/cli-reference
- https://code.claude.com/docs/en/plugins/install
**مدل‌های سازگار**: Claude Fable 5, Claude Opus 5, Claude Sonnet 5, Claude Sonnet 4.6, Claude Opus 4.8, Claude Haiku 4.5
