---
description: ایجاد مستندات جامع API از کد منبع
---

# تولید مستندات API

مستندات API را با این مراحل تولید کنید:

1. اسکن همه فایل‌های `/src/api/`
2. استخراج signatureهای تابع و کامنت‌های JSDoc
3. سازماندهی بر اساس endpoint/ماژول
4. ایجاد markdown با مثال‌ها
5. شامل schemaهای درخواست/پاسخ
6. افزودن مستندات خطا

قالب خروجی:
- فایل Markdown در `/docs/api.md`
- شامل مثال‌های curl برای همه endpointها
- افزودن typeهای TypeScript

---
**آخرین به‌روزرسانی**: ۴ اوت ۲۰۲۶
**نسخه Claude Code**: ۲.۱.۲۲۰
**منبع**:
- https://code.claude.com/docs/en/commands
**مدل‌های سازگار**: Claude Fable 5, Claude Opus 5, Claude Sonnet 5, Claude Sonnet 4.6, Claude Opus 4.8, Claude Haiku 4.5
