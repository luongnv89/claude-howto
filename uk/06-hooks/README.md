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
| `type` | Тип хука: `"command"` (bash), `"prompt"` (LLM), `"http"` (вебхук) або `"agent"` (субагент) | `"command"` |
| `command` | Shell-команда для виконання | `"$CLAUDE_PROJECT_DIR/.claude/hooks/format.sh"` |
| `timeout` | Необовʼязковий таймаут у секундах (за замовчуванням 60) | `30` |
| `once` | Якщо `true`, хук запускається лише один раз за сесію | `true` |

### Шаблони matcher

| Шаблон | Опис | Приклад |
|--------|------|---------|
| Точний рядок | Відповідає конкретному інструменту | `"Write"` |
| Regex-шаблон | Відповідає кільком інструментам | `"Edit\|Write"` |
| Підстановочний знак | Відповідає всім інструментам | `"*"` або `""` |
| MCP-інструменти | Шаблон сервера та інструмента | `"mcp__memory__.*"` |

**Значення matcher для InstructionsLoaded:**

| Значення matcher | Опис |
|-----------------|------|
| `session_start` | Інструкції завантажені при запуску сесії |
| `nested_traversal` | Інструкції завантажені при обході вкладених каталогів |
| `path_glob_match` | Інструкції завантажені через відповідність glob-шаблону шляху |

## Типи хуків

Claude Code підтримує чотири типи хуків:

### Command-хуки

Тип за замовчуванням. Виконує shell-команду та комунікує через JSON stdin/stdout і коди виходу.

```json
{
  "type": "command",
  "command": "python3 \"$CLAUDE_PROJECT_DIR/.claude/hooks/validate.py\"",
  "timeout": 60
}
```

### HTTP-хуки

> Додано у v2.1.63.

Віддалені вебхук-ендпоінти, які отримують той самий JSON-вхід, що й command-хуки. HTTP-хуки надсилають POST JSON на URL і отримують JSON-відповідь. HTTP-хуки маршрутизуються через пісочницю (sandbox), коли вона увімкнена. Інтерполяція змінних оточення в URL вимагає явного списку `allowedEnvVars` з міркувань безпеки.

```json
{
  "hooks": {
    "PostToolUse": [{
      "type": "http",
      "url": "https://my-webhook.example.com/hook",
      "matcher": "Write"
    }]
  }
}
```

**Ключові властивості:**
- `"type": "http"` — ідентифікує як HTTP-хук
- `"url"` — URL ендпоінту вебхука
- Маршрутизується через sandbox, коли sandbox увімкнено
- Вимагає явного списку `allowedEnvVars` для будь-якої інтерполяції змінних оточення в URL

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

### Agent-хуки

Хуки верифікації на основі субагентів, які створюють виділеного агента для оцінки умов або виконання складних перевірок. На відміну від prompt-хуків (однокрокова оцінка LLM), agent-хуки можуть використовувати інструменти та виконувати багатокрокове міркування.

```json
{
  "type": "agent",
  "prompt": "Verify the code changes follow our architecture guidelines. Check the relevant design docs and compare.",
  "timeout": 120
}
```

**Ключові властивості:**
- `"type": "agent"` — ідентифікує як agent-хук
- `"prompt"` — опис завдання для субагента
- Агент може використовувати інструменти (Read, Grep, Bash тощо) для оцінки
- Повертає структуроване рішення, аналогічне prompt-хукам

## Події хуків

Claude Code підтримує **26 подій хуків**:

