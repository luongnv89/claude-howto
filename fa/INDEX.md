<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# ایندکس کامل مثال‌های Claude Code

این سند ایندکس کامل همه فایل‌های مثال را ارائه می‌دهد که بر اساس نوع ویژگی سازمان‌دهی شده‌اند.

## آمار کلی

- **تعداد کل فایل‌ها**: بیش از ۱۰۰ فایل
- **دسته‌بندی‌ها**: ۱۰ دسته ویژگی
- **پلاگین‌ها**: ۳ پلاگین کامل
- **مهارت‌ها**: ۶ مهارت کامل
- **هوک‌ها**: ۱۱ هوک نمونه
- **آماده استفاده**: همه مثال‌ها

---

## ۰۱. دستورات اسلش (۱۰ فایل)

میان‌برهایی که کاربر فراخوانی می‌کند، برای جریان‌های کاری رایج.

| فایل | توضیح | مورد استفاده |
|------|-------------|----------|
| `optimize.md` | تحلیل‌گر بهینه‌سازی کد | یافتن مشکلات کارایی |
| `pr.md` | آماده‌سازی pull request | خودکارسازی جریان کاری PR |
| `generate-api-docs.md` | تولیدکننده مستندات API | تولید مستندات API |
| `commit.md` | کمک‌کننده پیام کامیت | کامیت‌های استاندارد |
| `setup-ci-cd.md` | راه‌اندازی خط لوله CI/CD | خودکارسازی DevOps |
| `push-all.md` | پوش کردن همه تغییرات | جریان کاری پوش سریع |
| `unit-test-expand.md` | گسترش پوشش تست واحد | خودکارسازی تست |
| `doc-refactor.md` | ری‌فاکتور مستندات | بهبود مستندات |
| `pr-slash-command.png` | نمونه تصویر | مرجع بصری |
| `README.md` | مستندات | راهنمای نصب و استفاده |

**مسیر نصب**: `.claude/commands/`

**نحوه استفاده**: `/optimize`، `/pr`، `/generate-api-docs`، `/commit`، `/setup-ci-cd`، `/push-all`، `/unit-test-expand`، `/doc-refactor`

---

## ۰۲. حافظه (۶ فایل)

زمینه پایدار و استانداردهای پروژه.

| فایل | توضیح | دامنه | مکان |
|------|-------------|-------|----------|
| `project-CLAUDE.md` | استانداردهای پروژه تیمی | کل پروژه | `./CLAUDE.md` |
| `directory-api-CLAUDE.md` | قواعد مخصوص API | دایرکتوری | `./src/api/CLAUDE.md` |
| `personal-CLAUDE.md` | ترجیحات شخصی | کاربر | `~/.claude/CLAUDE.md` |
| `memory-saved.png` | تصویر: حافظه ذخیره شد | - | مرجع بصری |
| `memory-ask-claude.png` | تصویر: پرسش از Claude | - | مرجع بصری |
| `README.md` | مستندات | - | مرجع |

**نصب**: در مکان مناسب کپی کنید

**نحوه استفاده**: به‌طور خودکار توسط Claude بارگذاری می‌شود

**AGENTS.md** (نسخه 2.1.277): وقتی هیچ‌کدام از `CLAUDE.md`، `.claude/CLAUDE.md` یا `CLAUDE.local.md` در دایرکتوری کاری یا بالاتر از آن وجود نداشته باشد، به‌عنوان دستورالعمل‌های پروژه خوانده می‌شود — به `02-memory/README.md#agentsmd` مراجعه کنید

---

## ۰۳. مهارت‌ها (۲۳ فایل)

قابلیت‌هایی که به‌طور خودکار فراخوانی می‌شوند، همراه با اسکریپت‌ها و قالب‌ها.

### مهارت بازبینی کد (۵ فایل)
```
code-review-specialist/
├── SKILL.md                          # تعریف مهارت
├── scripts/
│   ├── analyze-metrics.py            # تحلیل‌گر معیارهای کد
│   └── compare-complexity.py         # مقایسه پیچیدگی
└── templates/
    ├── review-checklist.md           # چک‌لیست بازبینی
    └── finding-template.md           # مستندسازی یافته‌ها
```

**هدف**: بازبینی جامع کد با تحلیل امنیت، کارایی و کیفیت

**فراخوانی خودکار**: هنگام بازبینی کد

---

### مهارت لحن برند (۴ فایل)
```
brand-voice/
├── SKILL.md                          # تعریف مهارت
├── templates/
│   ├── email-template.txt            # قالب ایمیل
│   └── social-post-template.txt      # قالب شبکه‌های اجتماعی
└── tone-examples.md                  # نمونه پیام‌ها
```

**هدف**: تضمین لحن یکسان برند در ارتباطات

**فراخوانی خودکار**: هنگام نوشتن متن تبلیغاتی

---

### مهارت تولیدکننده مستندات (۲ فایل)
```
doc-generator/
├── SKILL.md                          # تعریف مهارت
└── generate-docs.py                  # استخراج‌کننده مستندات پایتون
```

**هدف**: تولید مستندات جامع API از کد منبع

**فراخوانی خودکار**: هنگام ایجاد یا به‌روزرسانی مستندات API

---

### مهارت ری‌فاکتور (۵ فایل)
```
refactor/
├── SKILL.md                          # تعریف مهارت
├── scripts/
│   ├── analyze-complexity.py         # تحلیل‌گر پیچیدگی
│   └── detect-smells.py              # آشکارساز بوی کد
├── references/
│   ├── code-smells.md                # فهرست بوی کد
│   └── refactoring-catalog.md        # الگوهای ری‌فاکتور
└── templates/
    └── refactoring-plan.md           # قالب طرح ری‌فاکتور
```

