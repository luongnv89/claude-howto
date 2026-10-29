<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# مثال‌های Claude Code - کارت مرجع سریع

## 🚀 دستورات سریع نصب

### دستورات اسلش
```bash
# نصب همه
cp 01-slash-commands/*.md .claude/commands/

# نصب یک مورد مشخص
cp 01-slash-commands/optimize.md .claude/commands/
```

### حافظه
```bash
# حافظه پروژه
cp 02-memory/project-CLAUDE.md ./CLAUDE.md

# حافظه شخصی
cp 02-memory/personal-CLAUDE.md ~/.claude/CLAUDE.md
```

### مهارت‌ها
```bash
# مهارت‌های شخصی
cp -r 03-skills/code-review-specialist ~/.claude/skills/

# مهارت‌های پروژه
cp -r 03-skills/code-review-specialist .claude/skills/
```

### زیرایجنت‌ها
```bash
# نصب همه
cp 04-subagents/*.md .claude/agents/

# نصب یک مورد مشخص
cp 04-subagents/code-reviewer.md .claude/agents/
```

### MCP
```bash
# تنظیم اعتبارنامه‌ها
export GITHUB_PERSONAL_ACCESS_TOKEN="your_token"
export DATABASE_URL="postgresql://..."

# نصب پیکربندی (دامنه پروژه)
cp 05-mcp/github-mcp.json .mcp.json

# یا دامنه کاربر: به ~/.claude.json اضافه کنید
```

### هوک‌ها
```bash
# نصب هوک‌ها
mkdir -p ~/.claude/hooks
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh

# پیکربندی در تنظیمات (~/.claude/settings.json)
```

### پلاگین‌ها
```bash
# نصب از مثال‌ها (در صورت انتشار)
claude --plugin-dir ./07-plugins/pr-review
/plugin install devops-automation
/plugin install documentation
```

### چک‌پوینت‌ها
```bash
# چک‌پوینت‌ها با هر پرامپت کاربر به‌صورت خودکار ساخته می‌شوند
# برای بازگشت، دو بار Esc بزنید یا از دستور زیر استفاده کنید:
/rewind

# سپس انتخاب کنید: بازگردانی کد و گفت‌وگو، بازگردانی گفت‌وگو،
# بازگردانی کد، خلاصه کردن از اینجا، یا انصراف
```

### قابلیت‌های پیشرفته
```bash
# پیکربندی در تنظیمات (.claude/settings.json)
# 09-advanced-features/config-examples.json را ببینید

# حالت برنامه‌ریزی
/plan Task description

# حالت‌های مجوز (از پرچم --permission-mode استفاده کنید)
# manual         - درخواست تأیید برای هر اقدام (مقدار پیکربندی "default"؛ "manual" از v2.1.200 نام مستعار آن است)
# acceptEdits    - پذیرش خودکار ویرایش فایل‌ها، پرسش برای بقیه
# plan           - تحلیل فقط-خواندنی، بدون تغییر
# auto           - طبقه‌بند پس‌زمینه مجوزها را خودکار تعیین می‌کند
# dontAsk        - فقط ابزارهای از پیش تأییدشده اجرا می‌شوند؛ بقیه رد می‌شوند
# bypassPermissions - پذیرش همه اقدام‌ها (--permission-mode bypassPermissions؛ --dangerously-skip-permissions معادل آن است)

# مدیریت نشست
/resume                # از سرگیری گفت‌وگوی قبلی (بدون آرگومان = انتخابگر نشست‌های گذشته)
/rename "name"         # نام‌گذاری نشست فعلی
/fork [prompt]         # کپی گفت‌وگو به یک نشست پس‌زمینه جدید؛ کار در همین‌جا ادامه می‌یابد
/subtask <task>        # ایجاد یک زیرایجنت انشعابی که گفت‌وگو را به ارث می‌برد و نتیجه را گزارش می‌دهد
/branch [name]         # رفتن به یک کپی از گفت‌وگو، با حفظ نسخه اصلی
claude -c              # ادامه آخرین گفت‌وگو
claude -r "session"    # از سرگیری نشست با نام/شناسه
```

---

## 📋 برگه تقلب قابلیت‌ها

