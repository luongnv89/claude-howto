<!-- i18n-source: 05-mcp/README.md -->
<!-- i18n-source-sha: 63a1416 -->
<!-- i18n-date: 2026-04-09 -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../../resources/logos/claude-howto-logo.svg">
</picture>

# MCP (Model Context Protocol)

Ця папка містить вичерпну документацію та приклади конфігурацій MCP-серверів та їх використання з Claude Code.

## Огляд

MCP (Model Context Protocol) — це стандартизований спосіб доступу Claude до зовнішніх інструментів, API та джерел даних у реальному часі. На відміну від пам'яті, MCP забезпечує живий доступ до змінюваних даних.

Ключові характеристики:
- Доступ до зовнішніх сервісів у реальному часі
- Синхронізація даних у реальному часі
- Розширювана архітектура
- Безпечна автентифікація
- Взаємодія на основі інструментів

## Архітектура MCP

```mermaid
graph TB
    A["Claude"]
    B["MCP Server"]
    C["External Service"]

    A -->|Request: list_issues| B
    B -->|Query| C
    C -->|Data| B
    B -->|Response| A

    A -->|Request: create_issue| B
    B -->|Action| C
    C -->|Result| B
    B -->|Response| A

    style A fill:#e1f5fe,stroke:#333,color:#333
    style B fill:#f3e5f5,stroke:#333,color:#333
    style C fill:#e8f5e9,stroke:#333,color:#333
```

## Екосистема MCP

```mermaid
graph TB
    A["Claude"] -->|MCP| B["Filesystem<br/>MCP Server"]
    A -->|MCP| C["GitHub<br/>MCP Server"]
    A -->|MCP| D["Database<br/>MCP Server"]
    A -->|MCP| E["Slack<br/>MCP Server"]
    A -->|MCP| F["Google Docs<br/>MCP Server"]

    B -->|File I/O| G["Local Files"]
    C -->|API| H["GitHub Repos"]
    D -->|Query| I["PostgreSQL/MySQL"]
    E -->|Messages| J["Slack Workspace"]
    F -->|Docs| K["Google Drive"]

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

## Методи встановлення MCP

Claude Code підтримує кілька транспортних протоколів для підключення до MCP-серверів:

### HTTP-транспорт (рекомендовано)

```bash
# Базове HTTP-підключення
claude mcp add --transport http notion https://mcp.notion.com/mcp

# HTTP з заголовком автентифікації
claude mcp add --transport http secure-api https://api.example.com/mcp \
  --header "Authorization: Bearer your-token"
```

### Stdio-транспорт (локальний)

Для локально запущених MCP-серверів:

```bash
# Локальний Node.js-сервер
claude mcp add --transport stdio myserver -- npx @myorg/mcp-server

# Зі змінними оточення
claude mcp add --transport stdio myserver --env KEY=value -- npx server
```

### SSE-транспорт (застарілий)

Транспорт Server-Sent Events застарілий на користь `http`, але все ще підтримується:

```bash
claude mcp add --transport sse legacy-server https://example.com/sse
```

### Примітка для Windows

На нативній Windows (не WSL) використовуйте `cmd /c` для команд npx:

```bash
claude mcp add --transport stdio my-server -- cmd /c npx -y @some/package
```

### Автентифікація OAuth 2.0

Claude Code підтримує OAuth 2.0 для MCP-серверів, що його потребують. При підключенні до сервера з OAuth Claude Code обробляє весь потік автентифікації:

```bash
# Підключення до MCP-сервера з OAuth (інтерактивний потік)
claude mcp add --transport http my-service https://my-service.example.com/mcp

# Попередньо налаштовані облікові дані OAuth для неінтерактивного встановлення
claude mcp add --transport http my-service https://my-service.example.com/mcp \
  --client-id "your-client-id" \
  --client-secret "your-client-secret" \
  --callback-port 8080
```

| Функція | Опис |
|---------|------|
| **Інтерактивний OAuth** | Використовуйте `/mcp` для запуску OAuth-потоку через браузер |
| **Попередньо налаштовані OAuth-клієнти** | Вбудовані OAuth-клієнти для популярних сервісів: Notion, Stripe та інших (v2.1.30+) |
| **Попередньо налаштовані облікові дані** | Прапорці `--client-id`, `--client-secret`, `--callback-port` для автоматизованого встановлення |
| **Зберігання токенів** | Токени зберігаються безпечно у системному keychain |
| **Step-up auth** | Підтримка step-up автентифікації для привілейованих операцій |
| **Кешування виявлення** | Метадані OAuth discovery кешуються для швидших перепідключень |
| **Перевизначення метаданих** | `oauth.authServerMetadataUrl` у `.mcp.json` для перевизначення стандартного OAuth metadata discovery |

#### Перевизначення OAuth Metadata Discovery

Якщо ваш MCP-сервер повертає помилки на стандартному ендпоінті OAuth metadata (`/.well-known/oauth-authorization-server`), але має робочий OIDC-ендпоінт, ви можете вказати Claude Code отримувати метадані OAuth з конкретного URL. Встановіть `authServerMetadataUrl` в об'єкті `oauth` конфігурації сервера:

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

URL повинен використовувати `https://`. Ця опція потребує Claude Code v2.1.64 або новішої.

