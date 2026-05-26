<!-- i18n-source: INDEX.md -->
<!-- i18n-source-sha: 63a1416 -->
<!-- i18n-date: 2026-04-09 -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# Приклади Claude Code — Повний покажчик

Цей документ містить повний покажчик усіх файлів-прикладів, упорядкований за типом функціональності.

## Загальна статистика

- **Файлів**: 100+
- **Категорій**: 10 функціональних категорій
- **Плагінів**: 3 повних плагіни
- **Навичок (Skills)**: 6 повних навичок
- **Хуків**: 8 прикладів хуків
- **Готові до використання**: Усі приклади

---

## 01. Слеш-команди (10 файлів)

Ярлики для типових робочих процесів, які викликає користувач.

| Файл | Опис | Сценарій використання |
|------|------|----------------------|
| `optimize.md` | Аналізатор оптимізації коду | Пошук проблем продуктивності |
| `pr.md` | Підготовка pull request | Автоматизація PR-процесу |
| `generate-api-docs.md` | Генератор API-документації | Створення документації API |
| `commit.md` | Помічник з коміт-повідомлень | Стандартизовані коміти |
| `setup-ci-cd.md` | Налаштування CI/CD-пайплайну | DevOps-автоматизація |
| `push-all.md` | Відправити всі зміни | Швидкий push |
| `unit-test-expand.md` | Розширення покриття тестами | Автоматизація тестування |
| `doc-refactor.md` | Рефакторинг документації | Покращення документації |
| `pr-slash-command.png` | Скріншот-приклад | Візуальний довідник |
| `README.md` | Документація | Керівництво з налаштування |

**Шлях встановлення**: `.claude/commands/`

**Використання**: `/optimize`, `/pr`, `/generate-api-docs`, `/commit`, `/setup-ci-cd`, `/push-all`, `/unit-test-expand`, `/doc-refactor`

---

## 02. Пам'ять (6 файлів)

Постійний контекст та стандарти проекту.

| Файл | Опис | Область | Розташування |
|------|------|---------|-------------|
| `project-CLAUDE.md` | Командні стандарти проекту | Проект | `./CLAUDE.md` |
| `directory-api-CLAUDE.md` | Правила для API | Каталог | `./src/api/CLAUDE.md` |
| `personal-CLAUDE.md` | Персональні налаштування | Користувач | `~/.claude/CLAUDE.md` |
| `memory-saved.png` | Скріншот: пам'ять збережено | - | Візуальний довідник |
| `memory-ask-claude.png` | Скріншот: запит до Claude | - | Візуальний довідник |
| `README.md` | Документація | - | Довідник |

**Встановлення**: Скопіюйте у відповідне розташування

**Використання**: Автоматично завантажується Claude

---

## 03. Навички (Skills) (28 файлів)

Автоматично викликані можливості зі скриптами та шаблонами.

### Навичка Code Review (5 файлів)

```
code-review/
├── SKILL.md                          # Визначення навички
├── scripts/
│   ├── analyze-metrics.py            # Аналізатор метрик коду
│   └── compare-complexity.py         # Порівняння складності
└── templates/
    ├── review-checklist.md           # Чекліст ревʼю
    └── finding-template.md           # Шаблон знахідок
```

**Призначення**: Комплексне ревʼю коду з аналізом безпеки, продуктивності та якості

**Автовиклик**: При перегляді коду

---

### Навичка Brand Voice (4 файли)

```
brand-voice/
├── SKILL.md                          # Визначення навички
├── templates/
│   ├── email-template.txt            # Формат електронного листа
│   └── social-post-template.txt      # Формат соцмедіа
└── tone-examples.md                  # Приклади повідомлень
```

**Призначення**: Забезпечення єдиного стилю бренду в комунікаціях

**Автовиклик**: При створенні маркетингових текстів

---

### Навичка Documentation Generator (2 файли)

```
doc-generator/
├── SKILL.md                          # Визначення навички
└── generate-docs.py                  # Python-генератор документації
```

