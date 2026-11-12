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

### اسکریپت‌ها
- `deploy.sh` - خودکارسازی استقرار
- `rollback.sh` - خودکارسازی بازگشت
- `health-check.sh` - ابزارهای بررسی سلامت

### هوک‌ها

`hooks/hooks.json` هر دو اسکریپت را روی فراخوانی‌های ابزار Bash ثبت می‌کند. آن‌ها فقط روی فرمان‌های استقرار (`deploy.sh`، `rollback.sh`، `kubectl apply`، `kubectl set image`، `kubectl rollout restart|undo`، `helm install|upgrade|rollback`) عمل می‌کنند و برای هر فرمان دیگری با کد 0 خارج می‌شوند:

- `pre-deploy.js` (`PreToolUse`): وقتی `kubectl` نصب نباشد یا نتواند به کلاستر برسد، فرمان را مسدود می‌کند (کد خروج 2) و Claude دلیل آن را می‌بیند
- `post-deploy.js` (`PostToolUse`): استقرار را بررسی می‌کند و اگر ناموفق بوده باشد به Claude اطلاع می‌دهد. اگر `DEPLOY_DEPLOYMENT` تنظیم شده باشد، `kubectl rollout status` را اجرا می‌کند (تا 120 ثانیه) که منتظر podهای جدید می‌ماند. در غیر این صورت، اگر `DEPLOY_APP_LABEL` تنظیم شده باشد، به `kubectl wait` برای Ready شدن podهایی با آن برچسب بسنده می‌کند؛ podهای قدیمی‌ای که هنوز Ready هستند هم از این بررسی رد می‌شوند. اگر هیچ‌کدام تنظیم نشده باشد، از بررسی صرف‌نظر می‌کند. یادداشت آن برای Claude می‌گوید کدام بررسی اجرا شد

هر دو هوک فقط وضعیت کلاستر را می‌خوانند (`kubectl version`، `cluster-info`، `rollout status`، `wait`).

یک فرمان چگونه تشخیص داده می‌شود: اسکریپت‌ها بدنه‌های heredoc و رشته‌های داخل نقل‌قول را حذف می‌کنند، فرمان را روی خط‌های جدید، `&&`، `||`، `;`، `|` و `&` تقسیم می‌کنند و به اولین کلمه هر بخش نگاه می‌کنند (پس از `VAR=value` و پوشش‌هایی مانند `sudo` یا `env`). پرچم‌های سراسری پیش از فعل هم به حساب می‌آیند، پس `kubectl -n prod apply` و `helm -n prod upgrade` فرمان استقرار هستند، اما `echo "kubectl apply"`، `cat scripts/deploy.sh` و `git commit -m "helm upgrade notes"` نیستند. این یک روش تقریبی است، نه یک تجزیه‌گر shell: استقرارهایی را که در نقل‌قول پنهان شده‌اند (`bash -c "kubectl apply …"`)، پشت پوشش‌های دیگر (`ssh`، `xargs`، `make deploy`) یا درون اسکریپت‌های دیگر هستند، تشخیص نمی‌دهد. به آن به‌عنوان یک مرز ایمنی تکیه نکنید.

اگر هنگام اجرای یک فرمان استقرار `Ctrl+Enter` را بزنید و این کار نوبت را تمام کند، هوک post-deploy همچنان پس از پایان فرمان اجرا می‌شود، اما Claude Code آن را پس از 10 ثانیه، صرف‌نظر از `timeout` آن، متوقف می‌کند، پس ممکن است بررسی کامل نشود.

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
- Node.js (برای اجرای اسکریپت‌های هوک)
- Kubernetes CLI (kubectl)
- دسترسی کلاستر پیکربندی‌شده

## پیکربندی

هوک‌ها و اسکریپت‌ها از پیکربندی معمول `kubectl` شما استفاده می‌کنند (`~/.kube/config`، یا `KUBECONFIG` اگر آن را تنظیم کرده باشید).

اختیاری، برای بررسی پس از استقرار (`DEPLOY_DEPLOYMENT` را تنظیم کنید، یا `DEPLOY_APP_LABEL` را برای حالت جایگزین انتظار برای آمادگی podها):
```bash
export DEPLOY_DEPLOYMENT="myapp"
export DEPLOY_APP_LABEL="app=myapp"
export DEPLOY_NAMESPACE="staging"
```

## گردش‌کار نمونه

```text
کاربر: /devops-automation:deploy production

Claude:
۱. واگذاری به subagent deployment-specialist
۲. اجرای اسکریپت deploy.sh؛ هوک pre-deploy ابتدا kubectl و اتصال کلاستر را بررسی می‌کند
۳. هوک post-deploy منتظر آماده شدن podها می‌ماند
۴. ارائه خلاصه استقرار

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
**مدل‌های سازگار**: Claude Fable 5.2, Claude Fable 5.1, Claude Fable 5, Claude Opus 5.5, Claude Opus 5, Claude Sonnet 5.5, Claude Sonnet 5, Claude Sonnet 4.6, Claude Opus 4.8, Claude Haiku 5.5, Claude Haiku 4.5