**هدف**: ری‌فاکتور سیستماتیک کد همراه با تحلیل پیچیدگی

**فراخوانی خودکار**: هنگام ری‌فاکتور کد

---

### مهارت Claude MD (۱ فایل)
```
claude-md/
└── SKILL.md                          # تعریف مهارت
```

**هدف**: مدیریت و بهینه‌سازی فایل‌های CLAUDE.md

---

### مهارت پیش‌نویس وبلاگ (۳ فایل)
```
blog-draft/
├── SKILL.md                          # تعریف مهارت
└── templates/
    ├── draft-template.md             # قالب پیش‌نویس وبلاگ
    └── outline-template.md           # قالب طرح کلی وبلاگ
```

**هدف**: نوشتن پیش‌نویس پست وبلاگ با ساختار یکسان

**به‌علاوه**: `README.md` - مرور کلی مهارت‌ها و راهنمای استفاده

**مسیر نصب**: `~/.claude/skills/` یا `.claude/skills/`

---

## ۰۴. زیرایجنت‌ها (۱۰ فایل)

دستیارهای هوش مصنوعی تخصصی با قابلیت‌های سفارشی.

| فایل | توضیح | ابزارها | مورد استفاده |
|------|-------------|-------|----------|
| `code-reviewer.md` | تحلیل کیفیت کد | Read، Grep، Glob، Bash | بازبینی‌های جامع |
| `test-engineer.md` | تحلیل پوشش تست | Read، Write، Bash، Grep | خودکارسازی تست |
| `documentation-writer.md` | ایجاد مستندات | Read، Write، Grep | تولید مستندات |
| `secure-reviewer.md` | بازبینی امنیتی (فقط خواندن) | Read، Grep | ممیزی امنیتی |
| `implementation-agent.md` | پیاده‌سازی کامل | Read، Write، Edit، Bash، Grep، Glob | توسعه ویژگی |
| `debugger.md` | متخصص اشکال‌زدایی | Read، Edit، Bash، Grep، Glob | بررسی باگ |
| `data-scientist.md` | متخصص تحلیل داده | Bash، Read، Write | جریان‌های کاری داده |
| `clean-code-reviewer.md` | استانداردهای کد تمیز | Read، Grep، Glob، Bash | کیفیت کد |
| `performance-optimizer.md` | تحلیل گلوگاه‌های کارایی | Read، Edit، Bash، Grep، Glob | کار بهینه‌سازی |
| `README.md` | مستندات | - | راهنمای نصب و استفاده |

**مسیر نصب**: `.claude/agents/`

**نحوه استفاده**: به‌طور خودکار توسط ایجنت اصلی واگذار می‌شود

---

## ۰۵. پروتکل MCP (۵ فایل)

یکپارچه‌سازی با ابزارها و APIهای خارجی.

| فایل | توضیح | یکپارچه با | مورد استفاده |
|------|-------------|-----------------|----------|
| `github-mcp.json` | یکپارچه‌سازی GitHub | GitHub API | مدیریت PR و issue |
| `database-mcp.json` | پرس‌وجوی پایگاه داده | PostgreSQL/MySQL | پرس‌وجوی داده زنده |
| `filesystem-mcp.json` | عملیات فایل | فایل‌سیستم محلی | مدیریت فایل |
| `multi-mcp.json` | چندین سرور | GitHub + DB + Slack | یکپارچه‌سازی کامل |
| `README.md` | مستندات | - | راهنمای نصب و استفاده |

**مسیر نصب**: `.mcp.json` (دامنه پروژه) یا `~/.claude.json` (دامنه کاربر)

**نحوه استفاده**: `/mcp__github__list_prs` و غیره

---

## ۰۶. هوک‌ها (۱۲ فایل)

اسکریپت‌های خودکارسازی رویدادمحور که به‌طور خودکار اجرا می‌شوند.

| فایل | توضیح | رویداد | مورد استفاده |
|------|-------------|-------|----------|
| `format-code.sh` | قالب‌بندی خودکار کد | PostToolUse (matcher: Write) | قالب‌بندی کد |
| `pre-commit.sh` | اجرای تست‌ها پیش از کامیت | PreToolUse (matcher: Bash) | خودکارسازی تست |
| `pre-tool-check.sh` | اعتبارسنجی و ممیزی دستورات پیش از اجرا | PreToolUse (matcher: Bash) | حفاظ‌ها، گزارش ممیزی |
| `security-scan.sh` | اسکن امنیتی | PostToolUse (matcher: Write) | بررسی‌های امنیتی |
| `dependency-check.sh` | اسکن مانیفست‌های وابستگی برای آسیب‌پذیری | PostToolUse (matcher: Write) | بررسی‌های زنجیره تأمین |
| `log-bash.sh` | ثبت دستورات bash | PostToolUse (matcher: Bash) | گزارش‌گیری دستورات |
| `notify-team.sh` | ارسال اعلان | PostToolUse (matcher: Bash) | اعلان‌های تیمی |
| `validate-prompt.sh` | اعتبارسنجی پرامپت‌ها | UserPromptSubmit | اعتبارسنجی ورودی |
| `session-end.sh` | ثبت پیشرفت هنگام پایان نشست | SessionEnd | پیگیری پیشرفت |
| `context-tracker.py` | پیگیری مصرف پنجره زمینه | UserPromptSubmit, Stop | پایش زمینه |
| `context-tracker-tiktoken.py` | پیگیری زمینه بر پایه توکن | UserPromptSubmit, Stop | شمارش دقیق توکن |
| `README.md` | مستندات | - | راهنمای نصب و استفاده |