**Призначення**: Генерація комплексної API-документації з вихідного коду

**Автовиклик**: При створенні/оновленні API-документації

---

### Навичка Refactor (5 файлів)

```
refactor/
├── SKILL.md                          # Визначення навички
├── scripts/
│   ├── analyze-complexity.py         # Аналізатор складності
│   └── detect-smells.py              # Детектор code smells
├── references/
│   ├── code-smells.md                # Каталог code smells
│   └── refactoring-catalog.md        # Патерни рефакторингу
└── templates/
    └── refactoring-plan.md           # Шаблон плану рефакторингу
```

**Призначення**: Систематичний рефакторинг коду з аналізом складності

**Автовиклик**: При рефакторингу коду

---

### Навичка Claude MD (1 файл)

```
claude-md/
└── SKILL.md                          # Визначення навички
```

**Призначення**: Управління та оптимізація файлів CLAUDE.md

---

### Навичка Blog Draft (3 файли)

```
blog-draft/
├── SKILL.md                          # Визначення навички
└── templates/
    ├── draft-template.md             # Шаблон чернетки блогу
    └── outline-template.md           # Шаблон плану блогу
```

**Призначення**: Створення чернеток блог-постів зі стандартною структурою

**Додатково**: `README.md` — огляд навичок та керівництво з використання

**Шлях встановлення**: `~/.claude/skills/` або `.claude/skills/`

---

## 04. Субагенти (9 файлів)

Спеціалізовані AI-помічники з налаштованими можливостями.

| Файл | Опис | Інструменти | Сценарій |
|------|------|-------------|----------|
| `code-reviewer.md` | Аналіз якості коду | read, grep, diff, lint_runner | Комплексне ревʼю |
| `test-engineer.md` | Аналіз покриття тестами | read, write, bash, grep | Автоматизація тестування |
| `documentation-writer.md` | Створення документації | read, write, grep | Генерація документації |
| `secure-reviewer.md` | Ревʼю безпеки (лише читання) | read, grep | Аудит безпеки |
| `implementation-agent.md` | Повна реалізація | read, write, bash, grep, edit, glob | Розробка функцій |
| `debugger.md` | Спеціаліст з налагодження | read, bash, grep | Дослідження помилок |
| `data-scientist.md` | Спеціаліст з аналізу даних | read, write, bash | Робота з даними |
| `clean-code-reviewer.md` | Стандарти чистого коду | read, grep | Якість коду |
| `README.md` | Документація | - | Керівництво |

**Шлях встановлення**: `.claude/agents/`

**Використання**: Автоматичне делегування головним агентом

---

## 05. Протокол MCP (5 файлів)

Інтеграції із зовнішніми інструментами та API.

| Файл | Опис | Інтеграція з | Сценарій |
|------|------|-------------|----------|
| `github-mcp.json` | Інтеграція з GitHub | GitHub API | Управління PR/issue |
| `database-mcp.json` | Запити до бази даних | PostgreSQL/MySQL | Запити до даних |
| `filesystem-mcp.json` | Файлові операції | Локальна файлова система | Управління файлами |
| `multi-mcp.json` | Кілька серверів | GitHub + DB + Slack | Комплексна інтеграція |
| `README.md` | Документація | - | Керівництво |

**Шлях встановлення**: `.mcp.json` (рівень проекту) або `~/.claude.json` (рівень користувача)

**Використання**: `/mcp__github__list_prs` тощо

---

## 06. Хуки (9 файлів)

Скрипти автоматизації, що виконуються при певних подіях.

