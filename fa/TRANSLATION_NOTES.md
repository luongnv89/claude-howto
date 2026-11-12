# واژه‌نامه و راهنمای سبک ترجمه فارسی

# Persian Translation Glossary & Style Guide

> **مهم:** این سند قواعد ترجمهٔ مستندات Claude Code به فارسی را تعیین می‌کند. پیش از شروع کار آن را بخوانید.

## اصول پایه

- **زبان:** فارسی روان و رسمی، با لحن آموزشی (نه ترجمهٔ تحت‌اللفظی).
- **اصطلاحات فنی:** نام محصول‌ها، پرچم‌ها، دستورها و برچسب‌های کد به انگلیسی می‌مانند.
- **کد:** محتوای بلوک‌های کد ۱۰۰٪ بدون تغییر می‌ماند؛ فقط کامنت‌ها و متن‌های توضیحی داخل آن‌ها ترجمه می‌شوند.
- **Mermaid:** واژه‌های ساختاری (`graph`, `sequenceDiagram`, `participant`, `-->` و…) انگلیسی می‌مانند؛ برچسب‌های انسانی داخل نمودار ترجمه می‌شوند.
- **پیوندها:** مسیرها و لنگرها (anchor) تغییر نمی‌کنند؛ فقط متن نمایشی ترجمه می‌شود.
- **اعداد فهرست:** نشانگر فهرست باید با رقم ASCII باشد (`1.`، `2.`). رقم‌های فارسی در متن، تاریخ‌ها و جدول‌ها آزادند، اما `۱.` در ابتدای خط توسط Markdown به‌عنوان فهرست شناخته نمی‌شود.
- **نیم‌فاصله (U+200C):** در متن فارسی حفظ می‌شود. در لنگرهای درون‌صفحه‌ای هم گیت‌هاب نیم‌فاصله را نگه می‌دارد، پس لنگرها را با همان نویسه‌ای بنویسید که در عنوان آمده است.
- **پانویس نسخه:** هر صفحه با `**آخرین به‌روزرسانی**`، `**نسخه Claude Code**`، `**منابع**` و `**مدل‌های سازگار**` پایان می‌یابد و باید با فایل انگلیسی هم‌گام باشد.

---

## واژه‌نامهٔ فنی

| English | فارسی | توضیح |
|---------|-------|-------|
| Claude / Claude Code | Claude / Claude Code | نام محصول؛ هرگز «کلود» نوشته نمی‌شود |
| slash command | دستور اسلش | نام ویژگی Claude Code |
| hook | هوک | |
| skill | مهارت | نام ویژگی Claude Code |
| subagent | زیرایجنت | |
| agent | ایجنت | |
| agent team | تیم ایجنت | |
| memory | حافظه | |
| checkpoint / rewind | چک‌پوینت / rewind | `rewind` نام دستور است |
| plugin | پلاگین | |
| marketplace | مارکت‌پلیس | |
| mod | ماد | افزونهٔ ظاهر/رفتار در پلاگین |
| MCP (Model Context Protocol) | MCP | نام پروتکل ترجمه نمی‌شود |
| CLAUDE.md | CLAUDE.md | نام فایل ترجمه نمی‌شود |
| prompt | پرامپت | |
| context / context window | زمینه / پنجرهٔ زمینه | |
| session | نشست | نه «سیشن» |
| usage | استفاده / مصرف | نه «استخدام»؛ در آمار مصرف «مصرف» |
| workflow | گردش کار | |
| repository | مخزن | |
| issue | issue | در متن GitHub به همان شکل |
| release | انتشار / نسخه | بر اساس جمله |
| pull request / PR | pull request / PR | |
| commit | commit | نام دستور git |
| branch | شاخه | |
| merge | ادغام / merge | |
| worktree | درخت کاری / worktree | |
| frontmatter | frontmatter | |
| token | توکن | |
| fork | fork | در مفهوم زیرایجنت فورک‌شده |
| clone | clone | نام دستور git |
| sandbox | سندباکس | |
| permission mode | حالت مجوز | |
| auto mode | حالت خودکار | |
| manual / default mode | حالت دستی (Manual) | مقدار پیکربندی `default` است |
| plan mode | حالت برنامه‌ریزی | |
| settings | تنظیمات | |
| configuration | پیکربندی | |
| environment variable | متغیر محیطی | |
| template | قالب | |
| boilerplate | کد قالبی | |
| debugging | اشکال‌زدایی | |
| linting | لینت کردن | |
| refactoring | بازآرایی / ری‌فاکتور | |
| build | ساخت / بیلد | |
| deploy | استقرار | |
| feature | ویژگی | |
| pipeline | خط لوله | |
| best practice | بهترین شیوه | |
| trade-off | بده‌بستان | |
| endpoint | endpoint | در مستندات API |
| integration | یکپارچه‌سازی | نه «یکپارچگی» در معنای Integration |
| authentication | احراز هویت | نه «اعتبارسنجی» |
| telemetry | تلمتری | |
| team lead / teammate | سرپرست تیم / هم‌تیمی | |

---

## نام‌های ویژگی که ترجمه نمی‌شوند

این‌ها را همیشه به شکل انگلیسی نگه دارید: `/schedule`، `/loop`، `/design`، Remote Control، Agent SDK، Desktop، VS Code، Bedrock، Vertex، Foundry، GitHub Actions، Managed Agents، Claude Design، Ultrareview، Fast Mode، Auto Mode (در متن فارسی: حالت خودکار)، Agent Teams (در متن فارسی: تیم‌های ایجنت).

---

## هم‌گام‌سازی با نسخهٔ انگلیسی

هنگام به‌روزرسانی، تفاوت نسخهٔ انگلیسی را مبنا بگیرید:

```bash
git diff <last-synced-sha> origin/main -- ':!*/*.md' ':!ja' ':!uk' ':!vi' ':!zh'
```

برای هر فایل تغییرکرده، همان بخش را در `fa/` بازترجمه کنید و پانویس نسخه را به‌روز کنید. لنگرهای درون‌صفحه‌ای را پس از هر تغییر عنوان با `python scripts/check_cross_references.py` بررسی کنید.