### MCP-конектори Claude.ai

MCP-сервери, налаштовані у вашому обліковому записі Claude.ai, автоматично доступні в Claude Code. Будь-які MCP-підключення, налаштовані через веб-інтерфейс Claude.ai, будуть доступні без додаткової конфігурації.

MCP-конектори Claude.ai також доступні в режимі `--print` (v2.1.83+), що дозволяє неінтерактивне та скриптове використання.

Для вимкнення MCP-серверів Claude.ai у Claude Code встановіть змінну оточення `ENABLE_CLAUDEAI_MCP_SERVERS` у `false`:

```bash
ENABLE_CLAUDEAI_MCP_SERVERS=false claude
```

> **Примітка:** Ця функція доступна лише для користувачів, авторизованих через облікові записи Claude.ai.

## Процес налаштування MCP

```mermaid
sequenceDiagram
    participant User
    participant Claude as Claude Code
    participant Config as Config File
    participant Service as External Service

    User->>Claude: Type /mcp
    Claude->>Claude: List available MCP servers
    Claude->>User: Show options
    User->>Claude: Select GitHub MCP
    Claude->>Config: Update configuration
    Config->>Claude: Activate connection
    Claude->>Service: Test connection
    Service-->>Claude: Authentication successful
    Claude->>User: ✅ MCP connected!
```

## Пошук інструментів MCP

Коли описи інструментів MCP перевищують 10% контекстного вікна, Claude Code автоматично вмикає пошук інструментів для ефективного вибору правильних інструментів без перевантаження контексту моделі.

| Налаштування | Значення | Опис |
|-------------|----------|------|
| `ENABLE_TOOL_SEARCH` | `auto` (за замовч.) | Автоматично вмикається, коли описи інструментів перевищують 10% контексту |
| `ENABLE_TOOL_SEARCH` | `auto:<N>` | Автоматично вмикається при користувацькому порозі `N` інструментів |
| `ENABLE_TOOL_SEARCH` | `true` | Завжди увімкнено незалежно від кількості інструментів |
| `ENABLE_TOOL_SEARCH` | `false` | Вимкнено; всі описи інструментів надсилаються повністю |

> **Примітка:** Пошук інструментів потребує Sonnet 4 або новіший, або Opus 4 або новіший. Моделі Haiku не підтримують пошук інструментів.

## Динамічне оновлення інструментів

Claude Code підтримує сповіщення MCP `list_changed`. Коли MCP-сервер динамічно додає, видаляє або змінює доступні інструменти, Claude Code отримує оновлення та автоматично коригує список інструментів — без потреби перепідключення або перезапуску.

## MCP Apps

MCP Apps — перше офіційне розширення MCP, що дозволяє викликам інструментів MCP повертати інтерактивні UI-компоненти, які рендеряться безпосередньо в інтерфейсі чату. Замість текстових відповідей MCP-сервери можуть надавати інтерактивні дашборди, форми, візуалізації даних та багатокрокові воркфлови — все відображається прямо в розмові.

## MCP Elicitation

MCP-сервери можуть запитувати структурований ввід від користувача через інтерактивні діалоги (v2.1.49+). Це дозволяє MCP-серверу запитувати додаткову інформацію під час воркфлову — наприклад, підтвердження, вибір зі списку опцій або заповнення обов'язкових полів — додаючи інтерактивність до взаємодії з MCP-серверами.

## Ліміт описів інструментів та інструкцій

Починаючи з v2.1.84, Claude Code встановлює **ліміт 2 КБ** на описи та інструкції інструментів для кожного MCP-сервера. Це запобігає споживанню надмірного контексту окремими серверами з занадто багатослівними визначеннями інструментів.

## MCP Prompts як слеш-команди

MCP-сервери можуть надавати промпти, що відображаються як слеш-команди в Claude Code. Промпти доступні за конвенцією іменування:

```
/mcp__<server>__<prompt>
```

Наприклад, якщо сервер `github` надає промпт `review`, його можна викликати як `/mcp__github__review`.

## Дедуплікація серверів