| Файл | Опис | Подія | Сценарій |
|------|------|-------|----------|
| `format-code.sh` | Автоформатування коду | PreToolUse:Write | Форматування коду |
| `pre-commit.sh` | Тести перед комітом | PreToolUse:Bash | Автоматизація тестів |
| `security-scan.sh` | Сканування безпеки | PostToolUse:Write | Перевірка безпеки |
| `log-bash.sh` | Логування bash-команд | PostToolUse:Bash | Журналювання команд |
| `validate-prompt.sh` | Валідація промптів | PreToolUse | Валідація вводу |
| `notify-team.sh` | Надсилання сповіщень | Notification | Сповіщення команди |
| `context-tracker.py` | Відстеження контекстного вікна | PostToolUse | Моніторинг контексту |
| `context-tracker-tiktoken.py` | Підрахунок токенів | PostToolUse | Точний підрахунок токенів |
| `README.md` | Документація | - | Керівництво |

**Шлях встановлення**: Конфігурація в `~/.claude/settings.json`

**Використання**: Налаштовуються в settings, виконуються автоматично

**Типи хуків** (4 типи, 25 подій):

- Хуки інструментів: PreToolUse, PostToolUse, PostToolUseFailure, PermissionRequest
- Хуки сесії: SessionStart, SessionEnd, Stop, StopFailure, SubagentStart, SubagentStop
- Хуки завдань: UserPromptSubmit, TaskCompleted, TaskCreated, TeammateIdle
- Хуки життєвого циклу: ConfigChange, CwdChanged, FileChanged, PreCompact, PostCompact, WorktreeCreate, WorktreeRemove, Notification, InstructionsLoaded, Elicitation, ElicitationResult

---

## 07. Плагіни (3 повних плагіни, 40 файлів)

Пакетні набори функціональності.

### Плагін PR Review (10 файлів)

```
pr-review/
├── .claude-plugin/
│   └── plugin.json                   # Маніфест плагіна
├── commands/
│   ├── review-pr.md                  # Комплексне ревʼю
│   ├── check-security.md             # Перевірка безпеки
│   └── check-tests.md               # Перевірка покриття тестами
├── agents/
│   ├── security-reviewer.md          # Спеціаліст з безпеки
│   ├── test-checker.md               # Спеціаліст з тестування
│   └── performance-analyzer.md       # Спеціаліст з продуктивності
├── mcp/
│   └── github-config.json            # Інтеграція з GitHub
├── hooks/
│   └── pre-review.js                 # Валідація перед ревʼю
└── README.md                         # Документація плагіна
```

**Можливості**: Аналіз безпеки, покриття тестами, вплив на продуктивність

**Команди**: `/review-pr`, `/check-security`, `/check-tests`

**Встановлення**: `/plugin install pr-review`

---

### Плагін DevOps Automation (15 файлів)

```
devops-automation/
├── .claude-plugin/
│   └── plugin.json                   # Маніфест плагіна
├── commands/
│   ├── deploy.md                     # Розгортання
│   ├── rollback.md                   # Відкат
│   ├── status.md                     # Статус системи
│   └── incident.md                   # Реагування на інциденти
├── agents/
│   ├── deployment-specialist.md      # Експерт з розгортання
│   ├── incident-commander.md         # Координатор інцидентів
│   └── alert-analyzer.md             # Аналізатор сповіщень
├── mcp/
│   └── kubernetes-config.json        # Інтеграція з Kubernetes
├── hooks/
│   ├── pre-deploy.js                 # Перевірки перед розгортанням
│   └── post-deploy.js               # Дії після розгортання
├── scripts/
│   ├── deploy.sh                     # Автоматизація розгортання
│   ├── rollback.sh                   # Автоматизація відкату
│   └── health-check.sh              # Перевірка стану
└── README.md                         # Документація плагіна
```

**Можливості**: Розгортання Kubernetes, відкат, моніторинг, реагування на інциденти

**Команди**: `/deploy`, `/rollback`, `/status`, `/incident`

**Встановлення**: `/plugin install devops-automation`

---

### Плагін Documentation (14 файлів)