**مسیر نصب**: پیکربندی در `~/.claude/settings.json`

**نحوه استفاده**: در تنظیمات پیکربندی می‌شود، به‌طور خودکار اجرا می‌شود

**انواع هوک** (۵ مورد): `command`، `http`، `prompt`، `mcp_tool`، `agent` — شیوه اجرای هوک.

**رویدادهای هوک** (۳۳ مورد، در ۴ دسته) — زمان اجرا:
- هوک‌های ابزار: PreToolUse، PostToolUse، PostToolUseFailure، PostToolBatch، PermissionRequest، PermissionDenied
- هوک‌های نشست: SessionStart، Setup، SessionEnd، Stop، StopFailure، SubagentStart، SubagentStop
- هوک‌های وظیفه: UserPromptSubmit، UserPromptExpansion، MessageDisplay، TaskCompleted، TaskCreated، TeammateIdle (رویدادهای TaskCompleted و TaskCreated فقط وقتی فعال می‌شوند که ابزارهای todo فعال باشند — به‌طور پیش‌فرض فقط در مدل‌های Claude 3.x، Opus 4 تا 4.7، Sonnet 4 تا 4.6 و Haiku 4.5 در دسترس است)
- هوک‌های چرخه حیات: ConfigChange، CwdChanged، DirectoryAdded، FileChanged، PreCompact، PostCompact، PreModelSwitch، PostModelSwitch، WorktreeCreate، WorktreeRemove، Notification، InstructionsLoaded، Elicitation، ElicitationResult

---

## ۰۷. پلاگین‌ها (۳ پلاگین کامل، ۳۹ فایل)

مجموعه‌های بسته‌بندی‌شده از ویژگی‌ها.

### پلاگین بازبینی PR (۱۰ فایل)
```
pr-review/
├── .claude-plugin/
│   └── plugin.json                   # مانیفست پلاگین
├── commands/
│   ├── review-pr.md                  # بازبینی جامع
│   ├── check-security.md             # بررسی امنیتی
│   └── check-tests.md                # بررسی پوشش تست
├── agents/
│   ├── security-reviewer.md          # متخصص امنیت
│   ├── test-checker.md               # متخصص تست
│   └── performance-analyzer.md       # متخصص کارایی
├── mcp/
│   └── github-config.json            # یکپارچه‌سازی GitHub
├── hooks/
│   └── pre-review.js                 # اعتبارسنجی پیش از بازبینی
└── README.md                         # مستندات پلاگین
```

**ویژگی‌ها**: تحلیل امنیتی، پوشش تست، تأثیر بر کارایی

**دستورات**: `/review-pr`، `/check-security`، `/check-tests`

**نصب**: `claude --plugin-dir ./07-plugins/pr-review` (از ریشه مخزن)

---

### پلاگین خودکارسازی DevOps (۱۵ فایل)
```
devops-automation/
├── .claude-plugin/
│   └── plugin.json                   # مانیفست پلاگین
├── commands/
│   ├── deploy.md                     # استقرار
│   ├── rollback.md                   # بازگردانی
│   ├── status.md                     # وضعیت سیستم
│   └── incident.md                   # پاسخ به رخداد
├── agents/
│   ├── deployment-specialist.md      # متخصص استقرار
│   ├── incident-commander.md         # هماهنگ‌کننده رخداد
│   └── alert-analyzer.md             # تحلیل‌گر هشدار
├── mcp/
│   └── kubernetes-config.json        # یکپارچه‌سازی Kubernetes
├── hooks/
│   ├── pre-deploy.js                 # بررسی‌های پیش از استقرار
│   └── post-deploy.js                # وظایف پس از استقرار
├── scripts/
│   ├── deploy.sh                     # خودکارسازی استقرار
│   ├── rollback.sh                   # خودکارسازی بازگردانی
│   └── health-check.sh               # بررسی‌های سلامت
└── README.md                         # مستندات پلاگین
```

**ویژگی‌ها**: استقرار Kubernetes، بازگردانی، پایش، پاسخ به رخداد

**دستورات**: `/deploy`، `/rollback`، `/status`، `/incident`

**نصب**: `claude --plugin-dir ./07-plugins/devops-automation` (از ریشه مخزن)

---

### پلاگین مستندات (۱۴ فایل)
```
documentation/
├── .claude-plugin/
│   └── plugin.json                   # مانیفست پلاگین
├── commands/
│   ├── generate-api-docs.md          # تولید مستندات API
│   ├── generate-readme.md            # ایجاد README
│   ├── sync-docs.md                  # همگام‌سازی مستندات
│   └── validate-docs.md              # اعتبارسنجی مستندات
├── agents/
│   ├── api-documenter.md             # متخصص مستندات API
│   ├── code-commentator.md           # متخصص توضیحات کد
│   └── example-generator.md          # سازنده مثال
├── mcp/
│   └── github-docs-config.json       # یکپارچه‌سازی GitHub
├── templates/
│   ├── api-endpoint.md               # قالب نقطه پایانی API
│   ├── function-docs.md              # قالب مستندات تابع
│   └── adr-template.md               # قالب ADR
└── README.md                         # مستندات پلاگین
```

**ویژگی‌ها**: مستندات API، تولید README، همگام‌سازی مستندات، اعتبارسنجی

**دستورات**: `/generate-api-docs`، `/generate-readme`، `/sync-docs`، `/validate-docs`