Коли один і той самий MCP-сервер визначений на кількох рівнях (local, project, user), локальна конфігурація має пріоритет. Це дозволяє перевизначати налаштування MCP рівня проєкту або користувача локальними кастомізаціями без конфліктів.

## MCP-ресурси через @-згадки

Ви можете посилатися на MCP-ресурси безпосередньо в промптах через синтаксис `@`:

```
@server-name:protocol://resource/path
```

Наприклад, для посилання на конкретний ресурс бази даних:

```
@database:postgres://mydb/users
```

Це дозволяє Claude отримувати та включати вміст MCP-ресурсів у контекст розмови.

## Рівні MCP

Конфігурації MCP можна зберігати на різних рівнях з різним ступенем поширення:

| Рівень | Розташування | Опис | Доступний для | Потребує підтвердження |
|--------|-------------|------|---------------|----------------------|
| **Local** (за замовч.) | `~/.claude.json` (під шляхом проєкту) | Приватний для поточного користувача, лише поточний проєкт (раніше називався `project`) | Лише ви | Ні |
| **Project** | `.mcp.json` | Комітиться в git-репозиторій | Члени команди | Так (при першому використанні) |
| **User** | `~/.claude.json` | Доступний у всіх проєктах (раніше називався `global`) | Лише ви | Ні |

### Використання рівня Project

Зберігайте конфігурації MCP, специфічні для проєкту, у `.mcp.json`:

```json
{
  "mcpServers": {
    "github": {
      "type": "http",
      "url": "https://api.github.com/mcp"
    }
  }
}
```

Члени команди побачать запит на підтвердження при першому використанні MCP проєкту.

## Управління конфігурацією MCP

### Додавання MCP-серверів

```bash
# Додати HTTP-сервер
claude mcp add --transport http github https://api.github.com/mcp

# Додати локальний stdio-сервер
claude mcp add --transport stdio database -- npx @company/db-server

# Список всіх MCP-серверів
claude mcp list

# Деталі конкретного сервера
claude mcp get github

# Видалити MCP-сервер
claude mcp remove github

# Скинути вибори підтвердження для проєкту
claude mcp reset-project-choices

# Імпорт з Claude Desktop
claude mcp add-from-claude-desktop
```

## Таблиця доступних MCP-серверів

| MCP-сервер | Призначення | Типові інструменти | Авторизація | Реальний час |
|-----------|------------|-------------------|-------------|-------------|
| **Filesystem** | Файлові операції | read, write, delete | Дозволи ОС | ✅ Так |
| **GitHub** | Управління репозиторіями | list_prs, create_issue, push | OAuth | ✅ Так |
| **Slack** | Командна комунікація | send_message, list_channels | Токен | ✅ Так |
| **Database** | SQL-запити | query, insert, update | Облікові дані | ✅ Так |
| **Google Docs** | Доступ до документів | read, write, share | OAuth | ✅ Так |
| **Asana** | Управління проєктами | create_task, update_status | API Key | ✅ Так |
| **Stripe** | Платіжні дані | list_charges, create_invoice | API Key | ✅ Так |
| **Memory** | Постійна пам'ять | store, retrieve, delete | Локальна | ❌ Ні |

## Практичні приклади

### Приклад 1: Конфігурація GitHub MCP

**Файл:** `.mcp.json` (корінь проєкту)

```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "${GITHUB_TOKEN}"
      }
    }
  }
}
```

**Доступні інструменти GitHub MCP:**

#### Управління Pull Request
- `list_prs` — список усіх PR у репозиторії
- `get_pr` — деталі PR, включаючи diff
- `create_pr` — створення нового PR
- `update_pr` — оновлення опису/назви PR
- `merge_pr` — мердж PR у main
- `review_pr` — додавання коментарів рев'ю

**Приклад запиту:**
```
/mcp__github__get_pr 456

# Повертає:
Title: Add dark mode support
Author: @alice
Description: Implements dark theme using CSS variables
Status: OPEN
Reviewers: @bob, @charlie
```

#### Управління Issue
- `list_issues` — список усіх issue
- `get_issue` — деталі issue
- `create_issue` — створення нового issue
- `close_issue` — закриття issue
- `add_comment` — додавання коментаря

#### Інформація про репозиторій
- `get_repo_info` — деталі репозиторію
- `list_files` — структура файлового дерева
- `get_file_content` — читання вмісту файлу
- `search_code` — пошук по кодовій базі

#### Операції з комітами
- `list_commits` — історія комітів
- `get_commit` — деталі конкретного коміту
- `create_commit` — створення нового коміту