```
documentation/
├── .claude-plugin/
│   └── plugin.json                   # Маніфест плагіна
├── commands/
│   ├── generate-api-docs.md          # Генерація API-документації
│   ├── generate-readme.md            # Створення README
│   ├── sync-docs.md                  # Синхронізація документації
│   └── validate-docs.md              # Валідація документації
├── agents/
│   ├── api-documenter.md             # Спеціаліст з API-документації
│   ├── code-commentator.md           # Спеціаліст з коментарів
│   └── example-generator.md          # Генератор прикладів
├── mcp/
│   └── github-docs-config.json       # Інтеграція з GitHub
├── templates/
│   ├── api-endpoint.md               # Шаблон API-ендпоінту
│   ├── function-docs.md              # Шаблон документації функцій
│   └── adr-template.md               # Шаблон ADR
└── README.md                         # Документація плагіна
```

**Можливості**: API-документація, генерація README, синхронізація, валідація

**Команди**: `/generate-api-docs`, `/generate-readme`, `/sync-docs`, `/validate-docs`

**Встановлення**: `/plugin install documentation`

**Додатково**: `README.md` — огляд плагінів та керівництво

---

## 08. Контрольні точки та відкат (2 файли)

Збереження стану розмови та дослідження альтернативних підходів.

| Файл | Опис | Вміст |
|------|------|-------|
| `README.md` | Документація | Повний посібник з контрольних точок |
| `checkpoint-examples.md` | Практичні приклади | Міграція БД, оптимізація, UI-ітерації, налагодження |

**Ключові поняття**:

- **Контрольна точка (Checkpoint)**: Знімок стану розмови
- **Відкат (Rewind)**: Повернення до попередньої контрольної точки
- **Точка розгалуження (Branch Point)**: Дослідження кількох підходів

**Використання**:

```
# Контрольні точки створюються автоматично з кожним промптом
# Для відкату натисніть Esc двічі або скористайтеся:
/rewind
# Потім оберіть: Відновити код і розмову, Відновити розмову,
# Відновити код, Підсумувати звідси, або Скасувати
```

**Сценарії**:

- Спробувати різні реалізації
- Відновитися після помилок
- Безпечне експериментування
- Порівняння рішень
- A/B-тестування

---

## 09. Розширені функції (3 файли)

Просунуті можливості для складних робочих процесів.

| Файл | Опис | Функції |
|------|------|---------|
| `README.md` | Повний посібник | Документація всіх розширених функцій |
| `config-examples.json` | Приклади конфігурації | 10+ конфігурацій для різних сценаріїв |
| `planning-mode-examples.md` | Приклади планування | REST API, міграція БД, рефакторинг |
| Заплановані завдання | Повторювані завдання з `/loop` та cron | Автоматичні повторювані процеси |
| Інтеграція з Chrome | Автоматизація браузера через headless Chromium | Веб-тестування та скрейпінг |
| Віддалене керування (розширено) | Методи підключення, безпека, порівняння | Управління віддаленими сесіями |
| Налаштування клавіатури | Кастомні клавіші, акорди, контексти | Персоналізовані ярлики |
| Десктопний застосунок (розширено) | Конектори, launch.json, Enterprise | Десктопна інтеграція |

**Розширені функції**:

### Режим планування (Planning Mode)

- Створення детальних планів реалізації
- Оцінка часу та ризиків
- Систематичний розподіл завдань

### Розширене мислення (Extended Thinking)

- Глибокий аналіз складних проблем
- Аналіз архітектурних рішень
- Оцінка компромісів

### Фонові завдання (Background Tasks)

- Тривалі операції без блокування
- Паралельні робочі процеси
- Управління завданнями та моніторинг

### Режими дозволів (Permission Modes)

- **default**: Запитувати дозвіл на ризиковані дії
- **acceptEdits**: Автоматично приймати редагування, запитувати інше
- **plan**: Лише аналіз, без змін (тільки читання)
- **auto**: Автоматично схвалювати безпечні дії, запитувати ризиковані
- **dontAsk**: Приймати всі дії, крім ризикованих
- **bypassPermissions**: Приймати все (потребує `--dangerously-skip-permissions`)

### Headless-режим (`claude -p`)

- Інтеграція з CI/CD
- Автоматичне виконання завдань
- Пакетна обробка

