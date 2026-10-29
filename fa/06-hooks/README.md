<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../../resources/logos/claude-howto-logo.svg">
</picture>

# هوک‌ها

هوک‌ها اسکریپت‌های خودکاری هستند که در پاسخ به رویدادهای مشخص در طول نشست‌های Claude Code اجرا می‌شوند. آن‌ها خودکارسازی، اعتبارسنجی، مدیریت مجوز و جریان‌های کاری سفارشی را ممکن می‌کنند.

## مرور کلی

هوک‌ها اقدامات خودکار (دستورات شل، webhookهای HTTP، پرامپت‌های LLM، فراخوانی ابزارهای MCP یا ارزیابی‌های زیرایجنت) هستند که وقتی رویدادهای مشخصی در Claude Code رخ می‌دهند به‌طور خودکار اجرا می‌شوند. آن‌ها ورودی JSON دریافت می‌کنند و نتایج را از طریق کدهای خروج و خروجی JSON اعلام می‌کنند.

**ویژگی‌های کلیدی:**
- خودکارسازی رویدادمحور
- ورودی/خروجی مبتنی بر JSON
- پشتیبانی از انواع هوک `command`، `http`، `mcp_tool`، `prompt` و `agent`
- تطبیق الگو برای هوک‌های مخصوص ابزار

## پیکربندی

هوک‌ها در فایل‌های تنظیمات با ساختاری مشخص پیکربندی می‌شوند:

- `~/.claude/settings.json` - تنظیمات کاربر (همه پروژه‌ها)
- `.claude/settings.json` - تنظیمات پروژه (قابل اشتراک، کامیت‌شده)
- `.claude/settings.local.json` - تنظیمات محلی پروژه (کامیت نمی‌شود)
- خط‌مشی مدیریت‌شده - تنظیمات سراسر سازمان
- `hooks/hooks.json` در پلاگین - هوک‌های محدود به پلاگین
- frontmatter مهارت/ایجنت - هوک‌های چرخه عمر کامپوننت

### ساختار پایه پیکربندی

```json
{
  "hooks": {
    "EventName": [
      {
        "matcher": "ToolPattern",
        "hooks": [
          {
            "type": "command",
            "command": "your-command-here",
            "timeout": 60
          }
        ]
      }
    ]
  }
}
```

**فیلدهای کلیدی:**

| فیلد | توضیح | مثال |
|-------|-------------|---------|
| `matcher` | الگو برای تطبیق نام ابزارها (حساس به حروف) | `"Write"`، `"Edit\|Write"`، `"*"` |
| `hooks` | آرایه‌ای از تعاریف هوک | `[{ "type": "command", ... }]` |
| `type` | نوع هوک: `"command"` (bash)، `"prompt"` (LLM)، `"http"` (webhook)، `"mcp_tool"` (فراخوانی ابزار MCP، نسخه 2.1.118 به بعد)، یا `"agent"` (زیرایجنت) | `"command"` |
| `command` | دستور شلی که اجرا می‌شود | `"$CLAUDE_PROJECT_DIR/.claude/hooks/format.sh"` |
| `timeout` | مهلت زمانی اختیاری به ثانیه. پیش‌فرض‌ها: ۶۰۰ برای command/http/mcp_tool، ۳۰ برای prompt، ۶۰ برای agent. | `30` |
| `once` | اگر `true` باشد، هوک پس از نخستین اجرای موفق حذف می‌شود (اجراهای شکست‌خورده، مسدود یا مهلت‌گذشته آن را نگه می‌دارند). فقط در frontmatter مهارت؛ در تنظیمات و frontmatter ایجنت نادیده گرفته می‌شود | `true` |
| `async` | اگر `true` باشد، در پس‌زمینه و بدون بلوکه کردن اجرا می‌شود | `true` |
| `asyncRewake` | اگر `true` باشد، در پس‌زمینه اجرا می‌شود و در صورت کد خروج ۲، Claude را بیدار می‌کند. مستلزم `async` است. | `true` |
| `shell` | `"bash"` یا `"powershell"` را می‌پذیرد. پیش‌فرض `"bash"` است، یا در Windows وقتی Git Bash نصب نباشد `"powershell"`. کد خروج 2 یک هوک PowerShell فقط از v2.1.309 به بعد جلوی کار را می‌گیرد؛ پیش از تکیه بر یک هوک نگهبان PowerShell ارتقا دهید. | `"bash"` |
| `statusMessage` | پیام چرخان سفارشی که هنگام اجرای هوک نمایش داده می‌شود | `"Formatting…"` |
| `onFailure` | آنچه هنگام شکست یک هوک command یا HTTP با اقدام رخ می‌دهد (شروع نشدن، پایان مهلت، خروج با کد غیرمنتظره): `"continue"` (پیش‌فرض) یا `"block"` (نسخه 2.1.295 به بعد) | `"block"` |

> **توجه**: برخی رویدادها مهلت پیش‌فرض را کاهش می‌دهند. `UserPromptSubmit` پیش‌فرض `command`، `http` و `mcp_tool` را به ۳۰ ثانیه کاهش می‌دهد، و `MessageDisplay` آن را به ۱۰ ثانیه کاهش می‌دهد. هوک‌های `SessionEnd` سهمیه ۱.۵ ثانیه‌ای مشترک دارند؛ اگر تنظیمات شما `timeout` بزرگ‌تری برای هر هوک تعیین کند، Claude Code آن سهمیه را تا حداکثر ۶۰ ثانیه بالا می‌برد.

### الگوهای matcher

| الگو | توضیح | مثال |
|---------|-------------|---------|
| رشته دقیق | ابزار مشخصی را تطبیق می‌دهد | `"Write"` |
| الگوی regex | چند ابزار را تطبیق می‌دهد | `"Edit\|Write"` |
| جداشده با ویرگول | هر ابزاری در فهرست را تطبیق می‌دهد (نسخه 2.1.191 به بعد) | `"Write,Edit"` |
| نویسه عام | همه ابزارها را تطبیق می‌دهد | `"*"` یا `""` |
| ابزارهای MCP | الگوی سرور و ابزار | `"mcp__memory__.*"` |

> **matcherها دقیقاً تطبیق داده می‌شوند (نسخه 2.1.195 به بعد).** یک شناسه خط‌تیره‌دار (مثلاً نام ابزار MCP حاوی خط تیره) دیگر به‌طور تصادفی با ابزار دیگری به‌صورت زیررشته تطبیق داده نمی‌شود. matcherهای جداشده با ویرگول مانند `"Write,Edit"` روی هر ابزاری در فهرست فعال می‌شوند — نسخه‌های قبلی آن‌ها را بی‌صدا هرگز فعال نمی‌کردند.

**مقادیر matcher برای InstructionsLoaded:**

| مقدار matcher | توضیح |
|---------------|-------------|
| `session_start` | دستورالعمل‌های بارگذاری‌شده هنگام شروع نشست |
| `nested_traversal` | دستورالعمل‌های بارگذاری‌شده در پیمایش تودرتوی دایرکتوری |
| `path_glob_match` | دستورالعمل‌های بارگذاری‌شده از طریق تطبیق الگوی glob مسیر |

### محدودسازی با شرط‌های `if` (مسیرهای آرگومان ابزار)

فیلد `matcher` یک هوک را بر اساس **نام ابزار** انتخاب می‌کند (`"Write"`، `"Edit|Write"`، `"*"`). برای فیلترکردن دقیق‌تر بر اساس **آرگومان‌های** ابزار — مثلاً اجرای هوک فقط وقتی یک ویرایش به `src/` دست می‌زند، یا محافظت از خواندن فایل‌های محرمانه — یک شرط `if` به هندلر هوک اضافه کنید. این با matcher نام ابزار متفاوت است: `matcher` تعیین می‌کند *کدام ابزار*، و `if` تعیین می‌کند *کدام فراخوانی*.

