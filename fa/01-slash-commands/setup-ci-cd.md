---
name: setup-ci-cd
description: پیاده‌سازی pre-commit hookها و GitHub Actions برای اطمینان کیفیت
---

# راه‌اندازی خط لوله CI/CD

دروازه‌های کیفیت جامع DevOps را متناسب با نوع پروژه پیاده‌سازی کنید:

1. **تحلیل پروژه**: شناسایی زبان(ها)، فریم‌ورک، سیستم build و ابزارهای موجود
2. **پیکربندی pre-commit hookها** با ابزارهای خاص زبان:
   - قالب‌بندی: Prettier/Black/gofmt/rustfmt و غیره
   - Linting: ESLint/Ruff/golangci-lint/Clippy و غیره
   - امنیت: Bandit/gosec/cargo-audit/npm audit و غیره
   - بررسی نوع: TypeScript/mypy/flow (در صورت وجود)
   - تست‌ها: اجرای مجموعه تست‌های مرتبط
3. **ایجاد گردش کار GitHub Actions** (.github/workflows/):
   - بازتاب بررسی‌های pre-commit در push/PR
   - ماتریکس چندنسخه/پلتفرم (در صورت وجود)
   - تأیید build و تست
   - مراحل استقرار (در صورت نیاز)
4. **تأیید خط لوله**: تست محلی، ایجاد PR آزمایشی، تأیید عبور همه بررسی‌ها

از ابزارهای رایگان/متن‌باز استفاده کنید. به configهای موجود احترام بگذارید. اجرا را سریع نگه دارید.

---
**آخرین به‌روزرسانی**: ۴ اوت ۲۰۲۶
**نسخه Claude Code**: ۲.۱.۲۲۰
**منبع**:
- https://code.claude.com/docs/en/commands
**مدل‌های سازگار**: Claude Fable 5, Claude Opus 5, Claude Sonnet 5, Claude Sonnet 4.6, Claude Opus 4.8, Claude Haiku 4.5