### Управління сесіями

- Кілька робочих сесій
- Перемикання та збереження сесій
- Постійність сесій

### Інтерактивні функції

- Клавіатурні скорочення
- Історія команд
- Автодоповнення (Tab)
- Багаторядковий ввід

### Конфігурація

- Комплексне управління налаштуваннями
- Конфігурації для різних середовищ
- Налаштування на рівні проекту

### Заплановані завдання

- Повторювані завдання з командою `/loop`
- Інструменти cron: CronCreate, CronList, CronDelete
- Автоматичні повторювані процеси

### Інтеграція з Chrome

- Автоматизація браузера через headless Chromium
- Веб-тестування та скрейпінг
- Взаємодія зі сторінками та витяг даних

### Віддалене керування (розширено)

- Методи та протоколи підключення
- Безпека та найкращі практики
- Порівняльна таблиця варіантів віддаленого доступу

### Налаштування клавіатури

- Конфігурація кастомних клавіш
- Підтримка акордів (комбінацій клавіш)
- Контекстно-залежна активація

### Десктопний застосунок (розширено)

- Конектори для IDE-інтеграції
- Конфігурація launch.json
- Enterprise-функції та розгортання

---

## 10. Використання CLI (1 файл)

Патерни використання та довідник командного рядка.

| Файл | Опис | Вміст |
|------|------|-------|
| `README.md` | Документація CLI | Прапорці, опції та патерни використання |

**Ключові можливості CLI**:

- `claude` — Запуск інтерактивної сесії
- `claude -p "prompt"` — Headless/неінтерактивний режим
- `claude web` — Запуск веб-сесії
- `claude --model` — Вибір моделі (Sonnet 4.6, Opus 4.6)
- `claude --permission-mode` — Встановлення режиму дозволів
- `claude --remote` — Увімкнення віддаленого керування через WebSocket

---

## Файли документації (13 файлів)

| Файл | Розташування | Опис |
|------|-------------|------|
| `README.md` | `/` | Головний огляд прикладів |
| `INDEX.md` | `/` | Цей повний покажчик |
| `QUICK_REFERENCE.md` | `/` | Картка швидкого довідника |
| `README.md` | `/01-slash-commands/` | Посібник зі слеш-команд |
| `README.md` | `/02-memory/` | Посібник з пам'яті |
| `README.md` | `/03-skills/` | Посібник з навичок |
| `README.md` | `/04-subagents/` | Посібник із субагентів |
| `README.md` | `/05-mcp/` | Посібник з MCP |
| `README.md` | `/06-hooks/` | Посібник з хуків |
| `README.md` | `/07-plugins/` | Посібник з плагінів |
| `README.md` | `/08-checkpoints/` | Посібник з контрольних точок |
| `README.md` | `/09-advanced-features/` | Посібник з розширених функцій |
| `README.md` | `/10-cli/` | Посібник з CLI |

---

## Повне дерево файлів

```
claude-howto/
├── README.md                                    # Головний огляд
├── INDEX.md                                     # Цей файл
├── QUICK_REFERENCE.md                           # Картка довідника
├── claude_concepts_guide.md                     # Оригінальний посібник
│
├── 01-slash-commands/                           # Слеш-команди
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
├── 02-memory/                                   # Пам'ять
│   ├── project-CLAUDE.md
│   ├── directory-api-CLAUDE.md
│   ├── personal-CLAUDE.md
│   ├── memory-saved.png
│   ├── memory-ask-claude.png
│   └── README.md
│
├── 03-skills/                                   # Навички
│   ├── code-review/
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
├── 04-subagents/                                # Субагенти
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
├── 05-mcp/                                      # Протокол MCP
│   ├── github-mcp.json
│   ├── database-mcp.json
│   ├── filesystem-mcp.json
│   ├── multi-mcp.json
│   └── README.md
│
├── 06-hooks/                                    # Хуки
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
├── 07-plugins/                                  # Плагіни
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
├── 08-checkpoints/                              # Контрольні точки
│   ├── checkpoint-examples.md
│   └── README.md
│
├── 09-advanced-features/                        # Розширені функції
│   ├── config-examples.json
│   ├── planning-mode-examples.md
│   └── README.md
│
└── 10-cli/                                      # Використання CLI
    └── README.md
```

