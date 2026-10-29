<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../../../resources/logos/claude-howto-logo.svg">
</picture>

# پلاگین مستندسازی

تولید و نگهداری جامع مستندات برای پروژه شما.

## امکانات

✅ تولید مستندات API
✅ ایجاد و به‌روزرسانی README
✅ هماهنگ‌سازی مستندات
✅ بهبود کامنت‌های کد
✅ تولید نمونه

## نصب

```bash
claude --plugin-dir ./07-plugins/documentation
```

## محتویات

### دستورات Slash
- `/generate-api-docs` - تولید مستندات API
- `/generate-readme` - ایجاد یا به‌روزرسانی README
- `/sync-docs` - هماهنگ‌سازی مستندات با تغییرات کد
- `/validate-docs` - اعتبارسنجی مستندات

### subagentها
- `api-documenter` - متخصص مستندسازی API
- `code-commentator` - بهبود کامنت‌های کد
- `example-generator` - ایجاد نمونه‌های کد

### قالب‌ها
- `api-endpoint.md` - قالب مستندسازی endpoint API
- `function-docs.md` - قالب مستندسازی تابع
- `adr-template.md` - قالب ثبت تصمیم معماری

### سرورهای MCP
- یکپارچه‌سازی GitHub برای هماهنگ‌سازی مستندات

## استفاده

### تولید مستندات API
```
/generate-api-docs
```

### ایجاد README
```
/generate-readme
```

### هماهنگ‌سازی مستندات
```
/sync-docs
```

### اعتبارسنجی مستندات
```
/validate-docs
```

## نیازمندی‌ها

- Claude Code 2.1+
- دسترسی GitHub (اختیاری)

## گردش‌کار نمونه

```
کاربر: /generate-api-docs

Claude:
۱. اسکن همه endpointهای API در /src/api/
۲. واگذاری به subagent api-documenter
۳. استخراج امضای توابع و JSDoc
۴. سازمان‌دهی بر اساس ماژول/endpoint
۵. استفاده از قالب api-endpoint.md
۶. تولید مستندات جامع markdown
۷. شامل نمونه‌های curl، JavaScript و Python

نتیجه:
✅ مستندات API تولید شد
📄 فایل‌های ایجاد‌شده:
   - docs/api/users.md
   - docs/api/auth.md
   - docs/api/products.md
📊 پوشش: ۲۳/۲۳ endpoint مستندسازی شد
```

## استفاده از قالب‌ها

### قالب endpoint API
برای مستندسازی endpointهای REST API با نمونه‌های کامل استفاده کنید.

### قالب مستندسازی تابع
برای مستندسازی توابع/متدهای فردی استفاده کنید.

### قالب ADR
برای ثبت تصمیمات معماری استفاده کنید.

## پیکربندی

تنظیم GitHub token برای هماهنگ‌سازی مستندات:
```bash
export GITHUB_TOKEN="your_github_token"
```

## بهترین روش‌ها

- مستندات را نزدیک کد نگه دارید
- مستندات را با تغییرات کد به‌روزرسانی کنید
- نمونه‌های کاربردی ارائه دهید
- به‌طور منظم اعتبارسنجی کنید
- برای یکپارچگی از قالب‌ها استفاده کنید

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
