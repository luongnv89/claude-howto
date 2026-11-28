<!-- i18n-source: 06-hooks/README.md -->
<!-- i18n-source-sha: 63a1416 -->
<!-- i18n-date: 2026-04-09 -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../../resources/logos/claude-howto-logo.svg">
</picture>

# Хуки

Хуки — це автоматизовані скрипти, які виконуються у відповідь на конкретні події під час сесій Claude Code. Вони забезпечують автоматизацію, валідацію, управління дозволами та кастомні робочі процеси.

## Огляд

Хуки — це автоматичні дії (shell-команди, HTTP-вебхуки, LLM-промпти або оцінки субагентів), що виконуються автоматично при виникненні конкретних подій у Claude Code. Вони отримують JSON-вхід і повідомляють результати через коди виходу та JSON-вивід.

**Ключові можливості:**
- Автоматизація на основі подій
- Введення/виведення на основі JSON
- Підтримка типів хуків: command, prompt, HTTP та agent
- Відповідність шаблонам (pattern matching) для хуків, специфічних для інструментів

## Конфігурація

Хуки налаштовуються у файлах налаштувань з конкретною структурою:

- `~/.claude/settings.json` — налаштування користувача (усі проєкти)
- `.claude/settings.json` — налаштування проєкту (спільні, комітяться)
- `.claude/settings.local.json` — локальні налаштування проєкту (не комітяться)
- Керована політика (Managed policy) — загальноорганізаційні налаштування
- `hooks/hooks.json` плагіна — хуки з областю дії плагіна
- Frontmatter навичок/агентів — хуки часу життя компонентів

### Базова структура конфігурації

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

**Ключові поля:**

| Поле | Опис | Приклад |
|------|------|---------|
| `matcher` | Шаблон для відповідності назвам інструментів (чутливий до регістру) | `"Write"`, `"Edit\|Write"`, `"*"` |
| `hooks` | Масив визначень хуків | `[{ "type": "command", ... }]` |
| `type` | Тип хука: `"command"` (bash), `"prompt"` (LLM), `"http"` (вебхук), `"mcp_tool"` (виклик MCP-інструмента, v2.1.118+) або `"agent"` (субагент) | `"command"` |
| `command` | Shell-команда для виконання | `"$CLAUDE_PROJECT_DIR/.claude/hooks/format.sh"` |
| `timeout` | Необовʼязковий таймаут у секундах. За замовчуванням: 600 для command/http/mcp_tool, 30 для prompt, 60 для agent. | `30` |
| `once` | Якщо `true`, хук видаляється після першого успішного запуску (невдалі, заблоковані чи прострочені запуски його залишають). Лише у frontmatter навички; ігнорується в settings і frontmatter агента | `true` |
| `async` | Якщо `true`, виконується у фоні без блокування | `true` |
| `asyncRewake` | Якщо `true`, виконується у фоні та будить Claude при коді виходу 2. Неявно вмикає `async`. | `true` |
| `shell` | Приймає `"bash"` або `"powershell"`. За замовчуванням `"bash"`, або `"powershell"` у Windows, якщо Git Bash не встановлено. | `"bash"` |
| `statusMessage` | Власне повідомлення індикатора, що показується під час роботи хука | `"Форматування…"` |

> **Примітка**: Деякі події знижують типовий таймаут. `UserPromptSubmit` знижує типове значення для command, http і mcp_tool до 30 секунд, а `MessageDisplay` — до 10 секунд. Хуки `SessionEnd` мають спільний бюджет 1,5 секунди; якщо у ваших налаштуваннях указано довший `timeout` для окремого хука, Claude Code піднімає бюджет відповідно, до 60 секунд. У сесіях `claude -p` та Agent SDK Claude Code надсилає сигнал прогресу (heartbeat) кожні 30 секунд, поки хуки виконуються довго (v2.1.323), тож хост на кшталт Claude Desktop не завершить хід як завислий, щойно міститиме цю версію.

### Шаблони matcher

| Шаблон | Опис | Приклад |
|--------|------|---------|
| Точний рядок | Відповідає конкретному інструменту | `"Write"` |
| Regex-шаблон | Відповідає кільком інструментам | `"Edit\|Write"` |
| Розділені комою | Відповідає будь-якому інструменту зі списку (v2.1.191+) | `"Write,Edit"` |
| Підстановочний знак | Відповідає всім інструментам | `"*"` або `""` |
| MCP-інструменти | Шаблон сервера та інструмента | `"mcp__memory__.*"` |

> **Matcher збігаються точно (v2.1.195+).** Ідентифікатор із дефісом (наприклад, назва MCP-інструмента, що містить дефіс) більше не збігається випадково за підрядком з іншим інструментом. Matcher, розділені комою, як-от `"Write,Edit"`, спрацьовують на будь-який інструмент зі списку — попередні збірки мовчки ніколи їх не запускали.

**Значення matcher для InstructionsLoaded:**

| Значення matcher | Опис |
|-----------------|------|
| `session_start` | Інструкції завантажені при запуску сесії |
| `nested_traversal` | Інструкції завантажені при обході вкладених каталогів |
| `path_glob_match` | Інструкції завантажені через відповідність glob-шаблону шляху |

### Звуження за умовами `if` (шляхи аргументів інструмента)

Поле `matcher` обирає хук за **назвою інструмента** (`"Write"`, `"Edit|Write"`, `"*"`). Щоб відфільтрувати вужче за **аргументами** інструмента — наприклад, запускати хук лише коли правка торкається `src/`, або охопити читання файлів із секретами — додайте умову `if` до окремого обробника хука. Це відрізняється від matcher за назвою інструмента: `matcher` визначає *який інструмент*, а `if` — *який виклик*.

