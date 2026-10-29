# شروع سریع — دارایی‌های برند

## کپی دارایی‌ها به پروژه خود

```bash
# کپی همه منابع به پروژه وب شما
cp -r resources/ /path/to/your/website/

# یا فقط فاوآیکون‌ها برای وب
cp resources/favicons/* /path/to/your/website/public/
```

## اضافه کردن به HTML (کپی و جای‌گذاری)

```html
<!-- Favicons -->
<link rel="icon" type="image/svg+xml" href="/resources/favicons/favicon-32.svg" sizes="32x32">
<link rel="icon" type="image/svg+xml" href="/resources/favicons/favicon-16.svg" sizes="16x16">
<link rel="apple-touch-icon" href="/resources/favicons/favicon-128.svg">
<link rel="icon" type="image/svg+xml" href="/resources/favicons/favicon-256.svg" sizes="256x256">
<meta name="theme-color" content="#000000">
```

## استفاده در Markdown/مستندات

```markdown
# Claude How To

![Claude How To Logo](resources/logos/claude-howto-logo.svg)

![Icon](resources/icons/claude-howto-icon.svg)
```

## اندازه‌های پیشنهادی

| هدف | اندازه | فایل |
|---------|------|------|
| سربرگ وب‌سایت | 520×120 | `logos/claude-howto-logo.svg` |
| آیکون برنامه | 256×256 | `icons/claude-howto-icon.svg` |
| زبانه مرورگر | 32×32 | `favicons/favicon-32.svg` |
| صفحه‌خانه موبایل | 128×128 | `favicons/favicon-128.svg` |
| برنامه دسکتاپ | 256×256 | `favicons/favicon-256.svg` |
| آواتار کوچک | 64×64 | `favicons/favicon-64.svg` |

## مقادیر رنگ

```css
/* Use these in your CSS */
--color-primary: #000000;
--color-secondary: #6B7280;
--color-accent: #22C55E;
--color-bg-light: #FFFFFF;
--color-bg-dark: #0A0A0A;
```

## معنای طراحی آیکون

**قطب‌نما با براکت کد**:
- حلقه قطب‌نما = ناوبری، مسیر یادگیری ساختاریافته
- سوزن شمال سبز = جهت، پیشرفت، راهنمایی
- سوزن جنوب مشکی = استوار بودن، پایه محکم
- براکت `>` = پرامپت ترمینال، کد، بافت CLI
- علامت‌های درجه‌بندی = دقت، گام‌های ساختاریافته

این نماد «یافتن مسیر در کد با راهنمایی روشن» را نشان می‌دهد.

## چه چیزی را کجا استفاده کنید

### وب‌سایت
- **سربرگ**: لوگو (`logos/claude-howto-logo.svg`)
- **Favicon**: 32px (`favicons/favicon-32.svg`)
- **پیش‌نمایش اجتماعی**: آیکون (`icons/claude-howto-icon.svg`)

### گیت‌هاب
- **بَج README**: آیکون (`icons/claude-howto-icon.svg`) در اندازه 64-128px
- **آواتار مخزن**: آیکون (`icons/claude-howto-icon.svg`)

### رسانه‌های اجتماعی
- **تصویر پروفایل**: آیکون (`icons/claude-howto-icon.svg`)
- **بنر**: لوگو (`logos/claude-howto-logo.svg`)
- **تصویر بندانگشتی**: آیکون در 256×256px

### مستندات
- **سربرگ‌های فصل**: لوگو یا آیکون (با مقیاس مناسب)
- **آیکون‌های ناوبری**: Favicon (32-64px)

---

برای مستندات کامل به [README.md](README.md) مراجعه کنید.