---

## Швидкий старт за сценарієм

### Якість коду та ревʼю

```bash
# Встановити слеш-команду
cp 01-slash-commands/optimize.md .claude/commands/

# Встановити субагента
cp 04-subagents/code-reviewer.md .claude/agents/

# Встановити навичку
cp -r 03-skills/code-review-specialist ~/.claude/skills/

# Або встановити повний плагін
/plugin install pr-review
```

### DevOps та розгортання

```bash
# Встановити плагін (включає все)
/plugin install devops-automation
```

### Документація

```bash
# Встановити слеш-команду
cp 01-slash-commands/generate-api-docs.md .claude/commands/

# Встановити субагента
cp 04-subagents/documentation-writer.md .claude/agents/

# Встановити навичку
cp -r 03-skills/doc-generator ~/.claude/skills/

# Або встановити повний плагін
/plugin install documentation
```

### Командні стандарти

```bash
# Налаштувати пам'ять проекту
cp 02-memory/project-CLAUDE.md ./CLAUDE.md

# Відредагуйте під стандарти вашої команди
```

### Зовнішні інтеграції

```bash
# Встановити змінні оточення
export GITHUB_TOKEN="your_token"
export DATABASE_URL="postgresql://..."

# Встановити конфігурацію MCP (рівень проекту)
cp 05-mcp/multi-mcp.json .mcp.json
```

### Автоматизація та валідація

```bash
# Встановити хуки
mkdir -p ~/.claude/hooks
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh

# Налаштувати хуки в settings (~/.claude/settings.json)
# Див. 06-hooks/README.md
```

### Безпечне експериментування

```bash
# Контрольні точки створюються автоматично з кожним промптом
# Для відкату: натисніть Esc+Esc або скористайтесь /rewind
# Потім оберіть, що відновити, з меню відкату

# Див. 08-checkpoints/README.md для прикладів
```

### Розширені робочі процеси

```bash
# Налаштувати розширені функції
# Див. 09-advanced-features/config-examples.json

# Використати режим планування
/plan Implement feature X

# Використати режими дозволів
claude --permission-mode plan          # Для ревʼю коду (тільки читання)
claude --permission-mode acceptEdits   # Автоматично приймати редагування
claude --permission-mode auto          # Автоматично схвалювати безпечні дії

# Запустити в headless-режимі для CI/CD
claude -p "Run tests and report results"

# Запустити фонові завдання
Run tests in background

# Див. 09-advanced-features/README.md для повного посібника
```

---

## Матриця покриття функцій

| Категорія | Команди | Агенти | MCP | Хуки | Скрипти | Шаблони | Доки | Зображення | Разом |
|-----------|---------|--------|-----|------|---------|---------|------|------------|-------|
| **01 Слеш-команди** | 8 | - | - | - | - | - | 1 | 1 | **10** |
| **02 Пам'ять** | - | - | - | - | - | 3 | 1 | 2 | **6** |
| **03 Навички** | - | - | - | - | 5 | 9 | 1 | - | **28** |
| **04 Субагенти** | - | 8 | - | - | - | - | 1 | - | **9** |
| **05 MCP** | - | - | 4 | - | - | - | 1 | - | **5** |
| **06 Хуки** | - | - | - | 8 | - | - | 1 | - | **9** |
| **07 Плагіни** | 11 | 9 | 3 | 3 | 3 | 3 | 4 | - | **40** |
| **08 Контрольні точки** | - | - | - | - | - | - | 1 | 1 | **2** |
| **09 Розширені** | - | - | - | - | - | - | 1 | 2 | **3** |
| **10 CLI** | - | - | - | - | - | - | 1 | - | **1** |

