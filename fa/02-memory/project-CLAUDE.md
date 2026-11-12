# پیکربندی پروژه

## مرور کلی پروژه
- **نام**: پلتفرم تجارت الکترونیک
- **Tech Stack**: Node.js، PostgreSQL، React 18، Docker
- **اندازه تیم**: ۵ توسعه‌دهنده
- **مهلت**: Q4 2025

## معماری
@docs/architecture.md
@docs/api-standards.md
@docs/database-schema.md

## استانداردهای توسعه

### سبک کد
- از Prettier برای قالب‌بندی استفاده کنید
- از ESLint با config اولیه airbnb استفاده کنید
- حداکثر طول خط: ۱۰۰ کاراکتر
- از تورفتگی ۲-فضایی استفاده کنید

### قراردادهای نام‌گذاری
- **فایل‌ها**: kebab-case (user-controller.js)
- **کلاس‌ها**: PascalCase (UserService)
- **توابع/متغیرها**: camelCase (getUserById)
- **ثابت‌ها**: UPPER_SNAKE_CASE (API_BASE_URL)
- **جداول پایگاه‌داده**: snake_case (user_accounts)

### گردش کار Git
- نام شاخه‌ها: `feature/description` یا `fix/description`
- پیام‌های commit: از conventional commits پیروی کنید
- PR پیش از merge الزامی است
- همه بررسی‌های CI/CD باید عبور کنند
- حداقل ۱ تأیید لازم است

### الزامات تست
- حداقل ۸۰٪ پوشش کد
- همه مسیرهای بحرانی باید تست داشته باشند
- از Jest برای تست‌های واحد استفاده کنید
- از Cypress برای تست‌های E2E استفاده کنید
- نام فایل‌های تست: `*.test.ts` یا `*.spec.ts`

### استانداردهای API
- فقط endpointهای RESTful
- درخواست/پاسخ JSON
- استفاده صحیح از کدهای وضعیت HTTP
- نسخه‌بندی endpointهای API: `/api/v1/`
- همه endpointها را با مثال مستند کنید

### پایگاه‌داده
- از migration برای تغییرات schema استفاده کنید
- هرگز اعتبارنامه‌ها را hardcode نکنید
- از connection pooling استفاده کنید
- فعال کردن query logging در توسعه
- پشتیبان‌گیری منظم الزامی است

### استقرار
- استقرار مبتنی بر Docker
- هماهنگی Kubernetes
- استراتژی استقرار blue-green
- بازگشت خودکار در صورت شکست
- migrationهای پایگاه‌داده پیش از استقرار اجرا شوند

## دستورات متداول

| دستور | هدف |
|---------|---------|
| `npm run dev` | راه‌اندازی سرور توسعه |
| `npm test` | اجرای مجموعه تست |
| `npm run lint` | بررسی سبک کد |
| `npm run build` | build برای تولید |
| `npm run migrate` | اجرای migrationهای پایگاه‌داده |

## مخاطبان تیم
- سرپرست فنی: Sarah Chen (@sarah.chen)
- مدیر محصول: Mike Johnson (@mike.j)
- DevOps: Alex Kim (@alex.k)

## مسائل شناخته‌شده و راه‌حل‌ها
- connection pooling PostgreSQL در ساعات اوج به ۲۰ محدود است
- راه‌حل: پیاده‌سازی صف query
- مسائل سازگاری Safari 14 با async generatorها
- راه‌حل: استفاده از Babel transpiler

## پروژه‌های مرتبط
- داشبورد تحلیلی: `/projects/analytics`
- برنامه موبایل: `/projects/mobile`
- پنل مدیریت: `/projects/admin`

---
**آخرین به‌روزرسانی**: ۴ اوت ۲۰۲۶
**نسخه Claude Code**: ۲.۱.۲۲۰
**منبع**:
- https://code.claude.com/docs/en/memory
**مدل‌های سازگار**: Claude Fable 5, Claude Opus 5, Claude Sonnet 5, Claude Sonnet 4.6, Claude Opus 4.8, Claude Haiku 4.5