| Подія | Коли спрацьовує | Вхід matcher | Може блокувати | Типове використання |
|-------|----------------|-------------|----------------|---------------------|
| **SessionStart** | Початок/відновлення/очищення/компакція сесії | startup/resume/clear/compact | Ні | Налаштування середовища |
| **InstructionsLoaded** | Після завантаження CLAUDE.md або файлу правил | (немає) | Ні | Модифікація/фільтрація інструкцій |
| **UserPromptSubmit** | Користувач подає промпт | (немає) | Так | Валідація промптів |
| **PreToolUse** | Перед виконанням інструмента | Назва інструмента | Так (allow/deny/ask) | Валідація, модифікація вхідних даних |
| **PermissionRequest** | Показ діалогу дозволів | Назва інструмента | Так | Автозатвердження/відхилення |
| **PermissionDenied** | Користувач відхиляє запит дозволу | Назва інструмента | Ні | Логування, аналітика, політики |
| **PostToolUse** | Після успішного виконання інструмента | Назва інструмента | Ні | Контекст, зворотний звʼязок |
| **PostToolUseFailure** | Невдале виконання інструмента | Назва інструмента | Ні | Обробка помилок, логування |
| **Notification** | Надсилання сповіщення | Тип сповіщення | Ні | Кастомні сповіщення |
| **SubagentStart** | Створення субагента | Назва типу агента | Ні | Налаштування субагента |
| **SubagentStop** | Завершення субагента | Назва типу агента | Так | Валідація субагента |
| **Stop** | Claude завершує відповідь | (немає) | Так | Перевірка завершення завдання |
| **StopFailure** | Помилка API завершує хід | (немає) | Ні | Відновлення після помилок, логування |
| **TeammateIdle** | Неактивність учасника Agent Teams | (немає) | Так | Координація учасників |
| **TaskCompleted** | Завдання позначено як виконане | (немає) | Так | Дії після завершення завдання |
| **TaskCreated** | Завдання створене через TaskCreate | (немає) | Ні | Відстеження завдань, логування |
| **ConfigChange** | Зміна файлу конфігурації | (немає) | Так (крім policy) | Реакція на оновлення конфігурації |
| **CwdChanged** | Зміна робочого каталогу | (немає) | Ні | Налаштування для каталогу |
| **FileChanged** | Зміна відстежуваного файлу | (немає) | Ні | Моніторинг файлів, перебудова |
| **PreCompact** | Перед компакцією контексту | manual/auto | Ні | Дії перед компакцією |
| **PostCompact** | Після завершення компакції | (немає) | Ні | Дії після компакції |
| **WorktreeCreate** | Створення робочого дерева (worktree) | (немає) | Так (повернення шляху) | Ініціалізація worktree |
| **WorktreeRemove** | Видалення робочого дерева | (немає) | Ні | Очищення worktree |
| **Elicitation** | MCP-сервер запитує введення користувача | (немає) | Так | Валідація введення |
| **ElicitationResult** | Відповідь користувача на elicitation | (немає) | Так | Обробка відповіді |
| **SessionEnd** | Завершення сесії | (немає) | Ні | Очищення, фінальне логування |

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

**Типові matcher:** `Task`, `Bash`, `Glob`, `Grep`, `Read`, `Edit`, `Write`, `WebFetch`, `WebSearch`

**Управління виводом:**
- `permissionDecision`: `"allow"`, `"deny"` або `"ask"`
- `permissionDecisionReason`: Пояснення рішення
- `updatedInput`: Модифіковані вхідні параметри інструмента

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

### UserPromptSubmit

Запускається, коли користувач подає промпт, перед тим як Claude його обробить.

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

**Matcher:** `startup`, `resume`, `clear`, `compact`

**Спеціальна можливість:** Використовуйте `CLAUDE_ENV_FILE` для збереження змінних оточення (також доступно в хуках `CwdChanged` та `FileChanged`):

```bash
#!/bin/bash
if [ -n "$CLAUDE_ENV_FILE" ]; then
  echo 'export NODE_ENV=development' >> "$CLAUDE_ENV_FILE"
fi
exit 0
```

### SessionEnd

Запускається при завершенні сесії для очищення або фінального логування. Не може блокувати завершення.

**Значення поля reason:**
- `clear` — користувач очистив сесію
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
- `elicitation_dialog` — діалог, показаний користувачу

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
          once: true  # Запустити лише один раз за сесію
---
```

**Підтримувані події для хуків компонентів:** `PreToolUse`, `PostToolUse`, `Stop`

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
  "agent_type": "main",
  "worktree": "/path/to/worktree"
}
```

**Загальні поля:**

| Поле | Опис |
|------|------|
| `session_id` | Унікальний ідентифікатор сесії |
| `transcript_path` | Шлях до файлу транскрипту розмови |
| `cwd` | Поточний робочий каталог |
| `hook_event_name` | Назва події, що запустила хук |
| `agent_id` | Ідентифікатор агента, що запускає хук |
| `agent_type` | Тип агента (`"main"`, назва типу субагента тощо) |
| `worktree` | Шлях до git worktree, якщо агент працює в ньому |