`if` використовує [синтаксис правил дозволів](https://code.claude.com/docs/en/permissions) (`ToolName(pattern)`) і обчислюється водночас для назви інструмента **та** його аргументів. Для `Read`/`Edit`/`Write` шаблон шляху слідує семантиці gitignore з тими самими якорями, що й правила дозволів: гола назва на кшталт `.env` збігається на будь-якій глибині, `src/**` — відносно поточного каталогу, `/src/**` — відносно кореня проєкту, `~/...` — відносно вашого домашнього каталогу, а `//...` — абсолютний шлях файлової системи.

Поле `if` розташовується на **рівні обробника хука** — це сусід `type` і `command`, всередині масиву `hooks`, — а не на `matcher`:

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

Приклади дійсних шаблонів `if`: `Edit(src/**)` (редагування в `src/`), `Read(~/.ssh/**)` (читання будь-яких SSH-ключів), `Read(.env)` (будь-який `.env` у поточному каталозі та нижче), `Bash(git push *)` (лише підкоманди `git push`).

> **Оновлення v2.1.214**: односегментний шаблон `dir/**` в умові `if` хука (як `Edit(src/**)`) тепер збігається лише з `<cwd>/dir` — а не з цим каталогом на будь-якій глибині дерева. Раніше `src/**` збігався також із `foo/src/**`. Якщо потрібен збіг на будь-якій глибині, використовуйте `**/dir/**`. **Важливо**: це звуження стосується лише умов `if:` хуків і авто-затвердження allow-правил — правила дозволів deny/ask досі збігаються з `dir/**` на будь-якій глибині.

> **Оновлення v2.1.314**: шаблони `if` на кшталт `Monitor(tail *)` збігаються з shell-командами, які запускає інструмент Monitor, так само як `Bash(tail *)` збігається з командами Bash. Хуки з matcher `Bash` також запускаються на shell-командах Monitor; вони можуть блокувати чи питати, але не затверджувати або переписувати їх.

## Типи хуків

Claude Code підтримує пʼять типів хуків:

### Command-хуки

Тип за замовчуванням. Виконує shell-команду та комунікує через JSON stdin/stdout і коди виходу.

```json
{
  "type": "command",
  "command": "python3 \"$CLAUDE_PROJECT_DIR/.claude/hooks/validate.py\"",
  "timeout": 60
}
```

#### Exec-форма (`args`)

> Додано у v2.1.139.

Замість shell-форми `"command": "..."` command-хук може запускати бінарник напряму через `execve()` за допомогою масиву `args`. Парсингу shell немає, тому заповнювачі шляхів не потребують лапок, а конфігурація імунна до вразливостей shell-інʼєкцій.

```json
{
  "type": "command",
  "command": "python3",
  "args": ["${CLAUDE_PROJECT_DIR}/.claude/hooks/validate.py", "--strict"],
  "timeout": 60
}
```

`command` завжди обовʼязковий: коли задано `args`, `command` — це виконуваний файл для запуску (розвʼязується через `PATH`), а `args` — вектор його аргументів. Пропустіть `args` (shell-форма), коли потрібні пайпи, перенаправлення, ланцюжки `&&` або shell-розширення; використовуйте `args`, коли викликаєте один бінарник з аргументами.

### HTTP-хуки

> Додано у v2.1.63.

Віддалені вебхук-ендпоінти, які отримують той самий JSON-вхід, що й command-хуки. HTTP-хуки надсилають POST JSON на URL і отримують JSON-відповідь. HTTP-хуки маршрутизуються через пісочницю (sandbox), коли вона увімкнена. Інтерполяція змінних оточення у значення заголовків вимагає явного списку `allowedEnvVars` з міркувань безпеки.

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

**Ключові властивості:**
- `"type": "http"` — ідентифікує як HTTP-хук
- `"url"` — URL ендпоінту вебхука
- Маршрутизується через sandbox, коли sandbox увімкнено
- Вимагає явного списку `allowedEnvVars` для будь-якої інтерполяції змінних оточення у значеннях `headers`

### Prompt-хуки

Промпти, оцінювані LLM, де вміст хука є промптом, який оцінює Claude. Переважно використовуються з подіями `Stop` та `SubagentStop` для інтелектуальної перевірки завершення завдань.

```json
{
  "type": "prompt",
  "prompt": "Evaluate if Claude completed all requested tasks.",
  "timeout": 30
}
```

LLM оцінює промпт і повертає структуроване рішення (деталі див. у [Хуки на основі промптів](#хуки-на-основі-промптів)).

### MCP tool-хуки

> Додано у v2.1.118.

Тип `mcp_tool` викликає налаштований MCP-інструмент напряму; конфігурація посилається на ім'я MCP-сервера та інструмента, а не на shell-команду чи URL. Корисно, коли логіка валідації або реакції вже живе в налаштованому вами MCP-сервері.

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

**Ключові властивості:**
- `"type": "mcp_tool"` — ідентифікує як MCP tool-хук
- `"server"` — ім'я налаштованого MCP-сервера
- `"tool"` — ім'я інструмента, який слід викликати на цьому сервері
- `"input"` — необовʼязкові аргументи, передані інструменту; рядкові значення підтримують підстановку `${path}` із JSON-входу хука, як-от `"${tool_input.file_path}"`

Аргументи інструмента походять з `input` (з підстановкою `${path}`), а не безпосередньо з входу хука. Налаштування MCP-серверів див. у [налаштуванні MCP-серверів](../05-mcp/README.md). Якщо Claude Code не може прочитати відповідь інструмента (наприклад, відповідь понад 16 MiB від stdio- чи HTTP-сервера), хук `mcp_tool` на `PreToolUse` не дає вердикту, і виклик інструмента відхилено (v2.1.321; раніші версії пропускали хук).

### Agent-хуки

Хуки верифікації на основі субагентів, які створюють виділеного агента для оцінки умов або виконання складних перевірок. На відміну від prompt-хуків (однокрокова оцінка LLM), agent-хуки можуть використовувати інструменти та виконувати багатокрокове міркування.

```json
{
  "type": "agent",
  "prompt": "Verify the code changes follow our architecture guidelines. Check the relevant design docs and compare.",
  "timeout": 120
}
```

> **Примітка**: Agent-хуки є експериментальними і можуть змінитися.

> **Примітка**: Починаючи з v2.1.280, agent-хуки не запускаються на `PermissionRequest` — їхня відповідь ніколи не могла дозволити чи відхилити запит. Використовуйте там хук типу command або HTTP, що повертає об'єкт рішення (`ok: false` prompt-хука не діє на `PermissionRequest`).

**Ключові властивості:**
- `"type": "agent"` — ідентифікує як agent-хук
- `"prompt"` — опис завдання для субагента
- Агент може використовувати інструменти (Read, Grep, Bash тощо) для оцінки
- Повертає структуроване рішення, аналогічне prompt-хукам

## Події хуків

Claude Code підтримує **33 події хуків**:

| Подія | Коли спрацьовує | Вхід matcher | Може блокувати | Типове використання |
|-------|----------------|-------------|----------------|---------------------|
| **SessionStart** | Початок/відновлення/очищення/компакція/форк сесії | startup/resume/clear/compact/fork | Ні | Налаштування середовища |
| **Setup** | `--init-only` або `--init`/`--maintenance` з `-p` (підготовка CI/скриптів) | `init`/`maintenance` | Ні | Провізіонування інструментів, встановлення залежностей |
| **InstructionsLoaded** | Після завантаження CLAUDE.md або файлу правил | Причина завантаження (`session_start`/`nested_traversal`/`path_glob_match`/`include`/`compact`) | Ні | Аудит/логування для спостережуваності |
| **UserPromptSubmit** | Користувач подає промпт | (немає) | Так | Валідація промптів |
| **UserPromptExpansion** | Введена користувачем слеш-команда або MCP-промпт розгортається в промпт | Назва команди | Так | Перетворення або перевірка розгорнутого промпту |
| **MessageDisplay** | Під час відображення тексту відповіді асистента | (немає) | Ні | Перетворення або приховування показаного тексту (v2.1.152) |
| **PreToolUse** | Перед виконанням інструмента | Назва інструмента | Так (allow/deny/ask) | Валідація, модифікація вхідних даних |
| **PermissionRequest** | Показ діалогу дозволів | Назва інструмента | Так | Автозатвердження/відхилення |
| **PermissionDenied** | Режим auto відхиляє виклик інструмента | Назва інструмента | Ні | Логування, аналітика, політики |
| **PostToolUse** | Після успішного виконання інструмента | Назва інструмента | Ні | Контекст, зворотний звʼязок |
| **PostToolUseFailure** | Невдале виконання інструмента | Назва інструмента | Ні | Обробка помилок, логування |
| **PostToolBatch** | Після завершення пакета викликів інструментів | (немає) | Так | Зведена звітність, пакетна валідація |
| **Notification** | Надсилання сповіщення | Тип сповіщення | Ні | Кастомні сповіщення |
| **SubagentStart** | Створення субагента | Назва типу агента | Ні | Налаштування субагента |
| **SubagentStop** | Завершення субагента | Назва типу агента | Так | Валідація субагента |
| **Stop** | Claude завершує відповідь | (немає) | Так | Перевірка завершення завдання |
| **StopFailure** | Помилка API завершує хід | Тип помилки (`rate_limit`, `overloaded`, `server_error`, …) | Ні | Відновлення після помилок, логування |
| **TeammateIdle** | Неактивність учасника Agent Teams | (немає) | Так | Координація учасників |
| **TaskCompleted** | Завдання позначено як виконане | (немає) | Так | Дії після завершення завдання |
| **TaskCreated** | Завдання створене через TaskCreate | (немає) | Так | Відстеження завдань, логування |
| **ConfigChange** | Зміна файлу конфігурації | Джерело конфігурації (`user_settings`/`project_settings`/`local_settings`/`policy_settings`/`skills`) | Так (крім policy) | Реакція на оновлення конфігурації |
| **CwdChanged** | Зміна робочого каталогу | (немає) | Ні | Налаштування для каталогу |
| **DirectoryAdded** | Новий робочий каталог зареєстровано під час сесії через `/add-dir` або control-запит SDK `register_repo_root` (v2.1.219) | `slash_command`/`register_repo_root` | Ні | Налаштування інструментів для доданого каталогу |
| **FileChanged** | Зміна відстежуваного файлу | Назви файлів для відстеження (наприклад, `.envrc\|.env`) | Ні | Моніторинг файлів, перебудова |
| **PreCompact** | Перед компакцією контексту | manual/auto | Так | Дії перед компакцією |
| **PostCompact** | Після завершення компакції | (немає) | Ні | Дії після компакції |
| **PreModelSwitch** | Перед тим, як Claude Code застосує запитану зміну моделі | Канонічна назва моделі, на яку відбувається перехід (з `to_model`) | Так | Контроль або блокування зміни моделі |
| **PostModelSwitch** | Після зміни моделі сесії, зокрема змін, які Claude Code робить сам (наприклад, відновлення моделі при відновленні сесії) | Канонічна назва моделі, на яку відбувся перехід (з `to_model`) | Ні | Логування або реакція на зміну моделі |
| **WorktreeCreate** | Створення робочого дерева (worktree) | (немає) | Так (повернення шляху) | Ініціалізація worktree |
| **WorktreeRemove** | Видалення робочого дерева | (немає) | Так (ненульовий код виходу зриває видалення) | Очищення worktree |
| **Elicitation** | MCP-сервер запитує введення користувача | Назва MCP-сервера | Так | Валідація введення |
| **ElicitationResult** | Відповідь користувача на elicitation | Назва MCP-сервера | Так | Обробка відповіді |
| **SessionEnd** | Завершення сесії | Причина завершення (`clear`/`resume`/`logout`/`prompt_input_exit`/`other`) | Ні | Очищення, фінальне логування |

> **`TaskCreated` і `TaskCompleted` потребують увімкнених todo-інструментів (v2.1.233).** Ці події виникають від todo / task-tracking інструментів (`TaskCreate`/`Get`/`Update`/`List`, `TodoWrite`), які **доступні за замовчуванням лише на моделях Claude 3.x, Opus 4 — 4.7, Sonnet 4 — 4.6 та Haiku 4.5**. На інших моделях хук лишається валідною конфігурацією, але просто ніколи не спрацьовує — без виводу і без помилки. Встановіть `CLAUDE_CODE_ENABLE_TODO_TOOLS=1`, щоб повернути їх.

### PreToolUse

Запускається після створення параметрів інструмента Claude і перед обробкою. Використовується для валідації або модифікації вхідних даних інструмента.

**Конфігурація:**
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

**Типові matcher:** `Agent`, `Bash`, `Glob`, `Grep`, `Read`, `Edit`, `Write`, `WebFetch`, `WebSearch`

**Управління виводом:**
- `permissionDecision`: `"allow"`, `"deny"`, `"ask"` або `"defer"`
  - `"allow"` пропускає запит дозволу (крім інструментів, які потребують взаємодії з користувачем, та інструментів конекторів, для яких організація встановила `ask`)
  - `"deny"` блокує виклик інструмента
  - `"ask"` просить користувача підтвердити
  - `"defer"` завершує хід, щоб інструмент можна було відновити пізніше, і працює лише в неінтерактивному режимі з `-p` (інтерактивні сесії записують попередження в журнал і ігнорують його); результат містить `stop_reason: "tool_deferred"`. `permissionDecisionReason`, `updatedInput` та `additionalContext` для цього значення ігноруються
  - Правила deny та ask обчислюються незалежно від того, що повертає хук. Якщо кілька хуків `PreToolUse` дають різні рішення, пріоритет такий: `deny` > `defer` > `ask` > `allow`
- `permissionDecisionReason`: Пояснення рішення. Показується користувачеві (не Claude) для `"ask"`; показується Claude для `"deny"`; для `"allow"` та `"defer"` записується лише в журнал налагодження (debug log)
- `updatedInput`: Замінні вхідні дані інструмента (замінюють увесь вхідний об'єкт). З v2.1.300 вони перевіряються так само, як власні вхідні дані Claude — невідомі ключі відкидаються, а вхідні дані, які інструмент відхиляє, призводять до відмови у виклику.

### PostToolUse

Запускається одразу після завершення інструмента. Використовується для верифікації, логування або надання контексту назад Claude.

**Конфігурація:**
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

**Управління виводом:**
- Рішення `"block"` подає Claude зворотний звʼязок
- `additionalContext`: Контекст, доданий для Claude

**Додаткові поля введення (v2.1.119):**

| Поле | Тип | Опис |
|------|-----|------|
| `duration_ms` | number | Час виконання інструмента в мілісекундах. Не враховує час у запитах дозволів та виконанні хуків PreToolUse. Доступне і в хуках `PostToolUse`, і в `PostToolUseFailure`. |

#### Відновлювані блокування (`continueOnBlock`, v2.1.139)

Command-хук, який повертає `"decision": "block"` на `PostToolUse`, додає `reason` поруч із результатом інструмента; Claude все ще бачить оригінальний вивід. `continueOnBlock` — поле **prompt**-хука (у command- і agent-хуків його немає): за замовчуванням prompt-хук, що повернув `ok: false` на `PostToolUse`, завершує хід і показує reason як рядок попередження. Встановіть `"continueOnBlock": true` на prompt-хуку, щоб натомість повернути reason до Claude та продовжити хід — модель прочитає відгук і спробує знову або скоригується.

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

Використовуйте це, коли `reason` хука — те, з чим Claude може щось зробити (наприклад, «цей файл лише для читання; пишіть в інше місце»); залишайте вимкненим, коли блокування має повністю зупинити хід.

### UserPromptSubmit

Запускається, коли користувач подає промпт, перед тим як Claude його обробить. З v2.1.299 хук запускається до розгортання навички чи кастомної команди, тож блокування промпту зупиняє й рядки оболонки `!` цієї команди; `UserPromptExpansion` спрацьовує після нього.

**Конфігурація:**
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

**Управління виводом:**
- `decision`: `"block"` для запобігання обробці
- `reason`: Пояснення у разі блокування
- `additionalContext`: Контекст, доданий до промпта

### Stop та SubagentStop

Запускаються, коли Claude завершує відповідь (Stop) або субагент завершує роботу (SubagentStop). Підтримують оцінку на основі промптів для інтелектуальної перевірки завершення завдань.

**Додаткове поле введення:** Обидва хуки `Stop` та `SubagentStop` отримують поле `last_assistant_message` у JSON-вході, що містить останнє повідомлення від Claude або субагента перед зупинкою. Це корисно для оцінки завершення завдання.

**Конфігурація:**
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

> **Ліміт безпеки на послідовні блокування (v2.1.143)**: якщо хук `Stop` повертає `"decision": "block"` (або встановлює `continue: false`) **8 разів підряд** в межах одного ходу, Claude Code перекриває наступне блокування і завершує хід. Пороговий ліміт можна перевизначити змінною оточення `CLAUDE_CODE_STOP_HOOK_BLOCK_CAP=<ціле>` (значення `0` повністю вимикає ліміт). Це захищає від зациклення ходу несправним Stop-хуком.

**Поле повернення (v2.1.163):** хук `Stop` або `SubagentStop` може повернути `hookSpecificOutput.additionalContext`, щоб дати Claude відгук і **продовжити хід без показу мітки помилки**. Раніше вплинути на модель із Stop-хука було незручно; тепер хук може чисто впорскнути контекст, уникаючи поведінки мітки помилки старих шляхів зворотного звʼязку (як-от `"decision": "block"`).

```json
{
  "hookSpecificOutput": {
    "hookEventName": "Stop",
    "additionalContext": "Reminder: run the test suite before declaring done."
  }
}
```

### SubagentStart

Запускається при початку виконання субагента. Вхід matcher — назва типу агента, що дозволяє хукам націлюватися на конкретні типи субагентів.

**Конфігурація:**
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

Запускається при старті або відновленні сесії. Може зберігати змінні оточення.

**Matcher:** `startup`, `resume`, `clear`, `compact`, `fork`

> **Оновлення v2.1.214**: сесії, створені через форк, тепер повідомляють джерело `"fork"` замість попереднього `"resume"`.

**Спеціальна можливість:** Використовуйте `CLAUDE_ENV_FILE` для збереження змінних оточення (також доступно в хуках `CwdChanged` та `FileChanged`):

```bash
#!/bin/bash
if [ -n "$CLAUDE_ENV_FILE" ]; then
  echo 'export NODE_ENV=development' >> "$CLAUDE_ENV_FILE"
fi
exit 0
```

**Сесійні виходи (v2.1.152):** хук `SessionStart` може повернути JSON для повторного сканування навичок і встановлення заголовка сесії:

```json
{
  "reloadSkills": true,
  "hookSpecificOutput": {
    "sessionTitle": "Payments migration"
  }
}
```

Значення верхнього рівня `reloadSkills: true` запускає повторне сканування навичок у тій самій сесії (та сама дія, що й команда `/reload-skills`), роблячи щойно встановлені хуком навички одразу доступними. `hookSpecificOutput.sessionTitle` встановлює показуваний заголовок сесії при старті та відновленні.

### SessionEnd

Запускається при завершенні сесії для очищення або фінального логування. Не може блокувати завершення.

**Значення поля reason:**
- `clear` — користувач очистив сесію
- `resume` — сесію змінено через інтерактивну `/resume`
- `logout` — користувач вийшов із системи
- `prompt_input_exit` — користувач вийшов через введення промпта
- `other` — інша причина

**Конфігурація:**
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

### Подія Notification

Оновлені matcher для подій сповіщень:
- `permission_prompt` — сповіщення про запит дозволу
- `idle_prompt` — сповіщення про стан простою
- `auth_success` — успішна автентифікація
- `elicitation_dialog` — MCP-сервер відкрив форму elicitation
- `elicitation_url_dialog` — MCP-сервер просить відкрити URL у браузері
- `elicitation_complete` — elicitation у режимі URL повідомив про завершення
- `elicitation_response` — відповідь elicitation надіслано назад серверу
- `agent_needs_input` — фоновий агент потребує введення (v2.1.198)
- `agent_completed` — фоновий агент завершив роботу (v2.1.198)
- `quota_auto_resume_fired` / `quota_auto_resume_stale` / `quota_auto_resume_disabled` — результати авто-відновлення після ліміту використання (v2.1.234)
- `plugin_notification` — мод викликав сповіщення через `$.ui.notify`; `title` хука — імʼя мода, якщо мод не задав власне

### PreModelSwitch

Запускається **перед** тим, як Claude Code застосує запитану зміну моделі — наприклад, коли ви виконуєте `/model`, або коли компонент просить іншу модель. Потребує v2.1.251 або новішої.

**Matcher:** канонічна назва моделі, на яку відбувається перехід, похідна від `to_model`. Збігайте точну модель (`claude-opus-5`) або сімейство через regex (`.*opus.*`).

**Поля введення:** крім загальних полів, хук отримує `from_model` (модель, що використовувалася до переходу) та `to_model` (запитана модель).

**Може блокувати:** так. Код виходу `2` блокує зміну і показує stderr як помилку, тож сесія зберігає поточну модель. Використовуйте для контролю чи вето змін моделі — наприклад, щоб у проекті з бюджетом не опинитися на найдорожчій моделі.

**Таймаут:** ця подія знижує типовий таймаут для `command`, `http` і `mcp_tool` до 30 секунд.

**Конфігурація:**
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
# gate-model-switch.sh - refuse a switch to Opus on this project
input=$(cat)
to_model=$(echo "$input" | jq -r '.to_model')

if [[ "$to_model" == *opus* ]]; then
  echo "This project is budgeted for Sonnet; staying on the current model." >&2
  exit 2
fi

exit 0
```

### PostModelSwitch

Запускається **після** зміни моделі сесії. Він також спрацьовує для змін, які Claude Code робить сам — як-от відновлення раніше обраної моделі при відновленні сесії — а не лише для запитаних вами переходів. Потребує v2.1.251 або новішої.

**Matcher:** як у `PreModelSwitch` — канонічна назва, похідна від `to_model`.

**Поля введення:** `from_model` та `to_model` разом із загальними полями.

**Може блокувати:** ні. Зміна вже відбулася; хук може лише спостерігати та реагувати.

**Таймаут:** ця подія знижує типовий таймаут для `command`, `http` і `mcp_tool` до 30 секунд.

**Конфігурація:**
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
# log-model-switch.sh - append every model change to a session log
input=$(cat)
from=$(echo "$input" | jq -r '.from_model')
to=$(echo "$input" | jq -r '.to_model')

echo "$(date -Iseconds) $from -> $to" >> ~/.claude/model-switches.log
exit 0
```

## Хуки з областю дії компонентів

Хуки можна прикріплювати до конкретних компонентів (навички, агенти, команди) у їхньому frontmatter:

**У SKILL.md, agent.md або command.md:**

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
          once: true  # Лише frontmatter навички: видаляється після першого успішного запуску
---
```

**Підтримувані події:** усі події хуків. Хуки субагента працюють лише поки субагент активний (`Stop` → `SubagentStop`); хуки навички реєструються під час її виклику й лишаються активними до кінця сесії.

Це дозволяє визначати хуки безпосередньо в компоненті, що їх використовує, зберігаючи повʼязаний код разом.

### Хуки у frontmatter субагента

Коли хук `Stop` визначений у frontmatter субагента, він автоматично перетворюється на хук `SubagentStop` з областю дії цього субагента. Це гарантує, що хук зупинки спрацьовує лише коли завершує роботу саме цей субагент, а не при зупинці основної сесії.

```yaml
---
name: code-review-agent
description: Automated code review subagent
hooks:
  Stop:
    - hooks:
        - type: prompt
          prompt: "Verify the code review is thorough and complete."
  # Наведений Stop-хук автоматично перетворюється на SubagentStop для цього субагента
---
```

## Подія PermissionRequest

Обробка запитів дозволів з кастомним форматом виводу:

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

## Вхідні та вихідні дані хуків

### JSON-вхід (через stdin)

Усі хуки отримують JSON-вхід через stdin:

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

**Загальні поля:**

| Поле | Опис |
|------|------|
| `session_id` | Унікальний ідентифікатор сесії |
| `transcript_path` | Шлях до файлу транскрипту розмови |
| `cwd` | Поточний робочий каталог |
| `prompt_id` | UUID промпта, що обробляється; корелює з атрибутом OpenTelemetry `prompt.id` (v2.1.196) |
| `hook_event_name` | Назва події, що запустила хук |
| `agent_id` | Ідентифікатор агента, що запускає хук |
| `agent_type` | Ім'я агента (наприклад, `"Explore"` або `"security-reviewer"`); присутнє лише тоді, коли сесія використовує `--agent` або хук спрацьовує всередині субагента |
| `worktree` | Шлях до git worktree, якщо агент працює в ньому |
| `effort.level` | (v2.1.133+) Рівень зусилля (effort) на момент запуску хука, включно з рівнем навички, субагента чи `ultrathink`: `low`, `medium`, `high`, `xhigh` або `max`. Щойно змінений рівень може з'явитися тут до того, як набере чинності |

### Коди виходу

| Код виходу | Значення | Поведінка |
|-----------|----------|----------|
| **0** | Успіх | Продовжити, розібрати JSON stdout |
| **2** | Блокуюча помилка | Заблокувати операцію, stderr показується як помилка |
| **Інші** | Неблокуюча помилка | Продовжити; сповіщення `<hook name> hook error` у транскрипті показує перший рядок stderr |

### JSON-вивід (stdout, код виходу 0)

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

> **`retry` (PermissionDenied)**: Використайте JSON `hookSpecificOutput.retry: true`, щоб повідомити модель, що вона може повторити відхилений виклик інструмента.

> **Галузь застосування (v2.1.121+):** `hookSpecificOutput.updatedToolOutput` тепер діє для **всіх** інструментів, а не лише MCP-інструментів. Хук `PostToolUse` на `Bash`, `Edit`, `Read` тощо може переписати вивід інструмента до того, як його побачить Claude — корисно для видалення секретів, нормалізації дифів чи фільтрації шумного виводу команд. Значення має відповідати структурі виводу інструмента — `Bash` повертає обʼєкт із `stdout`, `stderr`, `interrupted` та `isImage`; для вбудованих інструментів значення, що не відповідає, ігнорується і використовується оригінальний вивід. Приклад (видалення ANSI-керівних послідовностей з виводу `Bash`):
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

> **Застаріла форма рішення `PreToolUse`**: для `PreToolUse` поля верхнього рівня `decision` і `reason` **застарілі** — використовуйте натомість `hookSpecificOutput.permissionDecision` (`allow` / `deny` / `ask` / `defer`) та `permissionDecisionReason`. Пріоритет серед рішень: `deny` > `defer` > `ask` > `allow`. Зверніть увагу: `suppressOutput` приймається, але **не має жодного ефекту**.

> **Ліміт виводу**: рядки `additionalContext`, `systemMessage` та `initialUserMessage` хука, а також його простий stdout, кожен обмежені 10 000 символів. Довший вивід зберігається у файл у каталозі сесії і замінюється його шляхом та передпруженням перших 2 000 символів; Claude не просять читати файл. З v2.1.314 це стосується і хуків `PreCompact`, чиїй дуже великій вивід міг змусити компакцію зазнати невдачі або повторитися.

#### `terminalSequence` (v2.1.141)

Хуки можуть надсилати сирі OSC (operating system command) escape-послідовності, встановивши `terminalSequence` у JSON-виводі. Хост записує послідовність у свій керівний термінал, коли хук повертається — корисно для десктопних сповіщень, оновлень заголовка вікна та термінальних дзвіночків без власного TTY.

| Поле | Тип | Опис |
|-------|------|-------------|
| `terminalSequence` | string | Сира escape-послідовність (зазвичай OSC 9 / OSC 0 / OSC 777). Записується в термінал хоста дослівно. |

Приклад — десктопне сповіщення OSC 9, коли довге завдання завершується. ESC і BEL записуйте як JSON-escape (`\u001b`, `\u0007`) або будуйте значення через `printf` і `jq`; сирі керівні байти всередині JSON-рядка не розбираються:

```json
{
  "terminalSequence": "\u001b]9;Task complete\u0007"
}
```

Налаштуйте це на хуку `Stop`, щоб сповіщення спрацьовувало, коли Claude завершує хід. Підтримка послідовностей залежить від термінала: iTerm2, Windows Terminal і WezTerm підтримують OSC 9, а Kitty використовує OSC 99.

## Змінні оточення

| Змінна | Доступність | Опис |
|--------|------------|------|
| `CLAUDE_PROJECT_DIR` | Усі хуки | Абсолютний шлях до кореня проєкту |
| `CLAUDE_ENV_FILE` | SessionStart, CwdChanged, FileChanged | Шлях до файлу для збереження змінних оточення |
| `CLAUDE_CODE_REMOTE` | Усі хуки | `"true"` при роботі у віддаленому середовищі |
| `${CLAUDE_PLUGIN_ROOT}` | Хуки плагінів | Шлях до каталогу плагіна |
| `${CLAUDE_PLUGIN_DATA}` | Хуки плагінів | Шлях до каталогу даних плагіна |
| `CLAUDE_CODE_SESSIONEND_HOOKS_TIMEOUT_MS` | Хуки SessionEnd | Налаштовуваний таймаут у мілісекундах для хуків SessionEnd (перевизначає стандартний) |
| `CLAUDE_CODE_SESSION_ID` | Субпроцеси інструмента Bash (v2.1.132+) | UUID сесії; збігається з полем `session_id` у JSON-вході хука. Використовуйте для кореляції bash-логів із телеметрією хуків. |
| `CLAUDE_EFFORT` | Субпроцеси інструмента Bash і команди хуків (v2.1.133+) | Рівень зусилля (effort) на момент старту субпроцесу (`low`/`medium`/`high`/`xhigh`/`max`); збігається з `effort.level` у JSON-вході хука. |
| `CLAUDE_CODE_STOP_HOOK_BLOCK_CAP` | На рівні процесу (v2.1.143+) | Максимум послідовних блокувань Stop-хуків, після якого Claude Code перекриває наступне блокування і завершує хід (типово `8`). Значення `0` вимикає ліміт. |

## Хуки на основі промптів

Для подій `Stop` та `SubagentStop` можна використовувати оцінку на основі LLM:

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

**Схема відповіді LLM:**
```json
{
  "ok": false,
  "reason": "Tests were not run after the last edit"
}
```

`ok: true` дозволяє дію; `reason` обов'язковий, коли `ok` дорівнює `false`.

## Приклади

### Приклад 1: Валідатор Bash-команд (PreToolUse)

**Файл:** `.claude/hooks/validate-bash.py`

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
            sys.exit(2)  # Код виходу 2 = блокуюча помилка

    sys.exit(0)

if __name__ == "__main__":
    main()
```

**Конфігурація:**
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

### Приклад 2: Сканер безпеки (PostToolUse)

**Файл:** `.claude/hooks/security-scan.py`

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

### Приклад 3: Автоформатування коду (PostToolUse)

**Файл:** `.claude/hooks/format-code.sh`

```bash
#!/bin/bash

# Читання JSON з stdin
INPUT=$(cat)
TOOL_NAME=$(echo "$INPUT" | python3 -c "import sys, json; print(json.load(sys.stdin).get('tool_name', ''))")
FILE_PATH=$(echo "$INPUT" | python3 -c "import sys, json; print(json.load(sys.stdin).get('tool_input', {}).get('file_path', ''))")

if [ "$TOOL_NAME" != "Write" ] && [ "$TOOL_NAME" != "Edit" ]; then
    exit 0
fi

# Форматування залежно від розширення файлу
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

### Приклад 4: Валідатор промптів (UserPromptSubmit)

**Файл:** `.claude/hooks/validate-prompt.py`

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

### Приклад 5: Інтелектуальний Stop-хук (на основі промпта)

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

### Приклад 6: Трекер використання контексту (пара хуків)

Відстеження споживання токенів на запит за допомогою хуків `UserPromptSubmit` (перед повідомленням) та `Stop` (після відповіді).

**Файл:** `.claude/hooks/context-tracker.py`

```python
#!/usr/bin/env python3
"""
Context Usage Tracker — Відстежує споживання токенів на запит.

Використовує UserPromptSubmit як хук "перед повідомленням" і Stop як хук "після відповіді"
для обчислення дельти використання токенів для кожного запиту.

Методи підрахунку токенів:
1. Оцінка за символами (за замовчуванням): ~4 символи на токен, без залежностей
2. tiktoken (необовʼязково): Точніший (~90-95%), потребує: pip install tiktoken
"""
import json
import os
import sys
import tempfile

# Конфігурація
CONTEXT_LIMIT = 1000000  # 1M у Opus 5, Sonnet 5, Opus 4.8, Sonnet 4.6; 200000 у Haiku 4.5 (налаштуйте для вашої моделі)
USE_TIKTOKEN = False    # Встановіть True, якщо tiktoken встановлено для кращої точності


def get_state_file(session_id: str) -> str:
    """Отримати шлях до тимчасового файлу для збереження лічильника токенів, ізольовано за сесією."""
    return os.path.join(tempfile.gettempdir(), f"claude-context-{session_id}.json")


def count_tokens(text: str) -> int:
    """
    Підрахунок токенів у тексті.

    Використовує tiktoken з кодуванням p50k_base, якщо доступно (~90-95% точності),
    інакше повертається до оцінки за символами (~80-90% точності).
    """
    if USE_TIKTOKEN:
        try:
            import tiktoken
            enc = tiktoken.get_encoding("p50k_base")
            return len(enc.encode(text))
        except ImportError:
            pass  # Повернутися до оцінки

    # Оцінка на основі символів: ~4 символи на токен для англійської
    return len(text) // 4


def read_transcript(transcript_path: str) -> str:
    """Читання та конкатенація всього вмісту з файлу транскрипту."""
    if not transcript_path or not os.path.exists(transcript_path):
        return ""

    content = []
    with open(transcript_path, "r") as f:
        for line in f:
            try:
                entry = json.loads(line.strip())
                # Витяг текстового вмісту з різних форматів повідомлень
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
    """Хук перед повідомленням: зберегти поточний лічильник токенів перед запитом."""
    session_id = data.get("session_id", "unknown")
    transcript_path = data.get("transcript_path", "")

    transcript_content = read_transcript(transcript_path)
    current_tokens = count_tokens(transcript_content)

    # Зберегти в тимчасовий файл для подальшого порівняння
    state_file = get_state_file(session_id)
    with open(state_file, "w") as f:
        json.dump({"pre_tokens": current_tokens}, f)


def handle_stop(data: dict) -> None:
    """Хук після відповіді: обчислити дельту та повідомити про використання."""
    session_id = data.get("session_id", "unknown")
    transcript_path = data.get("transcript_path", "")

    transcript_content = read_transcript(transcript_path)
    current_tokens = count_tokens(transcript_content)

    # Завантажити лічильник перед повідомленням
    state_file = get_state_file(session_id)
    pre_tokens = 0
    if os.path.exists(state_file):
        try:
            with open(state_file, "r") as f:
                state = json.load(f)
                pre_tokens = state.get("pre_tokens", 0)
        except (json.JSONDecodeError, IOError):
            pass

    # Обчислити дельту
    delta_tokens = current_tokens - pre_tokens
    remaining = CONTEXT_LIMIT - current_tokens
    percentage = (current_tokens / CONTEXT_LIMIT) * 100

    # Повідомити про використання
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

**Конфігурація:**
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

**Як це працює:**
1. `UserPromptSubmit` спрацьовує перед обробкою промпта — зберігає поточний лічильник токенів
2. `Stop` спрацьовує після відповіді Claude — обчислює дельту та повідомляє про використання
3. Кожна сесія ізольована через `session_id` в імені тимчасового файлу

**Методи підрахунку токенів:**

| Метод | Точність | Залежності | Швидкість |
|-------|----------|------------|-----------|
| Оцінка за символами | ~80-90% | Немає | <1мс |
| tiktoken (p50k_base) | ~90-95% | `pip install tiktoken` | <10мс |

> **Примітка:** Anthropic не випустили офіційний офлайн-токенізатор. Обидва методи є наближеннями. Транскрипт включає промпти користувача, відповіді Claude та вивід інструментів; з v2.1.300 він також записує системний промпт, інструменти й параметри кожного API-запиту.

### Приклад 7: Початкове налаштування дозволів Auto-Mode (одноразовий скрипт)

Одноразовий скрипт налаштування, що додає до `~/.claude/settings.json` безпечні правила дозволів, еквівалентні базовому набору auto-mode Claude Code — 32 типово, до 58 з усіма прапорцями категорій — без жодного хука, без запамʼятовування майбутніх виборів. Запустіть один раз; безпечно для повторного запуску (пропускає правила, що вже присутні).

**Файл:** `09-advanced-features/setup-auto-mode-permissions.py`

```bash
# Попередній перегляд того, що буде додано
python3 09-advanced-features/setup-auto-mode-permissions.py --dry-run

# Застосувати
python3 09-advanced-features/setup-auto-mode-permissions.py
```

**Що додається:**

| Категорія | Приклади |
|-----------|---------|
| Вбудовані інструменти | `Read(*)`, `Grep(*)`, `Agent(*)`, `WebSearch(*)` |
| Опціональне редагування (--include-edits) | `Edit(*)` |
| Git читання | `Bash(git status:*)`, `Bash(git log:*)`, `Bash(git diff:*)` |
| Git запис (локально) | `Bash(git add:*)`, `Bash(git commit:*)`, `Bash(git checkout:*)` |
| Пакетні менеджери | `Bash(npm ci:*)`, `Bash(npm install:*)`, `Bash(pip install:*)`, `Bash(pip3 install:*)` |
| Збірка та тестування | `Bash(make:*)`, `Bash(pytest:*)`, `Bash(go test:*)` |
| Загальні shell-команди | `Bash(ls:*)`, `Bash(cat:*)`, `Bash(wc:*)` |
| GitHub CLI | `Bash(gh pr view:*)`, `Bash(gh pr create:*)`, `Bash(gh issue list:*)` |

**Що навмисно виключено** (цей скрипт ніколи не додає):
- `rm -rf`, `sudo`, force push, `git reset --hard`
- `DROP TABLE`, `kubectl delete`, `terraform destroy`
- `npm publish`, `curl | bash`, деплої на продакшн

### Приклад 8: Логер прогресу навчання (SessionEnd)

Записуйте в кінці кожної сесії Claude Code, які модулі ви вивчали. Прогрес зберігається
у `~/.claude-howto-progress.json` — поза репозиторієм, тож він переживе `git pull`,
не будучи перезаписаним.

**Чому `SessionEnd`, а не `Stop`?**
`Stop` спрацьовує після *кожної* відповіді Claude. `SessionEnd` спрацьовує один раз,
коли сесія завершується — саме те, що потрібно для щоденника наприкінці сесії.

**Чому немає інтерактивного запиту?**
Хуки виконуються без керівного термінала, тож `/dev/tty` недоступний і хук не може
запитати вас. Передавайте модулі (і необовʼязкові нотатки) через змінні оточення
під час запуску Claude Code, наприклад `CLAUDE_HOWTO_MODULES=06,07 claude`.

**Файл:** `06-hooks/session-end.sh`

```bash
#!/usr/bin/env bash
# SessionEnd hook: records the modules worked on, then appends a session record
# to ~/.claude-howto-progress.json for persistent learning progress tracking.

PROGRESS_FILE="$HOME/.claude-howto-progress.json"

# Guard: only run inside this repo
if [[ "$CLAUDE_PROJECT_DIR" != *"claude-howto"* ]] && [[ "$PWD" != *"claude-howto"* ]]; then
  exit 0
fi

if [ ! -f "$PROGRESS_FILE" ]; then
  echo '{"sessions":[]}' > "$PROGRESS_FILE"
fi

DATE=$(date +"%Y-%m-%d")
TIME=$(date +"%H:%M")

# Modules worked on, e.g. launch with: CLAUDE_HOWTO_MODULES=06,07 claude
# 01=Slash  02=Memory  03=Skills  04=Subagents  05=MCP
# 06=Hooks  07=Plugins 08=Checkpoints 09=Advanced 10=CLI
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

# Optional notes, e.g. CLAUDE_HOWTO_NOTES="tried the pre-commit example"
NOTES="${CLAUDE_HOWTO_NOTES:-}"

# Pass NOTES as a separate argument so Python handles JSON escaping —
# avoids broken JSON when notes contain quotes or backslashes.
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

**Встановлення** — скопіюйте скрипт до каталогу хуків проекту, щоб шлях у `settings.json` розвʼязувався:

```bash
mkdir -p .claude/hooks
cp 06-hooks/session-end.sh .claude/hooks/
chmod +x .claude/hooks/session-end.sh
```

**Конфігурація** (у `.claude/settings.json`):

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

Хуки SessionEnd мають типовий бюджет 1,5 секунди. Встановлення `"timeout"` для окремого хука (у секундах) піднімає бюджет до цього значення, максимум 60 секунд; хук без власного `timeout` скасовується після 1,5 секунди.

**Вивід — `~/.claude-howto-progress.json`:**

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

**Продемонстровані ключові шаблони:**

| Шаблон | Чому це важливо |
|---------|----------------|
| Подія `SessionEnd` | Спрацьовує один раз при виході — не після кожної відповіді, як `Stop` |
| `INPUT="${CLAUDE_HOWTO_MODULES:-}"` | Хуки не мають термінала (`/dev/tty` недоступний), тож вхід — зі змінних оточення |
| `"timeout": 10` | Хуки SessionEnd скасовуються після 1,5 с, якщо не встановлять власний `timeout` |
| `$CLAUDE_PROJECT_DIR` | Портативний шлях — ніколи не хардкодьте `/Users/yourname/...` |
| Охоронна умова на початку | Уникає запуску хука в нерелевантних проектах, якщо встановлено глобально |
| Зберігання поза репозиторієм | Шлях `~/` переживає `git pull` без перезапису даних |

**Компаньйон: візуальний трекер прогресу**

Для повного UI з чекбоксами по всіх 10 модулях відкрийте вбудований трекер у браузері:

```bash
open ../../local-progress/index.html
```

Прогрес зберігається в `localStorage` браузера (ніколи не записується на диск всередині репозиторію). Кнопкою **Експорт** збережіть знімок у JSON, кнопкою **Імпорт** відновіть його.

## Хуки плагінів

Плагіни можуть включати хуки у файлі `hooks/hooks.json`:

**Файл:** `plugins/hooks/hooks.json`

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

**Змінні оточення в хуках плагінів:**
- `${CLAUDE_PLUGIN_ROOT}` — шлях до каталогу плагіна
- `${CLAUDE_PLUGIN_DATA}` — шлях до каталогу даних плагіна

Це дозволяє плагінам включати кастомні хуки валідації та автоматизації.

## Хуки MCP-інструментів

MCP-інструменти використовують шаблон `mcp__<server>__<tool>`:

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

## Міркування безпеки

### Застереження

**ВИКОРИСТОВУЙТЕ НА ВЛАСНИЙ РИЗИК**: Хуки виконують довільні shell-команди. Ви несете повну відповідальність за:
- Команди, які ви налаштовуєте
- Дозволи на доступ/модифікацію файлів
- Потенційну втрату даних або пошкодження системи
- Тестування хуків у безпечних середовищах перед використанням на продакшні

### Примітки щодо безпеки

- **Потрібна довіра до робочого простору:** Команди виводу хуків `statusLine` та `fileSuggestion` тепер вимагають прийняття довіри до робочого простору перед набранням чинності.
- **HTTP-хуки та змінні оточення:** HTTP-хуки вимагають явного списку `allowedEnvVars` для використання інтерполяції змінних оточення у значеннях заголовків. Це запобігає випадковому витоку чутливих змінних оточення на віддалені ендпоінти.
- **Ієрархія керованих налаштувань:** Налаштування `disableAllHooks` тепер поважає ієрархію керованих налаштувань, тобто налаштування рівня організації можуть примусово вимкнути хуки, що не може бути перевизначено окремими користувачами.

### Найкращі практики

| Рекомендовано | Не рекомендовано |
|-------------|-----------------|
| Валідувати та санітизувати всі вхідні дані | Довіряти вхідним даним сліпо |
| Екранувати змінні shell: `"$VAR"` | Використовувати без лапок: `$VAR` |
| Блокувати обхід шляху (`..`) | Дозволяти довільні шляхи |
| Використовувати абсолютні шляхи з `$CLAUDE_PROJECT_DIR` | Жорстко кодувати шляхи |
| Пропускати чутливі файли (`.env`, `.git/`, ключі) | Обробляти всі файли |
| Тестувати хуки окремо спочатку | Деплоїти неперевірені хуки |
| Використовувати явний `allowedEnvVars` для HTTP-хуків | Відкривати всі змінні оточення для вебхуків |

## Налагодження

### Увімкнення режиму налагодження

Запустіть Claude з прапорцем debug для детальних журналів хуків:

```bash
claude --debug
```

### Verbose-режим

Використовуйте `Ctrl+O` в Claude Code для увімкнення verbose-режиму та перегляду прогресу виконання хуків.

### Тестування хуків окремо

```bash
# Тест із зразковим JSON-вводом
echo '{"tool_name": "Bash", "tool_input": {"command": "ls -la"}}' | python3 .claude/hooks/validate-bash.py

# Перевірка коду виходу
echo $?
```

## Повний приклад конфігурації

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

## Деталі виконання хуків

| Аспект | Поведінка |
|--------|----------|
| **Таймаут** | 60 секунд за замовчуванням, налаштовується для кожної команди |
| **Паралелізація** | Усі відповідні хуки запускаються паралельно; починаючи з v2.1.312, одночасно виконується не більше 24 prompt- або agent-хуків на сесію (включно із субагентами), плюс не більше 12 тих, що чекали довше за таймаут своєї події, решта чекає своєї черги (v2.1.302–v2.1.311: не більше 12 однієї події) |
| **Дедуплікація** | Ідентичні команди хуків дедуплікуються |
| **Середовище** | Запускається в поточному каталозі з середовищем Claude Code |

## Усунення несправностей

### Хук не виконується
- Перевірте правильність синтаксису JSON-конфігурації
- Переконайтеся, що шаблон matcher відповідає назві інструмента
- Перевірте існування та виконуваність скрипта: `chmod +x script.sh`
- Запустіть `claude --debug` для перегляду журналів виконання хуків
- Переконайтеся, що хук читає JSON з stdin (не з аргументів команди)

### Хук блокує несподівано
- Тестуйте хук зі зразковим JSON: `echo '{"tool_name": "Write", ...}' | ./hook.py`
- Перевірте код виходу: має бути 0 для дозволу, 2 для блокування
- Перевірте вивід stderr (показується при коді виходу 2)

### Помилки парсингу JSON
- Завжди читайте з stdin, не з аргументів команди
- Використовуйте належний парсинг JSON (не маніпуляцію рядками)
- Обробляйте відсутні поля коректно

## Встановлення

### Крок 1: Створення каталогу хуків
```bash
mkdir -p ~/.claude/hooks
```

### Крок 2: Копіювання прикладів хуків
```bash
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh
```

### Крок 3: Налаштування у settings
Відредагуйте `~/.claude/settings.json` або `.claude/settings.json` з конфігурацією хуків, показаною вище.

## Повʼязані концепції

- **[Контрольні точки та відкат](../08-checkpoints/)** — збереження та відновлення стану розмови
- **[Слеш-команди](../01-slash-commands/)** — створення кастомних слеш-команд
- **[Навички](../03-skills/)** — повторно використовувані автономні можливості
- **[Субагенти](../04-subagents/)** — делеговане виконання завдань
- **[Плагіни](../07-plugins/)** — обʼєднані пакети розширень
- **[Розширені функції](../09-advanced-features/)** — дослідження розширених можливостей Claude Code

## Додаткові ресурси

- **[Офіційна документація хуків](https://code.claude.com/docs/en/hooks)** — повний довідник хуків
- **[Довідник CLI](https://code.claude.com/docs/en/cli-reference)** — документація інтерфейсу командного рядка
- **[Посібник з памʼяті](../02-memory/)** — конфігурація постійного контексту

---
**Останнє оновлення**: 13 листопада 2026
**Версія Claude Code**: 2.1.323
**Джерела**:
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
- https://code.claude.com/docs/en/changelog#2-1-312
- https://code.claude.com/docs/en/changelog#2-1-314
- https://code.claude.com/docs/en/hooks#pretooluse-ask-decisions-in-auto-mode
- https://code.claude.com/docs/en/hooks#common-input-fields
- https://code.claude.com/docs/en/hooks#json-output
- https://code.claude.com/docs/en/env-vars#variables
- https://code.claude.com/docs/en/model-config#extended-context
- https://code.claude.com/docs/en/agent-sdk/hooks#block-the-action-when-a-callback-fails
- https://code.claude.com/docs/en/hooks#mcp-tool-hook-fields
- https://code.claude.com/docs/en/changelog#2-1-321
- https://code.claude.com/docs/en/changelog#2-1-319
- https://code.claude.com/docs/en/hooks#posttooluse-after-an-interrupt
- https://code.claude.com/docs/en/changelog#2-1-323
**Сумісні моделі**: Claude Fable 5.2, Claude Fable 5.1, Claude Fable 5, Claude Opus 5.5, Claude Opus 5, Claude Sonnet 5.5, Claude Sonnet 5, Claude Sonnet 4.6, Claude Opus 4.8, Claude Haiku 5.5, Claude Haiku 4.5
