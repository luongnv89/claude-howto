---
description: پاکسازی کد، stage کردن تغییرات و آماده‌سازی pull request
allowed-tools: Bash(git add:*), Bash(git status:*), Bash(git diff:*), Bash(npm test:*), Bash(npm run lint:*)
---

# چک‌لیست آماده‌سازی Pull Request

پیش از ایجاد PR، این مراحل را اجرا کنید:

1. اجرای linting: `prettier --write .`
2. اجرای تست‌ها: `npm test`
3. بازبینی git diff: `git diff HEAD`
4. stage کردن تغییرات: `git add .`
5. ایجاد پیام commit بر اساس conventional commits:
   - `fix:` برای رفع باگ
   - `feat:` برای قابلیت‌های جدید
   - `docs:` برای مستندات
   - `refactor:` برای بازسازی کد
   - `test:` برای افزودن تست
   - `chore:` برای نگهداری

6. تولید خلاصه PR شامل:
   - چه چیزی تغییر کرد
   - چرا تغییر کرد
   - تست‌های انجام شده
   - تأثیرات بالقوه

---
**آخرین به‌روزرسانی**: ۴ اوت ۲۰۲۶
**نسخه Claude Code**: ۲.۱.۲۲۰
**منبع**:
- https://code.claude.com/docs/en/commands
**مدل‌های سازگار**: Claude Fable 5, Claude Opus 5, Claude Sonnet 5, Claude Sonnet 4.6, Claude Opus 4.8, Claude Haiku 4.5
