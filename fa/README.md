<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

<p align="center">
  <a href="https://github.com/trending">
    <img src="https://img.shields.io/badge/GitHub-🔥%20%231%20Trending-purple?style=for-the-badge&logo=github"/>
  </a>
</p>

[![GitHub Stars](https://img.shields.io/github/stars/luongnv89/claude-howto?style=flat&color=gold)](https://github.com/luongnv89/claude-howto/stargazers)
[![GitHub Forks](https://img.shields.io/github/forks/luongnv89/claude-howto?style=flat)](https://github.com/luongnv89/claude-howto/network/members)
[![License: MIT](https://img.shields.io/badge/License-MIT-blue.svg)](../LICENSE)
[![Version](https://img.shields.io/badge/version-2.1.310-brightgreen)](CHANGELOG.md)
[![Claude Code](https://img.shields.io/badge/Claude_Code-2.1+-purple)](https://code.claude.com)

🌐 **زبان / Language / 语言 / Мова:** [English](../README.md) | [Tiếng Việt](../vi/README.md) | [中文](../zh/README.md) | [Українська](../uk/README.md) | [日本語](../ja/README.md) | [فارسی](README.md)

# تسلط بر Claude Code در یک آخر هفته

از تایپ کردن `claude` تا هماهنگ‌سازی ایجنت‌ها، هوک‌ها، مهارت‌ها و سرورهای MCP — با آموزش‌های تصویری، قالب‌های آماده کپی و مسیر یادگیری راهنمایی‌شده.

**[در ۱۵ دقیقه شروع کنید](#شروع-در-۱۵-دقیقه)** | **[سطح خود را پیدا کنید](#مطمئن-نیستید-از-کجا-شروع-کنید)** | **[کاتالوگ ویژگی‌ها را مرور کنید](CATALOG.md)**

---

## فهرست مطالب

- [مشکل](#مشکل)
- [چگونه Claude How To این مشکل را حل می‌کند](#چگونه-claude-how-to-این-مشکل-را-حل-می‌کند)
- [نحوه کارکرد](#نحوه-کارکرد)
- [مطمئن نیستید از کجا شروع کنید؟](#مطمئن-نیستید-از-کجا-شروع-کنید)
- [شروع در ۱۵ دقیقه](#شروع-در-۱۵-دقیقه)
- [با این چه چیزی می‌توانید بسازید؟](#با-این-چه-چیزی-می‌توانید-بسازید)
- [سوالات متداول](#سوالات-متداول)
- [مشارکت](#مشارکت)
- [لایسنس](#لایسنس)

---

## مشکل

شما Claude Code را نصب کرده‌اید. چند پرامپت اجرا کرده‌اید. حالا چه؟

- **مستندات رسمی ویژگی‌ها را توصیف می‌کنند — اما نشان نمی‌دهند چگونه آن‌ها را ترکیب کنید.** شما می‌دانید که دستورهای اسلش وجود دارند، اما نمی‌دانید چگونه آن‌ها را با هوک‌ها، حافظه و زیرایجنت‌ها در یک خط لوله کاری که واقعاً ساعت‌ها زمان صرفه‌جویی می‌کند، زنجیره کنید.
- **مسیر یادگیری روشنی وجود ندارد.** آیا باید MCP را قبل از هوک‌ها یاد بگیرید؟ مهارت‌ها قبل از زیرایجنت‌ها؟ در نهایت همه‌چیز را سطحی می‌خوانید و به چیزی تسلط پیدا نمی‌کنید.
- **مثال‌ها بیش از حد ساده هستند.** یک دستور اسلش «hello world» به شما کمک نمی‌کند یک خط لوله بازبینی کد تولیدی بسازید که از حافظه استفاده می‌کند، کارها را به ایجنت‌های تخصصی سپرده و به‌طور خودکار اسکن‌های امنیتی اجرا می‌کند.

شما ۹۰ درصد قدرت Claude Code را روی میز رها می‌کنید — و نمی‌دانید چه چیزی را نمی‌دانید.

---

## چگونه Claude How To این مشکل را حل می‌کند

این فقط یک مرجع ویژگی نیست. یک **راهنمای ساختاریافته، تصویری و مبتنی بر مثال** است که به شما می‌آموزد هر ویژگی Claude Code را با قالب‌های واقعی که می‌توانید همین امروز در پروژه خود کپی کنید، استفاده کنید.

| | مستندات رسمی | این راهنما |
|--|---------------|------------|
| **قالب** | مستندات مرجع | آموزش‌های تصویری با نمودارهای Mermaid |
| **عمق** | توصیف ویژگی‌ها | نحوه کارکرد زیر کاپوت |
| **مثال‌ها** | قطعات پایه | قالب‌های آماده تولید که بلافاصله استفاده می‌کنید |
| **ساختار** | سازمان‌دهی بر اساس ویژگی | مسیر یادگیری پیش‌رونده (مبتدی تا پیشرفته) |
| **آماده‌سازی** | خودراهنما | نقشه راه راهنمایی‌شده با برآورد زمان |
| **ارزیابی خودکار** | هیچ | آزمون‌های تعاملی برای یافتن شکاف‌ها و ساخت مسیر شخصی‌سازی‌شده |

### آنچه دریافت می‌کنید:

- **۱۰ ماژول آموزشی** که هر ویژگی Claude Code را پوشش می‌دهد — از دستورهای اسلش تا تیم‌های ایجنت سفارشی
- **کانفیگ‌های آماده کپی** — دستورهای اسلش، قالب‌های CLAUDE.md، اسکریپت‌های هوک، کانفیگ‌های MCP، تعریف‌های زیرایجنت و بسته‌های کامل پلاگین
- **نمودارهای Mermaid** که نشان می‌دهد هر ویژگی درونی چگونه کار می‌کند، تا درک کنید *چرا*، نه فقط *چگونه*
- **مسیر یادگیری راهنمایی‌شده** که شما را در ۱۱ تا ۱۳ ساعت از مبتدی به کاربر حرفه‌ای می‌رساند
- **ارزیابی خودکار داخلی** — `/self-assessment` یا `/lesson-quiz hooks` را مستقیماً در Claude Code اجرا کنید تا شکاف‌ها را شناسایی کنید

**[شروع مسیر یادگیری ←](LEARNING-ROADMAP.md)**

---

## نحوه کارکرد

### ۱. سطح خود را پیدا کنید

[آزمون ارزیابی خودکار](LEARNING-ROADMAP.md#-سطح-خود-را-پیدا-کنید) را انجام دهید یا `/self-assessment` را در Claude Code اجرا کنید. یک نقشه راه شخصی‌سازی‌شده بر اساس آنچه از قبل می‌دانید دریافت کنید.

### ۲. مسیر راهنمایی‌شده را دنبال کنید

۱۰ ماژول را به ترتیب کار کنید — هر ماژون روی قبلی ساخته می‌شود. قالب‌ها را مستقیماً هنگام یادگیری در پروژه خود کپی کنید.

### ۳. ویژگی‌ها را در خطوط لوله کاری ترکیب کنید

قدرت واقعی در ترکیب ویژگی‌هاست. یاد بگیرید دستورهای اسلش + حافظه + زیرایجنت‌ها + هوک‌ها را در خطوط لوله خودکار که بازبینی کد، استقرار و تولید مستندات را مدیریت می‌کنند، سیم‌کشی کنید.

### ۴. درک خود را آزمایش کنید

`/lesson-quiz [topic]` را بعد از هر ماژون اجرا کنید. آزمون دقیقاً مشخص می‌کند چه چیزی را از دست داده‌اید تا شکاف‌ها را سریع پر کنید.

**[شروع در ۱۵ دقیقه](#شروع-در-۱۵-دقیقه)**

---

## مورد اعتماد توسعه‌دهندگان

- **ستاره‌های GitHub** از توسعه‌دهندگانی که روزانه از Claude Code استفاده می‌کنند
- **فورک‌ها** از تیم‌هایی که این راهنما را برای خط لوله کاری خود تطبیق می‌دهند
- **فعالاً نگهداری می‌شود** — با هر نسخه Claude Code هماهنگ است (آخرین: v2.1.310، اکتبر ۲۰۲۶)
- **محور جامعه** — مشارکت‌هایی از توسعه‌دهندگانی که کانفیگ‌های واقعی خود را به اشتراک می‌گذارند

[![نمودار تاریخچه ستاره](https://api.star-history.com/svg?repos=luongnv89/claude-howto&type=Date)](https://star-history.com/#luongnv89/claude-howto&Date)

---

## مطمئن نیستید از کجا شروع کنید؟

ارزیابی خودکار را انجام دهید یا سطح خود را انتخاب کنید:

| سطح | شما می‌توانید... | از اینجا شروع کنید | زمان |
|-------|-----------|------------|------|
| **مبتدی** | Claude Code را شروع کرده و چت کنید | [دستورهای اسلش](01-slash-commands/) | ~۲.۵ ساعت |
| **متوسط** | از CLAUDE.md و کامندهای سفارشی استفاده کنید | [مهارت‌ها](03-skills/) | ~۳.۵ ساعت |
| **پیشرفته** | سرورهای MCP و هوک‌ها را کانفیگ کنید | [ویژگی‌های پیشرفته](09-advanced-features/) | ~۵ ساعت |

**مسیر کامل یادگیری با همه ۱۰ ماژول:**

| ترتیب | ماژول | سطح | زمان |
|-------|--------|-------|------|
| ۱ | [دستورهای اسلش](01-slash-commands/) | مبتدی | ۳۰ دقیقه |
| ۲ | [حافظه](02-memory/) | مبتدی+ | ۴۵ دقیقه |
| ۳ | [چک‌پوینت‌ها](08-checkpoints/) | متوسط | ۴۵ دقیقه |
| ۴ | [پایه‌های CLI](10-cli/) | مبتدی+ | ۳۰ دقیقه |
| ۵ | [مهارت‌ها](03-skills/) | متوسط | ۱ ساعت |
| ۶ | [هوک‌ها](06-hooks/) | متوسط | ۱ ساعت |
| ۷ | [MCP](05-mcp/) | متوسط+ | ۱ ساعت |
| ۸ | [زیرایجنت‌ها](04-subagents/) | متوسط+ | ۱.۵ ساعت |
| ۹ | [ویژگی‌های پیشرفته](09-advanced-features/) | پیشرفته | ۲-۳ ساعت |
| ۱۰ | [پلاگین‌ها](07-plugins/) | پیشرفته | ۲ ساعت |

**[نقشه راه کامل یادگیری ←](LEARNING-ROADMAP.md)**

---

## شروع در ۱۵ دقیقه

> **یادداشت نصب**: از v2.1.113 به بعد، Claude Code به‌صورت یک باینری بومی برای هر پلتفرم (macOS/Linux/Windows) عرضه می‌شود. نصب پیشنهادی نصب‌کننده بومی است (`curl -fsSL https://claude.ai/install.sh | bash`)؛ نصب npm در README رسمی منسوخ شده است؛ از نصب‌کننده بومی، Homebrew (`brew install --cask claude-code`) یا WinGet (`winget install Anthropic.ClaudeCode`) استفاده کنید. برای مرجع، `npm install -g @anthropic-ai/claude-code` همان باینری بومی را از طریق یک وابستگی اختیاری برای هر پلتفرم در زمان نصب دریافت می‌کند. از v2.1.116، دانلودها از `https://downloads.claude.ai/claude-code-releases` انجام می‌شود — پروکسی‌های شرکتی باید این میزبان را به فهرست مجاز اضافه کنند.

```bash
# 1. کلون کردن راهنما
git clone https://github.com/luongnv89/claude-howto.git
cd claude-howto

# 2. اولین دستور اسلش خود را کپی کنید
mkdir -p /path/to/your-project/.claude/commands
cp 01-slash-commands/optimize.md /path/to/your-project/.claude/commands/

# 3. امتحان کنید — در Claude Code تایپ کنید:
# /optimize

# 4. آماده برای بیشتر؟ حافظه پروژه را تنظیم کنید:
cp 02-memory/project-CLAUDE.md /path/to/your-project/CLAUDE.md

# 5. یک مهارت نصب کنید:
cp -r 03-skills/code-review-specialist ~/.claude/skills/
```

راه‌اندازی کامل را می‌خواهید؟ در اینجا **راه‌اندازی اولیه ۱ ساعته** آمده است:

```bash
# دستورهای اسلش (15 min)
cp 01-slash-commands/*.md .claude/commands/

# حافظه پروژه (15 min)
cp 02-memory/project-CLAUDE.md ./CLAUDE.md

# نصب یک مهارت (15 min)
cp -r 03-skills/code-review-specialist ~/.claude/skills/

# هدف آخر هفته: اضافه کردن هوک‌ها، زیرایجنت‌ها، MCP و پلاگین‌ها
# مسیر یادگیری را برای راه‌اندازی راهنمایی‌شده دنبال کنید
```

**[مشاهده مرجع نصب کامل](#شروع-در-۱۵-دقیقه)**

---

## با این چه چیزی می‌توانید بسازید؟

| مورد استفاده | ویژگی‌هایی که ترکیب می‌کنید |
|----------|------------------------|
| **بازبینی خودکار کد** | دستورهای اسلش + زیرایجنت‌ها + حافظه + MCP |
| **آماده‌سازی تیم** | حافظه + دستورهای اسلش + پلاگین‌ها |
| **خودکارسازی CI/CD** | مرجع CLI + هوک‌ها + وظایف پس‌زمینه |
| **تولید مستندات** | مهارت‌ها + زیرایجنت‌ها + پلاگین‌ها |
| **ممیزی‌های امنیتی** | زیرایجنت‌ها + مهارت‌ها + هوک‌ها (حالت فقط‌خواندنی) |
| **خطوط لوله DevOps** | پلاگین‌ها + MCP + هوک‌ها + وظایف پس‌زمینه |
| **بازطراحی پیچیده** | چک‌پوینت‌ها + حالت برنامه‌ریزی + هوک‌ها |

---

## سوالات متداول

**آیا این رایگان است؟**
بله. با لایسنس MIT، برای همیشه رایگان است. در پروژه‌های شخصی، در محل کار، در تیم خود استفاده کنید — بدون محدودیت به جز گذاردن اعلان لایسنس.

**آیا این نگهداری می‌شود؟**
فعالاً. راهنما با هر نسخه Claude Code هماهنگ است. نسخه فعلی: v2.1.310 (اکتبر ۲۰۲۶)، سازگار با Claude Code 2.1+.

**این چگونه از مستندات رسمی متفاوت است؟**
مستندات رسمی یک مرجع ویژگی هستند. این راهنما یک آموزش با نمودارها، قالب‌های آماده تولید و مسیر یادگیری پیش‌رونده است. این دو مکمل یکدیگرند — برای یادگیری از اینجا شروع کنید، وقتی به جزئیات نیاز دارید به مستندات مراجعه کنید.

**چقدر طول می‌کشد همه‌چیز را بگذرانید؟**
۱۱ تا ۱۳ ساعت برای مسیر کامل. اما در ۱۵ دقیقه ارزش فوری دریافت می‌کنید — فقط یک قالب دستور اسلش را کپی و امتحان کنید.

**آیا می‌توانم با Claude Sonnet / Haiku / Opus از این استفاده کنم؟**
بله. همه قالب‌ها با Claude Fable 5.1، Claude Fable 5، Claude Opus 5.5، Claude Opus 5، Claude Sonnet 5.5، Claude Sonnet 5، Claude Sonnet 4.6، Claude Opus 4.8، Claude Haiku 5.5 و Claude Haiku 4.5 کار می‌کنند.

**آیا می‌توانم مشارکت کنم؟**
قطعاً. به [CONTRIBUTING.md](CONTRIBUTING.md) برای راهنمایی‌ها مراجعه کنید. از مثال‌های جدید، رفع اشکال، بهبود مستندات و قالب‌های جامعه استقبال می‌کنیم.

**آیا می‌توانم این را آفلاین بخوانم؟**
بله. `uv run scripts/build_epub.py` را اجرا کنید تا یک کتاب الکترونیکی EPUB با همه محتوا و نمودارهای رندر‌شده تولید شود.

---

## امروز تسلط بر Claude Code را شروع کنید

شما از قبل Claude Code را نصب کرده‌اید. تنها چیزی که بین شما و بهره‌وری ۱۰ برابری فاصله دارد، دانستن نحوه استفاده از آن است. این راهنما مسیر ساختاریافته، توضیحات تصویری و قالب‌های آماده کپی را برای رسیدن به آن به شما می‌دهد.

با لایسنس MIT. برای همیشه رایگان. آن را کلون کنید، فورک کنید، مال خودتان کنید.

**[شروع مسیر یادگیری ←](LEARNING-ROADMAP.md)** | **[مرور کاتالوگ ویژگی‌ها](CATALOG.md)** | **[شروع در ۱۵ دقیقه](#شروع-در-۱۵-دقیقه)**

---

<details>
<summary>ناوبری سریع — همه ویژگی‌ها</summary>

| ویژگی | توضیح | پوشه |
|---------|-------------|--------|
| **کاتالوگ ویژگی‌ها** | مرجع کامل با کامندهای نصب | [CATALOG.md](CATALOG.md) |
| **دستورهای اسلش** | میان‌برهای فراخوانی‌شده توسط کاربر | [01-slash-commands/](01-slash-commands/) |
| **حافظه** | زمینه پایدار | [02-memory/](02-memory/) |
| **مهارت‌ها** | قابلیت‌های قابل استفاده مجدد | [03-skills/](03-skills/) |
| **زیرایجنت‌ها** | دستیاران هوش مصنوعی تخصصی | [04-subagents/](04-subagents/) |
| **پروتکل MCP** | دسترسی به ابزار خارجی | [05-mcp/](05-mcp/) |
| **هوک‌ها** | خودکارسازی رویدادمحور | [06-hooks/](06-hooks/) |
| **پلاگین‌ها** | ویژگی‌های بسته‌بندی‌شده | [07-plugins/](07-plugins/) |
| **چک‌پوینت‌ها** | اسنپ‌شات جلسه و بازگشت | [08-checkpoints/](08-checkpoints/) |
| **ویژگی‌های پیشرفته** | برنامه‌ریزی، تفکر، وظایف پس‌زمینه | [09-advanced-features/](09-advanced-features/) |
| **مرجع CLI** | کامندها، پرچم‌ها و گزینه‌ها | [10-cli/](10-cli/) |
| **پست‌های وبلاگ** | نمونه‌های استفاده واقعی | [پست‌های وبلاگ](https://medium.com/@luongnv89) |

</details>

<details>
<summary>مقایسه ویژگی‌ها</summary>

| ویژگی | فراخوانی | پایداری | بهترین برای |
|---------|-----------|------------|----------|
| **دستورهای اسلش** | دستی (`/cmd`) | فقط جلسه | میان‌برهای سریع |
| **حافظه** | بارگذاری خودکار | بین جلسه‌ای | یادگیری بلندمدت |
| **مهارت‌ها** | فراخوانی خودکار | سیستم فایل | خط لوله‌های خودکار |
| **زیرایجنت‌ها** | سپردن خودکار | زمینه ایزوله | توزیع وظایف |
| **پروتکل MCP** | پرس‌وجوی خودکار | بلادرنگ | دسترسی داده زنده |
| **هوک‌ها** | راه‌اندازی رویدادی | کانفیگ‌شده | خودکارسازی و اعتبارسنجی |
| **پلاگین‌ها** | یک کامند | همه ویژگی‌ها | راه‌حل‌های کامل |
| **چک‌پوینت‌ها** | دستی/خودکار | مبتنی جلسه | آزمایش امن |
| **حالت برنامه‌ریزی** | دستی/خودکار | فاز برنامه | پیاده‌سازی‌های پیچیده |
| **وظایف پس‌زمینه** | دستی | مدت زمان وظیفه | عملیات‌های طولانی‌مدت |
| **مرجع CLI** | کامندهای ترمینال | جلسه/اسکریپت | خودکارسازی و اسکریپت‌نویسی |

</details>

<details>
<summary>مرجع سریع نصب</summary>

```bash
# دستورهای اسلش
cp 01-slash-commands/*.md .claude/commands/

# حافظه
cp 02-memory/project-CLAUDE.md ./CLAUDE.md

# مهارت‌ها
cp -r 03-skills/code-review-specialist ~/.claude/skills/

# زیرایجنت‌ها
cp 04-subagents/*.md .claude/agents/

# MCP
claude mcp add --transport http github https://api.githubcopilot.com/mcp/ --header "Authorization: Bearer YOUR_GITHUB_PAT"

# هوک‌ها
mkdir -p ~/.claude/hooks
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh

# پلاگین‌ها (بارگذاری یک پلاگین محلی از ریشه مخزن)
claude --plugin-dir ./07-plugins/pr-review

# چک‌پوینت‌ها (خودکار فعال می‌شوند، در تنظیمات کانفیگ کنید)
# به 08-checkpoints/README.md مراجعه کنید

# ویژگی‌های پیشرفته (در تنظیمات کانفیگ کنید)
# به 09-advanced-features/config-examples.json مراجعه کنید

# مرجع CLI (نیازی به نصب نیست)
# به 10-cli/README.md برای نمونه‌های استفاده مراجعه کنید
```

</details>

<details>
<summary>۰۱. دستورهای اسلش</summary>

**محل**: [01-slash-commands/](01-slash-commands/)

**چیست**: میان‌برهای فراخوانی‌شده توسط کاربر که به‌صورت فایل‌های Markdown ذخیره می‌شوند

**مثال‌ها**:
- `optimize.md` - تحلیل بهینه‌سازی کد
- `pr.md` - آماده‌سازی درخواست pull
- `generate-api-docs.md` - تولید مستندات API

**نصب**:
```bash
cp 01-slash-commands/*.md /path/to/project/.claude/commands/
```

**استفاده**:
```
/optimize
/pr
/generate-api-docs
```

**بیشتر بدانید**: [کشف دستورهای اسلشی Claude Code](https://medium.com/@luongnv89/discovering-claude-code-slash-commands-cdc17f0dfb29)

</details>

<details>
<summary>۰۲. حافظه</summary>

**محل**: [02-memory/](02-memory/)

**چیست**: زمینه پایدار بین جلسه‌ها

**مثال‌ها**:
- `project-CLAUDE.md` - استانداردهای پروژه برای کل تیم
- `directory-api-CLAUDE.md` - قوانین خاص دایرکتوری
- `personal-CLAUDE.md` - ترجیحات شخصی

**نصب**:
```bash
# حافظه پروژه
cp 02-memory/project-CLAUDE.md /path/to/project/CLAUDE.md

# حافظه دایرکتوری
cp 02-memory/directory-api-CLAUDE.md /path/to/project/src/api/CLAUDE.md

# حافظه شخصی
cp 02-memory/personal-CLAUDE.md ~/.claude/CLAUDE.md
```

**استفاده**: به‌طور خودکار توسط Claude بارگذاری می‌شود

</details>

<details>
<summary>۰۳. مهارت‌ها</summary>

**محل**: [03-skills/](03-skills/)

**چیست**: قابلیت‌های قابل استفاده مجدد، فراخوانی خودکار با دستورالعمل‌ها و اسکریپت‌ها

**مثال‌ها**:
- `code-review-specialist/` - بازبینی جامع کد با اسکریپت‌ها
- `brand-voice/` - بررسی‌کننده یکپارچگی لحن برند
- `doc-generator/` - تولیدکننده مستندات API

**نصب**:
```bash
# مهارت‌های شخصی
cp -r 03-skills/code-review-specialist ~/.claude/skills/

# مهارت‌های پروژه
cp -r 03-skills/code-review-specialist /path/to/project/.claude/skills/
```

**استفاده**: هنگام مرتبط بودن به‌طور خودکار فراخوانی می‌شود

</details>

<details>
<summary>۰۴. زیرایجنت‌ها</summary>

**محل**: [04-subagents/](04-subagents/)

**چیست**: دستیاران هوش مصنوعی تخصصی با زمینه‌های ایزوله و پرامپت‌های سفارشی

**مثال‌ها**:
- `code-reviewer.md` - تحلیل جامع کیفیت کد
- `test-engineer.md` - استراتژی و پوشش تست
- `documentation-writer.md` - مستندسازی فنی
- `secure-reviewer.md` - بازبینی متمرکز بر امنیت (فقط‌خواندنی)
- `implementation-agent.md` - پیاده‌سازی کامل ویژگی

**نصب**:
```bash
cp 04-subagents/*.md /path/to/project/.claude/agents/
```

**استفاده**: به‌طور خودکار توسط ایجنت اصلی سپرده می‌شود

</details>

<details>
<summary>۰۵. پروتکل MCP</summary>

**محل**: [05-mcp/](05-mcp/)

**چیست**: پروتکل Model Context برای دسترسی به ابزارها و APIهای خارجی

**مثال‌ها**:
- `github-mcp.json` - یکپارچگی GitHub
- `database-mcp.json` - پرس‌وجوی پایگاه داده (‏`DATABASE_URL` را به یک کاربر فقط-SELECT بدهید؛ [پیکربندی فقط‌خواندنی](05-mcp/README.md#نمونه-۲-راه‌اندازی-database-mcp) را ببینید)
- `filesystem-mcp.json` - عملیات فایل
- `multi-mcp.json` - چندین سرور MCP

**نصب**:
```bash
# تنظیم متغیرهای محیطی
export DATABASE_URL="postgresql://..."

# اضافه کردن سرور MCP از طریق CLI
claude mcp add --transport http github https://api.githubcopilot.com/mcp/ --header "Authorization: Bearer YOUR_GITHUB_PAT"

# یا اضافه کردن دستی به .mcp.json پروژه (به 05-mcp/ برای مثال‌ها مراجعه کنید)
```

**استفاده**: ابزارهای MCP پس از کانفیگ برای Claude به‌طور خودکار در دسترس هستند

</details>

<details>
<summary>۰۶. هوک‌ها</summary>

**محل**: [06-hooks/](06-hooks/)

**چیست**: کامندهای شل رویدادمحور که در پاسخ به رویدادهای Claude Code به‌طور خودکار اجرا می‌شوند

**مثال‌ها**:
- `format-code.sh` - قالب‌بندی خودکار کد پس از نوشتن
- `pre-commit.sh` - اجرای تست‌ها قبل از کامیت
- `security-scan.sh` - اسکن برای مسائل امنیتی
- `log-bash.sh` - ثبت همه کامندهای bash
- `validate-prompt.sh` - اعتبارسنجی پرامپت‌های کاربر
- `notify-team.sh` - ارسال اعلان‌ها هنگام رویدادها

**نصب**:
```bash
mkdir -p ~/.claude/hooks
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh
```

هوک‌ها را در `~/.claude/settings.json` کانفیگ کنید:
```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write",
        "hooks": [
          { "type": "command", "command": "~/.claude/hooks/format-code.sh" },
          { "type": "command", "command": "~/.claude/hooks/security-scan.sh" }
        ]
      }
    ]
  }
}
```

**استفاده**: هوک‌ها به‌طور خودکار هنگام رویدادها اجرا می‌شوند

**انواع هوک** (۵): `command`، `http`، `prompt`، `mcp_tool`، `agent` — نحوه اجرای هوک.

**رویدادهای هوک** (۳۳ مورد، در ۴ دسته) — زمان اجرا:
- **هوک‌های ابزار**: `PreToolUse`، `PostToolUse`، `PostToolUseFailure`، `PostToolBatch`، `PermissionRequest`، `PermissionDenied`
- **هوک‌های جلسه**: `SessionStart`، `Setup`، `SessionEnd`، `Stop`، `StopFailure`، `SubagentStart`، `SubagentStop`
- **هوک‌های وظیفه**: `UserPromptSubmit`، `UserPromptExpansion`، `MessageDisplay`، `TaskCompleted`، `TaskCreated`، `TeammateIdle` — `TaskCompleted` و `TaskCreated` فقط وقتی ابزارهای todo فعال باشند فعال می‌شوند، که به‌طور پیش‌فرض فقط روی مدل‌های Claude 3.x، Opus 4 تا 4.7، Sonnet 4 تا 4.6 و Haiku 4.5 در دسترس است (`CLAUDE_CODE_ENABLE_TODO_TOOLS=1` آن‌ها را بازمی‌گرداند)
- **هوک‌های چرخه حیات**: `ConfigChange`، `CwdChanged`، `DirectoryAdded`، `FileChanged`، `PreCompact`، `PostCompact`، `PreModelSwitch`، `PostModelSwitch`، `WorktreeCreate`، `WorktreeRemove`، `Notification`، `InstructionsLoaded`، `Elicitation`، `ElicitationResult`

</details>

<details>
<summary>۰۷. پلاگین‌ها</summary>

**محل**: [07-plugins/](07-plugins/)

**چیست**: مجموعه‌های بسته‌بندی‌شده از کامندها، ایجنت‌ها، MCP و هوک‌ها

**مثال‌ها**:
- `pr-review/` - خط لوله کامل بازبینی PR
- `devops-automation/` - استقرار و پایش
- `documentation/` - تولید مستندات

**نصب**:
```bash
# از ریشه مخزن (این مخزن هیچ مارکت‌پلیسی ندارد، بنابراین /plugin install اعمال نمی‌شود)
claude --plugin-dir ./07-plugins/pr-review
claude --plugin-dir ./07-plugins/devops-automation
claude --plugin-dir ./07-plugins/documentation
```

**استفاده**: از دستورهای اسلش و ویژگی‌های بسته‌بندی‌شده استفاده کنید

</details>

<details>
<summary>۰۸. چک‌پوینت‌ها و بازگشت</summary>

**محل**: [08-checkpoints/](08-checkpoints/)

**چیست**: ذخیره وضعیت مکالمه و بازگشت به نقاط قبلی برای کاوش رویکردهای متفاوت

**مفاهیم کلیدی**:
- **چک‌پوینت**: اسنپ‌شات از وضعیت مکالمه
- **بازگشت**: بازگشت به چک‌پوینت قبلی
- **نقطه انشعاب**: کاوش چندین رویکرد از یک چک‌پوینت

**استفاده**:
```
# چک‌پوینت‌ها به‌طور خودکار با هر پرامپت کاربر ایجاد می‌شوند
# برای بازگشت، دو بار Esc را فشار دهید یا استفاده کنید:
/rewind

# سپس از شش گزینه انتخاب کنید:
# 1. بازگردانی کد و مکالمه
# 2. بازگردانی مکالمه
# 3. بازگردانی کد
# 4. خلاصه از اینجا
# 5. خلاصه تا اینجا
# 6. مهم نیست
```

**موارد استفاده**:
- امتحان رویکردهای متفاوت پیاده‌سازی
- بازیابی از اشتباهات
- آزمایش امن
- مقایسه راه‌حل‌های جایگزین
- آزمون A/B طراحی‌های متفاوت

</details>

<details>
<summary>۰۹. ویژگی‌های پیشرفته</summary>

**محل**: [09-advanced-features/](09-advanced-features/)

**چیست**: قابلیت‌های پیشرفته برای خط لوله‌های پیچیده و خودکارسازی

**شامل**:
- **حالت برنامه‌ریزی** — ایجاد برنامه‌های پیاده‌سازی دقیق قبل از کدنویسی
- **تفکر گسترش‌یافته** — استدلال عمیق برای مسائل پیچیده (تغییر با `Alt+T` / `Option+T`)
- **وظایف پس‌زمینه** — اجرای عملیات‌های طولانی بدون مسدودسازی
- **حالت‌های اجازه** — `manual` (مقدار کانفیگ `default`)، `acceptEdits`، `plan`، `auto`، `dontAsk`، `bypassPermissions`
- **حالت بدون سر** — اجرای Claude Code در CI/CD: `claude -p "Run tests and generate report" --permission-mode auto`
- **مدیریت جلسه** — `/resume`، `/rename`، `/fork`، `/branch`، `claude -c`، `claude -r`
- **کانفیگ** — سفارشی‌سازی رفتار در `~/.claude/settings.json`

به [config-examples.json](../09-advanced-features/config-examples.json) برای کانفیگ‌های کامل مراجعه کنید.

</details>

<details>
<summary>۱۰. مرجع CLI</summary>

**محل**: [10-cli/](10-cli/)

**چیست**: مرجع کامل رابط خط فرمان برای Claude Code

**نمونه‌های سریع**:
```bash
# حالت تعاملی
claude "explain this project"

# حالت چاپ (غیرتعاملی)
claude -p "review this code"

# پردازش محتوای فایل
cat error.log | claude -p "explain this error"

# خروجی JSON برای اسکریپت‌ها
claude -p --output-format json "list functions"

# از سرگیری جلسه
claude -r "feature-auth" "continue implementation"
```

**موارد استفاده**: یکپارچگی خط لوله CI/CD، خودکارسازی اسکریپت، پردازش دسته‌ای، خط لوله‌های چندجلسه‌ای، کانفیگ‌های ایجنت سفارشی

</details>

<details>
<summary>نمونه خط لوله‌های کاری</summary>

### خط لوله کامل بازبینی کد

```markdown
# استفاده از: دستورهای اسلش + زیرایجنت‌ها + حافظه + MCP

کاربر: /review-pr

Claude:
1. حافظه پروژه را بارگذاری می‌کند (استانداردهای کدنویسی)
2. PR را از طریق GitHub MCP دریافت می‌کند
3. به زیرایجنت code-reviewer سپرده می‌شود
4. به زیرایجنت test-engineer سپرده می‌شود
5. یافته‌ها را ترکیب می‌کند
6. بازبینی جامع ارائه می‌دهد
```

### مستندسازی خودکار

```markdown
# استفاده از: مهارت‌ها + زیرایجنت‌ها + حافظه

کاربر: "Generate API documentation for the auth module"

Claude:
1. حافظه پروژه را بارگذاری می‌کند (استانداردهای مستندسازی)
2. درخواست تولید مستندات را تشخیص می‌دهد
3. مهارت doc-generator را خودکار فراخوانی می‌کند
4. به زیرایجنت api-documenter سپرده می‌شود
5. مستندات جامع با مثال‌ها ایجاد می‌کند
```

### استقرار DevOps

```markdown
# استفاده از: پلاگین‌ها + MCP + هوک‌ها

کاربر: /deploy production

Claude:
1. هوک pre-deploy را اجرا می‌کند (محیط را اعتبارسنجی می‌کند)
2. به زیرایجنت deployment-specialist سپرده می‌شود
3. استقرار را از طریق Kubernetes MCP اجرا می‌کند
4. پیشرفت را پایش می‌کند
5. هوک post-deploy را اجرا می‌کند (بررسی‌های سلامت)
6. وضعیت را گزارش می‌دهد
```

</details>

<details>
<summary>ساختار دایرکتوری</summary>

```
├── 01-slash-commands/
│   ├── optimize.md
│   ├── pr.md
│   ├── generate-api-docs.md
│   └── README.md
├── 02-memory/
│   ├── project-CLAUDE.md
│   ├── directory-api-CLAUDE.md
│   ├── personal-CLAUDE.md
│   └── README.md
├── 03-skills/
│   ├── code-review-specialist/
│   │   ├── SKILL.md
│   │   ├── scripts/
│   │   └── templates/
│   ├── brand-voice/
│   │   ├── SKILL.md
│   │   └── templates/
│   ├── doc-generator/
│   │   ├── SKILL.md
│   │   └── generate-docs.py
│   └── README.md
├── 04-subagents/
│   ├── code-reviewer.md
│   ├── test-engineer.md
│   ├── documentation-writer.md
│   ├── secure-reviewer.md
│   ├── implementation-agent.md
│   └── README.md
├── 05-mcp/
│   ├── github-mcp.json
│   ├── database-mcp.json
│   ├── filesystem-mcp.json
│   ├── multi-mcp.json
│   └── README.md
├── 06-hooks/
│   ├── format-code.sh
│   ├── pre-commit.sh
│   ├── security-scan.sh
│   ├── log-bash.sh
│   ├── validate-prompt.sh
│   ├── notify-team.sh
│   └── README.md
├── 07-plugins/
│   ├── pr-review/
│   ├── devops-automation/
│   ├── documentation/
│   └── README.md
├── 08-checkpoints/
│   ├── checkpoint-examples.md
│   └── README.md
├── 09-advanced-features/
│   ├── config-examples.json
│   ├── planning-mode-examples.md
│   └── README.md
├── 10-cli/
│   └── README.md
└── README.md (this file)
```

</details>

<details>
<summary>بهترین شیوه‌ها</summary>

### بایدها
- با دستورهای اسلش ساده شروع کنید
- ویژگی‌ها را به‌تدریج اضافه کنید
- از حافظه برای استانداردهای تیم استفاده کنید
- کانفیگ‌ها را اول محلی تست کنید
- پیاده‌سازی‌های سفارشی را مستند کنید
- کانفیگ‌های پروژه را کنترل نسخه کنید
- پلاگین‌ها را با تیم به اشتراک بگذارید

### نایدها
- ویژگی‌های اضافی نسازید
- اعتبارنامه‌ها را هاردکد نکنید
- مستندسازی را نادیده نگیرید
- وظایف ساده را بیش‌ازحد پیچیده نکنید
- بهترین شیوه‌های امنیتی را نادیده نگیرید
- داده‌های حساس را کامیت نکنید

</details>

<details>
<summary>عیب‌یابی</summary>

### ویژگی بارگذاری نمی‌شود
1. محل فایل و نام‌گذاری را بررسی کنید
2. نحو YAML frontmatter را تأیید کنید
3. مجوزهای فایل را بررسی کنید
4. سازگاری نسخه Claude Code را مرور کنید

### اتصال MCP ناموفق بود
1. متغیرهای محیطی را تأیید کنید
2. نصب سرور MCP را بررسی کنید
3. اعتبارنامه‌ها را تست کنید
4. اتصال شبکه را مرور کنید

### زیرایجنت سپردن نمی‌کند
1. مجوزهای ابزار را بررسی کنید
2. وضوح توضیح ایجنت را تأیید کنید
3. پیچیدگی وظیفه را مرور کنید
4. ایجنت را مستقل تست کنید

</details>

<details>
<summary>تست</summary>

این پروژه شامل تست‌های خودکار جامع است:

- **تست‌های واحد**: تست‌های پایتون با pytest (Python 3.10, 3.11, 3.12)
- **کیفیت کد**: lint و قالب‌بندی با Ruff
- **امنیت**: اسکن آسیب‌پذیری با Bandit
- **بررسی نوع**: تحلیل نوع استاتیک با mypy
- **تأیید ساخت**: تست تولید EPUB
- **ردیابی پوشش**: یکپارچگی Codecov

```bash
# نصب وابستگی‌های توسعه
uv pip install -r scripts/requirements-dev.txt

# اجرای همه تست‌های واحد
pytest scripts/tests/ -v

# اجرای تست‌ها با گزارش پوشش
pytest scripts/tests/ -v --cov=scripts --cov-report=html

# اجرای بررسی‌های کیفیت کد
ruff check scripts/
ruff format --check scripts/

# اجرای اسکن امنیتی
bandit -c scripts/pyproject.toml -r scripts/ --exclude scripts/tests/

# اجرای بررسی نوع
mypy scripts/ --ignore-missing-imports
```

تست‌ها به‌طور خودکار با هر push به `main`/`develop` و هر PR به `main` اجرا می‌شوند. برای اطلاعات دقیق به [TESTING.md](../.github/TESTING.md) (انگلیسی) مراجعه کنید.

</details>

<details>
<summary>تولید EPUB</summary>

می‌خواهید این راهنما را آفلاین بخوانید؟ یک کتاب الکترونیکی EPUB تولید کنید:

```bash
uv run scripts/build_epub.py
```

این `claude-howto-guide.epub` را با همه محتوا، شامل نمودارهای Mermaid رندر‌شده ایجاد می‌کند.

به [scripts/README.md](scripts/README.md) برای گزینه‌های بیشتر مراجعه کنید.

</details>

<details>
<summary>مشارکت</summary>

یک اشکال پیدا کردید یا می‌خواهید مثالی مشارکت کنید؟ از کمک شما استقبال می‌کنیم!

**لطفاً [CONTRIBUTING.md](CONTRIBUTING.md) را برای راهنمایی‌های دقیق درباره:**
- انواع مشارکت‌ها (مثال‌ها، مستندات، ویژگی‌ها، اشکال‌ها، بازخورد)
- نحوه راه‌اندازی محیط توسعه
- ساختار دایرکتوری و نحوه اضافه کردن محتوا
- راهنمایی‌های نوشتن و بهترین شیوه‌ها
- فرآیند کامیت و PR

**استانداردهای جامعه ما:**
- [CODE_OF_CONDUCT.md](CODE_OF_CONDUCT.md) - چگونه با هم رفتار می‌کنیم
- [SECURITY.md](SECURITY.md) - سیاست امنیتی و گزارش آسیب‌پذیری

### گزارش مسائل امنیتی

اگر یک آسیب‌پذیری امنیتی کشف کردید، لطفاً مسئولانه گزارش دهید:

1. **استفاده از گزارش خصوصی آسیب‌پذیری GitHub**: https://github.com/luongnv89/claude-howto/security/advisories
2. **یا بخوانید** [.github/SECURITY_REPORTING.md](../.github/SECURITY_REPORTING.md) (انگلیسی) برای دستورالعمل‌های دقیق
3. **این کار را نکنید** برای آسیب‌پذیری‌های امنیتی یک issue عمومی باز نکنید

شروع سریع:
1. مخزن را فورک و کلون کنید
2. یک شاخه توصیفی ایجاد کنید (`add/feature-name`, `fix/bug`, `docs/improvement`)
3. تغییرات خود را مطابق راهنمایی‌ها اعمال کنید
4. یک pull request با توضیح واضح ثبت کنید

**نیاز به کمک دارید؟** یک issue یا discussion باز کنید و ما شما را در فرآیند راهنمایی می‌کنیم.

</details>

<details>
<summary>منابع اضافی</summary>

- [مستندات Claude Code](https://code.claude.com/docs/en/overview)
- [مشخصات پروتکل MCP](https://modelcontextprotocol.io)
- [مخزن مهارت‌ها](https://github.com/luongnv89/skills) - مجموعه‌ای از مهارت‌های آماده استفاده
- [کتاب آشپزی Anthropic](https://github.com/anthropics/anthropic-cookbook)
- [خط لوله کاری Claude Code بوریس چرنی](https://x.com/bcherny/status/2007179832300581177) - خالق Claude Code خط لوله کاری سیستماتیک‌شده خود را به اشتراک می‌گذارد: ایجنت‌های موازی، CLAUDE.md مشترک، حالت Plan، دستورهای اسلش، زیرایجنت‌ها و هوک‌های تأیید برای جلسات خودکار طولانی‌مدت.

</details>

---

## مشارکت

ما از مشارکت‌ها استقبال می‌کنیم! لطفاً به [راهنمای مشارکت](CONTRIBUTING.md) برای جزئیات نحوه شروع مراجعه کنید.

---

## لایسنس

لایسنس MIT — به [LICENSE](../LICENSE) مراجعه کنید. آزاد برای استفاده، تغییر و توزیع. تنها الزام گذاردن اعلان لایسنس است.

---

**آخرین به‌روزرسانی**: ۲۶ اکتبر ۲۰۲۶
**نسخه Claude Code**: 2.1.310
**منابع**:
- https://code.claude.com/docs/en/tools-reference#task-tool-availability
- https://code.claude.com/docs/en/hooks
- https://code.claude.com/docs/en/overview
- https://code.claude.com/docs/en/changelog
- https://code.claude.com/docs/en/permission-modes
- https://platform.claude.com/docs/en/about-claude/models/overview
- https://github.com/anthropics/claude-code/releases
- https://github.com/anthropics/claude-code/releases/tag/v2.1.154
- https://code.claude.com/docs/en/model-config
- https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
- https://github.com/anthropics/claude-code/releases/tag/v2.1.296
- https://code.claude.com/docs/en/setup
- https://code.claude.com/docs/en/mcp
- https://code.claude.com/docs/en/plugins/install
- https://code.claude.com/docs/en/checkpointing
- https://github.com/anthropics/claude-code
- https://code.claude.com/docs/en/changelog#2-1-302
- https://code.claude.com/docs/en/changelog#2-1-310
- https://code.claude.com/docs/en/headless#auto-approve-tools
- https://code.claude.com/docs/en/permission-modes#which-mode-a-non-interactive-run-starts-in
- https://code.claude.com/docs/en/mcp#example-query-your-postgresql-database
**مدل‌های سازگار**: Claude Fable 5.1, Claude Fable 5, Claude Opus 5, Claude Sonnet 5, Claude Sonnet 4.6, Claude Opus 4.8, Claude Haiku 4.5