`if` از [نحو قواعد مجوز](https://code.claude.com/docs/en/permissions) استفاده می‌کند (`ToolName(pattern)`) و در برابر نام ابزار **و** آرگومان‌هایش با هم ارزیابی می‌شود. برای `Read`/`Edit`/`Write`، الگوی مسیر از معناشناسی gitignore پیروی می‌کند، با همان لنگرهای قواعد مجوز: نام بدون مسیر مانند `.env` در هر عمقی تطبیق می‌شود، `src/**` نسبت به دایرکتوری جاری است، `/src/**` نسبت به ریشه پروژه، `~/...` نسبت به دایرکتوری خانگی شما، و `//...` یک مسیر مطلق فایل‌سیستم است.

فیلد `if` در **سطح هندلر هوک** قرار دارد — هم‌رده `type` و `command`، درون آرایه `hooks` — نه روی `matcher`:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Edit|Write",
        "hooks": [
          {
            "type": "command",
            "if": "Edit(src/**)",
            "command": "./hooks/lint-src.sh"
          }
        ]
      },
      {
        "matcher": "Read",
        "hooks": [
          {
            "type": "command",
            "if": "Read(.env)",
            "command": "./hooks/block-secret-read.sh"
          }
        ]
      }
    ]
  }
}
```

نمونه‌هایی از الگوهای معتبر `if`: `Edit(src/**)` (ویرایش‌های زیر `src/`)، `Read(~/.ssh/**)` (خواندن هر کلید SSH)، `Read(.env)` (هر `.env` در دایرکتوری جاری یا پایین‌تر)، `Bash(git push *)` (فقط زیردستورهای `git push`).

> **به‌روزرسانی نسخه 2.1.214**: الگوی تک‌بخشی `dir/**` در شرط `if` یک هوک (مانند `Edit(src/**)`) اکنون فقط `<cwd>/dir` را تطبیق می‌دهد — نه آن دایرکتوری را در هر عمقی از درخت. پیش‌تر `src/**` هم `foo/src/**` را تطبیق می‌داد. اگر تطبیق در هر عمقی می‌خواهید از `**/dir/**` استفاده کنید. **مهم**: این محدودسازی فقط برای شرط‌های `if:` هوک و تأیید خودکار قواعد allow اعمال می‌شود — قواعد مجوز deny/ask هنوز `dir/**` را در هر عمقی تطبیق می‌دهند.

## انواع هوک

Claude Code از پنج نوع هوک پشتیبانی می‌کند:

### هوک‌های Command

نوع پیش‌فرض هوک. یک دستور شل اجرا می‌کند و از طریق stdin/stdout JSON و کدهای خروج ارتباط برقرار می‌کند.

```json
{
  "type": "command",
  "command": "python3 \"$CLAUDE_PROJECT_DIR/.claude/hooks/validate.py\"",
  "timeout": 60
}
```

#### شکل exec (`args`)

> در نسخه 2.1.139 اضافه شد.

به‌جای شکل شلی `"command": "..."`، یک هوک command می‌تواند یک باینری را مستقیماً از طریق `execve()` با یک آرایه `args` اجرا کند. هیچ تجزیه شلی وجود ندارد، بنابراین جای‌نگهدارهای مسیر هرگز نیاز به نقل‌قول ندارند و پیکربندی از باگ‌های تزریق شل در امان است.

```json
{
  "type": "command",
  "command": "python3",
  "args": ["${CLAUDE_PROJECT_DIR}/.claude/hooks/validate.py", "--strict"],
  "timeout": 60
}
```

`command` همیشه الزامی است: وقتی `args` تعیین شده باشد، `command` فایل اجرایی برای اجراست (که در `PATH` جستجو می‌شود) و `args` بردار آرگومان‌های آن است. وقتی به pipe، تغییر مسیر، زنجیره `&&` یا بسط‌های شل نیاز دارید `args` را حذف کنید (شکل شلی)؛ وقتی یک باینری را با آرگومان‌ها فراخوانی می‌کنید از `args` استفاده کنید.

### هوک‌های HTTP

> در نسخه 2.1.63 اضافه شد.

نقاط پایانی webhook از راه دور که همان ورودی JSON هوک‌های command را دریافت می‌کنند. هوک‌های HTTP یک JSON را با POST به URL می‌فرستند و پاسخ JSON دریافت می‌کنند. هوک‌های HTTP وقتی سندباکس فعال باشد از طریق سندباکس مسیریابی می‌شوند. جایگذاری متغیر محیطی در مقادیر هدر برای امنیت نیازمند فهرست صریح `allowedEnvVars` است.

```json
{
  "hooks": {
    "PostToolUse": [{
      "matcher": "Write",
      "hooks": [{
        "type": "http",
        "url": "https://my-webhook.example.com/hook"
      }]
    }]
  }
}
```

**ویژگی‌های کلیدی:**
- `"type": "http"` -- این را به‌عنوان هوک HTTP مشخص می‌کند
- `"url"` -- نشانی نقطه پایانی webhook
- وقتی سندباکس فعال باشد از طریق سندباکس مسیریابی می‌شود
- برای هر جایگذاری متغیر محیطی در مقادیر `headers` نیازمند فهرست صریح `allowedEnvVars` است

### هوک‌های Prompt

پرامپت‌های ارزیابی‌شده با LLM که محتوای هوک یک پرامپت است و Claude آن را ارزیابی می‌کند. عمدتاً با رویدادهای `Stop` و `SubagentStop` برای بررسی هوشمند تکمیل وظیفه استفاده می‌شود.

```json
{
  "type": "prompt",
  "prompt": "Evaluate if Claude completed all requested tasks.",
  "timeout": 30
}
```

LLM پرامپت را ارزیابی می‌کند و یک تصمیم ساختاریافته برمی‌گرداند (برای جزئیات به [هوک‌های مبتنی بر پرامپت](#هوک‌های-مبتنی-بر-پرامپت) مراجعه کنید).

### هوک‌های ابزار MCP

> در نسخه 2.1.118 اضافه شد.

نوع `mcp_tool` یک ابزار MCP پیکربندی‌شده را مستقیماً فراخوانی می‌کند؛ پیکربندی به‌جای دستور شل یا URL، به سرور MCP و نام ابزار ارجاع می‌دهد. این زمانی مفید است که منطق اعتبارسنجی یا واکنش از قبل در یک سرور MCP پیکربندی‌شده شما قرار دارد.

```json
{
  "matcher": "Edit",
  "hooks": [{
    "type": "mcp_tool",
    "server": "my-mcp-server",
    "tool": "validate_edit",
    "input": { "file_path": "${tool_input.file_path}" }
  }]
}
```

**ویژگی‌های کلیدی:**
- `"type": "mcp_tool"` -- این را به‌عنوان هوک ابزار MCP مشخص می‌کند
- `"server"` -- نام سرور MCP پیکربندی‌شده
- `"tool"` -- نام ابزاری روی آن سرور که فراخوانی می‌شود
- `"input"` -- آرگومان‌های اختیاری که به ابزار داده می‌شود؛ مقادیر رشته‌ای از جایگذاری `${path}` از ورودی JSON هوک پشتیبانی می‌کنند، مانند `"${tool_input.file_path}"`

آرگومان‌های ابزار از `input` می‌آیند (با جایگذاری `${path}`)، نه مستقیماً از ورودی هوک. برای پیکربندی سرورهای MCP به [راه‌اندازی سرور MCP](../05-mcp/README.md) مراجعه کنید.

### هوک‌های Agent

هوک‌های تأیید مبتنی بر زیرایجنت که یک ایجنت اختصاصی برای ارزیابی شرایط یا انجام بررسی‌های پیچیده ایجاد می‌کنند. برخلاف هوک‌های prompt (ارزیابی تک‌نوبتی LLM)، هوک‌های agent می‌توانند از ابزارها استفاده کنند و استدلال چندمرحله‌ای انجام دهند.

> **توجه**: هوک‌های Agent آزمایشی هستند و ممکن است تغییر کنند.

> **توجه**: از نسخه 2.1.280، هوک‌های agent روی `PermissionRequest` اجرا نمی‌شوند — پاسخ آن‌ها هرگز نمی‌توانست درخواست را تأیید یا رد کند. در آن رویداد از یک هوک command یا HTTP که یک شیء تصمیم برمی‌گرداند استفاده کنید (`ok: false` یک هوک prompt روی `PermissionRequest` اثری ندارد).

```json
{
  "type": "agent",
  "prompt": "Verify the code changes follow our architecture guidelines. Check the relevant design docs and compare.",
  "timeout": 120
}
```

**ویژگی‌های کلیدی:**
- `"type": "agent"` -- این را به‌عنوان هوک agent مشخص می‌کند
- `"prompt"` -- توصیف وظیفه برای زیرایجنت
- ایجنت می‌تواند از ابزارها (Read، Grep، Bash و غیره) برای ارزیابی خود استفاده کند
- یک تصمیم ساختاریافته مشابه هوک‌های prompt برمی‌گرداند

## رویدادهای هوک

Claude Code از **۳۳ رویداد هوک** پشتیبانی می‌کند:

| رویداد | زمان فعال‌سازی | ورودی matcher | می‌تواند مسدود کند | استفاده رایج |
|-------|---------------|---------------|-----------|------------|
| **SessionStart** | شروع/از سرگیری/پاک‌سازی/فشرده‌سازی نشست | startup/resume/clear/compact/fork | خیر | راه‌اندازی محیط |
| **Setup** | `--init-only`، یا `--init`/`--maintenance` همراه با `-p` (آماده‌سازی CI/اسکریپت) | `init`/`maintenance` | خیر | فراهم‌سازی ابزار، نصب وابستگی‌ها |
| **InstructionsLoaded** | پس از بارگذاری CLAUDE.md یا فایل قواعد | دلیل بارگذاری (`session_start`/`nested_traversal`/`path_glob_match`/`include`/`compact`) | خیر | گزارش ممیزی/قابلیت مشاهده |
| **UserPromptSubmit** | کاربر پرامپت ارسال می‌کند | (هیچ) | بله | اعتبارسنجی پرامپت‌ها |
| **UserPromptExpansion** | دستور اسلش تایپ‌شده کاربر یا پرامپت MCP به یک پرامپت باز می‌شود | نام دستور | بله | تغییر یا بررسی پرامپت بازشده |
| **PreToolUse** | پیش از اجرای ابزار | نام ابزار | بله (allow/deny/ask/defer) | اعتبارسنجی، تغییر ورودی‌ها |
| **PermissionRequest** | نمایش گفتگوی مجوز | نام ابزار | بله | تأیید/رد خودکار |
| **PermissionDenied** | حالت auto یک فراخوانی ابزار را رد می‌کند | نام ابزار | خیر | گزارش‌گیری، تحلیل، اعمال سیاست |
| **PostToolUse** | پس از موفقیت ابزار | نام ابزار | خیر | افزودن زمینه، بازخورد |
| **PostToolUseFailure** | اجرای ابزار شکست می‌خورد | نام ابزار | خیر | مدیریت خطا، گزارش‌گیری |
| **PostToolBatch** | پس از تکمیل یک دسته استفاده از ابزار | (هیچ) | بله | گزارش‌گیری تجمیعی، اعتبارسنجی دسته‌ای |
| **Notification** | ارسال اعلان | نوع اعلان | خیر | اعلان‌های سفارشی |
| **MessageDisplay** | هنگام نمایش متن پیام دستیار | (هیچ) | خیر | تغییر یا پنهان کردن متن پیام نمایش‌داده‌شده (نسخه 2.1.152) |
| **SubagentStart** | ایجاد زیرایجنت | نام نوع ایجنت | خیر | راه‌اندازی زیرایجنت |
| **SubagentStop** | پایان زیرایجنت | نام نوع ایجنت | بله | اعتبارسنجی زیرایجنت |
| **Stop** | Claude پاسخ‌دهی را تمام می‌کند | (هیچ) | بله | بررسی تکمیل وظیفه |
| **StopFailure** | خطای API نوبت را پایان می‌دهد | نوع خطا (`rate_limit`، `overloaded`، `server_error`، …) | خیر | بازیابی از خطا، گزارش‌گیری |
| **TeammateIdle** | هم‌تیمی تیم ایجنت بی‌کار می‌شود | (هیچ) | بله | هماهنگ‌سازی هم‌تیمی |
| **TaskCompleted** | وظیفه تکمیل‌شده علامت می‌خورد | (هیچ) | بله | اقدامات پس از وظیفه |
| **TaskCreated** | وظیفه از طریق TaskCreate ایجاد می‌شود | (هیچ) | بله | پیگیری وظایف، گزارش‌گیری |
| **ConfigChange** | فایل پیکربندی تغییر می‌کند | منبع پیکربندی (`user_settings`/`project_settings`/`local_settings`/`policy_settings`/`skills`) | بله (به‌جز خط‌مشی) | واکنش به به‌روزرسانی‌های پیکربندی |
| **CwdChanged** | دایرکتوری کاری تغییر می‌کند | (هیچ) | خیر | راه‌اندازی مخصوص دایرکتوری |
| **DirectoryAdded** | دایرکتوری کاری جدید در میانه نشست از طریق `/add-dir` یا درخواست کنترلی `register_repo_root` در SDK ثبت می‌شود (نسخه 2.1.219) | `slash_command`/`register_repo_root` | خیر | راه‌اندازی ابزار برای دایرکتوری تازه‌افزوده‌شده |
| **FileChanged** | تغییر فایل تحت پایش | نام فایل‌های تحت پایش (مثلاً `.envrc\|.env`) | خیر | پایش فایل، بازسازی |
| **PreCompact** | پیش از فشرده‌سازی زمینه | manual/auto | بله | اقدامات پیش از فشرده‌سازی |
| **PostCompact** | پس از تکمیل فشرده‌سازی | (هیچ) | خیر | اقدامات پس از فشرده‌سازی |
| **PreModelSwitch** | پیش از اعمال تغییر مدل درخواستی توسط Claude Code | نام کانونی مدلی که به آن تغییر می‌شود (از `to_model`) | بله | دروازه‌بانی یا وتوی تغییرات مدل |
| **PostModelSwitch** | پس از تغییر مدل نشست، شامل تغییراتی که خود Claude Code انجام می‌دهد (مانند بازیابی مدل هنگام از سرگیری) | نام کانونی مدلی که به آن تغییر شد (از `to_model`) | خیر | گزارش یا واکنش به تغییرات مدل |
| **WorktreeCreate** | ایجاد worktree | (هیچ) | بله (بازگشت مسیر) | مقداردهی اولیه worktree |
| **WorktreeRemove** | حذف worktree | (هیچ) | بله (کد خروج غیرصفر حذف را ناموفق می‌کند) | پاکسازی worktree |
| **Elicitation** | سرور MCP ورودی کاربر را درخواست می‌کند | نام سرور MCP | بله | اعتبارسنجی ورودی |
| **ElicitationResult** | کاربر به استخراج پاسخ می‌دهد | نام سرور MCP | بله | پردازش پاسخ |
| **SessionEnd** | خاتمه نشست | دلیل پایان (`clear`/`resume`/`logout`/`prompt_input_exit`/`other`) | خیر | پاکسازی، گزارش‌گیری نهایی |

`PreModelSwitch` و `PostModelSwitch` نیازمند نسخه 2.1.251 یا جدیدتر هستند. هر دو `from_model` و `to_model` را دریافت می‌کنند؛ matcher در برابر نام کانونی مشتق‌شده از `to_model` ارزیابی می‌شود (مثلاً `claude-opus-5`، `.*opus.*`). پیش‌فرض مهلت `command`، `http` و `mcp_tool` آن‌ها به ۳۰ ثانیه کاهش می‌یابد.

> **`TaskCreated` و `TaskCompleted` نیازمند فعال بودن ابزارهای todo هستند (نسخه 2.1.233).** این دو
> رویداد از ابزارهای todo/پیگیری وظایف (`TaskCreate`/`Get`/`Update`/`List`،
> `TodoWrite`) فعال می‌شوند که **به‌طور پیش‌فرض فقط در مدل‌های Claude 3.x، Opus 4 تا
> 4.7، Sonnet 4 تا 4.6 و Haiku 4.5 در دسترس هستند**. در مدل‌های دیگر هوک‌ها هنوز پیکربندی
> معتبری هستند اما هرگز فعال نمی‌شوند — نه خروجی می‌گیرید و نه خطا. برای بازگرداندن
> ابزارها و در نتیجه این رویدادها، `CLAUDE_CODE_ENABLE_TODO_TOOLS=1` را تعیین کنید.

> **مدت PostToolUse (نسخه 2.1.119):** ورودی هوک‌های `PostToolUse` و `PostToolUseFailure` اکنون شامل `duration_ms` است — برای جزئیات به بخش [PostToolUse](#posttooluse) مراجعه کنید.

### PreToolUse

پس از آنکه Claude پارامترهای ابزار را می‌سازد و پیش از پردازش اجرا می‌شود. از این برای اعتبارسنجی یا تغییر ورودی‌های ابزار استفاده کنید.

**پیکربندی:**
```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "$CLAUDE_PROJECT_DIR/.claude/hooks/validate-bash.py"
          }
        ]
      }
    ]
  }
}
```

**matcherهای رایج:** `Agent`، `Bash`، `Glob`، `Grep`، `Read`، `Edit`، `Write`، `WebFetch`، `WebSearch`

**کنترل خروجی:**
- `permissionDecision`: `"allow"`، `"deny"`، `"ask"` یا `"defer"`
  - `"allow"` پرامپت مجوز را رد می‌کند (به‌جز ابزارهایی که نیازمند تعامل کاربر هستند، و ابزارهای کانکتوری که سازمان شما روی `ask` گذاشته است)
  - `"deny"` از فراخوانی ابزار جلوگیری می‌کند
  - `"ask"` از کاربر می‌خواهد تأیید کند؛ پرامپت نام پلاگین یا مهارتی که هوک از آن آمده را نشان می‌دهد (نسخه 2.1.301)
  - `"defer"` نوبت را پایان می‌دهد تا ابزار بعداً از سر گرفته شود، و فقط در حالت غیرتعاملی با `-p` کار می‌کند (نشست‌های تعاملی هشدار ثبت و آن را نادیده می‌گیرند)؛ نتیجه `stop_reason: "tool_deferred"` را حمل می‌کند. برای این مقدار `permissionDecisionReason`، `updatedInput` و `additionalContext` همه نادیده گرفته می‌شوند
  - قواعد deny و ask بدون توجه به آنچه هوک برمی‌گرداند هنوز ارزیابی می‌شوند. وقتی چندین هوک `PreToolUse` اختلاف دارند، اولویت `deny` > `defer` > `ask` > `allow` است
- `permissionDecisionReason`: توضیح تصمیم. برای `"ask"` به کاربر نمایش داده می‌شود (نه به Claude)؛ برای `"deny"` به Claude نمایش داده می‌شود؛ برای `"allow"` و `"defer"` فقط در لاگ اشکال‌زدایی نوشته می‌شود
- `updatedInput`: ورودی جایگزین ابزار (کل شیء ورودی را جایگزین می‌کند). از نسخه 2.1.300 مانند ورودی خود Claude اعتبارسنجی می‌شود — کلیدهای ناشناخته حذف می‌شوند، و ورودی‌ای که ابزار رد کند باعث رد فراخوانی می‌شود. وقتی چند هوک `PreToolUse` برای یک فراخوانی `updatedInput` برمی‌گردانند، Claude Code بازنویسی‌ها را ادغام نمی‌کند و تضمین نمی‌کند ابزار با کدام‌یک اجرا شود، پس بگذارید فقط یک هوک ورودی یک ابزار را بازنویسی کند.

### PostToolUse

بلافاصله پس از تکمیل ابزار اجرا می‌شود. برای تأیید، گزارش‌گیری، یا ارائه زمینه به Claude استفاده کنید.

**پیکربندی:**
```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "$CLAUDE_PROJECT_DIR/.claude/hooks/security-scan.py"
          }
        ]
      }
    ]
  }
}
```

**کنترل خروجی:**
- تصمیم `"block"` به Claude بازخورد می‌دهد
- `additionalContext`: زمینه‌ای که برای Claude افزوده می‌شود

**فیلدهای ورودی اضافی (نسخه 2.1.119):**

| فیلد | نوع | توضیح |
|-------|------|-------------|
| `duration_ms` | number | زمان اجرای ابزار به میلی‌ثانیه. شامل زمان صرف‌شده در پرامپت‌های مجوز و اجرای هوک PreToolUse نیست. در هر دو هوک `PostToolUse` و `PostToolUseFailure` موجود است. |

#### مسدودسازی‌های قابل بازیابی (`continueOnBlock`، نسخه 2.1.139)

یک هوک command که روی `PostToolUse` مقدار `"decision": "block"` برمی‌گرداند، `reason` را کنار نتیجه ابزار اضافه می‌کند؛ Claude همچنان خروجی اصلی را می‌بیند. `continueOnBlock` یک فیلد مخصوص هوک **prompt** است (هوک‌های command و agent آن را ندارند): به‌طور پیش‌فرض، هوک prompt که روی `PostToolUse` مقدار `ok: false` برمی‌گرداند نوبت را پایان می‌دهد و دلیل را به‌عنوان یک خط هشدار نشان می‌دهد. برای اینکه به‌جای آن دلیل به Claude بازگردانده شود و نوبت ادامه یابد، روی هوک prompt مقدار `"continueOnBlock": true` را تعیین کنید تا مدل بتواند بازخورد را بخواند و دوباره تلاش کند یا تنظیم کند.

```json
{
  "hooks": {
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "prompt",
            "prompt": "Check this edit against our write policy (for example, read-only paths). Hook input: $ARGUMENTS",
            "continueOnBlock": true
          }
        ]
      }
    ]
  }
}
```

از این زمانی استفاده کنید که `reason` هوک چیزی باشد که Claude می‌تواند روی آن اقدام کند (مثلاً «این فایل فقط-خواندنی است؛ جای دیگری بنویس»)؛ وقتی یک مسدودسازی باید کل نوبت را متوقف کند آن را خاموش بگذارید.

### UserPromptSubmit

وقتی کاربر پرامپتی ارسال می‌کند و پیش از پردازش آن توسط Claude اجرا می‌شود. از نسخه 2.1.299 پیش از بازشدن یک مهارت یا دستور سفارشی اجرا می‌شود، بنابراین مسدود کردن پرامپت خطوط شل `!` آن دستور را هم متوقف می‌کند؛ `UserPromptExpansion` پس از آن فعال می‌شود.

**پیکربندی:**
```json
{
  "hooks": {
    "UserPromptSubmit": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "$CLAUDE_PROJECT_DIR/.claude/hooks/validate-prompt.py"
          }
        ]
      }
    ]
  }
}
```

**کنترل خروجی:**
- `decision`: `"block"` برای جلوگیری از پردازش
- `reason`: توضیح در صورت مسدودسازی
- `additionalContext`: زمینه‌ای که به پرامپت افزوده می‌شود

### Stop و SubagentStop

وقتی Claude پاسخ‌دهی را تمام می‌کند (Stop) یا یک زیرایجنت تکمیل می‌شود (SubagentStop) اجرا می‌شوند. از ارزیابی مبتنی بر پرامپت برای بررسی هوشمند تکمیل وظیفه پشتیبانی می‌کنند.

**فیلد ورودی اضافی:** هر دو هوک `Stop` و `SubagentStop` در ورودی JSON خود فیلد `last_assistant_message` را دریافت می‌کنند که شامل پیام نهایی Claude یا زیرایجنت پیش از توقف است. این برای ارزیابی تکمیل وظیفه مفید است.

**پیکربندی:**
```json
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "prompt",
            "prompt": "Evaluate if Claude completed all requested tasks.",
            "timeout": 30
          }
        ]
      }
    ]
  }
}
```

> **سقف ایمنی برای مسدودسازی‌های پیاپی (نسخه 2.1.143)**: اگر یک هوک `Stop` برای همان نوبت **۸ بار پیاپی** مقدار `"decision": "block"` را برگرداند (یا `continue: false` تعیین کند)، Claude Code مسدودسازی بعدی را نادیده می‌گیرد و نوبت را پایان می‌دهد. آستانه را با متغیر محیطی `CLAUDE_CODE_STOP_HOOK_BLOCK_CAP=<integer>` بازنویسی کنید (برای غیرفعال کردن کامل سقف آن را `0` بگذارید). این از حلقه بی‌پایان یک هوک Stop باگ‌دار جلوگیری می‌کند.

**فیلد بازگشتی (نسخه 2.1.163):** یک هوک `Stop` یا `SubagentStop` می‌تواند `hookSpecificOutput.additionalContext` را برگرداند تا به Claude بازخورد بدهد و **نوبت را بدون نمایش برچسب خطا ادامه دهد**. پیش‌تر تأثیرگذاری بر مدل از یک هوک Stop دشوار بود؛ اکنون هوک می‌تواند زمینه را به‌صورت تمیز تزریق کند و از رفتار برچسب خطای مسیرهای بازخورد قدیمی‌تر (مانند `"decision": "block"`) پرهیز کند.

```json
{
  "hookSpecificOutput": {
    "hookEventName": "Stop",
    "additionalContext": "Reminder: run the test suite before declaring done."
  }
}
```

### SubagentStart

وقتی یک زیرایجنت اجرا را آغاز می‌کند اجرا می‌شود. ورودی matcher نام نوع ایجنت است، که به هوک‌ها اجازه می‌دهد انواع مشخص زیرایجنت را هدف بگیرند.

**پیکربندی:**
```json
{
  "hooks": {
    "SubagentStart": [
      {
        "matcher": "code-review",
        "hooks": [
          {
            "type": "command",
            "command": "$CLAUDE_PROJECT_DIR/.claude/hooks/subagent-init.sh"
          }
        ]
      }
    ]
  }
}
```

### SessionStart

وقتی نشست شروع یا از سر گرفته می‌شود اجرا می‌شود. می‌تواند متغیرهای محیطی را پایدار کند.

**matcherها:** `startup`، `resume`، `clear`، `compact`، `fork`

> **به‌روزرسانی نسخه 2.1.214**: یک نشست منشعب اکنون منبع `"fork"` را گزارش می‌دهد — پیش‌تر `"resume"` را گزارش می‌داد.

**ویژگی ویژه:** از `CLAUDE_ENV_FILE` برای پایدارسازی متغیرهای محیطی استفاده کنید (در هوک‌های `CwdChanged` و `FileChanged` هم موجود است):

```bash
#!/bin/bash
if [ -n "$CLAUDE_ENV_FILE" ]; then
  echo 'export NODE_ENV=development' >> "$CLAUDE_ENV_FILE"
fi
exit 0
```

**خروجی‌های محدود به نشست (نسخه 2.1.152):** یک هوک `SessionStart` می‌تواند JSON برگرداند تا مهارت‌ها را دوباره اسکن کند و عنوان نشست را تعیین کند:

```json
{
  "reloadSkills": true,
  "hookSpecificOutput": {
    "sessionTitle": "Payments migration"
  }
}
```

`reloadSkills: true` در سطح بالا یک اسکن مجدد مهارت در همان نشست را فعال می‌کند (همان اقدام دستور `/reload-skills`)، و مهارت‌هایی که هوک همین حالا نصب کرده بلافاصله در دسترس می‌شوند. `hookSpecificOutput.sessionTitle` عنوان نمایشی نشست را هنگام شروع و از سرگیری تعیین می‌کند.

### SessionEnd

وقتی نشست پایان می‌یابد برای پاکسازی یا گزارش‌گیری نهایی اجرا می‌شود. نمی‌تواند خاتمه را مسدود کند.

**مقادیر فیلد reason:**
- `clear` - کاربر نشست را پاک کرد
- `resume` - نشست از طریق `/resume` تعاملی جابه‌جا شد
- `logout` - کاربر خارج شد
- `prompt_input_exit` - کاربر از طریق ورودی پرامپت خارج شد
- `other` - دلیل دیگر

**پیکربندی:**
```json
{
  "hooks": {
    "SessionEnd": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "\"$CLAUDE_PROJECT_DIR/.claude/hooks/session-cleanup.sh\""
          }
        ]
      }
    ]
  }
}
```

### رویداد Notification

matcherهای به‌روزشده برای رویدادهای اعلان:
- `permission_prompt` - اعلان درخواست مجوز
- `idle_prompt` - اعلان حالت بی‌کار
- `auth_success` - موفقیت احراز هویت
- `elicitation_dialog` - سرور MCP یک فرم استخراج باز کرد
- `elicitation_url_dialog` - سرور MCP از شما می‌خواهد یک URL مرورگر باز کنید
- `elicitation_complete` - استخراج حالت URL تکمیل‌شده گزارش شد
- `elicitation_response` - پاسخ استخراج به سرور بازگردانده شد
- `agent_needs_input` - ایجنت پس‌زمینه نیازمند ورودی است (نسخه 2.1.198)
- `agent_completed` - ایجنت پس‌زمینه تمام شد (نسخه 2.1.198)
- `quota_auto_resume_fired` / `quota_auto_resume_stale` / `quota_auto_resume_disabled` - نتایج از سرگیری خودکار پس از محدودیت استفاده (نسخه 2.1.234)
- `plugin_notification` - یک mod با `$.ui.notify` اعلانی فرستاد؛ `title` هوک نام آن mod است مگر اینکه mod خودش یکی تعیین کرده باشد

### PreModelSwitch

**پیش از** اعمال یک تغییر مدل درخواستی توسط Claude Code اجرا می‌شود — مثلاً وقتی `/model` را اجرا می‌کنید، یا وقتی یک کامپوننت مدل دیگری درخواست می‌کند. نیازمند نسخه 2.1.251 یا جدیدتر است.

**matcherها:** نام کانونی مدلی که به آن تغییر می‌شود، مشتق‌شده از `to_model`. یک مدل دقیق (`claude-opus-5`) یا یک خانواده با regex (`.*opus.*`) را تطبیق دهید.

**فیلدهای ورودی:** علاوه بر فیلدهای رایج، هوک `from_model` (مدل در حال استفاده پیش از تغییر) و `to_model` (مدل درخواستی) را دریافت می‌کند.

**می‌تواند مسدود کند:** بله. کد خروج `2` تغییر را مسدود می‌کند و stderr را به‌عنوان خطا نشان می‌دهد، بنابراین نشست مدل فعلی خود را نگه می‌دارد. از این برای دروازه‌بانی یا وتوی تغییرات مدل استفاده کنید — مثلاً برای نگه‌داشتن یک پروژه حساس به هزینه دور از گران‌ترین مدل.

**مهلت زمانی:** این رویداد مهلت پیش‌فرض `command`، `http` و `mcp_tool` را به ۳۰ ثانیه کاهش می‌دهد.

**پیکربندی:**
```json
{
  "hooks": {
    "PreModelSwitch": [
      {
        "matcher": ".*opus.*",
        "hooks": [
          {
            "type": "command",
            "command": "$CLAUDE_PROJECT_DIR/.claude/hooks/gate-model-switch.sh"
          }
        ]
      }
    ]
  }
}
```

```bash
#!/bin/bash
# gate-model-switch.sh — رد کردن تغییر به Opus در این پروژه
input=$(cat)
to_model=$(echo "$input" | jq -r '.to_model')

if [[ "$to_model" == *opus* ]]; then
  echo "This project is budgeted for Sonnet; staying on the current model." >&2
  exit 2
fi

exit 0
```

### PostModelSwitch

**پس از** تغییر مدل نشست اجرا می‌شود. برای تغییراتی که خود Claude Code انجام می‌دهد هم فعال می‌شود — مانند بازیابی مدل انتخاب‌شده قبلی هنگام از سرگیری یک نشست — نه فقط برای تغییراتی که شما درخواست می‌کنید. نیازمند نسخه 2.1.251 یا جدیدتر است.

**matcherها:** مانند `PreModelSwitch` — نام کانونی مشتق‌شده از `to_model`.

**فیلدهای ورودی:** `from_model` و `to_model`، در کنار فیلدهای رایج.

**می‌تواند مسدود کند:** خیر. تغییر قبلاً رخ داده است؛ هوک فقط می‌تواند مشاهده و واکنش کند.

**مهلت زمانی:** این رویداد مهلت پیش‌فرض `command`، `http` و `mcp_tool` را به ۳۰ ثانیه کاهش می‌دهد.

**پیکربندی:**
```json
{
  "hooks": {
    "PostModelSwitch": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "$CLAUDE_PROJECT_DIR/.claude/hooks/log-model-switch.sh"
          }
        ]
      }
    ]
  }
}
```

```bash
#!/bin/bash
# log-model-switch.sh — ثبت هر تغییر مدل در گزارش نشست
input=$(cat)
from=$(echo "$input" | jq -r '.from_model')
to=$(echo "$input" | jq -r '.to_model')

echo "$(date -Iseconds) $from -> $to" >> ~/.claude/model-switches.log
exit 0
```

## هوک‌های محدود به کامپوننت

هوک‌ها می‌توانند در frontmatter خود به کامپوننت‌های مشخص (مهارت‌ها، ایجنت‌ها، دستورات) متصل شوند:

**در SKILL.md، agent.md یا command.md:**

```yaml
---
name: secure-operations
description: Perform operations with security checks
hooks:
  PreToolUse:
    - matcher: "Bash"
      hooks:
        - type: command
          command: "./scripts/check.sh"
          once: true  # Skill frontmatter only: removed after first successful run
---
```

**رویدادهای پشتیبانی‌شده:** همه رویدادهای هوک. هوک‌های زیرایجنت فقط تا زمانی که زیرایجنت فعال است اجرا می‌شوند (`Stop` → `SubagentStop`)؛ هوک‌های مهارت هنگام فراخوانی مهارت ثبت می‌شوند و برای باقی نشست فعال می‌مانند. از v2.1.304، مهارت‌های یک منبع (پروژه‌ی شما، پوشه مهارت‌های شخصی شما یا یک پلاگین) حداکثر ۱٬۰۲۴ هوک و ۱۶٬۳۸۴ کاراکتر matcher در هر نشست ثبت می‌کنند؛ مهارت فراتر از این حد هیچ‌یک از هوک‌هایش را ثبت نمی‌کند (در لاگ `claude --debug` عبارت `registers none of its hooks` را جست‌وجو کنید).

این اجازه می‌دهد هوک‌ها را مستقیماً در کامپوننتی که از آن‌ها استفاده می‌کند تعریف کنید و کد مرتبط را کنار هم نگه دارید.

### هوک‌ها در frontmatter زیرایجنت

وقتی یک هوک `Stop` در frontmatter یک زیرایجنت تعریف می‌شود، به‌طور خودکار به یک هوک `SubagentStop` محدود به همان زیرایجنت تبدیل می‌شود. این تضمین می‌کند هوک stop فقط وقتی آن زیرایجنت مشخص تکمیل می‌شود فعال شود، نه وقتی نشست اصلی متوقف می‌شود.

```yaml
---
name: code-review-agent
description: Automated code review subagent
hooks:
  Stop:
    - hooks:
        - type: prompt
          prompt: "Verify the code review is thorough and complete."
  # هوک Stop بالا برای این زیرایجنت خودکار به SubagentStop تبدیل می‌شود
---
```

**نیازمند اعتماد به فضای کاری (نسخه 2.1.218):** هوک‌های frontmatter در یک زیرایجنت **پروژه** اکنون پیش از اجرا نیازمند پذیرش اعتماد فضای کاری برای پوشه‌ای هستند که فایل ایجنت از آن آمده است. پیش از نسخه 2.1.218 این هوک‌ها می‌توانستند از پوشه‌هایی اجرا شوند که به آن‌ها اعتماد نکرده بودید. برای اینکه کدام دامنه‌ها معاف هستند به [مستندات زیرایجنت‌ها](https://code.claude.com/docs/en/sub-agents#hooks-in-subagent-frontmatter) مراجعه کنید.

## رویداد PermissionRequest

درخواست‌های مجوز را با قالب خروجی سفارشی مدیریت می‌کند:

```json
{
  "hookSpecificOutput": {
    "hookEventName": "PermissionRequest",
    "decision": {
      "behavior": "allow|deny",
      "updatedInput": {},
      "message": "Custom message",
      "interrupt": false
    }
  }
}
```

## ورودی و خروجی هوک

### ورودی JSON (از طریق stdin)

همه هوک‌ها ورودی JSON را از طریق stdin دریافت می‌کنند:

```json
{
  "session_id": "abc123",
  "transcript_path": "/path/to/transcript.jsonl",
  "cwd": "/current/working/directory",
  "permission_mode": "default",
  "hook_event_name": "PreToolUse",
  "tool_name": "Write",
  "tool_input": {
    "file_path": "/path/to/file.js",
    "content": "..."
  },
  "tool_use_id": "toolu_01ABC123...",
  "agent_id": "agent-abc123",
  "agent_type": "security-reviewer",
  "worktree": "/path/to/worktree",
  "effort": { "level": "medium" }
}
```

**فیلدهای رایج:**

| فیلد | توضیح |
|-------|-------------|
| `session_id` | شناسه یکتای نشست |
| `transcript_path` | مسیر فایل رونوشت گفتگو |
| `cwd` | دایرکتوری کاری جاری |
| `prompt_id` | UUID پرامپتی که پردازش می‌شود؛ با صفت `prompt.id` در OpenTelemetry همبسته است (نسخه 2.1.196) |
| `hook_event_name` | نام رویدادی که هوک را فعال کرد |
| `agent_id` | شناسه ایجنتی که این هوک را اجرا می‌کند |
| `agent_type` | نام ایجنت (مثلاً `"Explore"` یا `"security-reviewer"`)؛ فقط وقتی موجود است که نشست از `--agent` استفاده کند یا هوک درون یک زیرایجنت فعال شود |
| `worktree` | مسیر worktree گیت، اگر ایجنت در یکی اجرا شود |
| `effort.level` | (نسخه 2.1.133 به بعد) سطح تلاش فعال: `low`، `medium`، `high`، `xhigh` یا `max` |

### کدهای خروج

| کد خروج | معنا | رفتار |
|-----------|---------|----------|
| **0** | موفقیت | ادامه، تجزیه stdout JSON |
| **2** | خطای مسدودکننده | مسدود کردن عملیات، stderr به‌عنوان خطا نمایش داده می‌شود |
| **سایر** | خطای غیرمسدودکننده | ادامه؛ یک اعلان `<hook name> hook error` در رونوشت، خط اول stderr را نشان می‌دهد |

### خروجی JSON (stdout، کد خروج ۰)

```json
{
  "continue": true,
  "stopReason": "Optional message if stopping",
  "suppressOutput": false,
  "systemMessage": "Optional warning message",
  "hookSpecificOutput": {
    "hookEventName": "PreToolUse",
    "permissionDecision": "allow",
    "permissionDecisionReason": "File is in allowed directory",
    "updatedInput": {
      "file_path": "/modified/path.js"
    }
  }
}
```

> **دامنه (نسخه 2.1.121 به بعد):** `hookSpecificOutput.updatedToolOutput` اکنون برای **همه** ابزارها اعمال می‌شود، نه فقط ابزارهای MCP. یک هوک `PostToolUse` روی `Bash`، `Edit`، `Read` و غیره می‌تواند خروجی ابزار را پیش از دیدن توسط Claude بازنویسی کند — مفید برای پوشاندن رازها، یکسان‌سازی diffها، یا فیلتر کردن خروجی پرنویز دستورات. مقدار باید با شکل خروجی ابزار مطابقت داشته باشد — `Bash` یک شیء با `stdout`، `stderr`، `interrupted` و `isImage` برمی‌گرداند؛ برای ابزارهای داخلی، مقداری که مطابقت نداشته باشد نادیده گرفته می‌شود و خروجی اصلی استفاده می‌شود. مثال (حذف کدهای رنگ ANSI از خروجی `Bash`):
>
> ```json
> {
>   "hookSpecificOutput": {
>     "hookEventName": "PostToolUse",
>     "updatedToolOutput": {
>       "stdout": "<output with ANSI escapes removed>",
>       "stderr": "",
>       "interrupted": false,
>       "isImage": false
>     }
>   }
> }
> ```

> **`retry` (PermissionDenied)**: از JSON `hookSpecificOutput.retry: true` استفاده کنید تا به مدل بگویید می‌تواند فراخوانی ابزار ردشده را دوباره امتحان کند.

> **شکل منسوخ تصمیم `PreToolUse`**: برای `PreToolUse`، فیلدهای سطح بالای `decision` و `reason` **منسوخ** هستند — به‌جای آن از `hookSpecificOutput.permissionDecision` (`allow` / `deny` / `ask` / `defer`) و `permissionDecisionReason` استفاده کنید. اولویت میان تصمیم‌ها `deny` > `defer` > `ask` > `allow` است. همچنین توجه کنید که `suppressOutput` پذیرفته می‌شود اما **هیچ اثری ندارد**.

#### `terminalSequence` (نسخه 2.1.141)

هوک‌ها می‌توانند با تعیین `terminalSequence` در خروجی JSON، دنباله‌های گریز خام OSC (دستور سیستم‌عامل) منتشر کنند. میزبان دنباله را وقتی هوک برمی‌گردد به ترمینال کنترل‌کننده خود می‌نویسد — مفید برای اعلان‌های دسکتاپ، به‌روزرسانی عنوان پنجره و زنگ ترمینال بدون نیاز به TTY اختصاصی.

| فیلد | نوع | توضیح |
|-------|------|-------------|
| `terminalSequence` | string | دنباله گریز خام (معمولاً OSC 9 / OSC 0 / OSC 777). عیناً به ترمینال میزبان نوشته می‌شود. |

مثال — ارسال یک اعلان دسکتاپ OSC 9 وقتی یک وظیفه طولانی تکمیل می‌شود. ESC و BEL را به‌صورت گریزهای JSON بنویسید (`\u001b`، `\u0007`) یا مقدار را با `printf` و `jq` بسازید؛ بایت‌های کنترلی خام درون یک رشته JSON تجزیه نمی‌شوند:

```json
{
  "terminalSequence": "\u001b]9;Task complete\u0007"
}
```

آن را روی یک هوک `Stop` پیکربندی کنید تا اعلان وقتی Claude یک نوبت را تمام می‌کند ارسال شود. پشتیبانی دنباله به ترمینال بستگی دارد؛ iTerm2، Windows Terminal و WezTerm از OSC 9 پشتیبانی می‌کنند، در حالی که Kitty از OSC 99 استفاده می‌کند.

## متغیرهای محیطی

| متغیر | دسترس‌پذیری | توضیح |
|----------|-------------|-------------|
| `CLAUDE_PROJECT_DIR` | همه هوک‌ها | مسیر مطلق ریشه پروژه |
| `CLAUDE_ENV_FILE` | SessionStart، CwdChanged، FileChanged | مسیر فایل برای پایدارسازی متغیرهای محیطی |
| `CLAUDE_CODE_REMOTE` | همه هوک‌ها | اگر در محیط‌های از راه دور اجرا شود `"true"` |
| `${CLAUDE_PLUGIN_ROOT}` | هوک‌های پلاگین | مسیر دایرکتوری پلاگین |
| `${CLAUDE_PLUGIN_DATA}` | هوک‌های پلاگین | مسیر دایرکتوری داده پلاگین |
| `CLAUDE_CODE_SESSIONEND_HOOKS_TIMEOUT_MS` | هوک‌های SessionEnd | مهلت زمانی قابل پیکربندی به میلی‌ثانیه برای هوک‌های SessionEnd (پیش‌فرض را بازنویسی می‌کند) |
| `CLAUDE_CODE_SESSION_ID` | زیرفرایندهای ابزار Bash (نسخه 2.1.132 به بعد) | UUID نشست؛ با فیلد `session_id` در JSON ورودی هوک مطابقت دارد. برای همبسته‌سازی لاگ‌های bash با تله‌متری هوک استفاده کنید. |
| `CLAUDE_EFFORT` | زیرفرایندهای ابزار Bash (نسخه 2.1.133 به بعد) | سطح تلاش فعال (`low`/`medium`/`high`/`xhigh`/`max`)؛ با `effort.level` در JSON ورودی هوک مطابقت دارد. |
| `CLAUDE_CODE_STOP_HOOK_BLOCK_CAP` | سراسر فرایند (نسخه 2.1.143 به بعد) | حداکثر مسدودسازی‌های پیاپی هوک Stop پیش از آنکه Claude Code مسدودسازی بعدی را نادیده بگیرد و نوبت را پایان دهد (پیش‌فرض `8`). برای غیرفعال کردن سقف آن را `0` بگذارید. |

## هوک‌های مبتنی بر پرامپت

برای رویدادهای `Stop` و `SubagentStop` می‌توانید از ارزیابی مبتنی بر LLM استفاده کنید:

```json
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "prompt",
            "prompt": "Review if all tasks are complete. Return your decision.",
            "timeout": 30
          }
        ]
      }
    ]
  }
}
```

**شمای پاسخ LLM:**
```json
{
  "ok": false,
  "reason": "Tests were not run after the last edit"
}
```

`ok: true` اقدام را مجاز می‌کند؛ وقتی `ok` برابر `false` است، `reason` الزامی است.

## مثال‌ها

### مثال ۱: اعتبارسنج دستور Bash (PreToolUse)

**فایل:** `.claude/hooks/validate-bash.py`

```python
#!/usr/bin/env python3
import json
import sys
import re

BLOCKED_PATTERNS = [
    (r"\brm\s+-rf\s+/", "Blocking dangerous rm -rf / command"),
    (r"\bsudo\s+rm", "Blocking sudo rm command"),
]

def main():
    input_data = json.load(sys.stdin)

    tool_name = input_data.get("tool_name", "")
    if tool_name != "Bash":
        sys.exit(0)

    command = input_data.get("tool_input", {}).get("command", "")

    for pattern, message in BLOCKED_PATTERNS:
        if re.search(pattern, command):
            print(message, file=sys.stderr)
            sys.exit(2)  # Exit 2 = blocking error

    sys.exit(0)

if __name__ == "__main__":
    main()
```

**پیکربندی:**
```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "python3 \"$CLAUDE_PROJECT_DIR/.claude/hooks/validate-bash.py\""
          }
        ]
      }
    ]
  }
}
```

### مثال ۲: اسکنر امنیتی (PostToolUse)

**فایل:** `.claude/hooks/security-scan.py`

```python
#!/usr/bin/env python3
import json
import sys
import re

SECRET_PATTERNS = [
    (r"password\s*=\s*['\"][^'\"]+['\"]", "Potential hardcoded password"),
    (r"api[_-]?key\s*=\s*['\"][^'\"]+['\"]", "Potential hardcoded API key"),
]

def main():
    input_data = json.load(sys.stdin)

    tool_name = input_data.get("tool_name", "")
    if tool_name not in ["Write", "Edit"]:
        sys.exit(0)

    tool_input = input_data.get("tool_input", {})
    content = tool_input.get("content", "") or tool_input.get("new_string", "")
    file_path = tool_input.get("file_path", "")

    warnings = []
    for pattern, message in SECRET_PATTERNS:
        if re.search(pattern, content, re.IGNORECASE):
            warnings.append(message)

    if warnings:
        output = {
            "hookSpecificOutput": {
                "hookEventName": "PostToolUse",
                "additionalContext": f"Security warnings for {file_path}: " + "; ".join(warnings)
            }
        }
        print(json.dumps(output))

    sys.exit(0)

if __name__ == "__main__":
    main()
```

### مثال ۳: قالب‌بندی خودکار کد (PostToolUse)

**فایل:** `.claude/hooks/format-code.sh`

```bash
#!/bin/bash

# خواندن JSON از stdin
INPUT=$(cat)
TOOL_NAME=$(echo "$INPUT" | python3 -c "import sys, json; print(json.load(sys.stdin).get('tool_name', ''))")
FILE_PATH=$(echo "$INPUT" | python3 -c "import sys, json; print(json.load(sys.stdin).get('tool_input', {}).get('file_path', ''))")

if [ "$TOOL_NAME" != "Write" ] && [ "$TOOL_NAME" != "Edit" ]; then
    exit 0
fi

# قالب بر اساس پسوند فایل
case "$FILE_PATH" in
    *.js|*.jsx|*.ts|*.tsx|*.json)
        command -v prettier &>/dev/null && prettier --write "$FILE_PATH" 2>/dev/null
        ;;
    *.py)
        command -v black &>/dev/null && black "$FILE_PATH" 2>/dev/null
        ;;
    *.go)
        command -v gofmt &>/dev/null && gofmt -w "$FILE_PATH" 2>/dev/null
        ;;
esac

exit 0
```

### مثال ۴: اعتبارسنج پرامپت (UserPromptSubmit)

**فایل:** `.claude/hooks/validate-prompt.py`

```python
#!/usr/bin/env python3
import json
import sys
import re

BLOCKED_PATTERNS = [
    (r"delete\s+(all\s+)?database", "Dangerous: database deletion"),
    (r"rm\s+-rf\s+/", "Dangerous: root deletion"),
]

def main():
    input_data = json.load(sys.stdin)
    prompt = input_data.get("prompt", "")

    for pattern, message in BLOCKED_PATTERNS:
        if re.search(pattern, prompt, re.IGNORECASE):
            output = {
                "decision": "block",
                "reason": f"Blocked: {message}"
            }
            print(json.dumps(output))
            sys.exit(0)

    sys.exit(0)

if __name__ == "__main__":
    main()
```

### مثال ۵: هوک Stop هوشمند (مبتنی بر پرامپت)

```json
{
  "hooks": {
    "Stop": [
      {
        "hooks": [
          {
            "type": "prompt",
            "prompt": "Review if Claude completed all requested tasks. Check: 1) Were all files created/modified? 2) Were there unresolved errors? If incomplete, explain what's missing.",
            "timeout": 30
          }
        ]
      }
    ]
  }
}
```

### مثال ۶: پیگیر مصرف زمینه (جفت هوک)

مصرف توکن هر درخواست را با استفاده هم‌زمان از هوک‌های `UserPromptSubmit` (پیش از پیام) و `Stop` (پس از پاسخ) پیگیری کنید.

**فایل:** `.claude/hooks/context-tracker.py`

```python
#!/usr/bin/env python3
"""
Context Usage Tracker - Tracks token consumption per request.

Uses UserPromptSubmit as "pre-message" hook and Stop as "post-response" hook
to calculate the delta in token usage for each request.

Token Counting Methods:
1. Character estimation (default): ~4 chars per token, no dependencies
2. tiktoken (optional): More accurate (~90-95%), requires: pip install tiktoken
"""
import json
import os
import sys
import tempfile

# پیکربندی
CONTEXT_LIMIT = 1000000  # 1M on Opus 5, Sonnet 5, Opus 4.8, Sonnet 4.6; 200000 on Haiku 4.5 (adjust for your model)
USE_TIKTOKEN = False    # Set True if tiktoken is installed for better accuracy


def get_state_file(session_id: str) -> str:
    """Get temp file path for storing pre-message token count, isolated by session."""
    return os.path.join(tempfile.gettempdir(), f"claude-context-{session_id}.json")


def count_tokens(text: str) -> int:
    """
    Count tokens in text.

    Uses tiktoken with p50k_base encoding if available (~90-95% accuracy),
    otherwise falls back to character estimation (~80-90% accuracy).
    """
    if USE_TIKTOKEN:
        try:
            import tiktoken
            enc = tiktoken.get_encoding("p50k_base")
            return len(enc.encode(text))
        except ImportError:
            pass  # Fall back to estimation

    # تخمین بر پایه نویسه: حدود ۴ نویسه به ازای هر توکن برای انگلیسی
    return len(text) // 4


def read_transcript(transcript_path: str) -> str:
    """Read and concatenate all content from transcript file."""
    if not transcript_path or not os.path.exists(transcript_path):
        return ""

    content = []
    with open(transcript_path, "r") as f:
        for line in f:
            try:
                entry = json.loads(line.strip())
                # استخراج محتوای متنی از قالب‌های مختلف پیام
                if "message" in entry:
                    msg = entry["message"]
                    if isinstance(msg.get("content"), str):
                        content.append(msg["content"])
                    elif isinstance(msg.get("content"), list):
                        for block in msg["content"]:
                            if isinstance(block, dict) and block.get("type") == "text":
                                content.append(block.get("text", ""))
            except json.JSONDecodeError:
                continue

    return "\n".join(content)


def handle_user_prompt_submit(data: dict) -> None:
    """Pre-message hook: Save current token count before request."""
    session_id = data.get("session_id", "unknown")
    transcript_path = data.get("transcript_path", "")

    transcript_content = read_transcript(transcript_path)
    current_tokens = count_tokens(transcript_content)

    # ذخیره در فایل موقت برای مقایسه بعدی
    state_file = get_state_file(session_id)
    with open(state_file, "w") as f:
        json.dump({"pre_tokens": current_tokens}, f)


def handle_stop(data: dict) -> None:
    """Post-response hook: Calculate and report token delta."""
    session_id = data.get("session_id", "unknown")
    transcript_path = data.get("transcript_path", "")

    transcript_content = read_transcript(transcript_path)
    current_tokens = count_tokens(transcript_content)

    # بارگذاری شمارش پیش از پیام
    state_file = get_state_file(session_id)
    pre_tokens = 0
    if os.path.exists(state_file):
        try:
            with open(state_file, "r") as f:
                state = json.load(f)
                pre_tokens = state.get("pre_tokens", 0)
        except (json.JSONDecodeError, IOError):
            pass

    # محاسبه اختلاف
    delta_tokens = current_tokens - pre_tokens
    remaining = CONTEXT_LIMIT - current_tokens
    percentage = (current_tokens / CONTEXT_LIMIT) * 100

    # گزارش مصرف
    method = "tiktoken" if USE_TIKTOKEN else "estimated"
    print(f"Context ({method}): ~{current_tokens:,} tokens ({percentage:.1f}% used, ~{remaining:,} remaining)", file=sys.stderr)
    if delta_tokens > 0:
        print(f"This request: ~{delta_tokens:,} tokens", file=sys.stderr)


def main():
    data = json.load(sys.stdin)
    event = data.get("hook_event_name", "")

    if event == "UserPromptSubmit":
        handle_user_prompt_submit(data)
    elif event == "Stop":
        handle_stop(data)

    sys.exit(0)


if __name__ == "__main__":
    main()
```

**پیکربندی:**
```json
{
  "hooks": {
    "UserPromptSubmit": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 \"$CLAUDE_PROJECT_DIR/.claude/hooks/context-tracker.py\""
          }
        ]
      }
    ],
    "Stop": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 \"$CLAUDE_PROJECT_DIR/.claude/hooks/context-tracker.py\""
          }
        ]
      }
    ]
  }
}
```

**نحوه کار:**
1. `UserPromptSubmit` پیش از پردازش پرامپت شما فعال می‌شود - تعداد توکن فعلی را ذخیره می‌کند
2. `Stop` پس از پاسخ Claude فعال می‌شود - اختلاف را محاسبه و مصرف را گزارش می‌کند
3. هر نشست از طریق `session_id` در نام فایل موقت جدا می‌شود

**روش‌های شمارش توکن:**

| روش | دقت | وابستگی‌ها | سرعت |
|--------|----------|--------------|-------|
| تخمین کاراکتری | حدود ۸۰ تا ۹۰ درصد | هیچ | <1ms |
| tiktoken (p50k_base) | حدود ۹۰ تا ۹۵ درصد | `pip install tiktoken` | <10ms |

> **توجه:** Anthropic توکنایزر آفلاین رسمی منتشر نکرده است. هر دو روش تقریبی هستند. رونوشت شامل پرامپت‌های کاربر، پاسخ‌های Claude و خروجی‌های ابزار است؛ از نسخه 2.1.300 پرامپت سیستم، ابزارها و پارامترهای هر درخواست API را هم ثبت می‌کند.

### مثال ۷: مقدارگذاری اولیه مجوزهای حالت خودکار (اسکریپت راه‌اندازی یک‌باره)

یک اسکریپت راه‌اندازی یک‌باره که `~/.claude/settings.json` را با قواعد مجوز ایمن معادل خط پایه حالت auto در Claude Code مقدارگذاری می‌کند — ۳۷ قاعده به‌طور پیش‌فرض، تا ۶۳ با فعال کردن همه پرچم‌های دسته — بدون هیچ هوکی، بدون به‌خاطر سپردن انتخاب‌های آینده. یک بار اجرا کنید؛ اجرای مجدد ایمن است (قواعد موجود را رد می‌کند).

**فایل:** `09-advanced-features/setup-auto-mode-permissions.py`

```bash
# پیش‌نمایش آنچه افزوده می‌شود
python3 09-advanced-features/setup-auto-mode-permissions.py --dry-run

# اعمال
python3 09-advanced-features/setup-auto-mode-permissions.py
```

**چه چیزی اضافه می‌شود:**

| دسته | مثال‌ها |
|----------|---------|
| ابزارهای داخلی | `Read(*)`، `Grep(*)`، `Agent(*)`، `WebSearch(*)` |
| ویرایش‌های اختیاری (--include-edits) | `Edit(*)` |
| خواندن گیت | `Bash(git status:*)`، `Bash(git log:*)`، `Bash(git diff:*)` |
| نوشتن گیت (محلی) | `Bash(git add:*)`، `Bash(git commit:*)`، `Bash(git checkout:*)` |
| مدیران بسته | `Bash(npm ci:*)`، `Bash(npm install:*)`، `Bash(pip install:*)`، `Bash(pip3 install:*)` |
| ساخت و تست | `Bash(make:*)`، `Bash(pytest:*)`، `Bash(go test:*)` |
| شل رایج | `Bash(ls:*)`، `Bash(cat:*)`، `Bash(find:*)` |
| GitHub CLI | `Bash(gh pr view:*)`، `Bash(gh pr create:*)`، `Bash(gh issue list:*)` |

**چه چیزی عمداً مستثنی شده است** (هرگز توسط این اسکریپت اضافه نمی‌شود):
- `rm -rf`، `sudo`، force push، `git reset --hard`
- `DROP TABLE`، `kubectl delete`، `terraform destroy`
- `npm publish`، `curl | bash`، استقرارهای عملیاتی

### مثال ۸: ثبت‌کننده پیشرفت یادگیری (SessionEnd)

در پایان هر نشست Claude Code ثبت کنید کدام ماژول‌ها را مطالعه کرده‌اید. پیشرفت در
`~/.claude-howto-progress.json` ذخیره می‌شود — بیرون از مخزن، بنابراین از `git pull` جان سالم به در می‌برد
و بازنویسی نمی‌شود.

**چرا `SessionEnd` و نه `Stop`؟**
`Stop` پس از *هر* پاسخ Claude فعال می‌شود. `SessionEnd` یک بار وقتی نشست
خاتمه می‌یابد فعال می‌شود — دقیقاً همان چیزی که برای یک یادداشت پایان نشست می‌خواهید.

**چرا پرامپت تعاملی نه؟**
هوک‌ها بدون ترمینال کنترل‌کننده اجرا می‌شوند، بنابراین `/dev/tty` در دسترس نیست و هوک نمی‌تواند
از شما سؤال بپرسد. ماژول‌ها (و یادداشت‌های اختیاری) را به‌عنوان متغیر محیطی هنگام
راه‌اندازی Claude Code بدهید، مثلاً `CLAUDE_HOWTO_MODULES=06,07 claude`.

**فایل:** `06-hooks/session-end.sh`

```bash
#!/usr/bin/env bash
# هوک SessionEnd: ماژول‌های کارشده را ثبت می‌کند، سپس یک رکورد نشست می‌افزاید
# به ~/.claude-howto-progress.json برای پیگیری پایدار پیشرفت یادگیری.

PROGRESS_FILE="$HOME/.claude-howto-progress.json"

# محافظ: فقط داخل این مخزن اجرا شود
if [[ "$CLAUDE_PROJECT_DIR" != *"claude-howto"* ]] && [[ "$PWD" != *"claude-howto"* ]]; then
  exit 0
fi

if [ ! -f "$PROGRESS_FILE" ]; then
  echo '{"sessions":[]}' > "$PROGRESS_FILE"
fi

DATE=$(date +"%Y-%m-%d")
TIME=$(date +"%H:%M")

# ماژول‌های کارشده، مثلاً با این اجرا کنید: CLAUDE_HOWTO_MODULES=06,07 claude
# 01=اسلش  02=حافظه  03=مهارت‌ها  04=زیرایجنت‌ها  05=MCP
# 06=هوک‌ها  07=پلاگین‌ها 08=چک‌پوینت‌ها 09=پیشرفته 10=CLI
INPUT="${CLAUDE_HOWTO_MODULES:-}"

if [ -z "$INPUT" ] || [ "$INPUT" = "skip" ]; then
  exit 0
fi

MODULES_JSON=$(echo "$INPUT" | tr ',' '\n' | tr -d ' ' | while read -r m; do
  case "$m" in
    01) echo '"01-slash-commands"' ;;
    02) echo '"02-memory"' ;;
    03) echo '"03-skills"' ;;
    04) echo '"04-subagents"' ;;
    05) echo '"05-mcp"' ;;
    06) echo '"06-hooks"' ;;
    07) echo '"07-plugins"' ;;
    08) echo '"08-checkpoints"' ;;
    09) echo '"09-advanced-features"' ;;
    10) echo '"10-cli"' ;;
    *)  echo "\"$m\"" ;;
  esac
done | paste -sd ',' -)

# یادداشت اختیاری، مثلاً CLAUDE_HOWTO_NOTES="نمونه pre-commit را امتحان کردم"
NOTES="${CLAUDE_HOWTO_NOTES:-}"

# NOTES را به‌عنوان آرگومان جدا بدهید تا پایتون فرار JSON را مدیریت کند —
# این کار JSON شکسته را وقتی یادداشت‌ها نقل‌قول یا بک‌اسلش دارند جلوگیری می‌کند.
python3 - "$PROGRESS_FILE" "$DATE" "$TIME" "$MODULES_JSON" "$NOTES" <<'PYEOF'
import sys, json

path, date, time_str, modules_raw, notes = sys.argv[1], sys.argv[2], sys.argv[3], sys.argv[4], sys.argv[5]

new_session = {
    "date": date,
    "time": time_str,
    "modules": json.loads(f"[{modules_raw}]") if modules_raw else [],
    "notes": notes,
}

with open(path, 'r') as f:
    data = json.load(f)

data.setdefault('sessions', []).append(new_session)

with open(path, 'w') as f:
    json.dump(data, f, indent=2)
PYEOF

echo " Saved to $PROGRESS_FILE"
```

**نصب** — اسکریپت را در دایرکتوری هوک پروژه کپی کنید تا مسیر در `settings.json` قابل حل باشد:

```bash
mkdir -p .claude/hooks
cp 06-hooks/session-end.sh .claude/hooks/
chmod +x .claude/hooks/session-end.sh
```

**پیکربندی** (در `.claude/settings.json`):

```json
{
  "hooks": {
    "SessionEnd": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "\"$CLAUDE_PROJECT_DIR/.claude/hooks/session-end.sh\"",
            "timeout": 10
          }
        ]
      }
    ]
  }
}
```

هوک‌های SessionEnd سهمیه پیش‌فرض ۱.۵ ثانیه‌ای دارند. تعیین `"timeout"` برای هر هوک (به ثانیه) سهمیه را به همان اندازه بالا می‌برد، تا حداکثر ۶۰ ثانیه؛ هوکی که `timeout` خودش را ندارد پس از ۱.۵ ثانیه لغو می‌شود.

**خروجی — `~/.claude-howto-progress.json`:**

```json
{
  "sessions": [
    {
      "date": "2026-04-18",
      "time": "14:32",
      "modules": ["06-hooks", "07-plugins"],
      "notes": "Installed first hook, tried pre-commit example"
    }
  ]
}
```

**الگوهای کلیدی نمایش‌داده‌شده:**

| الگو | چرا مهم است |
|---------|----------------|
| رویداد `SessionEnd` | یک بار هنگام خروج فعال می‌شود — نه پس از هر پاسخ مانند `Stop` |
| `INPUT="${CLAUDE_HOWTO_MODULES:-}"` | هوک‌ها ترمینال ندارند (`/dev/tty` در دسترس نیست)، بنابراین ورودی از متغیرهای محیطی می‌آید |
| `"timeout": 10` | هوک‌های SessionEnd پس از ۱.۵ ثانیه لغو می‌شوند مگر اینکه `timeout` خودشان را تعیین کنند |
| `$CLAUDE_PROJECT_DIR` | مسیر قابل حمل — هرگز `/Users/yourname/...` را سخت‌کد نکنید |
| بند محافظ در ابتدا | از اجرای هوک در پروژه‌های نامرتبط در صورت نصب سراسری جلوگیری می‌کند |
| ذخیره بیرون از مخزن | مسیر `~/` از `git pull` جان سالم به در می‌برد بدون بازنویسی داده‌های شما |

**همراه: پیگیر بصری پیشرفت**

برای یک رابط کاربری کامل مبتنی بر چک‌باکس که همه ۱۰ ماژول را پوشش می‌دهد، پیگیر همراه را در مرورگر خود باز کنید:

```bash
open local-progress/index.html
```

پیشرفت در `localStorage` مرورگر ذخیره می‌شود (هرگز روی دیسک درون مخزن نوشته نمی‌شود).
از دکمه **Export** برای ذخیره یک تصویر به‌صورت JSON و از **Import** برای بازیابی آن استفاده کنید.

## هوک‌های پلاگین

پلاگین‌ها می‌توانند هوک‌ها را در فایل `hooks/hooks.json` خود بگنجانند:

**فایل:** `plugins/hooks/hooks.json`

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "\"${CLAUDE_PLUGIN_ROOT}\"/scripts/validate.sh"
          }
        ]
      }
    ]
  }
}
```

**متغیرهای محیطی در هوک‌های پلاگین:**
- `${CLAUDE_PLUGIN_ROOT}` - مسیر دایرکتوری پلاگین
- `${CLAUDE_PLUGIN_DATA}` - مسیر دایرکتوری داده پلاگین

این به پلاگین‌ها اجازه می‌دهد هوک‌های اعتبارسنجی و خودکارسازی سفارشی داشته باشند.

## هوک‌های ابزار MCP

ابزارهای MCP از الگوی `mcp__<server>__<tool>` پیروی می‌کنند:

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "mcp__memory__.*",
        "hooks": [
          {
            "type": "command",
            "command": "echo '{\"systemMessage\": \"Memory operation logged\"}'"
          }
        ]
      }
    ]
  }
}
```

## ملاحظات امنیتی

### سلب مسئولیت

**با مسئولیت خودتان استفاده کنید**: هوک‌ها دستورات شل دلخواه اجرا می‌کنند. شما به‌تنهایی مسئول موارد زیر هستید:
- دستوراتی که پیکربندی می‌کنید
- مجوزهای دسترسی/تغییر فایل
- از دست رفتن احتمالی داده یا آسیب به سیستم
- تست هوک‌ها در محیط‌های ایمن پیش از استفاده در محیط عملیاتی

### نکات امنیتی

- **نیازمند اعتماد به فضای کاری:** دستورات خروجی هوک‌های `statusLine` و `fileSuggestion` اکنون پیش از اعمال، نیازمند پذیرش اعتماد فضای کاری هستند.
- **اندازه ترمینال خط وضعیت (نسخه 2.1.153):** اسکریپت‌های دستور خط وضعیت اکنون متغیرهای محیطی `COLUMNS` و `LINES` را دریافت می‌کنند، بنابراین اسکریپت می‌تواند خروجی خود را با عرض/ارتفاع ترمینال سازگار کند (مثلاً `[ "$COLUMNS" -lt 80 ] && short_output`).
- **هوک‌های HTTP و متغیرهای محیطی:** هوک‌های HTTP برای استفاده از جایگذاری متغیر محیطی در مقادیر هدر، نیازمند فهرست صریح `allowedEnvVars` هستند. این از افشای تصادفی متغیرهای محیطی حساس به نقاط پایانی از راه دور جلوگیری می‌کند.
- **سلسله‌مراتب تنظیمات مدیریت‌شده:** تنظیم `disableAllHooks` اکنون به سلسله‌مراتب تنظیمات مدیریت‌شده احترام می‌گذارد، یعنی تنظیمات سطح سازمان می‌تواند غیرفعال‌سازی هوک را الزام کند که کاربران عادی نمی‌توانند آن را بازنویسی کنند.
- **تأیید خودکار PowerShell (نسخه 2.1.119):** دستورات ابزار PowerShell می‌توانند در حالت مجوز به‌طور خودکار تأیید شوند، مانند Bash. این برابری را برای کاربران Windows که Claude Code را با ابزارهای شل مبتنی بر PowerShell اجرا می‌کنند فراهم می‌کند.
- **بسته شدن تأیید خودکار متغیر محیطی صرف در Bash (نسخه 2.1.145):** پیش از نسخه 2.1.145، یک دستور Bash به شکل `FOO=bar somecommand` (یک تخصیص متغیر صرف درون‌خطی با یک دستور غیرمجاز) می‌توانست وقتی فقط `FOO=bar` به‌تنهایی در فهرست مجاز بود، به‌طور خودکار تأیید شود. نسخه 2.1.145 این را می‌بندد — چنین دستوراتی اکنون به پرامپت مجوز می‌خورند. اسکریپت‌هایی که به این مجازبودن ضمنی تکیه می‌کنند شروع به پرسش خواهند کرد؛ آن‌ها را صریحاً با یک قاعده مجوز `Bash(...)` که کل دستور را پوشش می‌دهد (نه فقط تخصیص متغیر) دوباره مجاز کنید.

### بهترین شیوه‌ها

| انجام دهید | انجام ندهید |
|-----|-------|
| همه ورودی‌ها را اعتبارسنجی و پاکسازی کنید | کورکورانه به داده ورودی اعتماد کنید |
| متغیرهای شل را نقل‌قول کنید: `"$VAR"` | بدون نقل‌قول استفاده کنید: `$VAR` |
| پیمایش مسیر (`..`) را مسدود کنید | مسیرهای دلخواه را مجاز کنید |
| از مسیرهای مطلق با `$CLAUDE_PROJECT_DIR` استفاده کنید | مسیرها را سخت‌کد کنید |
| فایل‌های حساس (`.env`، `.git/`، کلیدها) را رد کنید | همه فایل‌ها را پردازش کنید |
| ابتدا هوک‌ها را جداگانه تست کنید | هوک‌های تست‌نشده را مستقر کنید |
| برای هوک‌های HTTP از `allowedEnvVars` صریح استفاده کنید | همه متغیرهای محیطی را به webhookها افشا کنید |

## اشکال‌زدایی

### فعال‌سازی حالت اشکال‌زدایی

Claude را با پرچم اشکال‌زدایی برای لاگ‌های تفصیلی هوک اجرا کنید:

```bash
claude --debug
```

### حالت پرگو

در Claude Code از `Ctrl+O` برای فعال‌سازی حالت پرگو و مشاهده پیشرفت اجرای هوک استفاده کنید.

### تست مستقل هوک‌ها

```bash
# آزمایش با ورودی JSON نمونه
echo '{"tool_name": "Bash", "tool_input": {"command": "ls -la"}}' | python3 .claude/hooks/validate-bash.py

# بررسی کد خروج
echo $?
```

## نمونه پیکربندی کامل

```json
{
  "hooks": {
    "PreToolUse": [
      {
        "matcher": "Bash",
        "hooks": [
          {
            "type": "command",
            "command": "python3 \"$CLAUDE_PROJECT_DIR/.claude/hooks/validate-bash.py\"",
            "timeout": 10
          }
        ]
      }
    ],
    "PostToolUse": [
      {
        "matcher": "Write|Edit",
        "hooks": [
          {
            "type": "command",
            "command": "\"$CLAUDE_PROJECT_DIR/.claude/hooks/format-code.sh\"",
            "timeout": 30
          },
          {
            "type": "command",
            "command": "python3 \"$CLAUDE_PROJECT_DIR/.claude/hooks/security-scan.py\"",
            "timeout": 10
          }
        ]
      }
    ],
    "UserPromptSubmit": [
      {
        "hooks": [
          {
            "type": "command",
            "command": "python3 \"$CLAUDE_PROJECT_DIR/.claude/hooks/validate-prompt.py\""
          }
        ]
      }
    ],
    "SessionStart": [
      {
        "matcher": "startup",
        "hooks": [
          {
            "type": "command",
            "command": "\"$CLAUDE_PROJECT_DIR/.claude/hooks/session-init.sh\""
          }
        ]
      }
    ],
    "Stop": [
      {
        "hooks": [
          {
            "type": "prompt",
            "prompt": "Verify all tasks are complete before stopping.",
            "timeout": 30
          }
        ]
      }
    ]
  }
}
```

## جزئیات اجرای هوک

| جنبه | رفتار |
|--------|----------|
| **مهلت زمانی** | پیش‌فرض ۶۰۰ ثانیه برای command/http/mcp_tool (۳۰ برای prompt، ۶۰ برای agent)؛ قابل پیکربندی برای هر هوک |
| **موازی‌سازی** | همه هوک‌های منطبق به‌طور موازی اجرا می‌شوند؛ از نسخه 2.1.302 حداکثر ۱۲ هوک prompt یا agent از یک رویداد هم‌زمان اجرا می‌شوند و بقیه نوبت خود را انتظار می‌کشند. |
| **حذف تکراری** | دستورات هوک یکسان حذف تکراری می‌شوند |
| **محیط** | در دایرکتوری جاری با محیط Claude Code اجرا می‌شود |

## عیب‌یابی

### هوک اجرا نمی‌شود
- تأیید کنید نحو پیکربندی JSON درست است
- بررسی کنید الگوی matcher با نام ابزار مطابقت دارد
- مطمئن شوید اسکریپت وجود دارد و قابل اجراست: `chmod +x script.sh`
- `claude --debug` را برای دیدن لاگ‌های اجرای هوک اجرا کنید
- تأیید کنید هوک JSON را از stdin می‌خواند (نه از آرگومان‌های دستور)

### هوک به‌طور غیرمنتظره مسدود می‌کند
- هوک را با JSON نمونه تست کنید: `echo '{"tool_name": "Write", ...}' | ./hook.py`
- کد خروج را بررسی کنید: برای مجاز بودن باید ۰ و برای مسدودسازی ۲ باشد
- خروجی stderr را بررسی کنید (در کد خروج ۲ نمایش داده می‌شود)

### خطاهای تجزیه JSON
- همیشه از stdin بخوانید، نه از آرگومان‌های دستور
- از تجزیه صحیح JSON استفاده کنید (نه دستکاری رشته)
- فیلدهای غایب را به‌صورت محترمانه مدیریت کنید

## نصب

### گام ۱: ایجاد دایرکتوری هوک‌ها
```bash
mkdir -p ~/.claude/hooks
```

### گام ۲: کپی هوک‌های نمونه
```bash
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh
```

### گام ۳: پیکربندی در تنظیمات
`~/.claude/settings.json` یا `.claude/settings.json` را با پیکربندی هوک نشان‌داده‌شده در بالا ویرایش کنید.

## مفاهیم مرتبط

- **[چک‌پوینت‌ها و بازگردانی](../08-checkpoints/)** - ذخیره و بازیابی وضعیت گفتگو
- **[دستورات اسلش](../01-slash-commands/)** - ساخت دستورات اسلش سفارشی
- **[مهارت‌ها](../03-skills/)** - قابلیت‌های خودمختار قابل استفاده مجدد
- **[زیرایجنت‌ها](../04-subagents/)** - اجرای واگذارشده وظایف
- **[پلاگین‌ها](../07-plugins/)** - بسته‌های افزونه بسته‌بندی‌شده
- **[ویژگی‌های پیشرفته](../09-advanced-features/)** - بررسی قابلیت‌های پیشرفته Claude Code

## منابع بیشتر

- **[مستندات رسمی هوک‌ها](https://code.claude.com/docs/en/hooks)** - مرجع کامل هوک‌ها
- **[مرجع CLI](https://code.claude.com/docs/en/cli-reference)** - مستندات رابط خط فرمان
- **[راهنمای حافظه](../02-memory/)** - پیکربندی زمینه پایدار

---

**آخرین به‌روزرسانی**: ۲۶ اکتبر ۲۰۲۶
**نسخه Claude Code**: 2.1.310
**منابع**:
- https://code.claude.com/docs/en/hooks
- https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
- https://code.claude.com/docs/en/sub-agents
- https://code.claude.com/docs/en/permissions
- https://code.claude.com/docs/en/tools-reference#task-tool-availability
- https://code.claude.com/docs/en/plugins/manifest-reference#quoting-and-path-separators
- https://github.com/anthropics/claude-code/releases/tag/v2.1.295
- https://code.claude.com/docs/en/hooks#pretooluse
- https://code.claude.com/docs/en/hooks#pretooluse-decision-control
- https://code.claude.com/docs/en/hooks#hook-lifecycle
- https://code.claude.com/docs/en/hooks#userpromptsubmit-input
- https://code.claude.com/docs/en/changelog#2-1-299
- https://code.claude.com/docs/en/changelog#2-1-300
- https://code.claude.com/docs/en/changelog#2-1-301
- https://code.claude.com/docs/en/changelog#2-1-302
- https://code.claude.com/docs/en/hooks#defer-a-tool-call-for-later
- https://code.claude.com/docs/en/hooks-guide#limitations
- https://code.claude.com/docs/en/hooks#notification
- https://code.claude.com/docs/en/changelog#2-1-304
- https://code.claude.com/docs/en/hooks#limits-on-skill-hooks
- https://code.claude.com/docs/en/changelog#2-1-309
- https://code.claude.com/docs/en/hooks#failed-hooks-on-windows-without-git-bash
**مدل‌های سازگار**: Claude Fable 5، Claude Opus 5، Claude Sonnet 5، Claude Sonnet 4.6، Claude Opus 4.8، Claude Haiku 4.5