**نصب**: `claude --plugin-dir ./07-plugins/documentation` (از ریشه مخزن)

**به‌علاوه**: `README.md` - مرور کلی پلاگین‌ها و راهنمای استفاده

---

## ۰۸. چک‌پوینت‌ها و بازگردانی (۲ فایل)

ذخیره وضعیت گفتگو و بررسی رویکردهای جایگزین.

| فایل | توضیح | محتوا |
|------|-------------|---------|
| `README.md` | مستندات | راهنمای جامع چک‌پوینت |
| `checkpoint-examples.md` | مثال‌های دنیای واقعی | مهاجرت پایگاه داده، بهینه‌سازی کارایی، تکرار رابط کاربری، اشکال‌زدایی |
| | | |

**مفاهیم کلیدی**:
- **چک‌پوینت**: تصویری از وضعیت گفتگو
- **بازگردانی (Rewind)**: بازگشت به چک‌پوینت قبلی
- **نقطه انشعاب**: بررسی چند رویکرد

**نحوه استفاده**:
```
# چک‌پوینت‌ها با هر پرامپت کاربر به‌طور خودکار ایجاد می‌شوند
# برای بازگردانی، دو بار Esc بزنید یا از این دستور استفاده کنید:
/rewind
# سپس انتخاب کنید: Restore code and conversation، Restore conversation،
# Restore code، Summarize from here، Summarize up to here، یا Never mind
```

**موارد استفاده**:
- امتحان پیاده‌سازی‌های مختلف
- بازیابی از اشتباهات
- آزمایش ایمن
- مقایسه راه‌حل‌ها
- تست A/B

---

## ۰۹. ویژگی‌های پیشرفته (۴ فایل)

قابلیت‌های پیشرفته برای جریان‌های کاری پیچیده.

| فایل | توضیح | ویژگی‌ها |
|------|-------------|----------|
| `README.md` | راهنمای کامل | مستندات همه ویژگی‌های پیشرفته |
| `config-examples.json` | نمونه‌های پیکربندی | بیش از ۱۰ پیکربندی مخصوص موارد استفاده |
| `planning-mode-examples.md` | نمونه‌های برنامه‌ریزی | REST API، مهاجرت پایگاه داده، ری‌فاکتور |
| `setup-auto-mode-permissions.py` | مقدارگذاری اولیه `permissions.allow` برای حالت auto | خودتوان (idempotent)، `--dry-run` و پرچم‌های اختیاری |
| جریان‌های کاری پویا | هماهنگ‌سازی قطعی چند‌ایجنتها از طریق `/workflows` (نسخه 2.1.154) | ممیزی جامع، مهاجرت، مقیاس‌پذیری |
| وظایف زمان‌بندی‌شده | وظایف تکرارشوندهٔ محدود به نشست با `/loop` و ابزارهای cron | جریان‌های کاری تکرارشونده خودکار |
| یکپارچه‌سازی Chrome | خودکارسازی مرورگر در Chrome خودتان از طریق افزونه Claude in Chrome | تست و استخراج داده وب |
| کنترل از راه دور (گسترش‌یافته) | روش‌های اتصال، امنیت، جدول مقایسه، کارت‌های دستگاه | مدیریت نشست از راه دور (دیگر پیش‌نمایش پژوهشی نیست) |
| پیام‌رسانی بین‌نشستی | `SendMessage` / `ListAgents`، شامل `notify_when_idle` (نسخه 2.1.236) | هماهنگ‌سازی نشست‌ها روی یک ماشین |
| سفارشی‌سازی صفحه‌کلید | کلیدهای میان‌بر سفارشی، پشتیبانی از chord، زمینه‌ها | میان‌برهای شخصی‌سازی‌شده |
| اپلیکیشن دسکتاپ (گسترش‌یافته) | کانکتورها، launch.json، ویژگی‌های سازمانی | یکپارچه‌سازی دسکتاپ |
| | | |

**ویژگی‌های پیشرفته پوشش‌داده‌شده**:

### حالت برنامه‌ریزی
- ایجاد طرح‌های پیاده‌سازی دقیق
- برآورد زمان و ارزیابی ریسک
- شکست سیستماتیک وظایف

### تفکر گسترده
- استدلال عمیق برای مسائل پیچیده
- تحلیل تصمیم‌های معماری
- ارزیابی بده‌بستان‌ها

### وظایف پس‌زمینه
- عملیات طولانی‌مدت بدون بلوکه کردن
- جریان‌های کاری توسعه موازی
- مدیریت و پایش وظایف

### جریان‌های کاری پویا (نسخه 2.1.154)
- هماهنگ‌سازی قطعی ده‌ها تا صدها زیرایجنت پس‌زمینه
- مراحل fan-out / pipeline / موازی برای پوشش جامع
- مشاهده اجراها با `/workflows`؛ کلید Ultracode در `/effort` (`/effort ultracode [on|off]`) آن را برای یک نشست فعال می‌کند بدون تغییر سطح effort (نسخه 2.1.284)؛ تنظیم `ultracode` آن را پایدار می‌کند
- از نسخه 2.1.219 دستورالعمل پیش‌فرض اندازه «متوسط» است (هدف: کمتر از ۱۰ ایجنت) — آن را با **Dynamic workflow size** در `/config` تغییر دهید

