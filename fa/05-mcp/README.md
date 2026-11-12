<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../../resources/logos/claude-howto-logo.svg">
</picture>

# MCP (پروتکل زمینهٔ مدل)

این پوشه شامل مستندات و نمونه‌های جامع برای پیکربندی و استفاده از سرورهای MCP در Claude Code است.

## نمای کلی

MCP (پروتکل زمینهٔ مدل) روشی استاندارد برای دسترسی Claude به ابزارهای خارجی، APIها و منابع دادهٔ بلادرنگ است. برخلاف حافظه، MCP دسترسی زنده به داده‌های در حال تغییر را فراهم می‌کند.

ویژگی‌های کلیدی:
- دسترسی بلادرنگ به سرویس‌های خارجی
- همگام‌سازی زندهٔ داده‌ها
- معماری قابل‌گسترش
- احراز هویت امن
- تعاملات مبتنی بر ابزار

## معماری MCP

```mermaid
graph TB
    A["Claude"]
    B["سرور MCP"]
    C["سرویس خارجی"]

    A -->|درخواست: list_issues| B
    B -->|پرس‌وجو| C
    C -->|داده| B
    B -->|پاسخ| A

    A -->|درخواست: create_issue| B
    B -->|اقدام| C
    C -->|نتیجه| B
    B -->|پاسخ| A

    style A fill:#e1f5fe,stroke:#333,color:#333
    style B fill:#f3e5f5,stroke:#333,color:#333
    style C fill:#e8f5e9,stroke:#333,color:#333
```

## اکوسیستم MCP

```mermaid
graph TB
    A["Claude"] -->|MCP| B["فایل‌سیستم<br/>سرور MCP"]
    A -->|MCP| C["GitHub<br/>سرور MCP"]
    A -->|MCP| D["پایگاه‌داده<br/>سرور MCP"]
    A -->|MCP| E["Slack<br/>سرور MCP"]
    A -->|MCP| F["Google Docs<br/>سرور MCP"]

    B -->|ورودی/خروجی فایل| G["فایل‌های محلی"]
    C -->|API| H["مخازن GitHub"]
    D -->|پرس‌وجو| I["PostgreSQL/MySQL"]
    E -->|پیام‌ها| J["فضای کاری Slack"]
    F -->|مستندات| K["Google Drive"]

    style A fill:#e1f5fe,stroke:#333,color:#333
    style B fill:#f3e5f5,stroke:#333,color:#333
    style C fill:#f3e5f5,stroke:#333,color:#333
    style D fill:#f3e5f5,stroke:#333,color:#333
    style E fill:#f3e5f5,stroke:#333,color:#333
    style F fill:#f3e5f5,stroke:#333,color:#333
    style G fill:#e8f5e9,stroke:#333,color:#333
    style H fill:#e8f5e9,stroke:#333,color:#333
    style I fill:#e8f5e9,stroke:#333,color:#333
    style J fill:#e8f5e9,stroke:#333,color:#333
    style K fill:#e8f5e9,stroke:#333,color:#333
```

## روش‌های نصب MCP

Claude Code از چندین پروتکل انتقال برای اتصال به سرورهای MCP پشتیبانی می‌کند:

### انتقال HTTP (توصیه‌شده)

```bash
# اتصال پایه HTTP
claude mcp add --transport http notion https://mcp.notion.com/mcp

# HTTP همراه با سرآیند احراز هویت
claude mcp add --transport http secure-api https://api.example.com/mcp \
  --header "Authorization: Bearer your-token"
```

### انتقال Stdio (محلی)

برای سرورهای MCP که به‌صورت محلی اجرا می‌شوند:

```bash
# سرور محلی Node.js
claude mcp add --transport stdio myserver -- npx @myorg/mcp-server

# همراه با متغیرهای محیطی
claude mcp add --transport stdio myserver --env KEY=value -- npx server
```

#### `CLAUDE_PROJECT_DIR` برای سرورهای stdio (v2.1.139+)

هر سرور stdio مربوط به MCP در حالی اجرا می‌شود که `CLAUDE_PROJECT_DIR=<مسیر مطلق ریشهٔ مخزن>` از قبل در محیط آن تنظیم شده است — همان قراردادی که برای هوک‌ها به کار می‌رود. فایل‌های `.mcp.json` پلاگین و پروژه می‌توانند در مقادیر `command`، `args` و `env` به `${CLAUDE_PROJECT_DIR}` ارجاع دهند و جای‌گذاری پیش از `execve()` انجام می‌شود:

```json
{
  "mcpServers": {
    "repo-tools": {
      "type": "stdio",
      "command": "node",
      "args": ["${CLAUDE_PROJECT_DIR:-.}/.claude/mcp/repo-tools.js"],
      "env": {
        "REPO_ROOT": "${CLAUDE_PROJECT_DIR:-.}"
      }
    }
  }
}
```

> **توجه**: در پیکربندی‌های پروژه، محلی و کاربر، `${CLAUDE_PROJECT_DIR:-.}` را همراه با یک مقدار پیش‌فرض بنویسید: این متغیر در محیط سرور تنظیم می‌شود، نه در محیط خود Claude Code. تنها پیکربندی‌های MCP پلاگین‌ها `${CLAUDE_PROJECT_DIR}` را مستقیماً جای‌گذاری می‌کنند.

از این امکان استفاده کنید وقتی سرور stdio شما باید فایل‌ها را نسبت به ریشهٔ پروژه بخواند، صرف‌نظر از این‌که Claude Code از کجا اجرا شده است.

سرورهای stdio مربوط به MCP همچنین `CLAUDE_CODE_SESSION_ID` را دریافت می‌کنند (همان مقداری که به هوک‌ها و Bash داده می‌شود)، از جمله زمانی که نشست با `--resume` از سر گرفته شود (v2.1.163+).

### انتقال SSE (منسوخ)

انتقال Server-Sent Events به نفع `http` منسوخ شده است، اما هنوز پشتیبانی می‌شود:

```bash
claude mcp add --transport sse legacy-server https://example.com/sse
```

### انتقال WebSocket (`ws`)

سرورهای WebSocket یک اتصال پایدار و دوسویه نگه می‌دارند که برای سرورهای MCP راهدور که رویدادها را بدون درخواست به Claude هل می‌دهند مناسب است. اگر سرور شما فقط به درخواست‌ها پاسخ می‌دهد، به‌جای آن از HTTP استفاده کنید، چون HTTP از OAuth و پرچم `claude mcp add --transport` پشتیبانی می‌کند، در حالی که WebSocket از هیچ‌کدام پشتیبانی نمی‌کند.

از آنجا که `--transport` مقدار `ws` را نمی‌پذیرد، آن را در `.mcp.json` یا از طریق `claude mcp add-json` پیکربندی کنید:

```json
{
  "type": "ws",
  "url": "wss://mcp.example.com/socket",
  "headers": {
    "Authorization": "Bearer YOUR_TOKEN"
  }
}
```

ورودی `type: "ws"` همان فیلدهای `url`، `headers`، `headersHelper`، `timeout` و `alwaysLoad` را مانند `http` می‌پذیرد. احراز هویت **فقط از طریق سرآیند** انجام می‌شود — هیچ جریان OAuth برای سرورهای WebSocket وجود ندارد.

> **توجه**: از نسخهٔ v2.1.285، دستور `claude mcp list` سرورهای WebSocket (`ws`) را همراه با URL و وضعیت سلامت آن‌ها فهرست می‌کند (نسخه‌های پیشین آن‌ها را نشان نمی‌دادند). می‌توانید آن‌ها را با `claude mcp get <name>` یا پنل `/mcp` نیز بررسی کنید.

مانند HTTP و SSE، اتصال‌های WebSocket از پنجرهٔ بی‌کاری ۵ دقیقه‌ای استفاده می‌کنند؛ stdio و WebSocket هیچ تایمری برای هر درخواست ندارند. ورودی `url` بدون `type` خطایی است که `"http"`، `"sse"` و `"ws"` را به‌عنوان مقادیر معتبر نام می‌برد.

### پوشه‌های کاری نشست (roots/list)

سرورهای MCP می‌توانند پوشه‌های کاری نشست را کشف کنند: پوشهٔ اجرا به‌همراه همهٔ ورودی‌های `--add-dir`/`additionalDirectories` از طریق درخواست `roots/list` مربوط به MCP بازگردانده می‌شوند و هر بار که این مجموعه تغییر کند، اعلان `notifications/roots/list_changed` فرستاده می‌شود (v2.1.203). مهلت بی‌کاری اکنون برای سرورهای stdio نیز اعمال می‌شود (۳۰ دقیقه)، و `timeout` هر سرور به‌عنوان کف بی‌کاری عمل می‌کند (v2.1.203).

### نکتهٔ ویژهٔ Windows

در Windows بومی (نه WSL)، برای دستورهای npx از `cmd /c` استفاده کنید:

```bash
claude mcp add --transport stdio my-server -- cmd /c npx -y @some/package
```

### احراز هویت OAuth 2.0

Claude Code از OAuth 2.0 برای سرورهای MCP که به آن نیاز دارند پشتیبانی می‌کند. هنگام اتصال به سروری با پشتیبانی OAuth، Claude Code کل جریان احراز هویت را مدیریت می‌کند:

```bash
# اتصال به سرور MCP دارای OAuth (جریان تعاملی)
claude mcp add --transport http my-service https://my-service.example.com/mcp

# پیش‌پیکربندی اعتبارنامه‌های OAuth برای راه‌اندازی غیرتعاملی
claude mcp add --transport http my-service https://my-service.example.com/mcp \
  --client-id "your-client-id" \
  --client-secret "your-client-secret" \
  --callback-port 8080
```

| ویژگی | توضیح |
|---------|-------------|
| **OAuth تعاملی** | برای راه‌اندازی جریان OAuth مبتنی بر مرورگر از `/mcp` استفاده کنید |
| **کلاینت‌های OAuth از پیش پیکربندی‌شده** | کلاینت‌های OAuth داخلی برای سرویس‌های رایج مانند Notion، Stripe و دیگران (v2.1.30+) |
| **اعتبارنامه‌های از پیش پیکربندی‌شده** | پرچم‌های `--client-id`، `--client-secret` و `--callback-port` برای راه‌اندازی خودکار |
| **ذخیره‌سازی توکن** | توکن‌ها به‌صورت امن در زنجیرهٔ کلید سیستم شما ذخیره می‌شوند |
| **احراز هویت پله‌ای** | از احراز هویت پله‌ای برای عملیات ممتاز پشتیبانی می‌کند |
| **کش کردن کشف** | فرادادهٔ کشف OAuth برای اتصال مجدد سریع‌تر کش می‌شود |
| **بازنویسی فراداده** | `oauth.authServerMetadataUrl` در `.mcp.json` برای بازنویسی کشف پیش‌فرض فرادادهٔ OAuth |