| قابلیت | مسیر نصب | استفاده |
|---------|-------------|-------|
| **دستورات اسلش (۶۰+)** | `.claude/commands/*.md` | `/command-name` |
| **حافظه** | `./CLAUDE.md` | بارگذاری خودکار |
| **مهارت‌ها** | `.claude/skills/*/SKILL.md` | فراخوانی خودکار |
| **زیرایجنت‌ها** | `.claude/agents/*.md` | واگذاری خودکار |
| **MCP** | `.mcp.json` (پروژه) یا `~/.claude.json` (کاربر) | `/mcp__server__action` |
| **هوک‌ها (۳۳ رویداد)** | `~/.claude/hooks/*.sh` | مبتنی بر رویداد (۵ نوع) |
| **پلاگین‌ها** | از طریق `/plugin install` | همه را بسته‌بندی می‌کند |
| **چک‌پوینت‌ها** | داخلی | `Esc+Esc` یا `/rewind` |
| **حالت برنامه‌ریزی** | داخلی | `/plan <task>` |
| **حالت‌های مجوز (۶)** | داخلی | `--allowedTools`، `--permission-mode` |
| **نشست‌ها** | داخلی | `/resume`، `/rename`، `/branch`، `/fork` |
| **کارهای پس‌زمینه** | داخلی | اجرا در پس‌زمینه |
| **کنترل از راه دور** | داخلی | `claude --remote-control` یا `/remote-control` |
| **نشست‌های وب** | داخلی | `claude --cloud "task"` |
| **worktreeهای گیت** | داخلی | `claude -w <name>` |
| **حافظه خودکار** | داخلی | ذخیره خودکار در `~/.claude/projects/<project>/memory/` |
| **فهرست وظایف** | داخلی | `Ctrl+T` (چک‌لیست)، `/tasks` (کار پس‌زمینه) |
| **مهارت‌های همراه** | داخلی | `/batch`، `/claude-api`، `/code-review [low\|medium\|high\|xhigh\|max\|ultra] [--fix] [--comment] [pr#\|branch\|path]` *(Claude می‌تواند خودش هم آن را شروع کند، از v2.1.246 در همه جا؛ اگر سطح داده نشود، آخرین سطحی را که تایپ کردید دوباره استفاده می‌کند، v2.1.223)*، `/simplify` *(بازبینی فقط-پاک‌سازی؛ از v2.1.154 دوباره از `/code-review` متمایز است)*، `/debug`، `/fewer-permission-prompts`، `/loop`، `/run` *(v2.1.145+)*، `/run-skill-generator` *(v2.1.145+)*، `/verify` *(v2.1.145+؛ از v2.1.215 فقط با فراخوانی صریح — Claude خودش آن را فعال نمی‌کند)* |

---

## 🎯 موارد استفاده رایج

### بازبینی کد
```bash
# روش ۱: دستور اسلش
cp 01-slash-commands/optimize.md .claude/commands/
# استفاده: /optimize

# روش ۲: زیرایجنت
cp 04-subagents/code-reviewer.md .claude/agents/
# استفاده: واگذاری خودکار

# روش ۳: مهارت
cp -r 03-skills/code-review-specialist ~/.claude/skills/
# استفاده: فراخوانی خودکار

# روش ۴: پلاگین (بهترین)
claude --plugin-dir ./07-plugins/pr-review
# استفاده: /review-pr
```

### مستندسازی
```bash
# دستور اسلش
cp 01-slash-commands/generate-api-docs.md .claude/commands/

# زیرایجنت
cp 04-subagents/documentation-writer.md .claude/agents/

# مهارت
cp -r 03-skills/doc-generator ~/.claude/skills/

# پلاگین (راه‌حل کامل)
/plugin install documentation
```

### DevOps
```bash
# پلاگین کامل
/plugin install devops-automation

# دستورات: /deploy، /rollback، /status، /incident
```

### استانداردهای تیم
```bash
# حافظه پروژه
cp 02-memory/project-CLAUDE.md ./CLAUDE.md

# برای تیم خود ویرایش کنید
vim CLAUDE.md
```

### اتوماسیون و هوک‌ها
```bash
# نصب هوک‌ها (۳۳ رویداد، ۵ نوع: command، http، mcp_tool، prompt، agent)
mkdir -p ~/.claude/hooks
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh

# مثال‌ها:
# - تست پیش از کامیت: pre-commit.sh
# - قالب‌بندی خودکار کد: format-code.sh
# - اسکن امنیتی: security-scan.sh

# حالت خودکار برای گردش کارهای کاملاً مستقل
claude --permission-mode auto -p "Refactor and test the auth module"
# یا چرخش تعاملی حالت‌ها با Shift+Tab
```