### حالت‌های مجوز
- **manual**: پیش از هر چیزی فراتر از خواندن، پرسش می‌شود (از نسخه 2.1.200 به‌صورت Manual نمایش داده می‌شود؛ مقدار پیکربندی هنوز `default` است)
- **acceptEdits**: پذیرش خودکار ویرایش فایل‌ها، پرسش برای بقیه
- **plan**: تحلیل فقط-خواندنی، بدون تغییر
- **auto**: همه چیز، با بررسی‌های ایمنی پس‌زمینه — یک طبقه‌بند دستورات و نوشتن‌ها در دایرکتوری‌های محافظت‌شده را بررسی می‌کند (از طریق شیء تنظیمات `autoMode` پیکربندی می‌شود)
- **dontAsk**: فقط ابزارهای از پیش تأییدشده — هر فراخوانی که در غیر این صورت پرسش می‌کرد را به‌طور خودکار رد می‌کند. Claude فقط تطابق‌های `permissions.allow`، دستورات Bash فقط-خواندنی، و فراخوانی‌های تأییدشده توسط هوک `PreToolUse` را اجرا می‌کند
- **bypassPermissions**: پذیرش همه (با `--permission-mode bypassPermissions` یا معادل آن `--dangerously-skip-permissions` فعال کنید)

### حالت بدون رابط (`claude -p`)
- یکپارچه‌سازی CI/CD
- اجرای خودکار وظایف
- پردازش دسته‌ای

### مدیریت نشست
- چندین نشست کاری
- جابه‌جایی و ذخیره نشست
- پایداری نشست

### ویژگی‌های تعاملی
- کلیدهای میان‌بر صفحه‌کلید
- تاریخچه دستورات
- تکمیل خودکار با Tab
- ورودی چندخطی

### پیکربندی
- مدیریت جامع تنظیمات
- پیکربندی‌های مخصوص محیط
- سفارشی‌سازی برای هر پروژه

### وظایف زمان‌بندی‌شده
- وظایف تکرارشونده با دستور `/loop`
- ابزارهای cron: CronCreate، CronList، CronDelete
- جریان‌های کاری تکرارشونده خودکار

### یکپارچه‌سازی Chrome
- خودکارسازی مرورگر در Chrome خودتان از طریق افزونه Claude in Chrome
- قابلیت‌های تست و استخراج داده وب
- تعامل با صفحه و استخراج داده

### کنترل از راه دور (گسترش‌یافته)
- روش‌ها و پروتکل‌های اتصال
- ملاحظات امنیتی و بهترین شیوه‌ها
- جدول مقایسه گزینه‌های دسترسی از راه دور
- خارج از پیش‌نمایش پژوهشی — ماشینی که `claude remote-control` را اجرا می‌کند، در تب Code اپلیکیشن Claude به‌عنوان کارت دستگاه نمایش داده می‌شود

### پیام‌رسانی بین‌نشستی
- `SendMessage` بین نشست‌های روی یک ماشین
- `notify_when_idle` — یک اعلان اختیاری وقتی نشست دیگر در آینده بی‌کار شود (نسخه 2.1.236)
- `ListAgents` نام خود نشست را گزارش می‌دهد و هم‌تیمی‌های فعال را فهرست می‌کند (نسخه 2.1.239)

### سفارشی‌سازی صفحه‌کلید
- پیکربندی کلیدهای میان‌بر سفارشی
- پشتیبانی از chord برای میان‌برهای چندکلیدی
- فعال‌سازی میان‌بر وابسته به زمینه

### اپلیکیشن دسکتاپ (گسترش‌یافته)
- کانکتورها برای یکپارچه‌سازی با IDE
- پیکربندی launch.json
- ویژگی‌ها و استقرار سازمانی

---

## ۱۰. استفاده از CLI (۱ فایل)

الگوهای استفاده از رابط خط فرمان و مرجع آن.

| فایل | توضیح | محتوا |
|------|-------------|---------|
| `README.md` | مستندات CLI | پرچم‌ها، گزینه‌ها و الگوهای استفاده |

**ویژگی‌های کلیدی CLI**:
- `claude` - شروع نشست تعاملی
- `claude -p "prompt"` - حالت بدون رابط / غیرتعاملی
- `claude --cloud "task"` - شروع نشست ابری (وب)
- `claude --model` - انتخاب مدل (Opus 5.5، Sonnet 5.5، Opus 5، Sonnet 5، Sonnet 4.6، Opus 4.8، Haiku 5.5، Haiku 4.5)
- `claude --permission-mode` - تعیین حالت مجوز
- `claude --remote-control` - شروع نشستی که می‌توانید از claude.ai یا اپلیکیشن Claude هم کنترلش کنید

---

## فایل‌های مستندات (۱۳ فایل)

| فایل | مکان | توضیح |
|------|----------|-------------|
| `README.md` | `/` | مرور کلی مثال‌ها |
| `INDEX.md` | `/` | همین ایندکس کامل |
| `QUICK_REFERENCE.md` | `/` | کارت مرجع سریع |
| `README.md` | `/01-slash-commands/` | راهنمای دستورات اسلش |
| `README.md` | `/02-memory/` | راهنمای حافظه |
| `README.md` | `/03-skills/` | راهنمای مهارت‌ها |
| `README.md` | `/04-subagents/` | راهنمای زیرایجنت‌ها |
| `README.md` | `/05-mcp/` | راهنمای MCP |
| `README.md` | `/06-hooks/` | راهنمای هوک‌ها |
| `README.md` | `/07-plugins/` | راهنمای پلاگین‌ها |
| `README.md` | `/08-checkpoints/` | راهنمای چک‌پوینت‌ها |
| `README.md` | `/09-advanced-features/` | راهنمای ویژگی‌های پیشرفته |
| `README.md` | `/10-cli/` | راهنمای CLI |