---

## Навчальний шлях

### Початківець (Тиждень 1)

1. ✅ Прочитати `README.md`
2. ✅ Встановити 1-2 слеш-команди
3. ✅ Створити файл пам'яті проекту
4. ✅ Спробувати базові команди

### Середній рівень (Тижні 2-3)

1. ✅ Налаштувати GitHub MCP
2. ✅ Встановити субагента
3. ✅ Спробувати делегувати завдання
4. ✅ Встановити навичку

### Просунутий (Тиждень 4+)

1. ✅ Встановити повний плагін
2. ✅ Створити власні слеш-команди
3. ✅ Створити власного субагента
4. ✅ Створити власну навичку
5. ✅ Створити власний плагін

### Експерт (Тиждень 5+)

1. ✅ Налаштувати хуки для автоматизації
2. ✅ Використовувати контрольні точки для експериментів
3. ✅ Налаштувати режим планування
4. ✅ Ефективно використовувати режими дозволів
5. ✅ Налаштувати headless-режим для CI/CD
6. ✅ Опанувати управління сесіями

---

## Пошук за ключовим словом

### Продуктивність

- `01-slash-commands/optimize.md` — Аналіз продуктивності
- `04-subagents/code-reviewer.md` — Ревʼю продуктивності
- `03-skills/code-review-specialist/` — Метрики продуктивності
- `07-plugins/pr-review/agents/performance-analyzer.md` — Спеціаліст з продуктивності

### Безпека

- `04-subagents/secure-reviewer.md` — Ревʼю безпеки
- `03-skills/code-review-specialist/` — Аналіз безпеки
- `07-plugins/pr-review/` — Перевірки безпеки

### Тестування

- `04-subagents/test-engineer.md` — Інженер з тестування
- `07-plugins/pr-review/commands/check-tests.md` — Покриття тестами

### Документація

- `01-slash-commands/generate-api-docs.md` — Команда генерації API-документації
- `04-subagents/documentation-writer.md` — Агент-документатор
- `03-skills/doc-generator/` — Навичка генерації документації
- `07-plugins/documentation/` — Повний плагін документації

### Розгортання

- `07-plugins/devops-automation/` — Повне DevOps-рішення

### Автоматизація

- `06-hooks/` — Автоматизація на основі подій
- `06-hooks/pre-commit.sh` — Автоматизація pre-commit
- `06-hooks/format-code.sh` — Автоформатування
- `09-advanced-features/` — Headless-режим для CI/CD

### Валідація

- `06-hooks/security-scan.sh` — Валідація безпеки
- `06-hooks/validate-prompt.sh` — Валідація промптів

### Експериментування

- `08-checkpoints/` — Безпечне експериментування з відкатом
- `08-checkpoints/checkpoint-examples.md` — Практичні приклади

### Планування

- `09-advanced-features/planning-mode-examples.md` — Приклади режиму планування
- `09-advanced-features/README.md` — Розширене мислення

### Конфігурація

- `09-advanced-features/config-examples.json` — Приклади конфігурації

---

## Примітки

- Усі приклади готові до використання
- Модифікуйте під ваші конкретні потреби
- Приклади дотримуються найкращих практик Claude Code
- Кожна категорія має власний README з детальними інструкціями
- Скрипти включають обробку помилок
- Шаблони можна налаштовувати

---

## Як долучитися

Хочете додати більше прикладів? Дотримуйтесь структури:

1. Створіть відповідний підкаталог
2. Додайте README.md з інструкціями
3. Дотримуйтесь конвенцій назв
4. Ретельно протестуйте
5. Оновіть цей покажчик

---

**Останнє оновлення**: 9 квітня 2026
**Версія Claude Code**: 2.1.97
**Прикладів**: 100+ файлів
**Категорій**: 10 функцій
**Хуків**: 8 скриптів автоматизації
**Прикладів конфігурації**: 10+ сценаріїв
**Готові до використання**: Усі приклади