### ری‌فاکتور ایمن
```bash
# چک‌پوینت‌ها پیش از هر پرامپت به‌صورت خودکار ساخته می‌شوند
# ری‌فاکتور را امتحان کنید
# اگر کار کرد: ادامه دهید
# اگر شکست خورد: Esc+Esc بزنید یا از /rewind برای بازگشت استفاده کنید
```

### پیاده‌سازی پیچیده
```bash
# از حالت برنامه‌ریزی استفاده کنید
/plan Implement user authentication system

# Claude طرح تفصیلی می‌سازد
# بازبینی و تأیید کنید
# Claude به‌صورت سیستماتیک پیاده‌سازی می‌کند
```

### یکپارچه‌سازی CI/CD
```bash
# اجرا در حالت بدون رابط (غیرتعاملی). بدون حالت مجوز، ‏-p در Manual شروع می‌شود
# (مقدار تنظیمات "default"، نسخه 2.1.302+): فراخوانی‌هایی که به تأیید نیاز دارند رد می‌شوند،
# پس `--allowedTools "Bash(npm test *)"` یا `--permission-mode auto` را اضافه کنید
claude -p "Run all tests and generate report" --permission-mode auto

# با حالت مجوز برای CI
claude -p "Run tests" --permission-mode dontAsk

# با حالت خودکار برای کارهای کاملاً مستقل CI
claude --permission-mode auto -p "Run tests and fix failures"

# با هوک‌ها برای اتوماسیون
# 09-advanced-features/README.md را ببینید
```

### یادگیری و آزمایش
```bash
# از حالت برنامه‌ریزی برای تحلیل ایمن استفاده کنید
claude --permission-mode plan

# ایمن آزمایش کنید - چک‌پوینت‌ها به‌صورت خودکار ساخته می‌شوند
# اگر نیاز به بازگشت داشتید: Esc+Esc بزنید یا از /rewind استفاده کنید
```

### تیم‌های ایجنت
```bash
# فعال‌سازی تیم‌های ایجنت
export CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1

# یا در settings.json
{ "env": { "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1" } }

# شروع با: "Implement feature X using a team approach"
```

### وظایف زمان‌بندی‌شده
```bash
# اجرای یک دستور هر ۵ دقیقه
/loop 5m /check-status

# یادآور یک‌باره: با زبان طبیعی بپرسید (/loop تا لغو تکرار می‌شود)
remind me in 30 minutes to check the deploy
```

---

## 📁 مرجع مکان فایل‌ها

```text
Your Project/
├── .claude/
│   ├── commands/              # دستورات اسلش اینجا قرار می‌گیرند
│   ├── agents/                # زیرایجنت‌ها اینجا قرار می‌گیرند
│   ├── skills/                # مهارت‌های پروژه اینجا قرار می‌گیرند
│   └── settings.json          # تنظیمات پروژه (هوک‌ها و غیره)
├── .mcp.json                  # پیکربندی MCP (دامنه پروژه)
├── CLAUDE.md                  # حافظه پروژه
└── src/
    └── api/
        └── CLAUDE.md          # حافظه مخصوص دایرکتوری

User Home/
├── .claude/
│   ├── commands/              # دستورات شخصی
│   ├── agents/                # ایجنت‌های شخصی
│   ├── skills/                # مهارت‌های شخصی
│   ├── hooks/                 # اسکریپت‌های هوک
│   ├── settings.json          # تنظیمات کاربر
│   └── CLAUDE.md              # حافظه شخصی
└── .claude.json               # پیکربندی MCP شخصی (دامنه کاربر)

System directory/              # macOS /Library/Application Support/ClaudeCode/، Linux /etc/claude-code/، Windows C:\Program Files\ClaudeCode\
├── managed-settings.json      # تنظیمات مدیریت‌شده (سازمانی)
└── managed-settings.d/        # افزودنی‌های تنظیمات مدیریت‌شده
```

---

## 🔍 یافتن مثال‌ها

### بر اساس دسته
- **دستورات اسلش**: `01-slash-commands/`
- **حافظه**: `02-memory/`
- **مهارت‌ها**: `03-skills/`
- **زیرایجنت‌ها**: `04-subagents/`
- **MCP**: `05-mcp/`
- **هوک‌ها**: `06-hooks/`
- **پلاگین‌ها**: `07-plugins/`
- **چک‌پوینت‌ها**: `08-checkpoints/`
- **قابلیت‌های پیشرفته**: `09-advanced-features/`
- **CLI**: `10-cli/`

