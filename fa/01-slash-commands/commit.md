---
allowed-tools: Bash(git add:*), Bash(git status:*), Bash(git commit:*), Bash(git diff:*)
argument-hint: [message]
description: ایجاد یک git commit با زمینه
---

## Context

- وضعیت فعلی git: !`git status`
- diff فعلی git: !`git diff HEAD`
- شاخه فعلی: !`git branch --show-current`
- commitهای اخیر: !`git log --oneline -10`

## وظیفه شما

بر اساس تغییرات بالا، یک git commit ایجاد کنید.

اگر پیامی از طریق آرگومان‌ها ارائه شده بود، از آن استفاده کنید: $ARGUMENTS

در غیر این صورت، تغییرات را تحلیل کنید و یک پیام commit مناسب بر اساس فرمت conventional commits ایجاد کنید:
- `feat:` برای قابلیت‌های جدید
- `fix:` برای رفع باگ
- `docs:` برای تغییرات مستندات
- `refactor:` برای بازسازی کد
- `test:` برای افزودن تست
- `chore:` برای وظایف نگهداری

---
**آخرین به‌روزرسانی**: ۴ اوت ۲۰۲۶
**نسخه Claude Code**: ۲.۱.۲۲۰
**منبع**:
- https://code.claude.com/docs/en/commands
**مدل‌های سازگار**: Claude Fable 5, Claude Opus 5, Claude Sonnet 5, Claude Sonnet 4.6, Claude Opus 4.8, Claude Haiku 4.5