**Налаштування**:
```bash
export GITHUB_TOKEN="your_github_token"
# Або додайте через CLI:
claude mcp add --transport stdio github -- npx @modelcontextprotocol/server-github
```

### Підстановка змінних оточення в конфігурації

Конфігурації MCP підтримують підстановку змінних оточення з резервними значеннями. Синтаксис `${VAR}` та `${VAR:-default}` працює в полях: `command`, `args`, `env`, `url` та `headers`.

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

Змінні розгортаються під час виконання:
- `${VAR}` — використовує змінну оточення, помилка якщо не встановлена
- `${VAR:-default}` — використовує змінну оточення, резервне значення якщо не встановлена

### Приклад 2: Налаштування Database MCP

**Конфігурація:**

```json
{
  "mcpServers": {
    "database": {
      "command": "npx",
      "args": ["@modelcontextprotocol/server-database"],
      "env": {
        "DATABASE_URL": "postgresql://user:pass@localhost/mydb"
      }
    }
  }
}
```

**Приклад використання:**

```markdown
User: Fetch all users with more than 10 orders

Claude: I'll query your database to find that information.

# Використання інструменту MCP database:
SELECT u.*, COUNT(o.id) as order_count
FROM users u
LEFT JOIN orders o ON u.id = o.user_id
GROUP BY u.id
HAVING COUNT(o.id) > 10
ORDER BY order_count DESC;

# Результати:
- Alice: 15 orders
- Bob: 12 orders
- Charlie: 11 orders
```

**Налаштування**:
```bash
export DATABASE_URL="postgresql://user:pass@localhost/mydb"
# Або додайте через CLI:
claude mcp add --transport stdio database -- npx @modelcontextprotocol/server-database
```

### Приклад 3: Мульти-MCP воркфлов

**Сценарій: генерація щоденного звіту**

```markdown
# Щоденний звіт з використанням кількох MCP

## Налаштування
1. GitHub MCP — метрики PR
2. Database MCP — дані продажів
3. Slack MCP — публікація звіту
4. Filesystem MCP — збереження звіту

## Воркфлов

### Крок 1: Отримання даних GitHub
/mcp__github__list_prs completed:true last:7days

### Крок 2: Запит до бази даних
SELECT COUNT(*) as sales, SUM(amount) as revenue
FROM orders
WHERE created_at > NOW() - INTERVAL '1 day'

### Крок 3: Генерація звіту

### Крок 4: Збереження у файлову систему

### Крок 5: Публікація в Slack
```

### Приклад 4: Операції Filesystem MCP

**Конфігурація:**

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

**Доступні операції:**

| Операція | Команда | Призначення |
|---------|---------|------------|
| Список файлів | `ls ~/projects` | Показати вміст каталогу |
| Читання файлу | `cat src/main.ts` | Читання вмісту файлу |
| Запис файлу | `create docs/api.md` | Створення нового файлу |
| Редагування файлу | `edit src/app.ts` | Модифікація файлу |
| Пошук | `grep "async function"` | Пошук у файлах |
| Видалення | `rm old-file.js` | Видалення файлу |

## MCP vs Пам'ять: матриця вибору

```mermaid
graph TD
    A["Need external data?"]
    A -->|No| B["Use Memory"]
    A -->|Yes| C["Does it change frequently?"]
    C -->|No/Rarely| B
    C -->|Yes/Often| D["Use MCP"]

    B -->|Stores| E["Preferences<br/>Context<br/>History"]
    D -->|Accesses| F["Live APIs<br/>Databases<br/>Services"]

    style A fill:#fff3e0,stroke:#333,color:#333
    style B fill:#e1f5fe,stroke:#333,color:#333
    style C fill:#fff3e0,stroke:#333,color:#333
    style D fill:#f3e5f5,stroke:#333,color:#333
    style E fill:#e8f5e9,stroke:#333,color:#333
    style F fill:#e8f5e9,stroke:#333,color:#333
```

## Патерн запит/відповідь

```mermaid
sequenceDiagram
    participant App as Claude
    participant MCP as MCP Server
    participant DB as Database

    App->>MCP: Request: "SELECT * FROM users WHERE id=1"
    MCP->>DB: Execute query
    DB-->>MCP: Result set
    MCP-->>App: Return parsed data
    App->>App: Process result
    App->>App: Continue task

    Note over MCP,DB: Real-time access<br/>No caching
```

## Змінні оточення

Зберігайте конфіденційні облікові дані у змінних оточення:

```bash
# ~/.bashrc або ~/.zshrc
export GITHUB_TOKEN="ghp_xxxxxxxxxxxxx"
export DATABASE_URL="postgresql://user:pass@localhost/mydb"
export SLACK_TOKEN="xoxb-xxxxxxxxxxxxx"
```