### بر اساس مورد استفاده
- **کارایی**: `01-slash-commands/optimize.md`
- **امنیت**: `04-subagents/secure-reviewer.md`
- **تست**: `04-subagents/test-engineer.md`
- **مستندات**: `03-skills/doc-generator/`
- **DevOps**: `07-plugins/devops-automation/`

### بر اساس پیچیدگی
- **ساده**: دستورات اسلش
- **متوسط**: زیرایجنت‌ها، حافظه
- **پیشرفته**: مهارت‌ها، هوک‌ها
- **کامل**: پلاگین‌ها

---

## 🎓 مسیر یادگیری

### روز ۱
```bash
# مرور کلی را بخوانید
cat README.md

# یک دستور نصب کنید
cp 01-slash-commands/optimize.md .claude/commands/

# امتحانش کنید
/optimize
```

### روز ۲ تا ۳
```bash
# راه‌اندازی حافظه
cp 02-memory/project-CLAUDE.md ./CLAUDE.md
vim CLAUDE.md

# نصب زیرایجنت
cp 04-subagents/code-reviewer.md .claude/agents/
```

### روز ۴ تا ۵
```bash
# راه‌اندازی MCP
export GITHUB_PERSONAL_ACCESS_TOKEN="your_token"
cp 05-mcp/github-mcp.json .mcp.json

# دستورات MCP را امتحان کنید
/mcp__github__list_prs
```

### هفته ۲
```bash
# نصب مهارت
cp -r 03-skills/code-review-specialist ~/.claude/skills/

# بگذارید خودکار فراخوانی شود
# فقط بگویید: "Review this code for issues"
```

### هفته ۳ به بعد
```bash
# نصب پلاگین کامل
claude --plugin-dir ./07-plugins/pr-review

# استفاده از قابلیت‌های بسته‌بندی‌شده
/review-pr
/check-security
/check-tests
```

---

## برجسته‌های قابلیت‌ها