---

## درخت کامل فایل‌ها

```
claude-howto/
├── README.md                                    # مرور کلی
├── INDEX.md                                     # همین فایل
├── QUICK_REFERENCE.md                           # کارت مرجع سریع
├── claude_concepts_guide.md                     # راهنمای اصلی
│
├── 01-slash-commands/                           # دستورات اسلش
│   ├── optimize.md
│   ├── pr.md
│   ├── generate-api-docs.md
│   ├── commit.md
│   ├── setup-ci-cd.md
│   ├── push-all.md
│   ├── unit-test-expand.md
│   ├── doc-refactor.md
│   ├── pr-slash-command.png
│   └── README.md
│
├── 02-memory/                                   # حافظه
│   ├── project-CLAUDE.md
│   ├── directory-api-CLAUDE.md
│   ├── personal-CLAUDE.md
│   ├── memory-saved.png
│   ├── memory-ask-claude.png
│   └── README.md
│
├── 03-skills/                                   # مهارت‌ها
│   ├── code-review-specialist/
│   │   ├── SKILL.md
│   │   ├── scripts/
│   │   │   ├── analyze-metrics.py
│   │   │   └── compare-complexity.py
│   │   └── templates/
│   │       ├── review-checklist.md
│   │       └── finding-template.md
│   ├── brand-voice/
│   │   ├── SKILL.md
│   │   ├── templates/
│   │   │   ├── email-template.txt
│   │   │   └── social-post-template.txt
│   │   └── tone-examples.md
│   ├── doc-generator/
│   │   ├── SKILL.md
│   │   └── generate-docs.py
│   ├── refactor/
│   │   ├── SKILL.md
│   │   ├── scripts/
│   │   │   ├── analyze-complexity.py
│   │   │   └── detect-smells.py
│   │   ├── references/
│   │   │   ├── code-smells.md
│   │   │   └── refactoring-catalog.md
│   │   └── templates/
│   │       └── refactoring-plan.md
│   ├── claude-md/
│   │   └── SKILL.md
│   ├── blog-draft/
│   │   ├── SKILL.md
│   │   └── templates/
│   │       ├── draft-template.md
│   │       └── outline-template.md
│   └── README.md
│
├── 04-subagents/                                # زیرایجنت‌ها
│   ├── code-reviewer.md
│   ├── test-engineer.md
│   ├── documentation-writer.md
│   ├── secure-reviewer.md
│   ├── implementation-agent.md
│   ├── debugger.md
│   ├── data-scientist.md
│   ├── clean-code-reviewer.md
│   └── README.md
│
├── 05-mcp/                                      # پروتکل MCP
│   ├── github-mcp.json
│   ├── database-mcp.json
│   ├── filesystem-mcp.json
│   ├── multi-mcp.json
│   └── README.md
│
├── 06-hooks/                                    # هوک‌ها
│   ├── format-code.sh
│   ├── pre-commit.sh
│   ├── security-scan.sh
│   ├── log-bash.sh
│   ├── validate-prompt.sh
│   ├── notify-team.sh
│   ├── context-tracker.py
│   ├── context-tracker-tiktoken.py
│   └── README.md
│
├── 07-plugins/                                  # پلاگین‌ها
│   ├── pr-review/
│   │   ├── .claude-plugin/
│   │   │   └── plugin.json
│   │   ├── commands/
│   │   │   ├── review-pr.md
│   │   │   ├── check-security.md
│   │   │   └── check-tests.md
│   │   ├── agents/
│   │   │   ├── security-reviewer.md
│   │   │   ├── test-checker.md
│   │   │   └── performance-analyzer.md
│   │   ├── mcp/
│   │   │   └── github-config.json
│   │   ├── hooks/
│   │   │   └── pre-review.js
│   │   └── README.md
│   ├── devops-automation/
│   │   ├── .claude-plugin/
│   │   │   └── plugin.json
│   │   ├── commands/
│   │   │   ├── deploy.md
│   │   │   ├── rollback.md
│   │   │   ├── status.md
│   │   │   └── incident.md
│   │   ├── agents/
│   │   │   ├── deployment-specialist.md
│   │   │   ├── incident-commander.md
│   │   │   └── alert-analyzer.md
│   │   ├── mcp/
│   │   │   └── kubernetes-config.json
│   │   ├── hooks/
│   │   │   ├── pre-deploy.js
│   │   │   └── post-deploy.js
│   │   ├── scripts/
│   │   │   ├── deploy.sh
│   │   │   ├── rollback.sh
│   │   │   └── health-check.sh
│   │   └── README.md
│   ├── documentation/
│   │   ├── .claude-plugin/
│   │   │   └── plugin.json
│   │   ├── commands/
│   │   │   ├── generate-api-docs.md
│   │   │   ├── generate-readme.md
│   │   │   ├── sync-docs.md
│   │   │   └── validate-docs.md
│   │   ├── agents/
│   │   │   ├── api-documenter.md
│   │   │   ├── code-commentator.md
│   │   │   └── example-generator.md
│   │   ├── mcp/
│   │   │   └── github-docs-config.json
│   │   ├── templates/
│   │   │   ├── api-endpoint.md
│   │   │   ├── function-docs.md
│   │   │   └── adr-template.md
│   │   └── README.md
│   └── README.md
│
├── 08-checkpoints/                              # چک‌پوینت‌ها
│   ├── checkpoint-examples.md
│   └── README.md
│
├── 09-advanced-features/                        # ویژگی‌های پیشرفته
│   ├── config-examples.json
│   ├── planning-mode-examples.md
│   └── README.md
│
└── 10-cli/                                      # استفاده از CLI
    └── README.md
```