### Коди виходу

| Код виходу | Значення | Поведінка |
|-----------|----------|----------|
| **0** | Успіх | Продовжити, розібрати JSON stdout |
| **2** | Блокуюча помилка | Заблокувати операцію, stderr показується як помилка |
| **Інші** | Неблокуюча помилка | Продовжити, stderr показується у verbose-режимі |

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

## Змінні оточення

| Змінна | Доступність | Опис |
|--------|------------|------|
| `CLAUDE_PROJECT_DIR` | Усі хуки | Абсолютний шлях до кореня проєкту |
| `CLAUDE_ENV_FILE` | SessionStart, CwdChanged, FileChanged | Шлях до файлу для збереження змінних оточення |
| `CLAUDE_CODE_REMOTE` | Усі хуки | `"true"` при роботі у віддаленому середовищі |
| `${CLAUDE_PLUGIN_ROOT}` | Хуки плагінів | Шлях до каталогу плагіна |
| `${CLAUDE_PLUGIN_DATA}` | Хуки плагінів | Шлях до каталогу даних плагіна |
| `CLAUDE_CODE_SESSIONEND_HOOKS_TIMEOUT_MS` | Хуки SessionEnd | Налаштовуваний таймаут у мілісекундах для хуків SessionEnd (перевизначає стандартний) |

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
  "decision": "approve",
  "reason": "All tasks completed successfully",
  "continue": false,
  "stopReason": "Task complete"
}
```

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
    prompt = input_data.get("user_prompt", "") or input_data.get("prompt", "")

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
CONTEXT_LIMIT = 128000  # Контекстне вікно Claude (налаштуйте для вашої моделі)
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

> **Примітка:** Anthropic не випустили офіційний офлайн-токенізатор. Обидва методи є наближеннями. Транскрипт включає промпти користувача, відповіді Claude та вивід інструментів, але НЕ системні промпти або внутрішній контекст.

### Приклад 7: Початкове налаштування дозволів Auto-Mode (одноразовий скрипт)

Одноразовий скрипт налаштування, що додає до `~/.claude/settings.json` ~67 безпечних правил дозволів, еквівалентних базовому набору auto-mode Claude Code — без жодного хука, без запамʼятовування майбутніх виборів. Запустіть один раз; безпечно для повторного запуску (пропускає правила, що вже присутні).

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
| Вбудовані інструменти | `Read(*)`, `Edit(*)`, `Write(*)`, `Glob(*)`, `Grep(*)`, `Agent(*)`, `WebSearch(*)` |
| Git читання | `Bash(git status:*)`, `Bash(git log:*)`, `Bash(git diff:*)` |
| Git запис (локально) | `Bash(git add:*)`, `Bash(git commit:*)`, `Bash(git checkout:*)` |
| Пакетні менеджери | `Bash(npm install:*)`, `Bash(pip install:*)`, `Bash(cargo build:*)` |
| Збірка та тестування | `Bash(make:*)`, `Bash(pytest:*)`, `Bash(go test:*)` |
| Загальні shell-команди | `Bash(ls:*)`, `Bash(cat:*)`, `Bash(find:*)`, `Bash(cp:*)`, `Bash(mv:*)` |
| GitHub CLI | `Bash(gh pr view:*)`, `Bash(gh pr create:*)`, `Bash(gh issue list:*)` |

**Що навмисно виключено** (цей скрипт ніколи не додає):
- `rm -rf`, `sudo`, force push, `git reset --hard`
- `DROP TABLE`, `kubectl delete`, `terraform destroy`
- `npm publish`, `curl | bash`, деплої на продакшн

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
            "command": "${CLAUDE_PLUGIN_ROOT}/scripts/validate.sh"
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
- **HTTP-хуки та змінні оточення:** HTTP-хуки вимагають явного списку `allowedEnvVars` для використання інтерполяції змінних оточення в URL. Це запобігає випадковому витоку чутливих змінних оточення на віддалені ендпоінти.
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
| **Паралелізація** | Усі відповідні хуки запускаються паралельно |
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
**Останнє оновлення**: 9 квітня 2026
**Версія Claude Code**: 2.1.97
**Сумісні моделі**: Claude Sonnet 4.6, Claude Opus 4.6, Claude Haiku 4.5
