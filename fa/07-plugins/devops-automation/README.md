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

پیش از بارگذاری، پلاگین را بررسی کنید:

```bash
claude plugin validate ./07-plugins/devops-automation
```

## محتویات

### دستورات Slash

دستورات پلاگین با `name` پلاگین در `plugin.json` فضای‌نام‌گذاری می‌شوند:

- `/devops-automation:deploy` - استقرار در محیط تولید یا staging
- `/devops-automation:rollback` - بازگشت به نسخه قبلی
- `/devops-automation:status` - بررسی سلامت سیستم
- `/devops-automation:incident` - مدیریت حوادث تولید

### subagentها
- `deployment-specialist` - عملیات استقرار
- `incident-commander` - هماهنگی حوادث
- `alert-analyzer` - تحلیل سلامت سیستم

### سرورهای MCP

`.mcp.json` یک سرور به نام `kubernetes` تعریف می‌کند: بسته npm `mcp-server-kubernetes` که با `npx` و `ALLOW_ONLY_NON_DESTRUCTIVE_TOOLS=true` اجرا می‌شود، پس ابزارهای حذف آن خاموش هستند. این سرور در `/mcp` با نام `plugin:devops-automation:kubernetes` نمایش داده می‌شود.

### اسکریپت‌ها
- `deploy.sh` - خودکارسازی استقرار
- `rollback.sh` - خودکارسازی بازگشت
- `health-check.sh` - ابزارهای بررسی سلامت

### هوک‌ها

`hooks/hooks.json` هر دو اسکریپت را روی فراخوانی‌های ابزار Bash ثبت می‌کند. آن‌ها فقط روی فرمان‌های استقرار (`deploy.sh`، `rollback.sh`، `kubectl apply`، `kubectl set image`، `kubectl rollout restart|undo`، `helm install|upgrade|rollback`) عمل می‌کنند و برای هر فرمان دیگری با کد 0 خارج می‌شوند:

- `pre-deploy.js` (`PreToolUse`): وقتی `kubectl` نصب نباشد یا نتواند به کلاستر برسد، فرمان را مسدود می‌کند (کد خروج 2) و Claude دلیل آن را می‌بیند
- `post-deploy.js` (`PostToolUse`): تا 120 ثانیه منتظر می‌ماند تا podهایی با برچسب `DEPLOY_APP_LABEL` آماده شوند و اگر آماده نشوند به Claude اطلاع می‌دهد. اگر `DEPLOY_APP_LABEL` تنظیم نشده باشد، از انتظار صرف‌نظر می‌کند

هر دو هوک فقط وضعیت کلاستر را می‌خوانند (`kubectl version`، `cluster-info`، `wait`).

## استفاده

### استقرار در staging
```text
/devops-automation:deploy staging
```

### استقرار در تولید
```text
/devops-automation:deploy production
```

### بازگشت
```text
/devops-automation:rollback production
```

### بررسی وضعیت
```text
/devops-automation:status
```

### مدیریت حادثه
```text
/devops-automation:incident
```

## نیازمندی‌ها

- Claude Code 2.1+
- Node.js (برای اجرای اسکریپت‌های هوک و سرور MCP)
- Kubernetes CLI (kubectl)
- دسترسی کلاستر پیکربندی‌شده

## پیکربندی

پیکربندی Kubernetes خود را تنظیم کنید (`.mcp.json` متغیر `KUBECONFIG` را به سرور MCP می‌دهد):
```bash
export KUBECONFIG=~/.kube/config
```

اختیاری، برای بررسی آمادگی پس از استقرار:
```bash
export DEPLOY_APP_LABEL="app=myapp"
export DEPLOY_NAMESPACE="staging"
```

## گردش‌کار نمونه

```text
کاربر: /devops-automation:deploy production

Claude:
۱. واگذاری به subagent deployment-specialist
۲. اجرای اسکریپت deploy.sh؛ هوک pre-deploy ابتدا kubectl و اتصال کلاستر را بررسی می‌کند
۳. مانیتورینگ پیشرفت استقرار از طریق Kubernetes MCP
۴. هوک post-deploy منتظر آماده شدن podها می‌ماند
۵. ارائه خلاصه استقرار

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