---

## شروع سریع بر اساس مورد استفاده

### کیفیت کد و بازبینی‌ها
```bash
# نصب دستور اسلش
cp 01-slash-commands/optimize.md .claude/commands/

# نصب زیرایجنت
cp 04-subagents/code-reviewer.md .claude/agents/

# نصب مهارت
cp -r 03-skills/code-review-specialist ~/.claude/skills/

# یا نصب پلاگین کامل
claude --plugin-dir ./07-plugins/pr-review
```

### DevOps و استقرار
```bash
# نصب پلاگین (همه چیز را شامل می‌شود)
claude --plugin-dir ./07-plugins/devops-automation
```

### مستندات
```bash
# نصب دستور اسلش
cp 01-slash-commands/generate-api-docs.md .claude/commands/

# نصب زیرایجنت
cp 04-subagents/documentation-writer.md .claude/agents/

# نصب مهارت
cp -r 03-skills/doc-generator ~/.claude/skills/

# یا نصب پلاگین کامل
claude --plugin-dir ./07-plugins/documentation
```

### استانداردهای تیمی
```bash
# راه‌اندازی حافظه پروژه
cp 02-memory/project-CLAUDE.md ./CLAUDE.md

# آن را مطابق استانداردهای تیم خود ویرایش کنید
```

### یکپارچه‌سازی‌های خارجی
```bash
# تعیین متغیرهای محیطی
export GITHUB_PERSONAL_ACCESS_TOKEN="your_token"
export DATABASE_URL="postgresql://..."
export SLACK_BOT_TOKEN="your-slack-bot-token"
export SLACK_TEAM_ID="T0000000000"

# نصب پیکربندی MCP (دامنه پروژه)
cp 05-mcp/multi-mcp.json .mcp.json
```

### خودکارسازی و اعتبارسنجی
```bash
# نصب هوک‌ها
mkdir -p ~/.claude/hooks
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh

# پیکربندی هوک‌ها در تنظیمات (~/.claude/settings.json)
# به 06-hooks/README.md مراجعه کنید
```

### آزمایش ایمن
```bash
# چک‌پوینت‌ها با هر پرامپت کاربر به‌طور خودکار ایجاد می‌شوند
# برای بازگردانی: Esc+Esc بزنید یا از /rewind استفاده کنید
# سپس از منوی بازگردانی انتخاب کنید چه چیزی بازیابی شود

# برای مثال‌ها به 08-checkpoints/README.md مراجعه کنید
```

### جریان‌های کاری پیشرفته
```bash
# پیکربندی ویژگی‌های پیشرفته
# به 09-advanced-features/config-examples.json مراجعه کنید

# استفاده از حالت برنامه‌ریزی
/plan Implement feature X

# استفاده از حالت‌های مجوز
claude --permission-mode plan          # برای بازبینی کد (فقط خواندن)
claude --permission-mode acceptEdits   # پذیرش خودکار ویرایش‌ها
claude --permission-mode auto          # تأیید خودکار اقدامات ایمن

# اجرا در حالت بدون رابط برای CI/CD
claude -p "Run tests and report results"

# اجرای وظایف پس‌زمینه
Run tests in background

# برای راهنمای کامل به 09-advanced-features/README.md مراجعه کنید
```

---

## ماتریس پوشش ویژگی‌ها

| دسته | دستورات | ایجنت‌ها | MCP | هوک‌ها | اسکریپت‌ها | قالب‌ها | مستندات | تصاویر | کل |
|----------|----------|--------|-----|-------|---------|-----------|------|--------|-------|
| **۰۱ دستورات اسلش** | 8 | - | - | - | - | - | 1 | 1 | **10** |
| **۰۲ حافظه** | - | - | - | - | - | 3 | 1 | 2 | **6** |
| **۰۳ مهارت‌ها** | - | - | - | - | 5 | 7 | 11 | - | **23** |
| **۰۴ زیرایجنت‌ها** | - | 9 | - | - | - | - | 1 | - | **10** |
| **۰۵ MCP** | - | - | 4 | - | - | - | 1 | - | **5** |
| **۰۶ هوک‌ها** | - | - | - | 11 | - | - | 1 | - | **12** |
| **۰۷ پلاگین‌ها** | 11 | 9 | 3 | 3 | 3 | 3 | 7 | - | **39** |
| **۰۸ چک‌پوینت‌ها** | - | - | - | - | - | - | 1 | 1 | **2** |
| **۰۹ پیشرفته** | - | - | - | - | 1 | 1 | 2 | - | **4** |
| **۱۰ CLI** | - | - | - | - | - | - | 1 | - | **1** |

---

## مسیر یادگیری

### مبتدی (هفته ۱)
1. ✅ `README.md` را بخوانید
2. ✅ ۱ تا ۲ دستور اسلش نصب کنید
3. ✅ فایل حافظه پروژه بسازید
4. ✅ دستورات پایه را امتحان کنید

### متوسط (هفته ۲ تا ۳)
1. ✅ GitHub MCP را راه‌اندازی کنید
2. ✅ یک زیرایجنت نصب کنید
3. ✅ واگذاری وظایف را امتحان کنید
4. ✅ یک مهارت نصب کنید

### پیشرفته (هفته ۴ به بعد)
1. ✅ پلاگین کامل نصب کنید
2. ✅ دستورات اسلش سفارشی بسازید
3. ✅ زیرایجنت سفارشی بسازید
4. ✅ مهارت سفارشی بسازید
5. ✅ پلاگین خودتان را بسازید

