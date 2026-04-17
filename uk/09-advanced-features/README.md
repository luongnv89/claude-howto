<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# Розширені функції

Повний посібник з розширених можливостей Claude Code, включаючи режим планування, розширене мислення, автоматичний режим, фонові завдання, режими дозволів, режим друку (неінтерактивний), управління сесіями, інтерактивні функції, канали, голосовий ввід, дистанційне керування, веб-сесії, десктопний додаток, список завдань, підказки промптів, git worktrees, пісочницю, керовані налаштування та конфігурацію.

## Зміст

1. [Огляд](#огляд)
2. [Режим планування](#режим-планування)
3. [Розширене мислення](#розширене-мислення)
4. [Auto Mode](#auto-mode)
5. [Фонові завдання](#фонові-завдання)
6. [Заплановані завдання](#заплановані-завдання)
7. [Режими дозволів](#режими-дозволів)
8. [Headless Mode](#headless-mode)
9. [Управління сесіями](#управління-сесіями)
10. [Інтерактивні функції](#інтерактивні-функції)
11. [Голосовий ввід](#голосовий-ввід)
12. [Канали](#канали)
13. [Інтеграція Chrome](#інтеграція-chrome)
14. [Remote Control](#remote-control)
15. [Веб-сесії](#веб-сесії)
16. [Десктопний додаток](#десктопний-додаток)
17. [Список завдань](#список-завдань)
18. [Підказки промптів](#підказки-промптів)
19. [Git Worktrees](#git-worktrees)
20. [Пісочниця](#пісочниця)
21. [Керовані налаштування (Enterprise)](#керовані-налаштування-enterprise)
22. [Конфігурація та налаштування](#конфігурація-та-налаштування)
23. [Agent Teams](#agent-teams)
24. [Найкращі практики](#найкращі-практики)
25. [Додаткові ресурси](#додаткові-ресурси)

---

## Огляд

Розширені функції Claude Code доповнюють базові можливості плануванням, міркуванням, автоматизацією та механізмами контролю. Ці функції забезпечують складні робочі процеси для комплексних завдань розробки, ревʼю коду, автоматизації та управління кількома сесіями.

**Ключові розширені функції:**
- **Режим планування**: Створення детальних планів реалізації перед кодуванням
- **Розширене мислення**: Глибоке міркування для складних проблем
- **Auto Mode**: Фоновий класифікатор безпеки перевіряє кожну дію перед виконанням (Research Preview)
- **Фонові завдання**: Виконання тривалих операцій без блокування розмови
- **Режими дозволів**: Контроль дій Claude (`default`, `acceptEdits`, `plan`, `auto`, `dontAsk`, `bypassPermissions`)
- **Режим друку**: Неінтерактивний запуск Claude Code для автоматизації та CI/CD (`claude -p`)
- **Управління сесіями**: Управління кількома робочими сесіями
- **Інтерактивні функції**: Клавіатурні скорочення, багаторядковий ввід та історія команд
- **Голосовий ввід**: Push-to-talk голосовий ввід з підтримкою STT для 20 мов
- **Канали**: MCP-сервери надсилають повідомлення в активні сесії (Research Preview)
- **Remote Control**: Управління Claude Code з Claude.ai або додатку Claude
- **Веб-сесії**: Запуск Claude Code у браузері на claude.ai/code
- **Десктопний додаток**: Автономний додаток для візуального перегляду diff та кількох сесій
- **Список завдань**: Постійне відстеження завдань між стисненнями контексту
- **Підказки промптів**: Розумні підказки команд на основі контексту
- **Git Worktrees**: Ізольовані робочі дерева для паралельної роботи
- **Пісочниця**: Ізоляція файлової системи та мережі на рівні ОС
- **Керовані налаштування**: Корпоративне розгортання через plist, Registry або керовані файли
- **Конфігурація**: Налаштування поведінки за допомогою JSON-файлів конфігурації

---

## Режим планування

Режим планування дозволяє Claude продумати складні завдання перед їх реалізацією, створюючи детальний план, який ви можете переглянути та затвердити.

### Що таке режим планування?

Режим планування — це двофазний підхід:
1. **Фаза планування**: Claude аналізує завдання та створює детальний план реалізації
2. **Фаза реалізації**: Після затвердження Claude виконує план

### Коли використовувати режим планування

✅ Використовуйте для:
- Складного рефакторингу кількох файлів
- Реалізації нових функцій
- Архітектурних змін
- Міграцій баз даних
- Масштабних змін API

❌ Не використовуйте для:
- Простого виправлення помилок
- Змін форматування
- Редагування одного файлу
- Швидких запитів

### Активація режиму планування

**Слеш-команда**:
```bash
/plan Implement user authentication system
```

**Прапорець CLI**:
```bash
claude --permission-mode plan
```

**Встановити за замовчуванням**:
```json
{
  "permissions": {
    "defaultMode": "plan"
  }
}
```

**Клавіатурне скорочення**:
- `Shift + Tab` — Перемикання режимів дозволів (включно з plan)
- `Alt + M` — Перемикання режимів дозволів (Windows/Linux)

### Переваги режиму планування

- **Структурований підхід до реалізації**: Детальна розбивка кроків реалізації
- **Перегляд та затвердження**: Затвердіть або скоригуйте план перед виконанням
- **Виявлення ризиків**: Визначення потенційних проблем до реалізації
- **Чіткі фази**: Організовані фази та етапи реалізації

### Приклад: Реалізація функції

```
User: /plan Add a real-time notification system

Claude: I'll create a plan for implementing real-time notifications.

## Implementation Plan

### Phase 1: Infrastructure Setup
1. Install WebSocket libraries (socket.io)
2. Set up WebSocket server
3. Configure connection management

### Phase 2: Backend Implementation
4. Create notification service
5. Implement notification queue
6. Add database schema for notifications
7. Create API endpoints

### Phase 3: Frontend Integration
8. Set up WebSocket client
9. Create notification UI components
10. Implement notification state management
11. Add notification permissions

### Phase 4: Testing & Deployment
12. Write unit tests
13. Write integration tests
14. Update documentation
15. Deploy to staging

Estimated time: 3-4 hours
Files to modify: 12
New files to create: 8

Ready to proceed? (yes/no/modify plan)

User: yes

Claude: [Begins implementation following the plan]
```

### Модифікація планів

```
User: Modify the plan - skip the queue for now, we'll add it later

Claude: Updated plan:
[Shows modified plan with queue removed]

User: Looks good, proceed

Claude: [Implements modified plan]
```

### Конфігурація режиму планування

Режим планування активується через прапорець CLI або слеш-команду:

```bash
# Активація режиму планування через CLI
claude --permission-mode plan

# Або використовуйте слеш-команду /plan всередині REPL
/plan Implement user authentication system
```

**Псевдонім моделі для планування**: Використовуйте `opusplan` як псевдонім моделі, щоб використовувати Opus для планування та Sonnet для виконання:

```bash
claude --model opusplan "design and implement the new API"
```

**Редагування плану зовні**: Натисніть `Ctrl+G`, щоб відкрити поточний план у зовнішньому редакторі для детальних змін.

### Ultraplan

Використовуйте `/ultraplan <prompt>` для наскрізного робочого процесу планування: Claude складає детальний план, відкриває його у браузері для перегляду, потім виконує план віддалено або повертає його у ваш термінал для локального виконання.

---

## Розширене мислення

Розширене мислення дозволяє Claude витрачати більше часу на обмірковування складних проблем перед наданням рішення.

### Що таке розширене мислення?

Розширене мислення — це цілеспрямований покроковий процес міркування, де Claude:
- Розбиває складні проблеми на частини
- Розглядає кілька підходів
- Оцінює компроміси
- Продумує граничні випадки

### Активація розширеного мислення

**Клавіатурне скорочення**:
- `Option + T` (macOS) / `Alt + T` (Windows/Linux) — Перемикання розширеного мислення

**Автоматична активація**:
- Увімкнено за замовчуванням для всіх моделей (Opus 4.6, Sonnet 4.6, Haiku 4.5)
- Opus 4.6: Адаптивне міркування з рівнями зусиль: `low` (○), `medium` (◐), `high` (●), `max` (тільки Opus 4.6)
- Інші моделі: Фіксований бюджет до 31 999 токенів

**Методи конфігурації**:
- Перемикання: `Alt+T` / `Option+T`, або через `/config`
- Перегляд міркувань: `Ctrl+O` (детальний режим)
- Встановлення зусиль: команда `/effort` або прапорець `--effort`

**Власний бюджет**:
```bash
export MAX_THINKING_TOKENS=1024
```

**Рівень зусиль** (тільки Opus 4.6):
```bash
export CLAUDE_CODE_EFFORT_LEVEL=high   # low (○), medium (◐), high (●), або max (тільки Opus 4.6)
```

**Прапорець CLI**:
```bash
claude --effort high "complex architectural review"
```

**Слеш-команда**:
```
/effort high
```

> **Примітка:** Ключове слово "ultrathink" у промптах активує режим глибокого міркування. Рівні зусиль `low`, `medium`, `high` та `max` (тільки Opus 4.6) контролюють обсяг міркувань Claude.

### Переваги розширеного мислення

- **Глибоке міркування**: Більше часу на обдумування складних проблем
- **Кращі архітектурні рішення**: Обґрунтовані рішення з комплексною оцінкою
- **Розгляд граничних випадків**: Продумування потенційних проблем і сценаріїв
- **Ретельний аналіз**: Структурований підхід до вирішення складних проблем

### Приклад: Архітектурне рішення

```
User: ultrathink Should we use microservices or a monolith for our e-commerce platform?

Claude: Let me think through this architectural decision carefully...

<extended_thinking>
## Context Analysis
- Team size: 5 developers
- Expected traffic: 10k daily users initially
- Need to scale to 100k+ users
- Limited DevOps resources
- 6-month timeline to MVP

## Approach 1: Microservices
Pros:
+ Independent scaling
+ Technology flexibility
+ Team independence
+ Fault isolation

Cons:
- Operational complexity
- Network overhead
- Distributed tracing needed
- Requires DevOps expertise
- Slower initial development

## Approach 2: Monolith
Pros:
+ Simpler deployment
+ Faster initial development
+ Easier debugging
+ Lower operational overhead
+ Single codebase

Cons:
- Scaling challenges later
- All-or-nothing deployments
- Technology lock-in
- Potential for tight coupling

## Decision Factors
1. Team size (5 devs) → Favors monolith
2. DevOps resources (limited) → Favors monolith
3. Timeline (6 months) → Favors monolith
4. Future scale (100k users) → Achievable with monolith + caching
5. Complexity budget → Limited

## Recommendation
Start with a **modular monolith**:
- Single deployment unit
- Clear module boundaries
- Clean interfaces between modules
- Prepare for future extraction to microservices if needed

This gives you:
✓ Fast initial development
✓ Low operational complexity
✓ Option to extract services later
✓ Clear architecture

Migration path: When you reach 50k+ users or specific modules need independent scaling, extract those modules into microservices.
</extended_thinking>

**Recommendation**: Implement a modular monolith with clean module boundaries.

This approach balances your current constraints (team size, timeline, DevOps resources) with future scalability needs. You can migrate specific modules to microservices later when there's a clear business need.
```

### Конфігурація розширеного мислення

Розширене мислення контролюється через змінні оточення, клавіатурні скорочення та прапорці CLI:

```bash
# Встановлення бюджету токенів мислення
export MAX_THINKING_TOKENS=16000

# Встановлення рівня зусиль (тільки Opus 4.6): low (○), medium (◐), high (●), або max (тільки Opus 4.6)
export CLAUDE_CODE_EFFORT_LEVEL=high
```

Перемикання під час сесії за допомогою `Alt+T` / `Option+T`, встановлення зусиль через `/effort` або конфігурація через `/config`.

---

## Auto Mode

Auto Mode — це режим дозволів Research Preview (березень 2026), який використовує фоновий класифікатор безпеки для перевірки кожної дії перед виконанням. Він дозволяє Claude працювати автономно, блокуючи небезпечні операції.

### Вимоги

- **План**: Team, Enterprise або API (недоступно на планах Pro або Max)
- **Модель**: Claude Sonnet 4.6 або Opus 4.6
- **Провайдер**: Тільки Anthropic API (не підтримується на Bedrock, Vertex або Foundry)
- **Класифікатор**: Працює на Claude Sonnet 4.6 (додаткова вартість токенів)

### Увімкнення Auto Mode

```bash
# Розблокування auto mode за допомогою прапорця CLI
claude --enable-auto-mode

# Потім перемикайте через Shift+Tab у REPL
```

Або встановіть як режим дозволів за замовчуванням:

```bash
claude --permission-mode auto
```

Встановлення через конфігурацію:
```json
{
  "permissions": {
    "defaultMode": "auto"
  }
}
```

### Як працює класифікатор

Фоновий класифікатор оцінює кожну дію в такому порядку:

1. **Правила дозволу/заборони** — Спочатку перевіряються явні правила дозволів
2. **Читання/редагування автоматично затверджуються** — Читання та редагування файлів проходять автоматично
3. **Класифікатор** — Фоновий класифікатор перевіряє дію
4. **Запасний варіант** — Повертається до запиту після 3 послідовних або 20 загальних блокувань

### Заблоковані дії за замовчуванням

Auto mode блокує наступне за замовчуванням:

| Заблокована дія | Приклад |
|----------------|---------|
| Встановлення через pipe-to-shell | `curl \| bash` |
| Надсилання конфіденційних даних назовні | API-ключі, облікові дані через мережу |
| Деплой на продакшн | Команди деплою на продакшн |
| Масове видалення | `rm -rf` на великих директоріях |
| Зміни IAM | Зміни дозволів та ролей |
| Force push у main | `git push --force origin main` |

### Дозволені дії за замовчуванням

| Дозволена дія | Приклад |
|----------------|---------|
| Локальні операції з файлами | Читання, запис, редагування файлів проєкту |
| Встановлення оголошених залежностей | `npm install`, `pip install` з маніфесту |
| HTTP тільки для читання | `curl` для отримання документації |
| Push у поточну гілку | `git push origin feature-branch` |

### Конфігурація Auto Mode

**Вивести правила за замовчуванням у JSON**:
```bash
claude auto-mode defaults
```

**Налаштування довіреної інфраструктури** через керовану настройку `autoMode.environment` для корпоративних розгортань. Це дозволяє адміністраторам визначати довірені середовища CI/CD, цілі деплою та шаблони інфраструктури.

### Запасна поведінка

Коли класифікатор невпевнений, auto mode повертається до запиту користувача:
- Після **3 послідовних** блокувань класифікатором
- Після **20 загальних** блокувань класифікатором за сесію

Це гарантує, що користувач завжди зберігає контроль, коли класифікатор не може впевнено затвердити дію.

### Посів дозволів Auto-Mode без Team-плану

Якщо у вас немає Team-плану або ви хочете простіший підхід без фонового класифікатора, ви можете наповнити ваш `~/.claude/settings.json` консервативним базовим набором безпечних правил дозволів. Скрипт починає з правил тільки для читання та локального інспектування, потім дозволяє вам додавати редагування, тести, локальний запис у git, встановлення пакетів та дії запису GitHub лише за потреби.

**Файл:** `09-advanced-features/setup-auto-mode-permissions.py`

```bash
# Попередній перегляд змін (без запису)
python3 09-advanced-features/setup-auto-mode-permissions.py --dry-run

# Застосувати консервативний базовий набір
python3 09-advanced-features/setup-auto-mode-permissions.py

# Додавати більше можливостей лише за потреби
python3 09-advanced-features/setup-auto-mode-permissions.py --include-edits --include-tests
python3 09-advanced-features/setup-auto-mode-permissions.py --include-git-write --include-packages
```

Скрипт додає правила в таких категоріях:

| Категорія | Приклади |
|----------|---------|
| Базові інструменти тільки для читання | `Read(*)`, `Glob(*)`, `Grep(*)`, `Agent(*)`, `WebSearch(*)`, `WebFetch(*)` |
| Локальне інспектування | `Bash(git status:*)`, `Bash(git log:*)`, `Bash(git diff:*)`, `Bash(cat:*)` |
| Опціональне редагування | `Edit(*)`, `Write(*)`, `NotebookEdit(*)` |
| Опціональні тести/збірка | `Bash(pytest:*)`, `Bash(python3 -m pytest:*)`, `Bash(cargo test:*)` |
| Опціональний запис у git | `Bash(git add:*)`, `Bash(git commit:*)`, `Bash(git stash:*)` |
| Git (локальний запис) | `Bash(git add:*)`, `Bash(git commit:*)`, `Bash(git checkout:*)` |
| Менеджери пакетів | `Bash(npm install:*)`, `Bash(pip install:*)`, `Bash(cargo build:*)` |
| Збірка та тести | `Bash(make:*)`, `Bash(pytest:*)`, `Bash(go test:*)` |
| Звичайні shell-команди | `Bash(ls:*)`, `Bash(cat:*)`, `Bash(find:*)`, `Bash(cp:*)`, `Bash(mv:*)` |
| GitHub CLI | `Bash(gh pr view:*)`, `Bash(gh pr create:*)`, `Bash(gh issue list:*)` |

Небезпечні операції (`rm -rf`, `sudo`, force push, `DROP TABLE`, `terraform destroy` тощо) навмисно виключені. Скрипт ідемпотентний — повторний запуск не дублює правила.

---

## Фонові завдання

Фонові завдання дозволяють виконувати тривалі операції без блокування вашої розмови.

### Що таке фонові завдання?

Фонові завдання виконуються асинхронно, поки ви продовжуєте працювати:
- Тривалі набори тестів
- Процеси збірки
- Міграції баз даних
- Скрипти деплою
- Інструменти аналізу

**Базове використання:**
```bash
User: Run tests in background

Claude: Started task bg-1234

/task list           # Показати всі завдання
/task status bg-1234 # Перевірити прогрес
/task show bg-1234   # Переглянути вивід
/task cancel bg-1234 # Скасувати завдання
```

### Запуск фонових завдань

```
User: Run the full test suite in the background

Claude: Starting tests in background (task-id: bg-1234)
You can continue working while tests run.

[You can continue the conversation]

User: Meanwhile, let's refactor the auth module

Claude: [Works on auth module while tests run in background]

[Later, when tests complete]

Claude: 📢 Background task bg-1234 completed:
✅ 245 tests passed
❌ 3 tests failed
View results: /task show bg-1234
```

### Управління фоновими завданнями

**Список активних завдань**:
```
User: /task list

Active background tasks:
1. [bg-1234] Running tests (50% complete, 2min remaining)
2. [bg-1235] Building Docker image (25% complete, 8min remaining)
3. [bg-1236] Deploying to staging (90% complete, 30sec remaining)
```

**Перевірка статусу завдання**:
```
User: /task status bg-1234

Task bg-1234: Running tests
Status: In progress
Progress: 120/245 tests (49%)
Started: 2025-11-08 10:30:15
Estimated completion: 2025-11-08 10:34:22
```

**Перегляд виводу завдання**:
```
User: /task show bg-1234

[Shows live output from the test run]
```

**Скасування завдання**:
```
User: /task cancel bg-1234

Cancelled background task bg-1234
```

### Приклад: Паралельна розробка

```
User: Run the build in the background

Claude: Starting build... (task-id: bg-5001)

User: Also run the linter in background

Claude: Starting linter... (task-id: bg-5002)

User: While those run, let's implement the new API endpoint

Claude: [Implements API endpoint while build and linter run]

[10 minutes later]

Claude: 📢 Build completed successfully (bg-5001)
📢 Linter found 12 issues (bg-5002)

User: Show me the linter issues

Claude: [Shows linter output from bg-5002]
```

### Конфігурація

```json
{
  "backgroundTasks": {
    "enabled": true,
    "maxConcurrentTasks": 5,
    "notifyOnCompletion": true,
    "autoCleanup": true,
    "logOutput": true
  }
}
```

---

## Заплановані завдання

Заплановані завдання дозволяють автоматично запускати промпти за розкладом або як одноразові нагадування. Завдання привʼязані до сесії — вони працюють, поки Claude Code активний, і очищуються при завершенні сесії. Доступно з v2.1.72+.

### Команда `/loop`

```bash
# Явний інтервал
/loop 5m check if the deployment finished

# Природна мова
/loop check build status every 30 minutes
```

Також підтримуються стандартні 5-польні cron-вирази для точного планування.

### Одноразові нагадування

Встановлення нагадувань, які спрацьовують один раз у визначений час:

```
remind me at 3pm to push the release branch
in 45 minutes, run the integration tests
```

### Управління запланованими завданнями

| Інструмент | Опис |
|------|-------------|
| `CronCreate` | Створити нове заплановане завдання |
| `CronList` | Показати всі активні заплановані завдання |
| `CronDelete` | Видалити заплановане завдання |

**Обмеження та поведінка**:
- До **50 запланованих завдань** на сесію
- Привʼязані до сесії — очищуються при завершенні сесії
- Повторювані завдання автоматично закінчуються через **3 дні**
- Завдання спрацьовують лише під час роботи Claude Code — пропущені запуски не компенсуються

### Деталі поведінки

| Аспект | Деталь |
|--------|--------|
| **Джитер повторюваних** | До 10% від інтервалу (макс. 15 хвилин) |
| **Джитер одноразових** | До 90 секунд на межах :00/:30 |
| **Пропущені запуски** | Без компенсації — пропускаються, якщо Claude Code не працював |
| **Збереження** | Не зберігаються між перезапусками |

### Хмарні заплановані завдання

Використовуйте `/schedule` для створення хмарних запланованих завдань, які працюють на інфраструктурі Anthropic:

```
/schedule daily at 9am run the test suite and report failures
```

Хмарні заплановані завдання зберігаються між перезапусками і не потребують локально запущеного Claude Code.

### Вимкнення запланованих завдань

```bash
export CLAUDE_CODE_DISABLE_CRON=1
```

### Приклад: Моніторинг деплою

```
/loop 5m check the deployment status of the staging environment.
        If the deploy succeeded, notify me and stop looping.
        If it failed, show the error logs.
```

> **Порада**: Заплановані завдання привʼязані до сесії. Для постійної автоматизації, яка переживає перезапуски, використовуйте CI/CD пайплайни, GitHub Actions або заплановані завдання десктопного додатку.

---

## Режими дозволів

Режими дозволів контролюють, які дії Claude може виконувати без явного схвалення.

### Доступні режими дозволів

| Режим | Поведінка |
|---|---|
| `default` | Тільки читання файлів; запитує дозвіл на всі інші дії |
| `acceptEdits` | Читання та редагування файлів; запитує дозвіл на команди |
| `plan` | Тільки читання файлів (режим дослідження, без редагувань) |
| `auto` | Усі дії з перевірками фонового класифікатора безпеки (Research Preview) |
| `bypassPermissions` | Усі дії, без перевірки дозволів (небезпечно) |
| `dontAsk` | Виконуються лише попередньо затверджені інструменти; всі інші відхиляються |

Перемикайте режими через `Shift+Tab` у CLI. Встановіть режим за замовчуванням через прапорець `--permission-mode` або налаштування `permissions.defaultMode`.

### Методи активації

**Клавіатурне скорочення**:
```bash
Shift + Tab  # Перемикання між усіма 6 режимами
```

**Слеш-команда**:
```bash
/plan                  # Увійти в режим планування
```

**Прапорець CLI**:
```bash
claude --permission-mode plan
claude --permission-mode auto
```

**Налаштування**:
```json
{
  "permissions": {
    "defaultMode": "auto"
  }
}
```

### Приклади режимів дозволів

#### Режим Default
Claude запитує підтвердження на значущі дії:

```
User: Fix the bug in auth.ts

Claude: I need to modify src/auth.ts to fix the bug.
The change will update the password validation logic.

Approve this change? (yes/no/show)
```

#### Режим Plan
Перегляд плану реалізації перед виконанням:

```
User: /plan Implement user authentication system

Claude: I'll create a plan for implementing authentication.

## Implementation Plan
[Detailed plan with phases and steps]

Ready to proceed? (yes/no/modify)
```

#### Режим Accept Edits
Автоматичне прийняття змін у файлах:

```
User: acceptEdits
User: Fix the bug in auth.ts

Claude: [Makes changes without asking]
```

### Випадки використання

**Ревʼю коду**:
```
User: claude --permission-mode plan
User: Review this PR and suggest improvements

Claude: [Reads code, provides feedback, but cannot modify]
```

**Парне програмування**:
```
User: claude --permission-mode default
User: Let's implement the feature together

Claude: [Asks for approval before each change]
```

**Автоматизовані завдання**:
```
User: claude --permission-mode acceptEdits
User: Fix all linting issues in the codebase

Claude: [Auto-accepts file edits without asking]
```

---

## Headless Mode

Режим друку (`claude -p`) дозволяє запускати Claude Code без інтерактивного вводу, ідеально для автоматизації та CI/CD. Це неінтерактивний режим, що замінює старий прапорець `--headless`.

### Що таке режим друку?

Режим друку забезпечує:
- Автоматизоване виконання скриптів
- Інтеграцію з CI/CD
- Пакетну обробку
- Виконання запланованих завдань

### Запуск у режимі друку (неінтерактивний)

```bash
# Запуск конкретного завдання
claude -p "Run all tests"

# Обробка переданого вмісту
cat error.log | claude -p "Analyze these errors"

# Інтеграція CI/CD (GitHub Actions)
- name: AI Code Review
  run: claude -p "Review PR"
```

### Додаткові приклади використання режиму друку

```bash
# Запуск завдання з захопленням виводу
claude -p "Run all tests and generate coverage report"

# Зі структурованим виводом
claude -p --output-format json "Analyze code quality"

# З вводом через stdin
echo "Analyze code quality" | claude -p "explain this"
```

### Приклад: Інтеграція CI/CD

**GitHub Actions**:
```yaml
# .github/workflows/code-review.yml
name: AI Code Review

on: [pull_request]

jobs:
  review:
    runs-on: ubuntu-latest
    steps:
      - uses: actions/checkout@v4

      - name: Install Claude Code
        run: npm install -g @anthropic-ai/claude-code

      - name: Run Claude Code Review
        env:
          ANTHROPIC_API_KEY: ${{ secrets.ANTHROPIC_API_KEY }}
        run: |
          claude -p --output-format json \
            --max-turns 3 \
            "Review this PR for:
            - Code quality issues
            - Security vulnerabilities
            - Performance concerns
            - Test coverage
            Output results as JSON" > review.json

      - name: Post Review Comment
        uses: actions/github-script@v7
        with:
          script: |
            const fs = require('fs');
            const review = JSON.parse(fs.readFileSync('review.json', 'utf8'));
            github.rest.issues.createComment({
              issue_number: context.issue.number,
              owner: context.repo.owner,
              repo: context.repo.repo,
              body: JSON.stringify(review, null, 2)
            });
```

### Конфігурація режиму друку

Режим друку (`claude -p`) підтримує кілька прапорців для автоматизації:

```bash
# Обмеження автономних ходів
claude -p --max-turns 5 "refactor this module"

# Структурований вивід JSON
claude -p --output-format json "analyze this codebase"

# З валідацією схеми
claude -p --json-schema '{"type":"object","properties":{"issues":{"type":"array"}}}' \
  "find bugs in this code"

# Вимкнення збереження сесії
claude -p --no-session-persistence "one-off analysis"
```

---

## Управління сесіями

Ефективне управління кількома сесіями Claude Code.

### Команди управління сесіями

| Команда | Опис |
|---------|-------------|
| `/resume` | Відновити розмову за ID або назвою |
| `/rename` | Назвати поточну сесію |
| `/fork` | Розгалужити поточну сесію в нову гілку |
| `claude -c` | Продовжити останню розмову |
| `claude -r "session"` | Відновити сесію за назвою або ID |

### Відновлення сесій

**Продовжити останню розмову**:
```bash
claude -c
```

**Відновити іменовану сесію**:
```bash
claude -r "auth-refactor" "finish this PR"
```

**Перейменувати поточну сесію** (всередині REPL):
```
/rename auth-refactor
```

### Розгалуження сесій

Розгалужте сесію, щоб спробувати альтернативний підхід без втрати оригіналу:

```
/fork
```

Або з CLI:
```bash
claude --resume auth-refactor --fork-session "try OAuth instead"
```

### Збереження сесій

Сесії автоматично зберігаються і можуть бути відновлені:

```bash
# Продовжити останню розмову
claude -c

# Відновити конкретну сесію за назвою або ID
claude -r "auth-refactor"

# Відновити та розгалужити для експериментів
claude --resume auth-refactor --fork-session "alternative approach"
```

---

## Інтерактивні функції

### Клавіатурні скорочення

Claude Code підтримує клавіатурні скорочення для ефективності. Ось повний довідник з офіційної документації:

| Скорочення | Опис |
|----------|-------------|
| `Ctrl+C` | Скасувати поточний ввід/генерацію |
| `Ctrl+D` | Вийти з Claude Code |
| `Ctrl+G` | Редагувати план у зовнішньому редакторі |
| `Ctrl+L` | Очистити екран терміналу |
| `Ctrl+O` | Перемкнути детальний вивід (перегляд міркувань) |
| `Ctrl+R` | Зворотний пошук в історії |
| `Ctrl+T` | Перемкнути перегляд списку завдань |
| `Ctrl+B` | Перевести завдання у фоновий режим |
| `Esc+Esc` | Відкотити код/розмову |
| `Shift+Tab` / `Alt+M` | Перемикання режимів дозволів |
| `Option+P` / `Alt+P` | Перемкнути модель |
| `Option+T` / `Alt+T` | Перемкнути розширене мислення |

**Редагування рядка (стандартні скорочення readline):**

| Скорочення | Дія |
|----------|--------|
| `Ctrl + A` | Перейти на початок рядка |
| `Ctrl + E` | Перейти на кінець рядка |
| `Ctrl + K` | Вирізати до кінця рядка |
| `Ctrl + U` | Вирізати до початку рядка |
| `Ctrl + W` | Видалити слово назад |
| `Ctrl + Y` | Вставити (yank) |
| `Tab` | Автодоповнення |
| `↑ / ↓` | Історія команд |

### Кастомізація клавіатурних скорочень

Створюйте власні клавіатурні скорочення, запустивши `/keybindings`, що відкриває `~/.claude/keybindings.json` для редагування (v2.1.18+).

**Формат конфігурації**:

```json
{
  "$schema": "https://www.schemastore.org/claude-code-keybindings.json",
  "bindings": [
    {
      "context": "Chat",
      "bindings": {
        "ctrl+e": "chat:externalEditor",
        "ctrl+u": null,
        "ctrl+k ctrl+s": "chat:stash"
      }
    },
    {
      "context": "Confirmation",
      "bindings": {
        "ctrl+a": "confirmation:yes"
      }
    }
  ]
}
```

Встановіть привʼязку в `null`, щоб відвʼязати скорочення за замовчуванням.

### Доступні контексти

Клавіатурні скорочення привʼязані до конкретних контекстів UI:

| Контекст | Ключові дії |
|---------|-------------|
| **Chat** | `submit`, `cancel`, `cycleMode`, `modelPicker`, `thinkingToggle`, `undo`, `externalEditor`, `stash`, `imagePaste` |
| **Confirmation** | `yes`, `no`, `previous`, `next`, `nextField`, `cycleMode`, `toggleExplanation` |
| **Global** | `interrupt`, `exit`, `toggleTodos`, `toggleTranscript` |
| **Autocomplete** | `accept`, `dismiss`, `next`, `previous` |
| **HistorySearch** | `search`, `previous`, `next` |
| **Settings** | Навігація налаштуваннями |
| **Tabs** | Перемикання та управління вкладками |
| **Help** | Навігація панеллю допомоги |

Загалом 18 контекстів, включаючи `Transcript`, `Task`, `ThemePicker`, `Attachments`, `Footer`, `MessageSelector`, `DiffDialog`, `ModelPicker` та `Select`.

### Підтримка акордів

Клавіатурні скорочення підтримують послідовності акордів (комбінації з кількох клавіш):

```
"ctrl+k ctrl+s"   → Двоклавішна послідовність: натисніть ctrl+k, потім ctrl+s
"ctrl+shift+p"    → Одночасне натискання модифікаторів
```

**Синтаксис клавіш**:
- **Модифікатори**: `ctrl`, `alt` (або `opt`), `shift`, `meta` (або `cmd`)
- **Великі літери включають Shift**: `K` еквівалентно `shift+k`
- **Спеціальні клавіші**: `escape`, `enter`, `return`, `tab`, `space`, `backspace`, `delete`, клавіші стрілок

### Зарезервовані та конфліктні клавіші

| Клавіша | Статус | Примітки |
|-----|--------|-------|
| `Ctrl+C` | Зарезервовано | Неможливо перепривʼязати (переривання) |
| `Ctrl+D` | Зарезервовано | Неможливо перепривʼязати (вихід) |
| `Ctrl+B` | Конфлікт терміналу | Префіксна клавіша tmux |
| `Ctrl+A` | Конфлікт терміналу | Префіксна клавіша GNU Screen |
| `Ctrl+Z` | Конфлікт терміналу | Призупинення процесу |

> **Порада**: Якщо скорочення не працює, перевірте конфлікти з вашим емулятором терміналу або мультиплексором.

### Tab-доповнення

Claude Code забезпечує інтелектуальне tab-доповнення:

```
User: /rew<TAB>
→ /rewind

User: /plu<TAB>
→ /plugin

User: /plugin <TAB>
→ /plugin install
→ /plugin enable
→ /plugin disable
```

### Історія команд

Доступ до попередніх команд:

```
User: <↑>  # Попередня команда
User: <↓>  # Наступна команда
User: Ctrl+R  # Пошук в історії

(reverse-i-search)`test': run all tests
```

### Багаторядковий ввід

Для складних запитів використовуйте багаторядковий режим:

```bash
User: \
> Long complex prompt
> spanning multiple lines
> \end
```

**Приклад:**

```
User: \
> Implement a user authentication system
> with the following requirements:
> - JWT tokens
> - Email verification
> - Password reset
> - 2FA support
> \end

Claude: [Processes the multi-line request]
```

### Inline-редагування

Редагування команд перед відправкою:

```
User: Deploy to prodcution<Backspace><Backspace>uction

[Edit in-place before sending]
```

### Режим Vim

Увімкнення Vi/Vim-клавіатурних привʼязок для редагування тексту:

**Активація**:
- Використовуйте команду `/vim` або `/config` для увімкнення
- Перемикання режимів: `Esc` для NORMAL, `i/a/o` для INSERT

**Клавіші навігації**:
- `h` / `l` — Рух вліво/вправо
- `j` / `k` — Рух вниз/вгору
- `w` / `b` / `e` — Рух по словах
- `0` / `$` — Перейти на початок/кінець рядка
- `gg` / `G` — Перейти на початок/кінець тексту

**Текстові обʼєкти**:
- `iw` / `aw` — Внутрішнє/зовнішнє слово
- `i"` / `a"` — Внутрішній/зовнішній рядок у лапках
- `i(` / `a(` — Внутрішнє/зовнішнє у дужках

### Режим Bash

Виконання shell-команд безпосередньо з префіксом `!`:

```bash
! npm test
! git status
! cat src/index.js
```

Використовуйте це для швидкого виконання команд без перемикання контексту.

---

## Голосовий ввід

Голосовий ввід забезпечує push-to-talk голосове введення для Claude Code, дозволяючи промовляти ваші промпти замість друкування.

### Активація голосового вводу

```
/voice
```

### Можливості

| Можливість | Опис |
|---------|-------------|
| **Push-to-talk** | Утримуйте клавішу для запису, відпустіть для відправки |
| **20 мов** | Розпізнавання мовлення підтримує 20 мов |
| **Власна клавіша** | Налаштуйте клавішу push-to-talk через `/keybindings` |
| **Вимога облікового запису** | Потрібен обліковий запис Claude.ai для обробки STT |

### Конфігурація

Налаштуйте клавішу push-to-talk у файлі привʼязок (`/keybindings`). Голосовий ввід використовує ваш обліковий запис Claude.ai для обробки мовлення в текст.

---

## Канали

Канали — це функція Research Preview, яка надсилає події від зовнішніх сервісів у запущену сесію Claude Code через MCP-сервери. Джерела включають Telegram, Discord, iMessage та довільні вебхуки, дозволяючи Claude реагувати на повідомлення в реальному часі без опитування.

### Підписка на канали

```bash
# Підписка на плагіни каналів при запуску
claude --channels discord,telegram

# Підписка на кілька джерел
claude --channels discord,telegram,imessage,webhooks
```

### Підтримувані інтеграції

| Інтеграція | Опис |
|-------------|-------------|
| **Discord** | Отримання та відповіді на повідомлення Discord у вашій сесії |
| **Telegram** | Отримання та відповіді на повідомлення Telegram у вашій сесії |
| **iMessage** | Отримання сповіщень iMessage у вашій сесії |
| **Webhooks** | Отримання подій від довільних джерел вебхуків |

### Конфігурація

Налаштуйте канали прапорцем `--channels` при запуску. Для корпоративних розгортань використовуйте керовану настройку для контролю дозволених плагінів каналів:

```json
{
  "allowedChannelPlugins": ["discord", "telegram"]
}
```

Керована настройка `allowedChannelPlugins` контролює, які плагіни каналів дозволені в організації.

### Як це працює

1. MCP-сервери діють як плагіни каналів, що підключаються до зовнішніх сервісів
2. Вхідні повідомлення та події надсилаються в активну сесію Claude Code
3. Claude може читати та відповідати на повідомлення в контексті сесії
4. Плагіни каналів мають бути затверджені через керовану настройку `allowedChannelPlugins`
5. Опитування не потрібне — події надсилаються в реальному часі

---

## Інтеграція Chrome

Інтеграція Chrome підключає Claude Code до вашого браузера Chrome або Microsoft Edge для автоматизації та відлагодження веб-сторінок у реальному часі. Це бета-функція, доступна з v2.0.73+ (підтримка Edge додана в v1.0.36+).

### Увімкнення інтеграції Chrome

**При запуску**:

```bash
claude --chrome      # Увімкнути зʼєднання з Chrome
claude --no-chrome   # Вимкнути зʼєднання з Chrome
```

**Всередині сесії**:

```
/chrome
```

Оберіть "Enabled by default" для активації інтеграції Chrome для всіх майбутніх сесій. Claude Code використовує стан входу вашого браузера, тому може взаємодіяти з автентифікованими веб-додатками.

### Можливості

| Можливість | Опис |
|------------|-------------|
| **Відлагодження в реальному часі** | Читання логів консолі, інспектування DOM-елементів, відлагодження JavaScript в реальному часі |
| **Перевірка дизайну** | Порівняння відрендерених сторінок з макетами дизайну |
| **Валідація форм** | Тестування відправки форм, валідації вводу та обробки помилок |
| **Тестування веб-додатків** | Взаємодія з автентифікованими додатками (Gmail, Google Docs, Notion тощо) |
| **Витягування даних** | Збір та обробка контенту з веб-сторінок |
| **Запис сесії** | Запис взаємодій з браузером у GIF-файли |

### Дозволи на рівні сайтів

Розширення Chrome управляє доступом до окремих сайтів. Надавайте або відкликайте доступ для конкретних сайтів у будь-який час через спливаюче вікно розширення. Claude Code взаємодіє лише з сайтами, які ви явно дозволили.

### Як це працює

Claude Code керує браузером у видимому вікні — ви можете спостерігати за діями в реальному часі. Коли браузер натрапляє на сторінку входу або CAPTCHA, Claude зупиняється і чекає, поки ви вручну обробите це, перш ніж продовжити.

### Відомі обмеження

- **Підтримка браузерів**: Тільки Chrome та Edge — Brave, Arc та інші браузери на базі Chromium не підтримуються
- **WSL**: Недоступно у Windows Subsystem for Linux
- **Сторонні провайдери**: Не підтримується з провайдерами API Bedrock, Vertex або Foundry
- **Idle service worker**: Service worker розширення Chrome може переходити у неактивний стан під час тривалих сесій

> **Порада**: Інтеграція Chrome є бета-функцією. Підтримка браузерів може розширитись у майбутніх релізах.

---

## Remote Control

Remote Control дозволяє продовжити локально запущену сесію Claude Code з телефону, планшета або будь-якого браузера. Ваша локальна сесія продовжує працювати на вашому компʼютері — нічого не переміщується у хмару. Доступно на планах Pro, Max, Team та Enterprise (v2.1.51+).

### Запуск Remote Control

**З CLI**:

```bash
# Запуск із назвою сесії за замовчуванням
claude remote-control

# Запуск із власною назвою
claude remote-control --name "Auth Refactor"
```

**Зсередини сесії**:

```
/remote-control
/remote-control "Auth Refactor"
```

**Доступні прапорці**:

| Прапорець | Опис |
|------|-------------|
| `--name "title"` | Власна назва сесії для зручної ідентифікації |
| `--verbose` | Показувати детальні логи зʼєднання |
| `--sandbox` | Увімкнути ізоляцію файлової системи та мережі |
| `--no-sandbox` | Вимкнути пісочницю (за замовчуванням) |

### Підключення до сесії

Три способи підключення з іншого пристрою:

1. **URL сесії** — Виводиться в термінал при запуску сесії; відкрийте у будь-якому браузері
2. **QR-код** — Натисніть `пробіл` після запуску для відображення QR-коду для сканування
3. **Пошук за назвою** — Перегляньте ваші сесії на claude.ai/code або у мобільному додатку Claude (iOS/Android)

### Безпека

- **Жодних вхідних портів** не відкривається на вашому компʼютері
- **Тільки вихідний HTTPS** через TLS
- **Обмежені облікові дані** — кілька короткоживучих токенів з вузькою областю дії
- **Ізоляція сесій** — кожна віддалена сесія незалежна

### Remote Control проти Claude Code у вебі

| Аспект | Remote Control | Claude Code у вебі |
|--------|---------------|-------------------|
| **Виконання** | Працює на вашому компʼютері | Працює у хмарі Anthropic |
| **Локальні інструменти** | Повний доступ до локальних MCP-серверів, файлів та CLI | Без локальних залежностей |
| **Випадок використання** | Продовження локальної роботи з іншого пристрою | Початок роботи з нуля в будь-якому браузері |

### Обмеження

- Одна віддалена сесія на екземпляр Claude Code
- Термінал має залишатись відкритим на хост-машині
- Сесія закінчується через ~10 хвилин, якщо мережа недоступна

### Випадки використання

- Управління Claude Code з мобільного пристрою або планшета, перебуваючи далеко від робочого місця
- Використання багатшого UI claude.ai зі збереженням локального виконання інструментів
- Швидке ревʼю коду на ходу з повним локальним середовищем розробки

---

## Веб-сесії

Веб-сесії дозволяють запускати Claude Code безпосередньо у браузері на claude.ai/code або створювати веб-сесії з CLI.

### Створення веб-сесії

```bash
# Створення нової веб-сесії з CLI
claude --remote "implement the new API endpoints"
```

Це запускає сесію Claude Code на claude.ai, до якої можна отримати доступ з будь-якого браузера.

### Відновлення веб-сесій локально

Якщо ви почали сесію у вебі і хочете продовжити локально:

```bash
# Відновити веб-сесію в локальному терміналі
claude --teleport
```

Або зсередини інтерактивного REPL:
```
/teleport
```

### Випадки використання

- Почати роботу на одному компʼютері і продовжити на іншому
- Поділитися URL сесії з членами команди
- Використовувати веб-UI для візуального перегляду diff, потім перемкнутися на термінал для виконання

---

## Десктопний додаток

Десктопний додаток Claude Code надає автономний додаток з візуальним переглядом diff, паралельними сесіями та інтегрованими конекторами. Доступний для macOS та Windows (плани Pro, Max, Team та Enterprise).

### Встановлення

Завантажте з [claude.ai](https://claude.ai) для вашої платформи:
- **macOS**: Універсальна збірка (Apple Silicon та Intel)
- **Windows**: Інсталятори для x64 та ARM64

Дивіться [Desktop Quickstart](https://code.claude.com/docs/en/desktop-quickstart) для інструкцій з налаштування.

### Передача з CLI

Передайте поточну CLI-сесію в десктопний додаток:

```
/desktop
```

### Основні функції

| Функція | Опис |
|---------|-------------|
| **Перегляд diff** | Візуальний перегляд файл за файлом з inline-коментарями; Claude читає коментарі та вносить виправлення |
| **Попередній перегляд додатку** | Автозапуск dev-серверів з вбудованим браузером для живої перевірки |
| **Моніторинг PR** | Інтеграція GitHub CLI з автовиправленням помилок CI та автозлиттям при проходженні перевірок |
| **Паралельні сесії** | Кілька сесій у бічній панелі з автоматичною ізоляцією Git worktree |
| **Заплановані завдання** | Повторювані завдання (щогодини, щодня, у робочі дні, щотижня), що працюють при відкритому додатку |
| **Багатий рендеринг** | Рендеринг коду, markdown та діаграм з підсвіткою синтаксису |

### Конфігурація попереднього перегляду додатку

Налаштуйте поведінку dev-сервера в `.claude/launch.json`:

```json
{
  "command": "npm run dev",
  "port": 3000,
  "readyPattern": "ready on",
  "persistCookies": true
}
```

### Конектори

Підключення зовнішніх сервісів для багатшого контексту:

| Конектор | Можливість |
|-----------|------------|
| **GitHub** | Моніторинг PR, трекінг issues, ревʼю коду |
| **Slack** | Сповіщення, контекст каналів |
| **Linear** | Трекінг issues, управління спринтами |
| **Notion** | Документація, доступ до бази знань |
| **Asana** | Управління завданнями, трекінг проєктів |
| **Calendar** | Обізнаність про розклад, контекст зустрічей |

> **Примітка**: Конектори недоступні для віддалених (хмарних) сесій.

### Віддалені та SSH-сесії

- **Віддалені сесії**: Працюють на хмарній інфраструктурі Anthropic; продовжуються навіть після закриття додатку. Доступні з claude.ai/code або мобільного додатку Claude
- **SSH-сесії**: Підключення до віддалених машин через SSH з повним доступом до віддаленої файлової системи та інструментів. Claude Code повинен бути встановлений на віддаленій машині

### Режими дозволів у десктопному додатку

Десктопний додаток підтримує ті самі 4 режими дозволів, що й CLI:

| Режим | Поведінка |
|------|----------|
| **Ask permissions** (за замовчуванням) | Перегляд та затвердження кожного редагування та команди |
| **Auto accept edits** | Редагування файлів автозатверджуються; команди потребують ручного затвердження |
| **Plan mode** | Перегляд підходу перед будь-якими змінами |
| **Bypass permissions** | Автоматичне виконання (лише у пісочниці, контролюється адміністратором) |

### Корпоративні функції

- **Консоль адміністратора**: Контроль доступу до вкладки Code та налаштувань дозволів для організації
- **Розгортання через MDM**: Розгортання через MDM на macOS або MSIX на Windows
- **Інтеграція SSO**: Вимога єдиного входу для членів організації
- **Керовані налаштування**: Централізоване управління конфігурацією команди та доступністю моделей

---

## Список завдань

Функція списку завдань забезпечує постійне відстеження завдань, яке переживає стиснення контексту (коли історія розмови обрізається для вміщення в контекстне вікно).

### Перемикання списку завдань

Натисніть `Ctrl+T` для перемикання перегляду списку завдань під час сесії.

### Постійні завдання

Завдання зберігаються між стисненнями контексту, гарантуючи, що тривалі робочі елементи не втрачаються при обрізці контексту розмови. Це особливо корисно для складних, багатоетапних реалізацій.

### Іменовані директорії завдань

Використовуйте змінну оточення `CLAUDE_CODE_TASK_LIST_ID` для створення іменованих директорій завдань, спільних між сесіями:

```bash
export CLAUDE_CODE_TASK_LIST_ID=my-project-sprint-3
```

Це дозволяє кільком сесіям використовувати один список завдань, що корисно для командних робочих процесів або проєктів з кількома сесіями.

---

## Підказки промптів

Підказки промптів відображають напівпрозорі приклади команд на основі вашої git-історії та поточного контексту розмови.

### Як це працює

- Підказки зʼявляються як напівпрозорий текст під вашим вводом
- Натисніть `Tab` для прийняття підказки
- Натисніть `Enter` для прийняття та негайної відправки
- Підказки враховують контекст, використовуючи git-історію та стан розмови

### Вимкнення підказок промптів

```bash
export CLAUDE_CODE_ENABLE_PROMPT_SUGGESTION=false
```

---

## Git Worktrees

Git Worktrees дозволяють запускати Claude Code в ізольованому робочому дереві, забезпечуючи паралельну роботу на різних гілках без stash або перемикання.

### Запуск у Worktree

```bash
# Запуск Claude Code в ізольованому робочому дереві
claude --worktree
# або
claude -w
```

### Розташування Worktree

Робочі дерева створюються за адресою:
```
<repo>/.claude/worktrees/<n>
```

### Sparse Checkout для монорепозиторіїв

Використовуйте налаштування `worktree.sparsePaths` для виконання sparse-checkout у монорепозиторіях, зменшуючи використання диску та час клонування:

```json
{
  "worktree": {
    "sparsePaths": ["packages/my-package", "shared/"]
  }
}
```

### Інструменти та хуки Worktree

| Елемент | Опис |
|------|-------------|
| `ExitWorktree` | Інструмент для виходу та очищення поточного робочого дерева |
| `WorktreeCreate` | Подія хуку при створенні робочого дерева |
| `WorktreeRemove` | Подія хуку при видаленні робочого дерева |

### Автоочищення

Якщо в робочому дереві не було зроблено змін, воно автоматично очищується при завершенні сесії.

### Випадки використання

- Робота над feature-гілкою зі збереженням незміненої основної гілки
- Запуск тестів в ізоляції без впливу на робочу директорію
- Спроба експериментальних змін у одноразовому середовищі
- Sparse-checkout конкретних пакетів у монорепозиторіях для швидшого запуску

---

## Пісочниця

Пісочниця забезпечує ізоляцію файлової системи та мережі на рівні ОС для Bash-команд, що виконуються Claude Code. Це доповнює правила дозволів і забезпечує додатковий рівень безпеки.

### Увімкнення пісочниці

**Слеш-команда**:
```
/sandbox
```

**Прапорці CLI**:
```bash
claude --sandbox       # Увімкнути пісочницю
claude --no-sandbox    # Вимкнути пісочницю
```

### Налаштування конфігурації

| Налаштування | Опис |
|---------|-------------|
| `sandbox.enabled` | Увімкнути або вимкнути пісочницю |
| `sandbox.failIfUnavailable` | Зупинитись, якщо пісочницю неможливо активувати |
| `sandbox.filesystem.allowWrite` | Шляхи з дозволом на запис |
| `sandbox.filesystem.allowRead` | Шляхи з дозволом на читання |
| `sandbox.filesystem.denyRead` | Шляхи з забороною читання |
| `sandbox.enableWeakerNetworkIsolation` | Увімкнути слабшу ізоляцію мережі на macOS |

### Приклад конфігурації

```json
{
  "sandbox": {
    "enabled": true,
    "failIfUnavailable": true,
    "filesystem": {
      "allowWrite": ["/Users/me/project"],
      "allowRead": ["/Users/me/project", "/usr/local/lib"],
      "denyRead": ["/Users/me/.ssh", "/Users/me/.aws"]
    },
    "enableWeakerNetworkIsolation": true
  }
}
```

### Як це працює

- Bash-команди виконуються у пісочниці з обмеженим доступом до файлової системи
- Мережевий доступ може бути ізольований для запобігання небажаним зовнішнім зʼєднанням
- Працює разом з правилами дозволів для глибокого захисту
- На macOS використовуйте `sandbox.enableWeakerNetworkIsolation` для мережевих обмежень (повна ізоляція мережі недоступна на macOS)

### Випадки використання

- Безпечний запуск ненадійного або згенерованого коду
- Запобігання випадковим змінам файлів за межами проєкту
- Обмеження мережевого доступу під час автоматизованих завдань

---

## Керовані налаштування (Enterprise)

Керовані налаштування дозволяють корпоративним адміністраторам розгортати конфігурацію Claude Code по всій організації за допомогою платформних засобів управління.

### Методи розгортання

| Платформа | Метод | Починаючи з |
|----------|--------|-------|
| macOS | Керовані plist-файли (MDM) | v2.1.51+ |
| Windows | Реєстр Windows | v2.1.51+ |
| Кросплатформний | Керовані файли конфігурації | v2.1.51+ |
| Кросплатформний | Керовані drop-ins (директорія `managed-settings.d/`) | v2.1.83+ |

### Керовані Drop-ins

Починаючи з v2.1.83, адміністратори можуть розгортати кілька файлів керованих налаштувань у директорію `managed-settings.d/`. Файли обʼєднуються в алфавітному порядку, дозволяючи модульну конфігурацію між командами:

```
~/.claude/managed-settings.d/
  00-org-defaults.json
  10-team-policies.json
  20-project-overrides.json
```

### Доступні керовані налаштування

| Налаштування | Опис |
|---------|-------------|
| `disableBypassPermissionsMode` | Заборонити користувачам вмикати обхід дозволів |
| `availableModels` | Обмежити моделі, доступні для вибору |
| `allowedChannelPlugins` | Контролювати дозволені плагіни каналів |
| `autoMode.environment` | Налаштувати довірену інфраструктуру для auto mode |
| Власні політики | Організаційні політики дозволів та інструментів |

### Приклад: macOS Plist

```xml
<?xml version="1.0" encoding="UTF-8"?>
<!DOCTYPE plist PUBLIC "-//Apple//DTD PLIST 1.0//EN"
  "http://www.apple.com/DTDs/PropertyList-1.0.dtd">
<plist version="1.0">
<dict>
  <key>disableBypassPermissionsMode</key>
  <true/>
  <key>availableModels</key>
  <array>
    <string>claude-sonnet-4-6</string>
    <string>claude-haiku-4-5</string>
  </array>
</dict>
</plist>
```

---

## Конфігурація та налаштування

### Розташування файлів конфігурації

1. **Глобальна конфігурація**: `~/.claude/config.json`
2. **Конфігурація проєкту**: `./.claude/config.json`
3. **Конфігурація користувача**: `~/.config/claude-code/settings.json`

### Повний приклад конфігурації

**Конфігурація основних розширених функцій:**

```json
{
  "permissions": {
    "mode": "default"
  },
  "hooks": {
    "PreToolUse:Edit": "eslint --fix ${file_path}",
    "PostToolUse:Write": "~/.claude/hooks/security-scan.sh"
  },
  "mcp": {
    "enabled": true,
    "servers": {
      "github": {
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-github"]
      }
    }
  }
}
```

**Розширений приклад конфігурації:**

```json
{
  "permissions": {
    "mode": "default",
    "allowedTools": ["Bash(git log:*)", "Read"],
    "disallowedTools": ["Bash(rm -rf:*)"]
  },

  "hooks": {
    "PreToolUse": [{ "matcher": "Edit", "hooks": ["eslint --fix ${file_path}"] }],
    "PostToolUse": [{ "matcher": "Write", "hooks": ["~/.claude/hooks/security-scan.sh"] }],
    "Stop": [{ "hooks": ["~/.claude/hooks/notify.sh"] }]
  },

  "mcp": {
    "enabled": true,
    "servers": {
      "github": {
        "command": "npx",
        "args": ["-y", "@modelcontextprotocol/server-github"],
        "env": {
          "GITHUB_TOKEN": "${GITHUB_TOKEN}"
        }
      }
    }
  }
}
```

### Змінні оточення

Перевизначення конфігурації через змінні оточення:

```bash
# Вибір моделі
export ANTHROPIC_MODEL=claude-opus-4-6
export ANTHROPIC_DEFAULT_OPUS_MODEL=claude-opus-4-6
export ANTHROPIC_DEFAULT_SONNET_MODEL=claude-sonnet-4-6
export ANTHROPIC_DEFAULT_HAIKU_MODEL=claude-haiku-4-5

# Конфігурація API
export ANTHROPIC_API_KEY=sk-ant-...

# Конфігурація мислення
export MAX_THINKING_TOKENS=16000
export CLAUDE_CODE_EFFORT_LEVEL=high

# Перемикачі функцій
export CLAUDE_CODE_DISABLE_AUTO_MEMORY=true
export CLAUDE_CODE_DISABLE_BACKGROUND_TASKS=true
export CLAUDE_CODE_DISABLE_CRON=1
export CLAUDE_CODE_DISABLE_GIT_INSTRUCTIONS=true
export CLAUDE_CODE_DISABLE_TERMINAL_TITLE=true
export CLAUDE_CODE_DISABLE_1M_CONTEXT=true
export CLAUDE_CODE_DISABLE_NONSTREAMING_FALLBACK=true
export CLAUDE_CODE_ENABLE_PROMPT_SUGGESTION=false
export CLAUDE_CODE_ENABLE_TASKS=true
export CLAUDE_CODE_SIMPLE=true              # Встановлюється прапорцем --bare

# Конфігурація MCP
export MAX_MCP_OUTPUT_TOKENS=50000
export ENABLE_TOOL_SEARCH=true

# Управління завданнями
export CLAUDE_CODE_TASK_LIST_ID=my-project-tasks

# Agent teams (експериментально)
export CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1

# Конфігурація субагентів та плагінів
export CLAUDE_CODE_SUBAGENT_MODEL=sonnet
export CLAUDE_CODE_PLUGIN_SEED_DIR=./my-plugins
export CLAUDE_CODE_NEW_INIT=1

# Підпроцеси та стрімінг
export CLAUDE_CODE_SUBPROCESS_ENV_SCRUB="SECRET_KEY,DB_PASSWORD"
export CLAUDE_AUTOCOMPACT_PCT_OVERRIDE=80
export CLAUDE_STREAM_IDLE_TIMEOUT_MS=30000
export ANTHROPIC_CUSTOM_MODEL_OPTION=my-custom-model
export SLASH_COMMAND_TOOL_CHAR_BUDGET=50000
```

### Команди управління конфігурацією

```
User: /config
[Opens interactive configuration menu]
```

Команда `/config` надає інтерактивне меню для перемикання налаштувань, таких як:
- Розширене мислення увімк./вимк.
- Детальний вивід
- Режим дозволів
- Вибір моделі

### Конфігурація на рівні проєкту

Створіть `.claude/config.json` у вашому проєкті:

```json
{
  "hooks": {
    "PreToolUse": [{ "matcher": "Bash", "hooks": ["npm test && npm run lint"] }]
  },
  "permissions": {
    "mode": "default"
  },
  "mcp": {
    "servers": {
      "project-db": {
        "command": "mcp-postgres",
        "env": {
          "DATABASE_URL": "${PROJECT_DB_URL}"
        }
      }
    }
  }
}
```

---

## Agent Teams

Agent Teams — це експериментальна функція, яка дозволяє кільком екземплярам Claude Code співпрацювати над завданням. Вимкнена за замовчуванням.

### Увімкнення Agent Teams

Увімкнення через змінну оточення або налаштування:

```bash
# Змінна оточення
export CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS=1
```

Або додайте до вашого JSON-файлу налаштувань:

```json
{
  "CLAUDE_CODE_EXPERIMENTAL_AGENT_TEAMS": "1"
}
```

### Як працюють Agent Teams

- **Лідер команди** координує загальне завдання та делегує підзавдання товаришам по команді
- **Товариші по команді** працюють незалежно, кожен зі своїм контекстним вікном
- **Спільний список завдань** забезпечує самокоординацію між членами команди
- Використовуйте визначення субагентів (`.claude/agents/` або прапорець `--agents`) для визначення ролей та спеціалізацій товаришів

### Режими відображення

Agent Teams підтримують два режими відображення, що налаштовуються прапорцем `--teammate-mode`:

| Режим | Опис |
|------|-------------|
| `in-process` (за замовчуванням) | Товариші працюють у тому ж процесі терміналу |
| `tmux` | Кожен товариш отримує окрему розділену панель (потрібен tmux або iTerm2) |
| `auto` | Автоматичний вибір найкращого режиму відображення |

```bash
# Використання tmux для відображення товаришів
claude --teammate-mode tmux

# Явне використання in-process режиму
claude --teammate-mode in-process
```

### Випадки використання

- Великі завдання рефакторингу, де різні товариші обробляють різні модулі
- Паралельне ревʼю коду та реалізація
- Координовані зміни кількох файлів по всій кодовій базі

> **Примітка**: Agent Teams є експериментальною функцією і може змінитися у майбутніх релізах. Дивіться [code.claude.com/docs/en/agent-teams](https://code.claude.com/docs/en/agent-teams) для повного довідника.

---

## Найкращі практики

### Режим планування
- ✅ Використовуйте для складних багатоетапних завдань
- ✅ Переглядайте плани перед затвердженням
- ✅ Модифікуйте плани за потреби
- ❌ Не використовуйте для простих завдань

### Розширене мислення
- ✅ Використовуйте для архітектурних рішень
- ✅ Використовуйте для вирішення складних проблем
- ✅ Переглядайте процес мислення
- ❌ Не використовуйте для простих запитів

### Фонові завдання
- ✅ Використовуйте для тривалих операцій
- ✅ Моніторте прогрес завдань
- ✅ Коректно обробляйте помилки завдань
- ❌ Не запускайте занадто багато паралельних завдань

### Дозволи
- ✅ Використовуйте `plan` для ревʼю коду (тільки читання)
- ✅ Використовуйте `default` для інтерактивної розробки
- ✅ Використовуйте `acceptEdits` для автоматизованих робочих процесів
- ✅ Використовуйте `auto` для автономної роботи із запобіжниками безпеки
- ❌ Не використовуйте `bypassPermissions` без крайньої необхідності

### Сесії
- ✅ Використовуйте окремі сесії для різних завдань
- ✅ Зберігайте важливі стани сесій
- ✅ Очищайте старі сесії
- ❌ Не змішуйте неповʼязану роботу в одній сесії

---

## Додаткові ресурси

Для отримання додаткової інформації про Claude Code та повʼязані функції:

- [Офіційна документація інтерактивного режиму](https://code.claude.com/docs/en/interactive-mode)
- [Офіційна документація Headless Mode](https://code.claude.com/docs/en/headless)
- [Довідник CLI](https://code.claude.com/docs/en/cli-reference)
- [Посібник з контрольних точок](../08-checkpoints/) — Управління сесіями та відкат
- [Слеш-команди](../01-slash-commands/) — Довідник команд
- [Посібник з памʼяті](../02-memory/) — Постійний контекст
- [Посібник з навичок](../03-skills/) — Автономні можливості
- [Посібник з субагентів](../04-subagents/) — Делеговане виконання завдань
- [Посібник з MCP](../05-mcp/) — Доступ до зовнішніх даних
- [Посібник з хуків](../06-hooks/) — Автоматизація на основі подій
- [Посібник з плагінів](../07-plugins/) — Пакетні розширення
- [Офіційна документація запланованих завдань](https://code.claude.com/docs/en/scheduled-tasks)
- [Офіційна документація інтеграції Chrome](https://code.claude.com/docs/en/chrome)
- [Офіційна документація Remote Control](https://code.claude.com/docs/en/remote-control)
- [Офіційна документація клавіатурних скорочень](https://code.claude.com/docs/en/keybindings)
- [Офіційна документація десктопного додатку](https://code.claude.com/docs/en/desktop)
- [Офіційна документація Agent Teams](https://code.claude.com/docs/en/agent-teams)

---
**Останнє оновлення**: 9 квітня 2026
**Версія Claude Code**: 2.1.97
**Сумісні моделі**: Claude Sonnet 4.6, Claude Opus 4.6, Claude Haiku 4.5
