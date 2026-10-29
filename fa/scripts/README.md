<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../../resources/logos/claude-howto-logo.svg">
</picture>

# اسکریپت‌های ساخت

این پوشه شامل دو تولیدکننده است که فایل‌های مارک‌داون آموزشی را
به قالب‌های قابل انتشار تبدیل می‌کنند:

- [**سازندهٔ EPUB**](#اسکریپت-سازنده-epub) — `build_epub.py`
- [**سازندهٔ وب‌سایت ایستا**](#سازنده-وب‌سایت-ایستا) — `build_website.py`

هر دو، فایل‌های `.md` را تنها منبع حقیقت در نظر می‌گیرند — پس از ویرایش مارک‌داون
اسکریپت مربوط را دوباره اجرا کنید تا خروجی بازتولید شود.

---

# اسکریپت سازندهٔ EPUB

یک کتاب الکترونیکی EPUB از فایل‌های مارک‌داون Claude How-To بسازید.

## امکانات

- فصل‌ها را بر پایهٔ ساختار پوشه سازمان می‌دهد (01-slash-commands، 02-memory و غیره)
- نمودارهای Mermaid را با [Pele](https://github.com/obsidianmd/pele) به تصاویر SVG تبدیل می‌کند؛ بسته‌ای با نسخهٔ ثابت که Node.js آن را اجرا می‌کند؛ متغیرهای CSS روی پس‌زمینهٔ سفید به رنگ‌های ساده تخت می‌شوند تا هر خوانندهٔ EPUB آن‌ها را نمایش دهد
- نمودارهای یکسان را کش می‌کند تا هر نمودار یگانه فقط یک بار رندر شود
- تصویر جلد را از لوگوی پروژه تولید می‌کند
- پیوندهای داخلی مارک‌داون را به ارجاع‌های فصل EPUB تبدیل می‌کند
- حالت خطای سخت‌گیرانه - در صورت ناتوانی در رندر هر نمودار، شکست می‌خورد

## پیش‌نیازها

- Python 3.10+
- [uv](https://github.com/astral-sh/uv)
- Node.js >= 20 روی `PATH` برای رندر نمودارهای Mermaid. بستهٔ Pele با نسخهٔ ثابت در نخستین اجرا دانلود می‌شود (یک بار به شبکه نیاز است)، با sha256 بررسی و در `scripts/.vendor-cache/pele/` کش می‌شود

## شروع سریع

```bash
# ساده‌ترین روش - uv همه‌چیز را خودش انجام می‌دهد
uv run scripts/build_epub.py
```

## راه‌اندازی محیط توسعه

```bash
# ساخت محیط مجازی
uv venv

# فعال‌سازی و نصب وابستگی‌ها
source .venv/bin/activate
uv pip install -r requirements-dev.txt

# اجرای تست‌ها
pytest scripts/tests/ -v

# اجرای اسکریپت
python scripts/build_epub.py
```

## گزینه‌های خط فرمان

```
usage: build_epub.py [-h] [--root ROOT] [--output OUTPUT] [--verbose]
                     [--lang {en,vi,zh,ja}]

options:
  -h, --help            show this help message and exit
  --root, -r ROOT       Root directory (default: repo root)
  --output, -o OUTPUT   Output path (default: claude-howto-guide.epub)
  --verbose, -v         Enable verbose logging
  --lang {en,vi,zh,ja}  Language to build (default: en)
```

## نمونه‌ها

```bash
# ساخت با خروجی پرجزئیات
uv run scripts/build_epub.py --verbose

# مسیر خروجی سفارشی
uv run scripts/build_epub.py --output ~/Desktop/claude-guide.epub

# ساخت نسخهٔ ترجمه‌شده
uv run scripts/build_epub.py --lang vi
```

## خروجی

فایل `claude-howto-guide.epub` را در پوشهٔ ریشهٔ مخزن ایجاد می‌کند.

فایل EPUB این موارد را در بر می‌گیرد:
- تصویر جلد با لوگوی پروژه
- فهرست مطالب با بخش‌های تودرتو
- همهٔ محتوای مارک‌داون که به HTML سازگار با EPUB تبدیل شده است
- نمودارهای Mermaid که به تصاویر SVG تبدیل شده‌اند

## اجرای تست‌ها

```bash
# با محیط مجازی
source .venv/bin/activate
pytest scripts/tests/ -v

# یا مستقیماً با uv
uv run --with pytest --with pytest-asyncio \
    --with ebooklib --with markdown --with beautifulsoup4 \
    --with pillow \
    pytest scripts/tests/ -v
```

## وابستگی‌ها

از طریق فرادادهٔ درون‌خطی اسکریپت PEP 723 مدیریت می‌شود:

| بسته | کاربرد |
|---------|---------|
| `ebooklib` | تولید EPUB |
| `markdown` | تبدیل مارک‌داون به HTML |
| `beautifulsoup4` | تجزیهٔ HTML |
| `pillow` | تولید تصویر جلد |

## رفع مشکلات

**ساخت با خطای `Pele is unavailable` شکست می‌خورد**: Node.js >= 20 را نصب کنید و مطمئن شوید `node` روی `PATH` قرار دارد (`node --version`).

**خطا در دانلود یا checksum بستهٔ Pele**: نخستین ساخت، بستهٔ Pele با نسخهٔ ثابت را از cdn.jsdelivr.net دانلود می‌کند و sha256 هر فایل را بررسی می‌کند. در حالت آفلاین یا پشت پراکسی، یک ساخت را با دسترسی به شبکه اجرا کنید؛ ساخت‌های بعدی از کش در `scripts/.vendor-cache/pele/<version>/` استفاده می‌کنند. ناهمخوانی checksum یعنی دانلود تغییر کرده یا ناقص شده است: آن پوشه را حذف کنید و دوباره بسازید.

**نبود لوگو**: اگر `claude-howto-logo.png` پیدا نشود، اسکریپت جلدی فقط متنی تولید می‌کند.

---

# سازندهٔ وب‌سایت ایستا

یک وب‌سایت ایستای شکیل و سازگار با موبایل از همان فایل‌های مارک‌داونی بسازید
که ساخت EPUB از آن‌ها استفاده می‌کند. وب‌سایت، نمای رندرشده است؛ فایل‌های `.md`
همچنان تنها منبع حقیقت می‌مانند.

## امکانات

- برای هر منبع مارک‌داون یک صفحهٔ HTML — پیوندهای داخلی `.md` به
  صفحه‌های متناظر در سایت بازنویسی می‌شوند
- ارجاع‌ها به فایل‌های غیرمارک‌داون مخزن (قالب‌ها، اسکریپت‌ها، JSON) به
  نشانی‌های blob گیت‌هاب تبدیل می‌شوند که منبع را در github.com باز می‌کنند
- نمودارهای Mermaid در سمت کلاینت با Pele (`pele.global.js`) رندر می‌شوند و
  از سایت ساخته‌شده ارائه می‌شوند (بدون CDN در زمان اجرا)؛ از کلید حالت تاریک پیروی می‌کنند
- Tailwind CSS با CLI مستقل (باینری Go، بدون Node.js) کامپایل می‌شود و
  از سایت ساخته‌شده ارائه می‌شود — چیدمان واکنش‌گرا با ناوبری کناری،
  فهرست مطالب درون‌صفحه، کلید حالت تاریک و ناوبری صفحهٔ قبلی/بعدی
- فونت‌های Inter + JetBrains Mono در کنار CSS به‌صورت خودمیزبان ارائه می‌شوند — بدون
  درخواست به طرف سوم هنگام بارگذاری صفحه
- ترتیب برنامهٔ درسی EPUB را بازتاب می‌دهد (`01-` … `10-` به‌علاوهٔ اسناد سطح بالا)
- به‌شکل فایل‌های ایستای ساده قابل میزبانی است — برای استقرار در GitHub Pages طراحی شده است

## شروع سریع

```bash
# ساخت وب‌سایت انگلیسی در ./site/
uv run scripts/build_website.py

# پیش‌نمایش محلی
python -m http.server --directory site 8080
# سپس http://localhost:8080 را باز کنید
```

## گزینه‌های خط فرمان

```
usage: build_website.py [-h] [--root ROOT] [--output OUTPUT]
                        [--lang {en,vi,zh,ja,uk}] [--repo-url REPO_URL]
                        [--branch BRANCH] [--verbose]

options:
  --root, -r ROOT       Source root (default: repo root)
  --output, -o OUTPUT   Output directory (default: <repo>/site)
  --lang LANG           Language to build: en | vi | zh | ja | uk
  --repo-url URL        GitHub repo for blob links (default: luongnv89/claude-howto)
  --branch BRANCH       Branch for blob links (default: main)
  --verbose, -v         Enable verbose logging
```

## استقرار در GitHub Pages

مخزن یک ورک‌فلوی در `.github/workflows/pages.yml` دارد که سایت را در هر
پوش به `main` می‌سازد (زمانی که فایل `.md` یا فایل سازنده‌ای تغییر کند) و
از طریق `actions/deploy-pages` منتشر می‌کند. برای فعال‌سازی، GitHub Pages را در تنظیمات مخزن
با **Source: GitHub Actions** فعال کنید.

## معماری

`build_website.py` منطق ترتیب فصل‌ها را از `build_epub.py` بازاستفاده می‌کند و
قالب‌های HTML را زیر `scripts/website_templates/` ارائه می‌دهد:

- `page.html.j2` — قالب Jinja2 مخصوص هر صفحه با ناوبری کناری، فهرست مطالب و قبلی/بعدی
- `tailwind.config.js`، `tailwind.input.css` — پیکربندی و CSS ورودی برای
  CLI مستقل Tailwind؛ این CLI خروجی HTML را پیمایش می‌کند و
  `site/assets/tailwind.css` را تنها با کلاس‌های واقعاً استفاده‌شده تولید می‌کند
- `site.css` — لایهٔ کوچکی از سبک‌های مخصوص سایت به‌همراه تم Pygments

باینری CLI مربوط به Tailwind، بستهٔ Pele و فایل‌های فونت در
نخستین ساخت در `scripts/.vendor-cache/` دانلود می‌شوند (در gitignore) — ببینید
`scripts/vendor_assets.py`.

لنگرهای عنوان با الگوریتم دقیق موجود در
`check_cross_references.heading_to_anchor` تولید می‌شوند، بنابراین پیوندهای `#anchor` که
هوک پیش از کامیت اعتبارسنجی می‌کند، در سایت رندرشده به‌درستی حل می‌شوند.