### متخصص (هفته ۵ به بعد)
1. ✅ هوک‌ها را برای خودکارسازی راه‌اندازی کنید
2. ✅ از چک‌پوینت‌ها برای آزمایش استفاده کنید
3. ✅ حالت برنامه‌ریزی را پیکربندی کنید
4. ✅ از حالت‌های مجوز به‌طور مؤثر استفاده کنید
5. ✅ حالت بدون رابط را برای CI/CD راه‌اندازی کنید
6. ✅ به مدیریت نشست مسلط شوید

---

## جستجو بر اساس کلیدواژه

### کارایی
- `01-slash-commands/optimize.md` - تحلیل کارایی
- `04-subagents/code-reviewer.md` - بازبینی کارایی
- `03-skills/code-review-specialist/` - معیارهای کارایی
- `07-plugins/pr-review/agents/performance-analyzer.md` - متخصص کارایی

### امنیت
- `04-subagents/secure-reviewer.md` - بازبینی امنیتی
- `03-skills/code-review-specialist/` - تحلیل امنیتی
- `07-plugins/pr-review/` - بررسی‌های امنیتی

### تست
- `04-subagents/test-engineer.md` - مهندس تست
- `07-plugins/pr-review/commands/check-tests.md` - پوشش تست

### مستندات
- `01-slash-commands/generate-api-docs.md` - دستور مستندات API
- `04-subagents/documentation-writer.md` - ایجنت نویسنده مستندات
- `03-skills/doc-generator/` - مهارت تولیدکننده مستندات
- `07-plugins/documentation/` - پلاگین کامل مستندات

### استقرار
- `07-plugins/devops-automation/` - راه‌حل کامل DevOps

### خودکارسازی
- `06-hooks/` - خودکارسازی رویدادمحور
- `06-hooks/pre-commit.sh` - خودکارسازی پیش از کامیت
- `06-hooks/format-code.sh` - قالب‌بندی خودکار
- `09-advanced-features/` - حالت بدون رابط برای CI/CD

### اعتبارسنجی
- `06-hooks/security-scan.sh` - اعتبارسنجی امنیتی
- `06-hooks/validate-prompt.sh` - اعتبارسنجی پرامپت

### آزمایش
- `08-checkpoints/` - آزمایش ایمن با بازگردانی
- `08-checkpoints/checkpoint-examples.md` - مثال‌های دنیای واقعی

### برنامه‌ریزی
- `09-advanced-features/planning-mode-examples.md` - نمونه‌های حالت برنامه‌ریزی
- `09-advanced-features/README.md` - تفکر گسترده

### پیکربندی
- `09-advanced-features/config-examples.json` - نمونه‌های پیکربندی

---

## یادداشت‌ها

- همه مثال‌ها آماده استفاده هستند
- آن‌ها را مطابق نیازهای خاص خود تغییر دهید
- مثال‌ها از بهترین شیوه‌های Claude Code پیروی می‌کنند
- هر دسته README مخصوص خود را با دستورالعمل‌های دقیق دارد
- اسکریپت‌ها مدیریت خطای مناسب دارند
- قالب‌ها قابل سفارشی‌سازی هستند

---

## مشارکت

می‌خواهید مثال‌های بیشتری اضافه کنید؟ این ساختار را دنبال کنید:
1. زیردایرکتوری مناسب ایجاد کنید
2. README.md را همراه با نحوه استفاده اضافه کنید
3. قراردادهای نام‌گذاری را رعایت کنید
4. به‌طور کامل تست کنید
5. این ایندکس را به‌روزرسانی کنید

---

**آخرین به‌روزرسانی**: ۲۶ اکتبر ۲۰۲۶
**نسخه Claude Code**: 2.1.310
**منابع**:
- https://code.claude.com/docs/en/tools-reference#task-tool-availability
- https://code.claude.com/docs/en/workflows#set-a-size-guideline
- https://code.claude.com/docs/en/memory#agents-md
- https://code.claude.com/docs/en/overview
- https://code.claude.com/docs/en/hooks
- https://code.claude.com/docs/en/commands
- https://code.claude.com/docs/en/permission-modes
- https://github.com/anthropics/claude-code/releases/tag/v2.1.153
- https://github.com/anthropics/claude-code/releases/tag/v2.1.154
- https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
- https://code.claude.com/docs/en/model-config
- https://code.claude.com/docs/en/workflows#let-claude-decide-with-ultracode
- https://code.claude.com/docs/en/cli-reference
- https://code.claude.com/docs/en/plugins/install
- https://code.claude.com/docs/en/checkpointing
- https://code.claude.com/docs/en/remote-control
- https://code.claude.com/docs/en/chrome
- https://code.claude.com/docs/en/headless#auto-approve-tools
- https://code.claude.com/docs/en/permission-modes#which-mode-a-non-interactive-run-starts-in
- https://code.claude.com/docs/en/scheduled-tasks
**مدل‌های سازگار**: Claude Fable 5، Claude Opus 5، Claude Sonnet 5، Claude Sonnet 4.6، Claude Opus 4.8، Claude Haiku 4.5
**تعداد کل مثال‌ها**: بیش از ۱۰۰ فایل
**دسته‌بندی‌ها**: ۱۰ ویژگی
**هوک‌ها**: ۱۱ اسکریپت خودکارسازی
**نمونه‌های پیکربندی**: بیش از ۱۰ سناریو
**آماده استفاده**: همه مثال‌ها