| قابلیت | توضیح | استفاده |
|---------|-------------|-------|
| **حالت خودکار** | عملیات کاملاً مستقل با طبقه‌بند پس‌زمینه؛ از v2.1.207 به‌طور پیش‌فرض روی Bedrock/Vertex/Foundry در دسترس است | `Shift+Tab` برای چرخش حالت‌ها، یا `--permission-mode auto` |
| **کانال‌ها** | یکپارچه‌سازی Discord و Telegram | پرچم `--channels`، ربات‌های Discord/Telegram |
| **دیکته صوتی** | دستورات و زمینه را به Claude بگویید | دستور `/voice` |
| **سبک‌های خروجی** | نقش، لحن و قالب پاسخ پیش‌فرض Claude را تغییر دهید | `/config` → Output style، یا تنظیم `outputStyle`. داخلی: Default، Proactive، Explanatory، Learning، Concise |
| **خط وضعیت** | وضعیت سفارشی پایین نشست از یک دستور | `/statusline`، یا تنظیم `statusLine`؛ JSON نشست/مدل/هزینه/زمینه را روی stdin می‌گیرد |
| **هوک‌ها (۳۳ رویداد)** | سیستم هوک گسترده با ۵ نوع | انواع command، http، mcp_tool، prompt، agent |
| **استخراج MCP** | سرورهای MCP می‌توانند در زمان اجرا ورودی کاربر بخواهند | هنگام نیاز سرور به شفاف‌سازی، خودکار پرسیده می‌شود |
| **LSP پلاگین** | پشتیبانی Language Server Protocol برای پلاگین‌ها | `userConfig`، متغیر `${CLAUDE_PLUGIN_DATA}` |
| **کنترل از راه دور** | یک نشست محلی را از claude.ai یا اپ Claude هدایت کنید | `claude --remote-control` (یا `/remote-control` در نشست) |
| **نشست‌های وب** | نشست‌های ابری در claude.ai/code | `claude --cloud "task"` برای شروع از ترمینال |
| **اپ دسکتاپ** | اپلیکیشن دسکتاپ بومی | دانلود از claude.ai/download |
| **فهرست وظایف** | مدیریت کارهای پس‌زمینه | `/tasks` (نام مستعار `/bashes`) |
| **حافظه خودکار** | ذخیره خودکار حافظه از گفت‌وگوها | Claude یادداشت‌ها را در `~/.claude/projects/<project>/memory/MEMORY.md` ذخیره می‌کند؛ با `/memory` مدیریت کنید |
| **AGENTS.md** *(v2.1.277)* | فایل زمینه پروژه بین‌ابزاری، که وقتی `CLAUDE.md` در دایرکتوری کاری یا بالاتر از آن وجود ندارد به‌عنوان دستورالعمل پروژه خوانده می‌شود | تغییر حالت با **Project instructions** در `/config`. [AGENTS.md](02-memory/README.md#agentsmd) را ببینید |
| **worktreeهای گیت** | فضاهای کاری مجزا برای توسعه موازی | `claude --worktree <name>` (یا `-w`) |
| **انتخاب مدل** | جابه‌جایی بین Fable 5.1، Fable 5، Opus 5.5، Opus 5، Sonnet 5.5، Sonnet 5، Sonnet 4.6، Opus 4.8، Haiku 5.5 و Haiku 4.5 | `/model` (`sonnet` روی API آنتروپیک به Sonnet 5.5 تبدیل می‌شود، v2.1.284+) — از v2.1.153 انتخاب به‌عنوان پیش‌فرض نشست‌های جدید ذخیره می‌شود؛ برای فقط-این-نشست `s` را بزنید |
| **تیم‌های ایجنت** | هماهنگی چند ایجنت روی وظایف | فعال‌سازی با متغیر محیطی `CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1` (آزمایشی) |
| **گردش کارهای پویا** *(v2.1.154)* | هماهنگ‌سازی چندایجنت قطعی؛ از v2.1.219 راهنمای اندازه پیش‌فرض متوسط است (هدف: کمتر از ۱۰ ایجنت) | `/workflows` برای مشاهده اجراها؛ از Claude بخواهید یکی بسازد؛ اندازه را با **Dynamic workflow size** در `/config` تغییر دهید |
| **وظایف زمان‌بندی‌شده (محدود به نشست)** | وظایف تکرارشونده با `/loop` درون یک نشست | `/loop 5m /command` یا ابزار CronCreate |
| **یکپارچه‌سازی Chrome** | خودکارسازی مرورگر | پرچم `--chrome` یا دستور `/chrome` |
| **سفارشی‌سازی صفحه‌کلید** | کلیدهای میان‌بر سفارشی | دستور `/keybindings` |
| **/usage-credits** | پیکربندی محدودیت‌های مصرف اضافی (در v2.1.144 از `/extra-usage` تغییر نام یافت؛ نام قدیمی هنوز به‌عنوان مستعار کار می‌کند) | `/usage-credits` |
| **/run** *(v2.1.145+)* | اجرای اپ این پروژه برای دیدن تغییر در حال اجرا | `/run` |
| **/verify** *(v2.1.145+)* | ساخت، اجرا و مشاهده اپ برای تأیید کارکرد یک اصلاح (از v2.1.215 فقط با فراخوانی صریح — Claude خودش آن را فعال نمی‌کند) | `/verify` |
| **/run-skill-generator** *(v2.1.145+)* | آموزش `/run`/`/verify` برای رسیدگی به یک پروژه خاص | `/run-skill-generator` |
| **اسکن خروجی زیرایجنت** *(v2.1.210+)* | گزارش‌های زیرایجنت را برای الگوهای تزریق پرامپت اسکن و خنثی می‌کند | به‌طور پیش‌فرض روشن، بدون امکان غیرفعال‌سازی |
| **سقف WebSearch و محدودیت‌های انشعاب زیرایجنت** *(v2.1.212، تمدید در v2.1.219)* | ۲۰۰ فراخوانی WebSearch در هر نشست (در هر نوبت با `-p` و Agent SDK)، با شارژ مجدد ۱۰۰ فراخوانی در ساعت در نشست‌های تعاملی از v2.1.290؛ سقف زیرایجنت هم‌زمان (پیش‌فرض ۲۰) در v2.1.217 اضافه شد؛ از v2.1.219 زیرایجنت‌ها می‌توانند زیرایجنت تودرتو تا **عمق ۳ به‌طور پیش‌فرض** بسازند (v2.1.217 تودرتویی را غیرفعال کرده بود). سقف ۲۰۰ زیرایجنت در هر نشست **در v2.1.224 حذف شد** — دیگر هیچ محدودیتی برای مجموع زیرایجنت‌ها در هر نشست وجود ندارد | `CLAUDE_CODE_MAX_WEB_SEARCHES_PER_SESSION` (پیش‌فرض ۲۰۰؛ `/clear` بازنشانی می‌کند)، `CLAUDE_CODE_WEB_SEARCH_REFILLS_PER_HOUR` (پیش‌فرض ۱۰۰ تعاملی، ۰ با `-p`)، `CLAUDE_CODE_MAX_CONCURRENT_SUBAGENTS` (پیش‌فرض ۲۰)، `CLAUDE_CODE_MAX_SUBAGENT_SPAWN_DEPTH` (پیش‌فرض ۳؛ برای غیرفعال‌سازی ۱ بگذارید) |
| **حالت صفحه‌خوان** *(v2.1.208)* | حالت رندر متن ساده برای صفحه‌خوان‌ها | پرچم `--ax-screen-reader`، `CLAUDE_AX_SCREEN_READER=1` در شل شما، یا `"axScreenReader": true` در تنظیمات کاربر (`~/.claude/settings.json`)، تنظیمات مدیریت‌شده یا فایل `--settings` — از نسخه 2.1.305 در تنظیمات پروژه و محلی نادیده گرفته می‌شود |
| **حالت محدود** *(v2.1.248+)* | ابزارهای داخلی اجرای دستور یا کد (مانند Bash و PowerShell) و WebFetch را حذف می‌کند، مگر اینکه `--tools` آن‌ها را جداگانه نام ببرد (نه از طریق پیش‌تنظیم `default`)؛ تنظیمات کاربر، پروژه و محلی را نادیده می‌گیرد (تنظیمات مدیریت‌شده و `--settings` همچنان اعمال می‌شوند)؛ ابزارهای فایل را به دایرکتوری‌های کاری محدود می‌کند؛ `bypassPermissions` و نشست‌های ابری را رد می‌کند | `claude --restricted`، یا `CLAUDE_CODE_RESTRICTED=1` |
| **TTL کش زیرایجنت** *(v2.1.248+)* | فیلد frontmatter ایجنت `experimental.cacheTtl` تعیین می‌کند کش پرامپت زیرایجنت چقدر زنده بماند | `experimental:` با `cacheTtl: "5m"` (یا `"1h"`) را به frontmatter ایجنت اضافه کنید. [زیرایجنت‌ها](04-subagents/README.md) را ببینید |
| **مدل اجباری زیرایجنت** *(v2.1.257+)* | `CLAUDE_CODE_SUBAGENT_MODEL_FORCE=1` باعث می‌شود `CLAUDE_CODE_SUBAGENT_MODEL` بر frontmatter ایجنت اولویت یابد. از v2.1.251 متغیر محیطی به‌طور پیش‌فرض برنده نیست — frontmatter (شامل `model: inherit`) اولویت دارد مگر اینکه این تنظیم شود | `CLAUDE_CODE_SUBAGENT_MODEL=sonnet CLAUDE_CODE_SUBAGENT_MODEL_FORCE=1 claude` |

---

## نکات و ترفندها

### سفارشی‌سازی
- با مثال‌ها همان‌طور که هستند شروع کنید
- برای تناسب با نیاز خود تغییر دهید
- پیش از اشتراک با تیم تست کنید
- پیکربندی‌های خود را در کنترل نسخه نگه دارید

### بهترین شیوه‌ها
- برای استانداردهای تیم از حافظه استفاده کنید
- برای گردش کارهای کامل از پلاگین‌ها استفاده کنید
- برای کارهای پیچیده از زیرایجنت‌ها استفاده کنید
- برای کارهای سریع از دستورات اسلش استفاده کنید

### اشکال‌زدایی
```bash
# بررسی مکان فایل‌ها
ls -la .claude/commands/
ls -la .claude/agents/

# تأیید سینتکس YAML
head -20 .claude/agents/code-reviewer.md

# تست اتصال MCP
echo $GITHUB_PERSONAL_ACCESS_TOKEN
```

---

## 📊 ماتریس قابلیت‌ها

| نیاز | از این استفاده کنید | مثال |
|------|----------|---------|
| میان‌بر سریع | دستور اسلش (۶۰+) | `01-slash-commands/optimize.md` |
| استانداردهای تیم | حافظه | `02-memory/project-CLAUDE.md` |
| گردش کار خودکار | مهارت | `03-skills/code-review-specialist/` |
| وظیفه تخصصی | زیرایجنت | `04-subagents/code-reviewer.md` |
| داده خارجی | MCP (+ استخراج) | `05-mcp/github-mcp.json` |
| اتوماسیون رویداد | هوک (۳۳ رویداد، ۵ نوع) | `06-hooks/pre-commit.sh` |
| راه‌حل کامل | پلاگین (+ پشتیبانی LSP) | `07-plugins/pr-review/` |
| آزمایش ایمن | چک‌پوینت | `08-checkpoints/checkpoint-examples.md` |
| کاملاً مستقل | حالت خودکار | `--permission-mode auto` یا `Shift+Tab` |
| یکپارچه‌سازی چت | کانال‌ها | `--channels` (Discord، Telegram) |
| خط لوله CI/CD | CLI | `10-cli/README.md` |

---

## 🔗 پیوندهای سریع

- **راهنمای اصلی**: `README.md`
- **ایندکس کامل**: `INDEX.md`
- **راهنمای اصلی (مفاهیم)**: `claude_concepts_guide.md`

---

## 📞 پرسش‌های رایج

**پ: از کدام استفاده کنم؟**
ج: با دستورات اسلش شروع کنید و قابلیت‌ها را بر اساس نیاز اضافه کنید.

**پ: می‌توانم قابلیت‌ها را ترکیب کنم؟**
ج: بله! با هم کار می‌کنند. حافظه + دستورات + MCP = قدرتمند.

**پ: چگونه با تیم به اشتراک بگذارم؟**
ج: دایرکتوری `.claude/` را در git کامیت کنید.

**پ: درباره رمزها چه؟**
ج: از متغیرهای محیطی استفاده کنید، هرگز جاسازی نکنید.

**پ: می‌توانم مثال‌ها را تغییر دهم؟**
ج: قطعاً! آن‌ها قالب‌هایی برای سفارشی‌سازی هستند.

---

## ✅ چک‌لیست

چک‌لیست شروع کار:

- [ ] `README.md` را بخوانید
- [ ] ۱ دستور اسلش نصب کنید
- [ ] دستور را امتحان کنید
- [ ] `CLAUDE.md` پروژه را بسازید
- [ ] ۱ زیرایجنت نصب کنید
- [ ] ۱ یکپارچه‌سازی MCP راه‌اندازی کنید
- [ ] ۱ مهارت نصب کنید
- [ ] یک پلاگین کامل امتحان کنید
- [ ] برای نیازهای خود سفارشی کنید
- [ ] با تیم به اشتراک بگذارید

---

**شروع سریع**: `cat README.md`

**ایندکس کامل**: `cat INDEX.md`

**این کارت**: برای مرجع سریع آن را در دسترس نگه دارید!

---

**آخرین به‌روزرسانی**: ۲۶ اکتبر ۲۰۲۶
**نسخه Claude Code**: 2.1.310
**منابع**:
- https://code.claude.com/docs/en/workflows#set-a-size-guideline
- https://code.claude.com/docs/en/memory#agents-md
- https://code.claude.com/docs/en/changelog
- https://code.claude.com/docs/en/cli-reference
- https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
- https://code.claude.com/docs/en/sub-agents
- https://code.claude.com/docs/en/model-config
- https://code.claude.com/docs/en/settings
- https://code.claude.com/docs/en/hooks
- https://code.claude.com/docs/en/env-vars
- https://code.claude.com/docs/en/commands
- https://code.claude.com/docs/en/remote-control
- https://code.claude.com/docs/en/agent-teams
- https://code.claude.com/docs/en/memory#storage-location
- https://code.claude.com/docs/en/permission-modes
- https://code.claude.com/docs/en/managed-settings
- https://code.claude.com/docs/en/scheduled-tasks
- https://code.claude.com/docs/en/code-review-local
- https://code.claude.com/docs/en/changelog#2-1-307
- https://code.claude.com/docs/en/settings-reference#axscreenreader
- https://code.claude.com/docs/en/headless
- https://code.claude.com/docs/en/permission-modes#tool-calls-denied-in-claude-p-and-agent-sdk-runs
- https://code.claude.com/docs/en/tools-reference#session-search-limit
- https://code.claude.com/docs/en/routines
**مدل‌های سازگار**: Claude Fable 5.1, Claude Fable 5, Claude Opus 5, Claude Sonnet 5, Claude Sonnet 4.6, Claude Opus 4.8, Claude Haiku 4.5
