<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../../../resources/logos/claude-howto-logo.svg">
</picture>

# پلاگین بازبینی PR

گردش‌کار کامل بازبینی PR با بررسی‌های امنیتی، تست و مستندات.

## امکانات

✅ تحلیل امنیتی
✅ بررسی پوشش تست
✅ اعتبارسنجی مستندات
✅ ارزیابی کیفیت کد
✅ تحلیل تأثیر بر عملکرد

## نصب

```bash
claude --plugin-dir ./07-plugins/pr-review
```

پیش از بارگذاری، پلاگین را بررسی کنید:

```bash
claude plugin validate ./07-plugins/pr-review
```

## محتویات

```text
pr-review/
├── .claude-plugin/
│   └── plugin.json      # "name": "pr-review" sets the command prefix
├── commands/            # each file becomes /pr-review:<file>
├── agents/
├── hooks/
│   ├── hooks.json       # registers pre-review.js
│   └── pre-review.js
└── .mcp.json            # GitHub MCP server
```

### دستورات Slash

دستورات پلاگین با `name` پلاگین در `plugin.json` فضای‌نام‌گذاری می‌شوند:

- `/pr-review:review-pr` - بازبینی جامع PR
- `/pr-review:check-security` - بازبینی با تمرکز بر امنیت
- `/pr-review:check-tests` - تحلیل پوشش تست

### subagentها
- `security-reviewer` - شناسایی آسیب‌پذیری‌های امنیتی
- `test-checker` - تحلیل پوشش تست
- `performance-analyzer` - ارزیابی تأثیر بر عملکرد

### سرورهای MCP

`.mcp.json` یک سرور به نام `github` تعریف می‌کند: سرور MCP رسمی GitHub (`ghcr.io/github/github-mcp-server`) که با Docker در حالت فقط‌خواندنی اجرا می‌شود. این سرور در `/mcp` با نام `plugin:pr-review:github` نمایش داده می‌شود.

### هوک‌ها

`hooks/hooks.json` فایل `pre-review.js` را روی رویداد `UserPromptExpansion` و با یک matcher برای سه دستور بالا ثبت می‌کند. وقتی یکی از آن‌ها را تایپ می‌کنید، هوک:

- اگر پوشه جاری مخزن git نباشد، دستور را مسدود می‌کند (کد خروج 2)
- در غیر این صورت، شاخه جاری و یادداشتی درباره تغییرات کامیت‌نشده را به زمینه Claude اضافه می‌کند

## استفاده

### بازبینی پایه PR
```text
/pr-review:review-pr
```

### فقط بررسی امنیت
```text
/pr-review:check-security
```

### بررسی پوشش تست
```text
/pr-review:check-tests
```

## نیازمندی‌ها

- Claude Code 2.1+
- Node.js (برای اجرای اسکریپت هوک)
- Docker (برای اجرای سرور MCP گیت‌هاب)
- یک توکن دسترسی شخصی GitHub
- مخزن Git

## پیکربندی

پیش از اجرای Claude Code، GitHub token خود را تنظیم کنید:
```bash
export GITHUB_TOKEN="your_github_token"
```

`.mcp.json` آن را با نام `GITHUB_PERSONAL_ACCESS_TOKEN`، یعنی متغیری که سرور می‌خواند، به سرور می‌دهد. برای بررسی اتصال `plugin:pr-review:github`، دستور `/mcp` را اجرا کنید.

## گردش‌کار نمونه

```text
کاربر: /pr-review:review-pr

Claude:
۱. هوک pre-review مخزن git را بررسی می‌کند و شاخه را به زمینه اضافه می‌کند
۲. دریافت داده‌های PR از طریق GitHub MCP
۳. واگذاری بازبینی امنیت به subagent security-reviewer
۴. واگذاری تست به subagent test-checker
۵. واگذاری عملکرد به subagent performance-analyzer
۶. جمع‌آوری همه یافته‌ها
۷. ارائه گزارش جامع بازبینی

نتیجه:
✅ امنیت: مشکل حیاتی پیدا نشد
⚠️  تست: پوشش ۶۵٪ است، ۸۰٪+ پیشنهاد می‌شود
✅ عملکرد: تأثیر قابل‌توجهی نیست
📝 پیشنهادات: برای موارد حاشیه‌ای تست اضافه کنید
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