#### بازنویسی کشف فرادادهٔ OAuth

اگر سرور MCP شما روی نقطهٔ پایانی استاندارد فرادادهٔ OAuth (`/.well-known/oauth-authorization-server`) خطا برمی‌گرداند اما یک نقطهٔ پایانی OIDC کارآمد ارائه می‌دهد، می‌توانید به Claude Code بگویید فرادادهٔ OAuth را از یک URL مشخص واکشی کند. `authServerMetadataUrl` را در شیء `oauth` پیکربندی سرور خود تنظیم کنید:

```json
{
  "mcpServers": {
    "my-server": {
      "type": "http",
      "url": "https://mcp.example.com/mcp",
      "oauth": {
        "authServerMetadataUrl": "https://auth.example.com/.well-known/openid-configuration"
      }
    }
  }
}
```

URL باید از `https://` استفاده کند. این گزینه به Claude Code نسخهٔ v2.1.64 یا بالاتر نیاز دارد.

#### اعلان احراز هویت هنگام شروع و بازتازه‌سازی سرآیند پویا (v2.1.193)

- **اعلان احراز هویت هنگام شروع (v2.1.193+)**: هنگام شروع، Claude Code اعلانی نمایش می‌دهد که هر سرور MCP نیازمند احراز هویت را فهرست می‌کند، تا سروری که به ورود نیاز دارد بی‌صدا از کار نیفتد.
- **بازتازه‌سازی خودکار `headersHelper` (v2.1.193+)**: اگر احراز هویت سفارشی را از طریق `headersHelper` ارائه دهید، هر زمان سروری HTTP 401 یا 403 برگرداند، این کمک‌کننده به‌طور خودکار دوباره فراخوانی می‌شود. اعتبارنامه‌ها بدون اتصال مجدد دستی و در همان لحظه بازتازه می‌شوند. [استفاده از سرآیندهای پویا برای احراز هویت سفارشی](https://code.claude.com/docs/en/mcp) را ببینید.

> **هشدار** (v2.1.238): یک `headersHelper` در `.mcp.json` پروژه، و سرورهای MCP درون‌خطی در فایل‌های ایجنت پروژه یا `--add-dir`، اکنون نیازمند پذیرفته‌شدن گفت‌وگوی اعتماد آن پوشه هستند — از جمله زیر `claude -p`. چنین کمک‌کننده‌هایی همچنین **بدون متغیرهای محیطی اعتبارنامهٔ ارث‌رسیده** اجرا می‌شوند؛ کمک‌کننده‌های محدودهٔ کاربر، مدیریت‌شده و claude.ai در عوض از پوشهٔ پیکربندی Claude اجرا می‌شوند. پیکربندی پروژه‌ای که به اعتبارنامه‌های ارث‌رسیده یا اجرای بدون اعتماد تکیه کرده باشد، تا زمانی که گفت‌وگوی اعتماد را نپذیرید و اعتبارنامه را به روشی دیگر تأمین نکنید، از کار می‌افتد.

### کانکتورهای MCP در Claude.ai

سرورهای MCP پیکربندی‌شده در حساب Claude.ai شما به‌طور خودکار در Claude Code در دسترس هستند. این یعنی هر اتصال MCP که از طریق رابط وب Claude.ai ایجاد کرده‌اید، بدون پیکربندی اضافی قابل دسترسی خواهد بود.

کانکتورهای MCP در Claude.ai در حالت `--print` نیز در دسترس هستند (v2.1.83+)، که استفادهٔ غیرتعاملی و اسکریپتی را ممکن می‌کند.

> **نکتهٔ شروع (v2.1.117+):** وقتی هم سرورهای MCP محلی و هم claude.ai پیکربندی شده باشند، اتصال هم‌زمان حالت پیش‌فرض است (پیش‌تر سریالی بود) و تأخیر شروع را هنگام استفاده از چندین سرور کاهش می‌دهد.

برای غیرفعال‌کردن سرورهای MCP در Claude.ai در Claude Code، متغیر محیطی `ENABLE_CLAUDEAI_MCP_SERVERS` را روی `false` تنظیم کنید:

```bash
ENABLE_CLAUDEAI_MCP_SERVERS=false claude
```

> **توجه:** این ویژگی فقط برای کاربرانی در دسترس است که با حساب‌های Claude.ai وارد شده‌اند.

## فرایند راه‌اندازی MCP

```mermaid
sequenceDiagram
    participant User
    participant Claude as Claude Code
    participant Config as فایل پیکربندی
    participant Service as سرویس خارجی

    User->>Claude: /mcp را تایپ کنید
    Claude->>Claude: فهرست سرورهای MCP موجود
    Claude->>User: نمایش گزینه‌ها
    User->>Claude: انتخاب GitHub MCP
    Claude->>Config: به‌روزرسانی پیکربندی
    Config->>Claude: فعال‌سازی اتصال
    Claude->>Service: آزمون اتصال
    Service-->>Claude: احراز هویت موفق
    Claude->>User: ✅ MCP متصل شد!
```

### دستور `/mcp`

برای فهرست‌کردن سرورهای متصل، راه‌اندازی جریان‌های OAuth و بررسی وضعیت اتصال، درون یک نشست `/mcp` را تایپ کنید.

- از **v2.1.121**، MCP اتصال اولیه را در صورت خطاهای گذرا تا ۳ بار دوباره تلاش می‌کند.
- از **v2.1.128**، دستور `/mcp` **تعداد ابزار** هر سرور متصل را نمایش می‌دهد و سرورهایی را که **۰ ابزار** گزارش می‌کنند به‌صورت بصری علامت می‌زند تا سرورهای بدپیکربندی در یک نگاه مشخص شوند.

## جست‌وجوی ابزار MCP

جست‌وجوی ابزار به‌طور پیش‌فرض فعال است: ابزارهای MCP به تعویق می‌افتند و در صورت نیاز کشف می‌شوند، بنابراین تعریف‌های آن‌ها زمینهٔ مدل را پر نمی‌کند. از v2.1.304 پشت یک دروازهٔ سفارشی `ANTHROPIC_BASE_URL` نیز روشن می‌ماند؛ آن دروازه باید فیلدهای ابزار `defer_loading` و بلوک‌های `tool_reference` را منتقل کند. از v2.1.305، Claude Code درخواستی را که دروازه با 400 یا 422 رد کند بدون جست‌وجوی ابزار دوباره تلاش می‌کند. برای بارگذاری همهٔ ابزارها از ابتدا و رد نکردن آن درخواست‌ها، `ENABLE_TOOL_SEARCH=false` را تنظیم کنید. پیش از v2.1.304، جست‌وجوی ابزار پشت یک دروازه خاموش بود مگر اینکه `ENABLE_TOOL_SEARCH` روی `true`، `auto` یا `auto:N` باشد.

| تنظیم | مقدار | توضیح |
|---------|-------|-------------|
| `ENABLE_TOOL_SEARCH` | (تنظیم‌نشده — پیش‌فرض) | همهٔ ابزارهای MCP به تعویق می‌افتند و در صورت نیاز بارگذاری می‌شوند |
| `ENABLE_TOOL_SEARCH` | `auto` | حالت آستانه: ابزارها از ابتدا بارگذاری می‌شوند تا تعریف‌هایشان به ۱۰٪ پنجرهٔ زمینه برسد، سپس همه به تعویق می‌افتند |
| `ENABLE_TOOL_SEARCH` | `auto:<N>` | حالت آستانه با درصد سفارشی (۰-۱۰۰) — برای نمونه `auto:5` برای ۵٪ |
| `ENABLE_TOOL_SEARCH` | `true` | همهٔ ابزارهای MCP به تعویق می‌افتند |
| `ENABLE_TOOL_SEARCH` | `false` | غیرفعال؛ همهٔ توضیحات ابزارها به‌طور کامل فرستاده می‌شوند |

> **توجه:** جست‌وجوی ابزار به مدلی نیاز دارد که از بلوک‌های `tool_reference` پشتیبانی کند: Claude Opus 4، Claude Sonnet 4، Claude Haiku 4.5 و مدل‌های بعدی (Opus 4.5، Sonnet 4.5، Haiku 4.5 و بعدی در Agent Platform گوگل کلاد).

### دور زدن جست‌وجوی ابزار برای هر سرور (v2.1.121+)

اگر ابزارهای یک سرور MCP خاص در هر نوبت لازم است، پیکربندی آن را
با `"alwaysLoad": true` علامت بزنید تا از تعویق جست‌وجوی ابزار صرف‌نظر شود و
ابزارهای آن همیشه در دسترس بمانند:

```json
{
  "mcpServers": {
    "always-on-tool": {
      "command": "node",
      "args": ["./tools/always.js"],
      "alwaysLoad": true
    }
  }
}
```

این کار را کم استفاده کنید — هر ابزار همیشه‌بارگذاری‌شده زمینه‌ای مصرف می‌کند که
در غیر این صورت می‌توانست برای جست‌وجوی ابزار جهت نمایش ابزاری مرتبط‌تر به کار رود.

برای این‌که همهٔ ابزارهای یک سرور پشت جست‌وجوی ابزار بمانند،
`"alwaysLoad": false` را در ورودی آن سرور تنظیم کنید (v2.1.287+). این شامل
ابزارهایی هم می‌شود که نویسندهٔ سرور برای بارگذاری از ابتدا علامت زده است؛ اگر
`alwaysLoad` را حذف کنید، آن ابزارهای علامت‌خورده از ابتدا بارگذاری می‌شوند. نویسندگان سرور
یک ابزار را با تنظیم `"anthropic/alwaysLoad"` در شیء
`_meta` آن ابزار علامت می‌زنند و تنظیم `alwaysLoad` در سطح سرور در
پیکربندی شما می‌تواند آن را بازنویسی کند.

نویسندگان سرور: ابزارهایی را که فراخوانی دوباره‌شان ایمن است، با حاشیه‌نویسی `idempotentHint` یا `readOnlyHint` در ورودی `tools/list` آن‌ها علامت بزنید. از v2.1.307، Claude Code فراخوانی‌ای را که هنگام بسته شدن یک اتصال HTTP یا کانکتور claude.ai در انتظار بود فقط برای همان ابزارها تکرار می‌کند؛ فراخوانی‌های دیگر با `connection closed before the tool call was answered` شکست می‌خورند.

## به‌روزرسانی‌های پویای ابزار

Claude Code از اعلان‌های `list_changed` مربوط به MCP پشتیبانی می‌کند. وقتی یک سرور MCP ابزارهای موجود خود را به‌صورت پویا اضافه، حذف یا تغییر می‌دهد، Claude Code به‌روزرسانی را دریافت می‌کند و فهرست ابزارهای خود را به‌طور خودکار تنظیم می‌کند -- بدون نیاز به اتصال مجدد یا راه‌اندازی دوباره.

## اپ‌های MCP

MCP Apps نخستین افزونهٔ رسمی MCP است که امکان می‌دهد فراخوانی‌های ابزار MCP مؤلفه‌های رابط کاربری تعاملی را برگردانند که مستقیماً در رابط گفتگو رندر می‌شوند. سرورهای MCP به‌جای پاسخ‌های متنی ساده می‌توانند داشبوردهای غنی، فرم‌ها، مصورسازی داده‌ها و گردش‌کارهای چندمرحله‌ای ارائه دهند -- همه به‌صورت درون‌خطی و بدون خروج از گفتگو نمایش داده می‌شوند.

## دریافت ورودی از کاربر در MCP

سرورهای MCP می‌توانند ورودی ساختاریافته را از کاربر از طریق گفت‌وگوهای تعاملی درخواست کنند (v2.1.49+). این امکان به سرور MCP اجازه می‌دهد در میانهٔ گردش‌کار اطلاعات بیشتری بخواهد -- برای نمونه درخواست تأیید، انتخاب از فهرستی از گزینه‌ها یا پر کردن فیلدهای الزامی -- و به این ترتیب تعاملات سرور MCP را تعاملی‌تر می‌کند.

## سقف توضیح ابزار و دستورالعمل‌ها

Claude Code توضیح هر ابزار MCP و دستورالعمل‌های هر سرور را کوتاه می‌کند تا سرورهای پرگو زمینه را متورم نکنند. محدودیت‌های پیش‌فرض **۴٬۰۹۶ نویسه** برای دستورالعمل‌های سرور و برای توضیحات ابزارهایی است که از ابتدا بارگذاری می‌شوند (v2.1.296؛ تا پیش از آن ۲٬۰۴۸ از v2.1.84)، و **۱۶٬۳۸۴ نویسه** برای توضیحاتی که Claude از طریق جست‌وجوی ابزار بارگذاری می‌کند (v2.1.295). از v2.1.280، متغیر `CLAUDE_CODE_MAX_MCP_DESCRIPTION_LENGTH` این‌ها را بازنویسی می‌کند: عددی که تنظیم می‌کنید جای **هر دو** محدودیت را می‌گیرد (`8192` کوتاه‌تر را بالا و بلندتر را پایین می‌آورد). از v2.1.299، توضیحات و دستورالعمل‌های سرورهای MCP طرف اول Anthropic در `api.anthropic.com` به‌طور کامل به Claude می‌رسند. جزئیات حیاتی را نزدیک ابتدای توضیح قرار دهید.

## پرامپت‌های MCP به‌صورت دستورهای اسلش

سرورهای MCP می‌توانند پرامپت‌هایی ارائه دهند که در Claude Code به‌صورت دستورهای اسلش نمایش داده می‌شوند. این پرامپت‌ها با قرارداد نام‌گذاری زیر در دسترس هستند:

```
/mcp__<server>__<prompt>
```

برای نمونه، اگر سروری با نام `github` پرامپتی به نام `review` ارائه دهد، می‌توانید آن را به‌صورت `/mcp__github__review` فراخوانی کنید.

## حذف تکراری‌های سرور

وقتی همان سرور MCP در چند محدوده (محلی، پروژه، کاربر) تعریف شده باشد، پیکربندی محلی اولویت دارد. این امکان به شما می‌دهد تنظیمات MCP در سطح پروژه یا سطح کاربر را با سفارشی‌سازی‌های محلی و بدون تعارض بازنویسی کنید.

## اصلاحات اخیر چرخهٔ عمر (v2.1.136)

دو باگ دیرینهٔ چرخهٔ عمر MCP در v2.1.136 رفع شد — اگر راه‌اندازی چندسروری دارید، ارتقا به این نسخه ارزشش را دارد:

- **ماندگاری سرورهای MCP پس از `/clear`**: سرورهایی که از طریق `.mcp.json`، پلاگین‌ها یا کانکتورهای claude.ai پیکربندی شده‌اند دیگر پس از `/clear` در VS Code، JetBrains یا Agent SDK ناپدید نمی‌شوند. نسخه‌های پیشین آن‌ها را بی‌صدا حذف می‌کردند و نیاز به راه‌اندازی دوباره بود.
- **رفع بازتازه‌سازی هم‌زمان توکن‌های تازه‌سازی در OAuth**: راه‌اندازی‌های چندسروری OAuth دیگر توکن‌های تازه‌سازی را زمانی که چند سرور هم‌زمان برای بازتازه‌سازی با هم رقابت می‌کنند از دست نمی‌دهند. این کار الگوی «هر روز صبح باید دوباره احراز هویت کنم» را که راه‌اندازی‌های دارای چند سرور MCP محافظت‌شده با OAuth را درگیر می‌کرد از میان می‌برد.

## منابع MCP از طریق منشن‌های @

می‌توانید با استفاده از نحو منشن `@`، به منابع MCP مستقیماً در پرامپت‌های خود ارجاع دهید:

```
@server-name:protocol://resource/path
```

برای نمونه، برای ارجاع به یک منبع مشخص پایگاه‌داده:

```
@database:postgres://mydb/users
```

این کار به Claude امکان می‌دهد محتوای منبع MCP را به‌صورت درون‌خطی به‌عنوان بخشی از زمینه گفتگو واکشی و درج کند.

## محدوده‌های MCP

پیکربندی‌های MCP را می‌توان در محدوده‌های مختلف با سطوح اشتراک‌گذاری متفاوت ذخیره کرد:

| محدوده | فلگ | مکان | توضیح | اشتراک‌گذاری با | نیازمند تأیید |
|-------|------|----------|-------------|-------------|------------------|
| **محلی** (پیش‌فرض) | `--scope local` | `~/.claude.json` (زیر مسیر پروژه) | خصوصی برای کاربر فعلی، فقط پروژه فعلی (در نسخه‌های قدیمی‌تر `project` نامیده می‌شد) | فقط شما | خیر |
| **پروژه** | `--scope project` | `.mcp.json` | در مخزن گیت ثبت می‌شود | اعضای تیم | بله (اولین استفاده) |
| **کاربر** | `--scope user` | `~/.claude.json` | در همه پروژه‌ها در دسترس است (در نسخه‌های قدیمی‌تر `global` نامیده می‌شد) | فقط شما | خیر |

هنگام افزودن سرور با `--scope` (شکل کوتاه `-s`) یک محدوده انتخاب کنید. اگر آن را حذف کنید،
Claude Code از `local` استفاده می‌کند:

```bash
# محدوده پروژه — در .mcp.json می‌نویسد تا تیم آن را به اشتراک بگذارد
claude mcp add --scope project --transport http github https://api.githubcopilot.com/mcp/ --header "Authorization: Bearer YOUR_GITHUB_PAT"

# محدوده کاربر — در هر پروژه‌ای در دسترس است
claude mcp add --scope user --transport stdio memory -- npx @modelcontextprotocol/server-memory
```

### استفاده از محدوده پروژه

پیکربندی‌های MCP مخصوص پروژه را در `.mcp.json` ذخیره کنید:

```json
{
  "mcpServers": {
    "github": {
      "type": "http",
      "url": "https://api.githubcopilot.com/mcp/",
      "headers": {
        "Authorization": "Bearer ${GITHUB_PERSONAL_ACCESS_TOKEN}"
      }
    }
  }
}
```

اعضای تیم در اولین استفاده از MCPهای پروژه، یک پرامپت تأیید می‌بینند. در یک محیط کاری نامطمئن، سرورهایی که یک مخزن از طریق `.claude/settings.json` کامیت‌شده خودش آن‌ها را تأیید کرده است، توسط `claude mcp list`/`get` به‌طور خودکار اجرا **نمی‌شوند** — آن‌ها تا زمانی که گفتگوی اعتماد را نپذیرید `⏸ Pending approval` را نشان می‌دهند و `enableAllProjectMcpServers` در پوشه نامطمئن نادیده گرفته می‌شود (v2.1.196).

## مدیریت پیکربندی MCP

### افزودن سرورهای MCP

```bash
# افزودن سرور مبتنی بر HTTP
claude mcp add --transport http github https://api.githubcopilot.com/mcp/ --header "Authorization: Bearer YOUR_GITHUB_PAT"

# افزودن سرور stdio محلی
claude mcp add --transport stdio database -- npx @company/db-server

# فهرست کردن همه سرورهای MCP
claude mcp list

# دریافت جزئیات یک سرور مشخص
claude mcp get github

# حذف یک سرور MCP
claude mcp remove github

# بازنشانی انتخاب‌های تأیید مخصوص پروژه
claude mcp reset-project-choices

# احراز هویت یک سرور MCP از CLI (v2.1.186+)
claude mcp login github

# خروج از یک سرور MCP (v2.1.186+)
claude mcp logout github

# وارد کردن از Claude Desktop
claude mcp add-from-claude-desktop

# افزودن سرور از یک بلاب JSON (برای راه‌اندازی اسکریپتی مفید است)
claude mcp add-json events-server '{"type":"stdio","command":"npx","args":["@modelcontextprotocol/server-events"]}'
```

> **نکته**: در پیکربندی‌های JSON — `.mcp.json`، `~/.claude.json` یا `claude mcp add-json` — فیلد `type` مقدار `streamable-http` را به‌عنوان نام جایگزین برای `http` می‌پذیرد. مشخصات MCP برای این ترنسپورت از نام `streamable-http` استفاده می‌کند، بنابراین پیکربندی‌هایی که از مستندات خود سرور کپی شده‌اند، بدون تغییر کار می‌کنند.

از v2.1.238، دستورهای `claude mcp list` و `claude mcp get` سرورهای غیرفعال را به‌صورت `⊘ Disabled` نشان می‌دهند، بدون اینکه برای بررسی سلامت به آن‌ها متصل شوند.

دستورهای `claude mcp login <name>` / `claude mcp logout <name>` معادل غیرتعاملی جریان OAuth در منوی `/mcp` هستند — بدون باز کردن آن، احراز هویت کنید یا خارج شوید. برای تکمیل OAuth از طریق SSH یا در یک نشست بدون رابط گرافیکی، `--no-browser` را به `login` اضافه کنید (این فلگ جریان را از طریق stdin هدایت می‌کند).

## جدول سرورهای MCP موجود

| سرور MCP | هدف | ابزارهای رایج | احراز هویت | بلادرنگ |
|------------|---------|--------------|------|-----------|
| **Filesystem** | عملیات فایل | read, write, delete | مجوزهای سیستم‌عامل | ✅ بله |
| **GitHub** | مدیریت مخزن | list_prs, create_issue, push | OAuth | ✅ بله |
| **Slack** | ارتباط تیمی | send_message, list_channels | توکن | ✅ بله |
| **Database** | پرس‌وجوهای SQL | query, insert, update | اعتبارنامه | ✅ بله |
| **Google Docs** | دسترسی به اسناد | read, write, share | OAuth | ✅ بله |
| **Asana** | مدیریت پروژه | create_task, update_status | API Key | ✅ بله |
| **Stripe** | داده‌های پرداخت | list_charges, create_invoice | API Key | ✅ بله |
| **Memory** | حافظه پایدار | store, retrieve, delete | محلی | ❌ خیر |

## نمونه‌های عملی

### نمونه ۱: پیکربندی GitHub MCP

**فایل:** `.mcp.json` (ریشه پروژه)

```json
{
  "mcpServers": {
    "github": {
      "type": "http",
      "url": "https://api.githubcopilot.com/mcp/",
      "headers": {
        "Authorization": "Bearer ${GITHUB_PERSONAL_ACCESS_TOKEN}"
      }
    }
  }
}
```

**ابزارهای MCP موجود GitHub:**

#### مدیریت پول‌ریکوئست
- `list_prs` - فهرست کردن همه PRهای مخزن
- `get_pr` - دریافت جزئیات PR همراه با diff
- `create_pr` - ایجاد PR جدید
- `update_pr` - به‌روزرسانی توضیحات/عنوان PR
- `merge_pr` - ادغام PR در شاخه main
- `review_pr` - افزودن دیدگاه‌های بازبینی

**درخواست نمونه:**
```
/mcp__github__get_pr 456

# خروجی:
عنوان: افزودن پشتیبانی از حالت تاریک
نویسنده: @alice
توضیحات: تم تاریک را با متغیرهای CSS پیاده‌سازی می‌کند
وضعیت: OPEN
بازبین‌ها: @bob, @charlie
```

#### مدیریت ایشو
- `list_issues` - فهرست کردن همه ایشوها
- `get_issue` - دریافت جزئیات ایشو
- `create_issue` - ایجاد ایشوی جدید
- `close_issue` - بستن ایشو
- `add_comment` - افزودن دیدگاه به ایشو

#### اطلاعات مخزن
- `get_repo_info` - جزئیات مخزن
- `list_files` - ساختار درختی فایل‌ها
- `get_file_content` - خواندن محتوای فایل
- `search_code` - جست‌وجو در سراسر کدبیس

#### عملیات کامیت
- `list_commits` - تاریخچه کامیت
- `get_commit` - جزئیات یک کامیت مشخص
- `create_commit` - ایجاد کامیت جدید

**راه‌اندازی**:
```bash
export GITHUB_PERSONAL_ACCESS_TOKEN="your_github_token"
# یا از CLI برای افزودن مستقیم استفاده کنید:
claude mcp add --transport http github https://api.githubcopilot.com/mcp/ --header "Authorization: Bearer YOUR_GITHUB_PAT"
```

### بسط متغیرهای محیطی در پیکربندی

پیکربندی‌های MCP از بسط متغیرهای محیطی با مقادیر پیش‌فرض جایگزین پشتیبانی می‌کنند. نحو `${VAR}` و `${VAR:-default}` در فیلدهای زیر کار می‌کند: `command`، `args`، `env`، `url` و `headers`.

```json
{
  "mcpServers": {
    "api-server": {
      "type": "http",
      "url": "${API_BASE_URL:-https://api.example.com}/mcp",
      "headers": {
        "Authorization": "Bearer ${API_KEY}",
        "X-Custom-Header": "${CUSTOM_HEADER:-default-value}"
      }
    },
    "local-server": {
      "command": "${MCP_BIN_PATH:-npx}",
      "args": ["${MCP_PACKAGE:-@company/mcp-server}"],
      "env": {
        "DB_URL": "${DATABASE_URL:-postgresql://localhost/dev}"
      }
    }
  }
}
```

متغیرها در زمان اجرا بسط می‌یابند:
- `${VAR}` - از متغیر محیطی استفاده می‌کند؛ اگر تنظیم نشده باشد (و پیش‌فرضی نداشته باشد)، سرور همچنان با مقدار تحت‌اللفظی `${VAR}` بارگذاری می‌شود و `claude mcp list` و `/mcp` درباره متغیر ناموجود هشدار می‌دهند
- `${VAR:-default}` - از متغیر محیطی استفاده می‌کند و اگر تنظیم نشده باشد به پیش‌فرض برمی‌گردد

### نمونه ۲: راه‌اندازی Database MCP

**پیکربندی:**

```json
{
  "mcpServers": {
    "database": {
      "command": "npx",
      "args": ["-y", "@bytebase/dbhub", "--dsn", "${DATABASE_URL}"]
    }
  }
}
```

**استفاده نمونه:**

```markdown
کاربر: همه کاربرانی را که بیش از ۱۰ سفارش دارند بیاور

Claude: پایگاه‌داده شما را پرس‌وجو می‌کنم تا آن اطلاعات را پیدا کنم.

# استفاده از ابزار پایگاه‌داده MCP:
SELECT u.*, COUNT(o.id) as order_count
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
GROUP BY u.id
HAVING COUNT(o.id) > 10
ORDER BY order_count DESC;

# نتایج:
- Alice: ۱۵ سفارش
- Bob: ۱۲ سفارش
- Charlie: ۱۱ سفارش
```

**راه‌اندازی**:
```bash
export DATABASE_URL="postgresql://user:pass@localhost/mydb"
claude mcp add --transport stdio database -- npx -y @bytebase/dbhub \
  --dsn "$DATABASE_URL"
```

> **هشدار**: این راه‌اندازی به Claude دسترسی نوشتن می‌دهد. ابزار `execute_sql` در DBHub هر SQL‌ای را که دریافت کند اجرا می‌کند، از جمله `UPDATE`، `DELETE` و `DROP`، مگر اینکه حالت فقط‌خواندنی را روشن کنید. از یک پایگاه‌داده محلی یا موقت استفاده کنید، هرگز از محیط عملیاتی.

**راه‌اندازی فقط‌خواندنی (توصیه‌شده):**

یک کاربر پایگاه‌داده بسازید که فقط بتواند `SELECT` اجرا کند (نمونه PostgreSQL):

```sql
CREATE ROLE claude_readonly LOGIN PASSWORD 'change-me';
GRANT CONNECT ON DATABASE mydb TO claude_readonly;
GRANT USAGE ON SCHEMA public TO claude_readonly;
GRANT SELECT ON ALL TABLES IN SCHEMA public TO claude_readonly;
```

حالت فقط‌خواندنی را در یک `dbhub.toml` روشن کنید. فلگ قدیمی `--readonly` دیگر کار نمی‌کند. DBHub مقدار `${DATABASE_URL}` را از محیط شما پر می‌کند، بنابراین هیچ اعتبارنامه‌ای در فایل قرار نمی‌گیرد:

```toml
[[sources]]
id = "default"
dsn = "${DATABASE_URL}"

[[tools]]
name = "execute_sql"
source = "default"
readonly = true
```

سپس DBHub را به‌جای پاس دادن `--dsn` به این فایل اشاره دهید. ابتدا سرور `database` با دسترسی نوشتن را که در بالا افزودید حذف کنید، زیرا Claude Code سرور دومی با همان نام اضافه نمی‌کند:

```bash
# جایگزینی سرور با دسترسی نوشتن که در بالا اضافه شد
claude mcp remove database
export DATABASE_URL="postgresql://claude_readonly:change-me@localhost/mydb"
claude mcp add --transport stdio database -- npx -y @bytebase/dbhub \
  --config "$PWD/dbhub.toml"
```

حالت فقط‌خواندنی متن SQL را فیلتر می‌کند و در گذشته دورزدن‌هایی داشته است (در DBHub 0.22.6 رفع شد)، بنابراین کاربری که فقط `SELECT` دارد چیزی است که واقعاً از داده‌های شما محافظت می‌کند. [حالت فقط‌خواندنی DBHub](https://dbhub.ai/tools/execute-sql#read-only-mode) را ببینید.

### نمونه ۳: گردش‌کار چندگانه MCP

**سناریو: تولید گزارش روزانه**

```markdown
# گردش‌کار گزارش روزانه با استفاده از چندین MCP

## راه‌اندازی
۱. GitHub MCP - واکشی معیارهای PR
۲. Database MCP - پرس‌وجوی داده‌های فروش
۳. Slack MCP - انتشار گزارش
۴. Filesystem MCP - ذخیره گزارش

## گردش‌کار

### گام ۱: واکشی داده‌های GitHub
/mcp__github__list_prs completed:true last:7days

خروجی:
- مجموع PRها: ۴۲
- میانگین زمان ادغام: ۲.۳ ساعت
- زمان بازبینی: ۱.۱ ساعت

### گام ۲: پرس‌وجوی پایگاه‌داده
SELECT COUNT(*) as sales, SUM(amount) as revenue
FROM orders
WHERE created_at > NOW() - INTERVAL '1 day'

خروجی:
- فروش: ۲۴۷
- درآمد: $۱۲,۴۵۰

### گام ۳: تولید گزارش
ترکیب داده‌ها در یک گزارش HTML

### گام ۴: ذخیره در فایل‌سیستم
نوشتن report.html در /reports/

### گام ۵: انتشار در Slack
ارسال خلاصه به کانال #daily-reports

خروجی نهایی:
✅ گزارش تولید و منتشر شد
📊 ۴۷ PR این هفته ادغام شد
💰 $۱۲,۴۵۰ فروش روزانه
```

**راه‌اندازی**:
```bash
export GITHUB_PERSONAL_ACCESS_TOKEN="your_github_token"
export DATABASE_URL="postgresql://user:pass@localhost/mydb"
export SLACK_BOT_TOKEN="your_slack_bot_token"
export SLACK_TEAM_ID="your_slack_team_id"
# هر سرور MCP را از طریق CLI اضافه کنید یا آن‌ها را در .mcp.json پیکربندی کنید
```

### مثال ۴: عملیات MCP فایل‌سیستم

**پیکربندی:**

```json
{
  "mcpServers": {
    "filesystem": {
      "command": "npx",
      "args": ["@modelcontextprotocol/server-filesystem", "/home/user/projects"]
    }
  }
}
```

**عملیات موجود:**

| عملیات | دستور | هدف |
|-----------|---------|---------|
| فهرست فایل‌ها | `ls ~/projects` | نمایش محتویات دایرکتوری |
| خواندن فایل | `cat src/main.ts` | خواندن محتویات فایل |
| نوشتن فایل | `create docs/api.md` | ایجاد فایل جدید |
| ویرایش فایل | `edit src/app.ts` | تغییر فایل |
| جستجو | `grep "async function"` | جستجو در فایل‌ها |
| حذف | `rm old-file.js` | حذف فایل |

**راه‌اندازی**:
```bash
# برای افزودن مستقیم از CLI استفاده کنید:
claude mcp add --transport stdio filesystem -- npx @modelcontextprotocol/server-filesystem /home/user/projects
```

## MCP در برابر حافظه: ماتریس تصمیم

```mermaid
graph TD
    A["به داده خارجی نیاز دارید؟"]
    A -->|خیر| B["از حافظه استفاده کنید"]
    A -->|بله| C["آیا مکرراً تغییر می‌کند؟"]
    C -->|خیر/به‌ندرت| B
    C -->|بله/اغلب| D["از MCP استفاده کنید"]

    B -->|ذخیره می‌کند| E["ترجیحات<br/>زمینه<br/>تاریخچه"]
    D -->|دسترسی می‌گیرد| F["APIهای زنده<br/>پایگاه‌های داده<br/>سرویس‌ها"]

    style A fill:#fff3e0,stroke:#333,color:#333
    style B fill:#e1f5fe,stroke:#333,color:#333
    style C fill:#fff3e0,stroke:#333,color:#333
    style D fill:#f3e5f5,stroke:#333,color:#333
    style E fill:#e8f5e9,stroke:#333,color:#333
    style F fill:#e8f5e9,stroke:#333,color:#333
```

## الگوی درخواست/پاسخ

```mermaid
sequenceDiagram
    participant App as Claude
    participant MCP as سرور MCP
    participant DB as پایگاه داده

    App->>MCP: درخواست: "SELECT * FROM users WHERE id=1"
    MCP->>DB: اجرای کوئری
    DB-->>MCP: مجموعه نتیجه
    MCP-->>App: بازگرداندن داده‌های تجزیه‌شده
    App->>App: پردازش نتیجه
    App->>App: ادامه وظیفه

    Note over MCP,DB: دسترسی بلادرنگ<br/>بدون کش
```

## متغیرهای محیطی

اعتبارنامه‌های حساس را در متغیرهای محیطی ذخیره کنید:

```bash
# ~/.bashrc یا ~/.zshrc
export GITHUB_PERSONAL_ACCESS_TOKEN="ghp_xxxxxxxxxxxxx"
export DATABASE_URL="postgresql://user:pass@localhost/mydb"
export SLACK_BOT_TOKEN="your-slack-bot-token"
export SLACK_TEAM_ID="T0000000000"
```

سپس در پیکربندی MCP به آن‌ها ارجاع دهید:

```json
{
  "env": {
    "GITHUB_PERSONAL_ACCESS_TOKEN": "${GITHUB_PERSONAL_ACCESS_TOKEN}"
  }
}
```

## Claude به‌عنوان سرور MCP (`claude mcp serve`)

خود Claude Code می‌تواند به‌عنوان یک سرور MCP برای برنامه‌های دیگر عمل کند. این امکان را می‌دهد که ابزارهای خارجی، ویرایشگرها و سیستم‌های اتوماسیون از قابلیت‌های Claude از طریق پروتکل استاندارد MCP بهره ببرند.

```bash
# اجرای Claude Code به‌عنوان سرور MCP روی stdio
claude mcp serve
```

برنامه‌های دیگر سپس می‌توانند مانند هر سرور MCP مبتنی بر stdio به این سرور متصل شوند. برای نمونه، برای افزودن Claude Code به‌عنوان سرور MCP در نمونه دیگری از Claude Code:

```bash
claude mcp add --transport stdio claude-agent -- claude mcp serve
```

این برای ساخت گردش‌کارهای چندایجنت مفید است، جایی که یک نمونه Claude نمونه دیگر را هماهنگ می‌کند.

## پیکربندی مدیریت‌شده MCP (سازمانی)

برای استقرارهای سازمانی، مدیران IT سیاست سرور MCP را از طریق دو سازوکار جداگانه اعمال می‌کنند: فایل `managed-mcp.json` که مجموعه‌ای ثابت از سرورها را با کنترل انحصاری مستقر می‌کند، و کلیدهای تنظیمات `allowedMcpServers` / `deniedMcpServers` که تعیین می‌کنند کدام سرورهای پیکربندی‌شده می‌توانند بارگذاری شوند.

**مکان:**
- macOS: `/Library/Application Support/ClaudeCode/managed-mcp.json`
- Linux و WSL: `/etc/claude-code/managed-mcp.json`
- Windows: `C:\Program Files\ClaudeCode\managed-mcp.json`

`managed-mcp.json` از همان قالبی استفاده می‌کند که `.mcp.json` پروژه دارد — یک نگاشت سطح‌بالای `mcpServers`. این فایل سرورها را مستقر می‌کند؛ آن‌ها را فیلتر نمی‌کند:

```json
{
  "mcpServers": {
    "example-remote": {
      "type": "http",
      "url": "https://mcp.example.com/mcp"
    },
    "company-internal": {
      "type": "stdio",
      "command": "/usr/local/bin/company-mcp-server",
      "args": ["--config", "/etc/company/mcp-config.json"]
    }
  }
}
```

هر کاربری روی دستگاه می‌تواند این فایل را بخواند، بنابراین هرگز اعتبارنامه‌ها را در بلوک `env` قرار ندهید. به‌جای آن از بسط `${VAR}`، OAuth یا `headersHelper` استفاده کنید.

> **نکته (v2.1.305):** سرورهای داخل `managed-mcp.json` به مدخل `allowedMcpServers` نیازی ندارند. فهرست مجاز یک سرور مدیریت‌شده را فقط وقتی بررسی می‌کند که از بسط `${VAR}` در بیرون `env` استفاده کند؛ پیش از v2.1.305 سرورهایی را هم بررسی می‌کرد که `${VAR}` را فقط در `env` به کار می‌بردند. اگر برای خاموش نگه‌داشتن چنین سروری به `allowedMcpServers` تکیه کرده بودید، حالا پس از ارتقا بدون هیچ پرسشی بارگذاری می‌شود؛ به‌جایش برای آن یک مدخل `deniedMcpServers` اضافه کنید.

**فیلترکردن: فهرست‌های مجاز و مسدود**

`allowedMcpServers`، `deniedMcpServers` و `allowAllClaudeAiMcps` **کلیدهای تنظیمات هستند، نه فیلدهای `managed-mcp.json`**. آن‌ها را در یک منبع تنظیمات مدیریت‌شده قرار دهید — تنظیمات مدیریت‌شده توسط سرور، `managed-settings.json`، یک پروفایل MDM یا رجیستری — تا قابل اعمال باشند:

- `allowedMcpServers` -- فهرست مجازِ سرورهای موردقبول. `allowManagedMcpServersOnly: true` را در کنار آن و در همان منبع مدیریت‌شده تنظیم کنید، وگرنه فهرست‌های مجاز از همه دامنه‌ها ادغام می‌شوند و کاربر می‌تواند فهرست شما را گسترش دهد.
- `deniedMcpServers` -- فهرست مسدود سرورهای بلاک‌شده. در هر حال از همه دامنه‌ها ادغام می‌شود.
- `allowAllClaudeAiMcps` -- کانکتورهای ابری claude.ai را در کنار `managed-mcp.json` مستقرشده بارگذاری می‌کند (v2.1.149+). فقط از سطوح سیاست تحت کنترل مدیر خوانده می‌شود.

هر ورودی شیئی است با یک کلید **منفرد**:

| کلید | مطابقت |
|-----|---------|
| `serverUrl` | یک URL سرور راه‌دور، دقیق یا با نویسه‌های عام `*` |
| `serverCommand` | دستور و آرگومان‌های دقیقی که یک سرور stdio را راه‌اندازی می‌کنند، به‌صورت آرایه — همه آرگومان‌ها، به ترتیب |
| `serverName` | برچسبی که کاربر تعیین کرده است. **فقط مطابقت دقیق؛ نویسه‌های عام گسترش نمی‌یابند** |

**پیکربندی نمونه:**

```json
{
  "allowedMcpServers": [
    { "serverUrl": "https://mcp.example.com/*" },
    { "serverCommand": ["/usr/local/bin/company-mcp-server", "--config", "/etc/company/mcp-config.json"] }
  ],
  "deniedMcpServers": [
    { "serverName": "untrusted-server" },
    { "serverUrl": "http://*" }
  ],
  "allowManagedMcpServersOnly": true
}
```

یک تنظیم مدیریت‌شده سوم، `managedMcpServers` (v2.1.259+)، به سازمان اجازه می‌دهد سرورهای MCP از نوع HTTP/SSE را در اختیار همه کاربران قرار دهد. ورودی‌ها همان شکل `.mcp.json` را دارند؛ ورودی‌هایی که دستوری برای اجرا مشخص می‌کنند نادیده گرفته می‌شوند.

> **توجه:** وقتی هم `allowedMcpServers` و هم `deniedMcpServers` با یک سرور مطابقت داشته باشند، قاعده مسدودسازی اولویت دارد.

## سرورهای MCP ارائه‌شده توسط پلاگین

پلاگین‌ها می‌توانند سرورهای MCP خودشان را همراه داشته باشند و هنگام نصب پلاگین به‌طور خودکار در دسترس قرار دهند. سرورهای MCP ارائه‌شده توسط پلاگین به دو روش تعریف می‌شوند:

1. **`.mcp.json` مستقل** -- یک فایل `.mcp.json` در پوشه ریشه پلاگین قرار دهید
2. **درون‌خطی در `plugin.json`** -- سرورهای MCP را مستقیماً در مانیفست پلاگین تعریف کنید

از متغیر `${CLAUDE_PLUGIN_ROOT}` برای ارجاع به مسیرهای نسبی به پوشه نصب پلاگین استفاده کنید:

```json
{
  "mcpServers": {
    "plugin-tools": {
      "command": "node",
      "args": ["${CLAUDE_PLUGIN_ROOT}/dist/mcp-server.js"],
      "env": {
        "CONFIG_PATH": "${CLAUDE_PLUGIN_ROOT}/config.json"
      }
    }
  }
}
```

## MCP محدود به زیرایجنت

سرورهای MCP را می‌توان به‌صورت درون‌خطی در فرانت‌متر ایجنت با کلید `mcpServers:` تعریف کرد و آن‌ها را به یک زیرایجنت خاص محدود کرد، نه کل پروژه. این زمانی مفید است که یک ایجنت به سرور MCP مشخصی نیاز دارد که دیگر ایجنت‌های گردش‌کار به آن نیازی ندارند.

```yaml
---
name: my-tool-agent
description: از my-tool برای عملیات تخصصی استفاده می‌کند
mcpServers:
  my-tool:
    type: http
    url: https://my-tool.example.com/mcp
---

شما ایجنتی هستید که برای عملیات تخصصی به my-tool دسترسی دارید.
```

سرورهای MCP محدود به زیرایجنت فقط در زمینه اجرای همان ایجنت در دسترس‌اند و با ایجنت والد یا هم‌سطح به اشتراک گذاشته نمی‌شوند.

## محدودیت‌های خروجی MCP

Claude Code محدودیت‌هایی بر خروجی ابزار MCP اعمال می‌کند تا از سرریز زمینه جلوگیری شود:

| محدودیت | آستانه | رفتار |
|-------|-----------|----------|
| **هشدار** | ۱۰٬۰۰۰ توکن | هشداری نمایش داده می‌شود که خروجی حجیم است |
| **حداکثر پیش‌فرض** | ۲۵٬۰۰۰ توکن | خروجی بزرگ‌تر در یک فایل ذخیره می‌شود و مسیر فایل به‌جای آن وارد گفتگو می‌شود |
| **ماندگاری روی دیسک** | ۵۰٬۰۰۰ نویسه | نتایج ابزاری که از ۵۰ هزار نویسه فراتر می‌روند روی دیسک نگهداری می‌شوند |

حداکثر محدودیت خروجی از طریق متغیر محیطی `MAX_MCP_OUTPUT_TOKENS` قابل پیکربندی است:

```bash
# افزایش حداکثر خروجی به ۵۰٬۰۰۰ توکن
export MAX_MCP_OUTPUT_TOKENS=50000
```

## انتقال خودکار فراخوانی‌های طولانی ابزار به پس‌زمینه (v2.1.212)

فراخوانی‌های ابزار MCP که بیش از ۲ دقیقه طول می‌کشند اکنون به‌طور خودکار به پس‌زمینه منتقل می‌شوند تا نشست قابل استفاده بماند و روی یک ابزار کند قفل نشود. آستانه قابل پیکربندی است و رفتار آن را می‌توان از طریق `CLAUDE_CODE_MCP_AUTO_BACKGROUND_MS` تنظیم یا غیرفعال کرد:

```bash
# تغییر آستانه انتقال خودکار به پس‌زمینه به ۵ دقیقه (۳۰۰٬۰۰۰ میلی‌ثانیه)
export CLAUDE_CODE_MCP_AUTO_BACKGROUND_MS=300000
```

آن را روی `0` بگذارید تا انتقال خودکار به پس‌زمینه خاموش شود؛ `CLAUDE_CODE_DISABLE_BACKGROUND_TASKS=1` آن را همراه با فرمان‌های پس‌زمینه و زیرایجنت‌های پس‌زمینه خاموش می‌کند. برای محدودکردن مدت اجرای یک فراخوانی، یک `timeout` به میلی‌ثانیه در هر سرور اضافه کنید (یک حد سخت زمانی واقعی) یا `MCP_TOOL_TIMEOUT` را برای همهٔ سرورها تنظیم کنید (پیش‌فرض حدود ۲۸ ساعت).

### MCP Tasks (بتای عمومی، v2.1.304+)

سروری که افزونهٔ tasks در MCP را پشتیبانی می‌کند می‌تواند یک کار طولانی را خودش اجرا کند: فراخوانی ابزار Claude به‌محض پذیرش کار توسط سرور برمی‌گردد، پانوشت شمارشی مثل `1 MCP task` نشان می‌دهد و Claude با پایان کار نتیجه را می‌گیرد. با `x` در `/tasks` یکی را متوقف کنید. یک task روی سرور دوردست پس از خروج شما هم ادامه می‌یابد؛ همان نشست را ازسرگیری کنید تا دوباره آن را دنبال کنید. Tasks به بازبینی پروتکل 2026-07-28، واکشی با feature-flag (پس نه Bedrock، Vertex، Foundry یا تلمتری خاموش) و یک نشست ترمینال CLI، Agent SDK یا GitHub Actions نیاز دارند. یک اجرای غیرتعاملی آن‌ها را فقط از Agent SDK یا `claude -p --input-format stream-json` می‌گیرد، و هر کدام `CLAUDE_AUTO_BACKGROUND_TASKS=1` لازم دارند (یک `claude -p \"<prompt>\"` ساده آن‌ها را نمی‌گیرد). VS Code و اپ دسکتاپ آن‌ها را نمی‌گیرند، و فراخوانی‌های زیرایجنت‌ها هرگز task نمی‌شوند. برای اینکه Claude منتظر نتیجهٔ یک task بماند، `CLAUDE_CODE_DISABLE_MCP_TASK_BACKGROUND=1` را تنظیم کنید (یا `CLAUDE_CODE_MCP_AUTO_BACKGROUND_MS=0` برای منتظرماندن روی هر فراخوانی MCP).

## حل تورم زمینه با اجرای کد

با گسترش پذیرش MCP، اتصال به ده‌ها سرور با صدها یا هزاران ابزار چالش بزرگی ایجاد می‌کند: **تورم زمینه**. این را می‌توان بزرگ‌ترین مشکل MCP در مقیاس دانست، و تیم مهندسی Anthropic راه‌حلی زیبا پیشنهاد کرده است — استفاده از اجرای کد به‌جای فراخوانی مستقیم ابزار.

> **منبع**: [Code Execution with MCP: Building More Efficient Agents](https://www.anthropic.com/engineering/code-execution-with-mcp) — وبلاگ مهندسی Anthropic

### مشکل: دو منبع هدر رفتن توکن

**۱. تعریف‌های ابزار پنجره زمینه را اشباع می‌کنند**

بیشتر کلاینت‌های MCP همه تعریف‌های ابزار را از ابتدا بارگذاری می‌کنند. وقتی به هزاران ابزار متصل باشید، مدل باید پیش از آنکه حتی درخواست کاربر را بخواند، صدها هزار توکن را پردازش کند.

**۲. نتایج میانی توکن بیشتری مصرف می‌کنند**

هر نتیجه میانی ابزار از زمینه مدل عبور می‌کند. انتقال متن صورت‌جلسه یک جلسه از Google Drive به Salesforce را در نظر بگیرید — متن کامل صورت‌جلسه **دو بار** از زمینه عبور می‌کند: یک بار هنگام خواندن و بار دیگر هنگام نوشتن در مقصد. متن صورت‌جلسه یک جلسه ۲ ساعته می‌تواند بیش از ۵۰٬۰۰۰ توکن اضافی باشد.

```mermaid
graph LR
    A["مدل"] -->|"فراخوانی ابزار: getDocument"| B["سرور MCP"]
    B -->|"متن کامل صورت‌جلسه (۵۰ هزار توکن)"| A
    A -->|"فراخوانی ابزار: updateRecord<br/>(ارسال دوباره متن کامل صورت‌جلسه)"| B
    B -->|"تأیید"| A

    style A fill:#ffcdd2,stroke:#333,color:#333
    style B fill:#f3e5f5,stroke:#333,color:#333
```

### راه‌حل: ابزارهای MCP به‌عنوان APIهای کد

ایجنت به‌جای عبور دادن تعریف‌های ابزار و نتایج از پنجره زمینه، **کدی می‌نویسد** که ابزارهای MCP را به‌عنوان API فراخوانی می‌کند. کد در محیط اجرای سندباکس‌شده اجرا می‌شود و تنها نتیجه نهایی به مدل بازمی‌گردد.

```mermaid
graph LR
    A["مدل"] -->|"کد می‌نویسد"| B["محیط<br/>اجرای کد"]
    B -->|"فراخوانی مستقیم ابزارها"| C["سرورهای MCP"]
    C -->|"داده در محیط اجرا<br/>باقی می‌ماند"| B
    B -->|"فقط نتیجه نهایی<br/>(حداقل توکن)"| A

    style A fill:#c8e6c9,stroke:#333,color:#333
    style B fill:#e1f5fe,stroke:#333,color:#333
    style C fill:#f3e5f5,stroke:#333,color:#333
```

#### نحوه کار

ابزارهای MCP به‌صورت درخت فایلی از توابع تایپ‌دار ارائه می‌شوند:

```
servers/
├── google-drive/
│   ├── getDocument.ts
│   └── index.ts
├── salesforce/
│   ├── updateRecord.ts
│   └── index.ts
└── ...
```

هر فایل ابزار شامل یک پوشش‌دهنده تایپ‌دار است:

```typescript
// ./servers/google-drive/getDocument.ts
import { callMCPTool } from "../../../client.js";

interface GetDocumentInput {
  documentId: string;
}

interface GetDocumentResponse {
  content: string;
}

export async function getDocument(
  input: GetDocumentInput
): Promise<GetDocumentResponse> {
  return callMCPTool<GetDocumentResponse>(
    'google_drive__get_document', input
  );
}
```

سپس ایجنت کدی برای هماهنگ‌سازی ابزارها می‌نویسد:

```typescript
import * as gdrive from './servers/google-drive';
import * as salesforce from './servers/salesforce';

// داده‌ها مستقیماً بین ابزارها جریان می‌یابند — هرگز از طریق مدل
const transcript = (
  await gdrive.getDocument({ documentId: 'abc123' })
).content;

await salesforce.updateRecord({
  objectType: 'SalesMeeting',
  recordId: '00Q5f000001abcXYZ',
  data: { Notes: transcript }
});
```

**نتیجه: مصرف توکن از حدود ۱۵۰٬۰۰۰ به حدود ۲٬۰۰۰ کاهش می‌یابد — یعنی ۹۸.۷٪ صرفه‌جویی.**

### مزایای کلیدی

| مزیت | توضیح |
|---------|-------------|
| **افشای تدریجی** | ایجنت فایل‌سیستم را مرور می‌کند تا فقط تعریف ابزارهایی را که نیاز دارد بارگذاری کند، نه همه ابزارها را از ابتدا |
| **نتایج بهینه از نظر زمینه** | داده‌ها پیش از بازگشت به مدل، در محیط اجرا فیلتر یا تبدیل می‌شوند |
| **جریان کنترل قدرتمند** | حلقه‌ها، شرط‌ها و مدیریت خطا در کد اجرا می‌شوند، بدون رفت‌وبرگشت از طریق مدل |
| **حفظ حریم خصوصی** | داده‌های میانی (PII، رکوردهای حساس) در محیط اجرا می‌مانند و هرگز به زمینه مدل وارد نمی‌شوند |
| **ماندگاری وضعیت** | ایجنت‌ها می‌توانند نتایج میانی را در فایل‌ها ذخیره کنند و توابع مهارتی قابل استفاده مجدد بسازند |

#### مثال: فیلتر کردن مجموعه‌داده‌های بزرگ

```typescript
// بدون اجرای کد — هر ۱۰٬۰۰۰ سطر از زمینه عبور می‌کند
// فراخوانی ابزار: gdrive.getSheet(sheetId: 'abc123')
//   -> ۱۰٬۰۰۰ سطر را در زمینه برمی‌گرداند

// با اجرای کد — فیلتر در محیط اجرا
const allRows = await gdrive.getSheet({ sheetId: 'abc123' });
const pendingOrders = allRows.filter(
  row => row["Status"] === 'pending'
);
console.log(`Found ${pendingOrders.length} pending orders`);
console.log(pendingOrders.slice(0, 5)); // فقط ۵ سطر به مدل می‌رسد
```

#### مثال: حلقه بدون رفت‌وبرگشت

```typescript
// نظرسنجی برای اعلان استقرار — کاملاً در کد اجرا می‌شود
let found = false;
while (!found) {
  const messages = await slack.getChannelHistory({
    channel: 'C123456'
  });
  found = messages.some(
    m => m.text.includes('deployment complete')
  );
  if (!found) await new Promise(r => setTimeout(r, 5000));
}
console.log('Deployment notification received');
```

### بده‌بستان‌هایی که باید در نظر گرفت

اجرای کد، پیچیدگی خودش را به همراه می‌آورد. اجرای کد تولیدشده توسط ایجنت نیازمند موارد زیر است:

- یک **محیط اجرای سندباکس امن** با محدودیت‌های منابع مناسب
- **پایش و ثبت گزارش** کدهای اجراشده
- **سربار زیرساختی** اضافی در مقایسه با فراخوانی مستقیم ابزار

مزایا — کاهش هزینه توکن، تأخیر کمتر، ترکیب‌پذیری بهتر ابزارها — باید در برابر این هزینه‌های پیاده‌سازی سنجیده شوند. برای ایجنت‌هایی که فقط چند سرور MCP دارند، فراخوانی مستقیم ابزار ممکن است ساده‌تر باشد. برای ایجنت‌ها در مقیاس بزرگ (ده‌ها سرور، صدها ابزار)، اجرای کد پیشرفتی چشمگیر است.

### MCPorter: رانتایمی برای ترکیب ابزارهای MCP

[MCPorter](https://github.com/steipete/mcporter) یک رانتایم TypeScript و مجموعه ابزار CLI است که فراخوانی سرورهای MCP را بدون کدهای تکراری عملی می‌کند — و با نمایش انتخابی ابزارها و پوشش‌های تایپ‌شده به کاهش تورم زمینه کمک می‌کند.

**چه مشکلی را حل می‌کند:** به‌جای بارگذاری همه تعریف‌های ابزار از همه سرورهای MCP از ابتدا، MCPorter به شما امکان می‌دهد ابزارهای مشخصی را به‌صورت درخواستی کشف، بررسی و فراخوانی کنید — و زمینه‌تان را سبک نگه دارید.

**ویژگی‌های کلیدی:**

| ویژگی | توضیح |
|---------|-------------|
| **کشف بدون پیکربندی** | سرورهای MCP را به‌طور خودکار از Cursor، Claude، Codex یا پیکربندی‌های محلی کشف می‌کند |
| **کلاینت‌های ابزار تایپ‌شده** | `mcporter emit-ts` رابط‌های `.d.ts` و پوشش‌های آماده اجرا تولید می‌کند |
| **API ترکیب‌پذیر** | `createServerProxy()` ابزارها را به‌صورت متدهای camelCase با کمک‌کننده‌های `.text()`، `.json()`، `.markdown()` در دسترس قرار می‌دهد |
| **تولید CLI** | `mcporter generate-cli` هر سرور MCP را به یک CLI مستقل با فیلتر `--include-tools` / `--exclude-tools` تبدیل می‌کند |
| **پنهان‌سازی پارامترها** | پارامترهای اختیاری به‌طور پیش‌فرض پنهان می‌مانند و پرحرفی شِما را کاهش می‌دهند |

**نصب:**

```bash
npx mcporter list          # بدون نیاز به نصب — سرورها را فوراً کشف کنید
pnpm add mcporter          # افزودن به یک پروژه
brew install steipete/tap/mcporter  # مک‌او‌اس از طریق Homebrew
```

**مثال — ترکیب ابزارها در TypeScript:**

```typescript
import { createRuntime, createServerProxy } from "mcporter";

const runtime = await createRuntime();
const gdrive = createServerProxy(runtime, "google-drive");
const salesforce = createServerProxy(runtime, "salesforce");

// داده‌ها بین ابزارها جریان می‌یابند بدون عبور از زمینه مدل
const doc = await gdrive.getDocument({ documentId: "abc123" });
await salesforce.updateRecord({
  objectType: "SalesMeeting",
  recordId: "00Q5f000001abcXYZ",
  data: { Notes: doc.text() }
});
```

**مثال — فراخوانی ابزار از CLI:**

```bash
# فراخوانی مستقیم یک ابزار مشخص
npx mcporter call linear.create_comment issueId:ENG-123 body:'Looks good!'

# فهرست سرورها و ابزارهای موجود
npx mcporter list
```

MCPorter رویکرد اجرای کد که در بالا توضیح داده شد را با فراهم کردن زیرساخت رانتایم برای فراخوانی ابزارهای MCP به‌صورت APIهای تایپ‌شده تکمیل می‌کند — و نگه داشتن داده‌های میانی خارج از زمینه مدل را ساده می‌سازد.

## بهترین شیوه‌ها

### ملاحظات امنیتی

#### کارهایی که باید بکنید ✅
- برای همه اعتبارنامه‌ها از متغیرهای محیطی استفاده کنید
- توکن‌ها و کلیدهای API را به‌طور منظم بچرخانید (ماهانه توصیه می‌شود)
- در صورت امکان از توکن‌های فقط‌خواندنی استفاده کنید
- دامنه دسترسی سرور MCP را به حداقل لازم محدود کنید
- استفاده از سرور MCP و گزارش‌های دسترسی را پایش کنید
- در صورت وجود، برای سرویس‌های خارجی از OAuth استفاده کنید
- محدودسازی نرخ را روی درخواست‌های MCP پیاده‌سازی کنید
- اتصال‌های MCP را پیش از استفاده در محیط عملیاتی آزمایش کنید
- همه اتصال‌های فعال MCP را مستند کنید
- بسته‌های سرور MCP را به‌روز نگه دارید

#### کارهایی که نباید بکنید ❌
- اعتبارنامه‌ها را در فایل‌های پیکربندی به‌صورت سخت‌کدشده ننویسید
- توکن‌ها یا اسرار را در git کامیت نکنید
- توکن‌ها را در چت‌های تیمی یا ایمیل‌ها به اشتراک نگذارید
- از توکن‌های شخصی برای پروژه‌های تیمی استفاده نکنید
- مجوزهای غیرضروری اعطا نکنید
- خطاهای احراز هویت را نادیده نگیرید
- نقاط پایانی MCP را به‌صورت عمومی افشا نکنید
- سرورهای MCP را با امتیازهای root/مدیر اجرا نکنید
- داده‌های حساس را در گزارش‌ها کش نکنید
- سازوکارهای احراز هویت را غیرفعال نکنید

### بهترین شیوه‌های پیکربندی

1. **کنترل نسخه**: `.mcp.json` را در git نگه دارید اما برای اسرار از متغیرهای محیطی استفاده کنید
2. **کمترین امتیاز**: برای هر سرور MCP حداقل مجوزهای لازم را اعطا کنید
3. **جداسازی**: در صورت امکان سرورهای MCP مختلف را در فرایندهای جداگانه اجرا کنید
4. **پایش**: همه درخواست‌ها و خطاهای MCP را برای ردپای حسابرسی ثبت کنید
5. **آزمایش**: همه پیکربندی‌های MCP را پیش از استقرار در محیط عملیاتی آزمایش کنید

### نکات کارایی

- داده‌های پرکاربرد را در سطح برنامه کش کنید
- از کوئری‌های MCP دقیق استفاده کنید تا انتقال داده کاهش یابد
- زمان پاسخ عملیات MCP را پایش کنید
- محدودسازی نرخ را برای APIهای خارجی در نظر بگیرید
- هنگام انجام چندین عملیات از دسته‌بندی استفاده کنید

## دستورالعمل‌های نصب

### پیش‌نیازها
- Node.js و npm نصب شده باشد
- Claude Code CLI نصب شده باشد
- توکن‌ها یا اعتبارنامه‌های API برای سرویس‌های خارجی

### راه‌اندازی گام‌به‌گام

1. **نخستین سرور MCP خود را اضافه کنید** با استفاده از CLI (مثال: GitHub):
```bash
claude mcp add --transport http github https://api.githubcopilot.com/mcp/ --header "Authorization: Bearer YOUR_GITHUB_PAT"
```

   یا یک فایل `.mcp.json` در ریشه پروژه خود بسازید:
```json
{
  "mcpServers": {
    "github": {
      "type": "http",
      "url": "https://api.githubcopilot.com/mcp/",
      "headers": {
        "Authorization": "Bearer ${GITHUB_PERSONAL_ACCESS_TOKEN}"
      }
    }
  }
}
```

2. **متغیرهای محیطی را تنظیم کنید:**
```bash
export GITHUB_PERSONAL_ACCESS_TOKEN="your_github_personal_access_token"
```

3. **اتصال را آزمایش کنید:**
```bash
claude /mcp
```

4. **از ابزارهای MCP استفاده کنید:**
```bash
/mcp__github__list_prs
/mcp__github__create_issue "Title" "Description"
```

### نصب برای سرویس‌های خاص

**MCP گیت‌هاب:**
```bash
npm install -g @modelcontextprotocol/server-github
```

**MCP پایگاه داده:**
```bash
npm install -g @bytebase/dbhub
```

**MCP فایل‌سیستم:**
```bash
npm install -g @modelcontextprotocol/server-filesystem
```

**MCP اسلک (بسته منسوخ‌شده):**
```bash
npm install -g @modelcontextprotocol/server-slack
```

## عیب‌یابی

### با خروجی خطا شروع کنید (v2.1.219+)

اگر سروری متصل نمی‌شود، پیش از هر تغییری `claude mcp list` را اجرا کنید (یا `/mcp` را درون یک نشست). Claude Code اکنون **کد وضعیت HTTP و متن خطای سرور** را کنار سرور ناموفق چاپ می‌کند، بنابراین به‌جای یک پیام کلی «اتصال ناموفق» چیزی مثل `401 Unauthorized` یا `404 Not Found` می‌بینید:

```bash
# وضعیت اتصال به‌همراه کد وضعیت HTTP و متن خطا برای خطاها را نشان می‌دهد
claude mcp list
```

ابتدا وضعیت را بخوانید — به شما می‌گوید کدام راه‌حل کاربرد دارد:

- `401` / `403` ← اعتبارنامه نامعتبر یا منقضی؛ با `claude mcp login <name>` دوباره احراز هویت کنید
- `404` ← URL اشتباه (علت معمول، نبودِ پسوند مسیر `/mcp` یا `/sse` است)
- `5xx` / timeout ← سرور راه‌دور از کار افتاده است؛ [اتمام زمان اتصال](#اتمام-زمان-اتصال) را ببینید

### فاصله‌های سفید پنهان در مقادیر پیکربندی (v2.1.219+)

Claude Code زمانی هشدار می‌دهد که یک مقدار پیکربندی MCP **فاصله سفید ابتدایی یا انتهایی** داشته باشد. این یکی از علت‌های رایج و سخت‌کشف شکست احراز هویت است: توکنی که از مرورگر یا پیام چت کپی‌پیست شده اغلب یک فاصله یا خط جدید انتهایی دارد که عیناً در هدر `Authorization` فرستاده می‌شود و به‌عنوان اعتبارنامه نامعتبر رد می‌شود.

اگر این هشدار را دیدید، مقدار را در `.mcp.json` (یا متغیر محیطی‌ای که از آن باز می‌شود) دوباره بررسی و آن را اصلاح کنید:

```bash
# فاصله‌های سفید پنهان ابتدایی/انتهایی بین جداکننده‌ها را آشکار می‌کند
printf '[%s]\n' "$GITHUB_PERSONAL_ACCESS_TOKEN"
```

### سرورهای ردشده در اجراهای بدون رابط (v2.1.219+)

سرورهایی که از طریق `--mcp-config` داده می‌شوند و اعتبارسنجی پیکربندی را رد می‌کنند، **رد می‌شوند** و اجرا متوقف نمی‌شود؛ بنابراین یک اسکریپت بدون رابط ممکن است ظاهراً کار کند در حالی که نیمی از ابزارهایش را ندارد. Claude Code اکنون گزارش می‌دهد کدام‌ها حذف شده‌اند:

- **اجراهای بدون رابط / `-p`**: رویداد `init` در stream-json فیلدی به نام `mcp_server_errors` دارد که همه ورودی‌های ردشده را فهرست می‌کند. پیش از اعتماد به خروجی اجرا، آن را بررسی کنید.
- **اجراهای ترمینال تعاملی**: همین مشکل هنگام آغاز نشست به‌صورت هشدار شروع چاپ می‌شود.

```bash
# بررسی ورودی‌های ردشده --mcp-config در یک اجرای بدون رابط
claude -p "list my tools" --mcp-config ./servers.json \
  --output-format stream-json --verbose \
  | jq -r 'select(.type == "system" and .subtype == "init") | .mcp_server_errors'
```

### سرور MCP پیدا نشد
```bash
# بررسی نصب بودن سرور MCP
npm list -g @modelcontextprotocol/server-github

# در صورت نبود، نصب کنید
npm install -g @modelcontextprotocol/server-github
```

### احراز هویت ناموفق بود
```bash
# بررسی تنظیم بودن متغیر محیطی
echo $GITHUB_PERSONAL_ACCESS_TOKEN

# در صورت نیاز دوباره export کنید
export GITHUB_PERSONAL_ACCESS_TOKEN="your_token"

# بررسی صحیح بودن مجوزهای توکن
# دامنه‌های توکن GitHub را اینجا بررسی کنید: https://github.com/settings/tokens
```

### اتمام زمان اتصال
- اتصال شبکه را بررسی کنید: `ping api.github.com`
- بررسی کنید که نقطه پایانی API در دسترس باشد
- محدودیت‌های نرخ API را بررسی کنید
- `timeout` سرور (به میلی‌ثانیه) را در مدخل پیکربندی آن بالا ببرید، یا `MCP_TOOL_TIMEOUT` را برای همهٔ سرورها
- مشکلات فایروال یا پروکسی را بررسی کنید

### کرش سرور MCP
- گزارش‌های سرور MCP را بررسی کنید: `~/.claude/logs/`
- بررسی کنید که همه متغیرهای محیطی تنظیم شده باشند
- مجوزهای فایل مناسب را تضمین کنید
- نصب دوباره بسته سرور MCP را امتحان کنید
- فرایندهای متعارض روی همان پورت را بررسی کنید

## مفاهیم مرتبط

### حافظه در برابر MCP
- **حافظه**: داده‌های ماندگار و تغییرنکردنی (ترجیحات، زمینه، تاریخچه) را ذخیره می‌کند
- **MCP**: به داده‌های زنده و متغیر (APIها، پایگاه‌های داده، سرویس‌های بلادرنگ) دسترسی می‌گیرد

### چه زمانی از کدام استفاده کنیم
- **از حافظه استفاده کنید** برای: ترجیحات کاربر، تاریخچه گفتگو، زمینه آموخته‌شده
- **از MCP استفاده کنید** برای: ایشوهای فعلی GitHub، کوئری‌های زنده پایگاه داده، داده‌های بلادرنگ

### یکپارچگی با سایر ویژگی‌های Claude
- MCP را با حافظه ترکیب کنید تا زمینه غنی داشته باشید
- از ابزارهای MCP در پرامپت‌ها برای استدلال بهتر استفاده کنید
- از چندین MCP برای جریان‌های کاری پیچیده بهره بگیرید

## منابع بیشتر

- [مستندات رسمی MCP](https://code.claude.com/docs/en/mcp)
- [مشخصات پروتکل MCP](https://modelcontextprotocol.io/specification)
- [مخزن GitHub پروتکل MCP](https://github.com/modelcontextprotocol/servers)
- [سرورهای MCP موجود](https://github.com/modelcontextprotocol/servers)
- [MCPorter](https://github.com/steipete/mcporter) — رانتایم TypeScript و CLI برای فراخوانی سرورهای MCP بدون کد تکراری
- [اجرای کد با MCP](https://www.anthropic.com/engineering/code-execution-with-mcp) — وبلاگ مهندسی Anthropic درباره حل تورم زمینه
- [مرجع CLI Claude Code](https://code.claude.com/docs/en/cli-reference)
- [مستندات Claude API](https://docs.anthropic.com)

---

**آخرین به‌روزرسانی**: ۲۶ اکتبر ۲۰۲۶
**نسخه Claude Code**: 2.1.310
**منابع**:
- https://code.claude.com/docs/en/mcp
- https://code.claude.com/docs/en/managed-mcp
- https://code.claude.com/docs/en/changelog
- https://github.com/anthropics/claude-code/releases/tag/v2.1.117
- https://github.com/anthropics/claude-code/releases/tag/v2.1.139
- https://github.com/anthropics/claude-code/blob/main/CHANGELOG.md
- https://code.claude.com/docs/en/model-config
- https://code.claude.com/docs/en/mcp#configure-tool-search
- https://code.claude.com/docs/en/env-vars
- https://github.com/anthropics/claude-code/releases/tag/v2.1.285
- https://github.com/anthropics/claude-code/releases/tag/v2.1.296
- https://code.claude.com/docs/en/mcp#tool-search-for-mcp-server-authors
- https://code.claude.com/docs/en/mcp#environment-variable-expansion-in-mcp-json
- https://code.claude.com/docs/en/sub-agents
- https://code.claude.com/docs/en/changelog#2-1-304
- https://code.claude.com/docs/en/changelog#2-1-305
- https://code.claude.com/docs/en/mcp#tool-search-through-an-llm-gateway
- https://code.claude.com/docs/en/managed-mcp#how-allowlists-and-denylists-apply-to-the-managed-set
- https://code.claude.com/docs/en/mcp#mcp-tasks-that-run-on-the-server
- https://code.claude.com/docs/en/mcp#what-a-call-needs-to-become-an-mcp-task
- https://code.claude.com/docs/en/mcp#make-claude-wait-for-the-result-of-an-mcp-task
- https://code.claude.com/docs/en/mcp#automatic-backgrounding-of-long-tool-calls
- https://code.claude.com/docs/en/mcp#time-limits-on-mcp-tool-calls
- https://code.claude.com/docs/en/changelog#2-1-307
- https://code.claude.com/docs/en/mcp#mark-tools-that-are-safe-to-call-twice
**مدل‌های سازگار**: Claude Fable 5، Claude Opus 5، Claude Sonnet 5، Claude Sonnet 4.6، Claude Opus 4.8، Claude Haiku 4.5