Потім посилайтесь на них у конфігурації MCP:

```json
{
  "env": {
    "GITHUB_TOKEN": "${GITHUB_TOKEN}"
  }
}
```

## Claude як MCP-сервер (`claude mcp serve`)

Сам Claude Code може працювати як MCP-сервер для інших додатків. Це дозволяє зовнішнім інструментам, редакторам та системам автоматизації використовувати можливості Claude через стандартний протокол MCP.

```bash
# Запуск Claude Code як MCP-сервера через stdio
claude mcp serve
```

Інші додатки можуть підключатися до цього сервера як до будь-якого stdio-сервера MCP. Наприклад, додавання Claude Code як MCP-сервера в іншому екземплярі Claude Code:

```bash
claude mcp add --transport stdio claude-agent -- claude mcp serve
```

Це корисно для побудови мультиагентних воркфловів, де один екземпляр Claude оркеструє інший.

## Managed MCP Configuration (Enterprise)

Для корпоративних розгортань IT-адміністратори можуть застосовувати політики MCP-серверів через конфігураційний файл `managed-mcp.json`. Цей файл забезпечує ексклюзивний контроль над дозволеними або заблокованими MCP-серверами на рівні організації.

**Розташування:**
- macOS: `/Library/Application Support/ClaudeCode/managed-mcp.json`
- Linux: `~/.config/ClaudeCode/managed-mcp.json`
- Windows: `%APPDATA%\ClaudeCode\managed-mcp.json`

**Функції:**
- `allowedMcpServers` — білий список дозволених серверів
- `deniedMcpServers` — чорний список заборонених серверів
- Підтримує зіставлення за назвою сервера, командою та URL-патернами
- Загальноорганізаційні політики MCP застосовуються перед конфігурацією користувача
- Запобігає неавторизованим підключенням серверів

**Приклад конфігурації:**

```json
{
  "allowedMcpServers": [
    {
      "serverName": "github",
      "serverUrl": "https://api.github.com/mcp"
    },
    {
      "serverName": "company-internal",
      "serverCommand": "company-mcp-server"
    }
  ],
  "deniedMcpServers": [
    {
      "serverName": "untrusted-*"
    },
    {
      "serverUrl": "http://*"
    }
  ]
}
```

> **Примітка:** Коли і `allowedMcpServers`, і `deniedMcpServers` збігаються з сервером, правило заборони має пріоритет.

## MCP-сервери плагінів

Плагіни можуть включати власні MCP-сервери, які автоматично доступні при встановленні плагіна. MCP-сервери плагінів визначаються двома способами:

1. **Окремий `.mcp.json`** — розміщення файлу `.mcp.json` у кореневому каталозі плагіна
2. **Вбудований у `plugin.json`** — визначення MCP-серверів безпосередньо у маніфесті плагіна

Використовуйте змінну `${CLAUDE_PLUGIN_ROOT}` для посилання на шляхи відносно каталогу встановлення плагіна:

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

## MCP, обмежений субагентом

MCP-сервери можна визначати вбудовано у фронтматері агента через ключ `mcpServers:`, обмежуючи їх конкретним субагентом, а не всім проєктом. Це корисно, коли агенту потрібен доступ до конкретного MCP-сервера, який не потрібен іншим агентам у воркфлові.

```yaml
---
mcpServers:
  my-tool:
    type: http
    url: https://my-tool.example.com/mcp
---

You are an agent with access to my-tool for specialized operations.
```

MCP-сервери, обмежені субагентом, доступні лише в контексті виконання цього агента і не поширюються на батьківського чи суміжних агентів.

## Ліміти виводу MCP

Claude Code встановлює ліміти на вивід інструментів MCP для запобігання переповненню контексту:

| Ліміт | Поріг | Поведінка |
|-------|-------|----------|
| **Попередження** | 10 000 токенів | Відображається попередження про великий вивід |
| **Максимум за замовч.** | 25 000 токенів | Вивід обрізається за цим лімітом |
| **Збереження на диск** | 50 000 символів | Результати інструментів, що перевищують 50K символів, зберігаються на диск |

Максимальний ліміт виводу налаштовується через змінну оточення `MAX_MCP_OUTPUT_TOKENS`:

```bash
# Збільшити максимальний вивід до 50 000 токенів
export MAX_MCP_OUTPUT_TOKENS=50000
```

## Розв'язання проблеми роздування контексту через виконання коду

З масштабуванням MCP підключення до десятків серверів із сотнями або тисячами інструментів створює значну проблему: **роздування контексту** (context bloat). Це, мабуть, найбільша проблема MCP у масштабі, і інженерна команда Anthropic запропонувала елегантне рішення — використання виконання коду замість прямих викликів інструментів.

