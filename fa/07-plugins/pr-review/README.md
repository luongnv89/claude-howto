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

## محتویات

### دستورات Slash
- `/review-pr` - بازبینی جامع PR
- `/check-security` - بازبینی با تمرکز بر امنیت
- `/check-tests` - تحلیل پوشش تست

### subagentها
- `security-reviewer` - شناسایی آسیب‌پذیری‌های امنیتی
- `test-checker` - تحلیل پوشش تست
- `performance-analyzer` - ارزیابی تأثیر بر عملکرد

### سرورهای MCP
- یکپارچه‌سازی GitHub برای داده‌های PR

### هوک‌ها
- `pre-review.js` - اعتبارسنجی پیش از بازبینی

## استفاده

### بازبینی پایه PR
```
/review-pr
```

### فقط بررسی امنیت
```
/check-security
```

### بررسی پوشش تست
```
/check-tests
```

## نیازمندی‌ها

- Claude Code 2.1+
- دسترسی GitHub
- مخزن Git

## پیکربندی

تنظیم GitHub token خود:
```bash
export GITHUB_TOKEN="your_github_token"
```

## گردش‌کار نمونه

```
کاربر: /review-pr

Claude:
۱. اجرای هوک pre-review (اعتبارسنجی مخزن git)
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