> **Джерело**: [Code Execution with MCP: Building More Efficient Agents](https://www.anthropic.com/engineering/code-execution-with-mcp) — блог Anthropic Engineering

### Проблема: два джерела марнування токенів

**1. Визначення інструментів перевантажують контекстне вікно**

Більшість MCP-клієнтів завантажують усі визначення інструментів наперед. При підключенні до тисяч інструментів модель повинна обробити сотні тисяч токенів, перш ніж прочитати запит користувача.

**2. Проміжні результати споживають додаткові токени**

Кожен проміжний результат інструменту проходить через контекст моделі. Наприклад, при перенесенні транскрипту зустрічі з Google Drive до Salesforce — повний транскрипт проходить через контекст **двічі**: при читанні та при записі в призначення. Дводинна зустріч може означати 50 000+ додаткових токенів.

```mermaid
graph LR
    A["Model"] -->|"Tool Call: getDocument"| B["MCP Server"]
    B -->|"Full transcript (50K tokens)"| A
    A -->|"Tool Call: updateRecord<br/>(re-sends full transcript)"| B
    B -->|"Confirmation"| A

    style A fill:#ffcdd2,stroke:#333,color:#333
    style B fill:#f3e5f5,stroke:#333,color:#333
```

### Рішення: MCP-інструменти як код-API

Замість передачі визначень інструментів та результатів через контекстне вікно, агент **пише код**, який викликає MCP-інструменти як API. Код виконується в ізольованому середовищі, і лише кінцевий результат повертається до моделі.

```mermaid
graph LR
    A["Model"] -->|"Writes code"| B["Code Execution<br/>Environment"]
    B -->|"Calls tools directly"| C["MCP Servers"]
    C -->|"Data stays in<br/>execution env"| B
    B -->|"Only final result<br/>(minimal tokens)"| A

    style A fill:#c8e6c9,stroke:#333,color:#333
    style B fill:#e1f5fe,stroke:#333,color:#333
    style C fill:#f3e5f5,stroke:#333,color:#333
```

#### Як це працює

MCP-інструменти представляються як файлове дерево типізованих функцій:

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

Кожен файл інструменту містить типізовану обгортку:

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

Агент пише код для оркестрації інструментів:

```typescript
import * as gdrive from './servers/google-drive';
import * as salesforce from './servers/salesforce';

// Дані передаються безпосередньо між інструментами — ніколи через модель
const transcript = (
  await gdrive.getDocument({ documentId: 'abc123' })
).content;

await salesforce.updateRecord({
  objectType: 'SalesMeeting',
  recordId: '00Q5f000001abcXYZ',
  data: { Notes: transcript }
});
```

**Результат: використання токенів знижується з ~150 000 до ~2 000 — зменшення на 98,7%.**

### Ключові переваги

| Перевага | Опис |
|---------|------|
| **Прогресивне розкриття** | Агент переглядає файлову систему для завантаження лише потрібних визначень інструментів |
| **Ефективність контексту** | Дані фільтруються/трансформуються в середовищі виконання перед поверненням до моделі |
| **Потужний контроль потоку** | Цикли, умови та обробка помилок виконуються в коді без повернення через модель |
| **Збереження конфіденційності** | Проміжні дані (персональні дані, чутливі записи) залишаються в середовищі виконання; ніколи не потрапляють у контекст моделі |
| **Збереження стану** | Агенти можуть зберігати проміжні результати у файли та будувати повторно використовувані функції |

#### Приклад: фільтрація великих наборів даних

```typescript
// Без виконання коду — всі 10 000 рядків проходять через контекст
// TOOL CALL: gdrive.getSheet(sheetId: 'abc123')
//   -> повертає 10 000 рядків у контекст

// З виконанням коду — фільтрація в середовищі виконання
const allRows = await gdrive.getSheet({ sheetId: 'abc123' });
const pendingOrders = allRows.filter(
  row => row["Status"] === 'pending'
);
console.log(`Found ${pendingOrders.length} pending orders`);
console.log(pendingOrders.slice(0, 5)); // Лише 5 рядків потрапляють до моделі
```

#### Приклад: цикл без повернення через модель

```typescript
// Опитування для сповіщення про деплой — виконується цілком у коді
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

### Компроміси

Виконання коду додає власну складність. Запуск коду, згенерованого агентом, потребує:

- **Безпечного ізольованого середовища виконання** з відповідними лімітами ресурсів
- **Моніторингу та логування** виконаного коду
- Додаткових **інфраструктурних витрат** порівняно з прямими викликами інструментів

Переваги — зменшення вартості токенів, нижча затримка, покращена композиція інструментів — слід зважити проти цих витрат на впровадження. Для агентів з кількома MCP-серверами прямі виклики інструментів можуть бути простішими. Для агентів у масштабі (десятки серверів, сотні інструментів) виконання коду — значне покращення.

### MCPorter: середовище виконання для композиції MCP-інструментів

[MCPorter](https://github.com/steipete/mcporter) — TypeScript-середовище виконання та CLI-інструментарій для виклику MCP-серверів без шаблонного коду, що допомагає зменшити роздування контексту через вибіркове надання інструментів та типізовані обгортки.

**Що вирішує:** замість завантаження всіх визначень інструментів з усіх MCP-серверів наперед, MCPorter дозволяє виявляти, інспектувати та викликати конкретні інструменти за потребою — тримаючи контекст компактним.

**Ключові функції:**

| Функція | Опис |
|---------|------|
| **Zero-config discovery** | Автовиявлення MCP-серверів з Cursor, Claude, Codex або локальних конфігурацій |
| **Типізовані клієнти інструментів** | `mcporter emit-ts` генерує `.d.ts` інтерфейси та готові обгортки |
| **Composable API** | `createServerProxy()` надає інструменти як camelCase-методи з хелперами `.text()`, `.json()`, `.markdown()` |
| **Генерація CLI** | `mcporter generate-cli` перетворює будь-який MCP-сервер у CLI з фільтрацією `--include-tools` / `--exclude-tools` |
| **Приховування параметрів** | Опціональні параметри приховані за замовчуванням, зменшуючи багатослівність схеми |

**Встановлення:**

```bash
npx mcporter list          # Без встановлення — виявлення серверів миттєво
pnpm add mcporter          # Додати до проєкту
brew install steipete/tap/mcporter  # macOS через Homebrew
```

**Приклад — композиція інструментів у TypeScript:**

```typescript
import { createRuntime, createServerProxy } from "mcporter";

const runtime = await createRuntime();
const gdrive = createServerProxy(runtime, "google-drive");
const salesforce = createServerProxy(runtime, "salesforce");

// Дані передаються між інструментами без проходження через контекст моделі
const doc = await gdrive.getDocument({ documentId: "abc123" });
await salesforce.updateRecord({
  objectType: "SalesMeeting",
  recordId: "00Q5f000001abcXYZ",
  data: { Notes: doc.text() }
});
```

**Приклад — виклик інструменту через CLI:**

```bash
# Виклик конкретного інструменту
npx mcporter call linear.create_comment issueId:ENG-123 body:'Looks good!'

# Список доступних серверів та інструментів
npx mcporter list
```

MCPorter доповнює підхід з виконанням коду, описаний вище, надаючи інфраструктуру для виклику MCP-інструментів як типізованих API — спрощуючи утримання проміжних даних поза контекстом моделі.

## Найкращі практики

### Безпекові рекомендації

#### Рекомендовано ✅
- Використовуйте змінні оточення для всіх облікових даних
- Регулярно ротуйте токени та API-ключі (рекомендовано щомісяця)
- Використовуйте токени лише для читання, де можливо
- Обмежуйте область доступу MCP-серверів до мінімально необхідної
- Моніторте використання MCP-серверів та журнали доступу
- Використовуйте OAuth для зовнішніх сервісів, де доступно
- Впроваджуйте rate limiting для MCP-запитів
- Тестуйте MCP-підключення перед продакшен-використанням
- Документуйте всі активні MCP-підключення
- Тримайте пакети MCP-серверів оновленими

#### Не рекомендовано ❌
- Не хардкодьте облікові дані в конфігураційних файлах
- Не комітьте токени чи секрети в git
- Не поширюйте токени в командних чатах чи листах
- Не використовуйте персональні токени для командних проєктів
- Не надавайте зайвих дозволів
- Не ігноруйте помилки автентифікації
- Не відкривайте MCP-ендпоінти публічно
- Не запускайте MCP-сервери з правами root/admin
- Не кешуйте чутливі дані в журналах
- Не вимикайте механізми автентифікації

### Найкращі практики конфігурації

1. **Контроль версій**: тримайте `.mcp.json` у git, але використовуйте змінні оточення для секретів
2. **Мінімальні привілеї**: надавайте мінімальні дозволи для кожного MCP-сервера
3. **Ізоляція**: запускайте різні MCP-сервери в окремих процесах, де можливо
4. **Моніторинг**: логуйте всі MCP-запити та помилки для аудиту
5. **Тестування**: тестуйте всі конфігурації MCP перед розгортанням у продакшен

### Поради щодо продуктивності

- Кешуйте часто запитувані дані на рівні додатку
- Використовуйте конкретні MCP-запити для зменшення передачі даних
- Моніторте час відповіді MCP-операцій
- Розгляньте rate limiting для зовнішніх API
- Використовуйте пакетну обробку для кількох операцій

## Інструкції з встановлення

### Передумови
- Node.js та npm встановлені
- Claude Code CLI встановлений
- API-токени/облікові дані для зовнішніх сервісів

### Покрокове налаштування

1. **Додайте перший MCP-сервер** через CLI (приклад: GitHub):
```bash
claude mcp add --transport stdio github -- npx @modelcontextprotocol/server-github
```

   Або створіть файл `.mcp.json` у корені проєкту:
```json
{
  "mcpServers": {
    "github": {
      "command": "npx",
      "args": ["@modelcontextprotocol/server-github"],
      "env": {
        "GITHUB_TOKEN": "${GITHUB_TOKEN}"
      }
    }
  }
}
```

2. **Встановіть змінні оточення:**
```bash
export GITHUB_TOKEN="your_github_personal_access_token"
```

3. **Протестуйте підключення:**
```bash
claude /mcp
```

4. **Використовуйте MCP-інструменти:**
```bash
/mcp__github__list_prs
/mcp__github__create_issue "Title" "Description"
```

### Встановлення конкретних сервісів

**GitHub MCP:**
```bash
npm install -g @modelcontextprotocol/server-github
```

**Database MCP:**
```bash
npm install -g @modelcontextprotocol/server-database
```

**Filesystem MCP:**
```bash
npm install -g @modelcontextprotocol/server-filesystem
```

**Slack MCP:**
```bash
npm install -g @modelcontextprotocol/server-slack
```

## Усунення несправностей

### MCP-сервер не знайдено
```bash
# Перевірте, чи встановлений MCP-сервер
npm list -g @modelcontextprotocol/server-github

# Встановіть, якщо відсутній
npm install -g @modelcontextprotocol/server-github
```

### Помилка автентифікації
```bash
# Перевірте, чи встановлена змінна оточення
echo $GITHUB_TOKEN

# Перевстановіть, якщо потрібно
export GITHUB_TOKEN="your_token"

# Перевірте дозволи токена
# Дозволи GitHub-токена: https://github.com/settings/tokens
```

### Таймаут з'єднання
- Перевірте мережеве з'єднання: `ping api.github.com`
- Перевірте доступність API-ендпоінта
- Перевірте rate limits API
- Спробуйте збільшити таймаут у конфігурації
- Перевірте наявність фаєрволу або проксі

### MCP-сервер аварійно завершується
- Перевірте журнали MCP-сервера: `~/.claude/logs/`
- Перевірте, що всі змінні оточення встановлені
- Перевірте дозволи файлів
- Спробуйте перевстановити пакет MCP-сервера
- Перевірте конфліктуючі процеси на тому ж порту

## Пов'язані концепції

### Пам'ять vs MCP
- **Пам'ять**: зберігає постійні, незмінні дані (налаштування, контекст, історія)
- **MCP**: доступ до живих, змінюваних даних (API, бази даних, сервіси реального часу)

### Коли використовувати кожен
- **Пам'ять** для: налаштувань користувача, історії розмов, засвоєного контексту
- **MCP** для: поточних GitHub issue, живих запитів до бази даних, даних реального часу

### Інтеграція з іншими функціями Claude
- Комбінуйте MCP з пам'яттю для збагаченого контексту
- Використовуйте MCP-інструменти в промптах для кращого міркування
- Поєднуйте кілька MCP для складних воркфловів

## Додаткові ресурси

- [Офіційна документація MCP](https://code.claude.com/docs/en/mcp)
- [Специфікація протоколу MCP](https://modelcontextprotocol.io/specification)
- [GitHub-репозиторій MCP](https://github.com/modelcontextprotocol/servers)
- [Доступні MCP-сервери](https://github.com/modelcontextprotocol/servers)
- [MCPorter](https://github.com/steipete/mcporter) — TypeScript-середовище та CLI для виклику MCP-серверів
- [Code Execution with MCP](https://www.anthropic.com/engineering/code-execution-with-mcp) — блог Anthropic Engineering
- [Довідник CLI Claude Code](https://code.claude.com/docs/en/cli-reference)
- [Документація Claude API](https://docs.anthropic.com)

---
**Останнє оновлення**: 9 квітня 2026
**Версія Claude Code**: 2.1.97
**Сумісні моделі**: Claude Sonnet 4.6, Claude Opus 4.6, Claude Haiku 4.5
