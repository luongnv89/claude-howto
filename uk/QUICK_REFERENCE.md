<!-- i18n-source: QUICK_REFERENCE.md -->
<!-- i18n-source-sha: 63a1416 -->
<!-- i18n-date: 2026-04-09 -->

<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../resources/logos/claude-howto-logo.svg">
</picture>

# Приклади Claude Code — Картка швидкого довідника

## 🚀 Команди швидкого встановлення

### Слеш-команди

```bash
# Встановити всі
cp 01-slash-commands/*.md .claude/commands/

# Встановити конкретну
cp 01-slash-commands/optimize.md .claude/commands/
```

### Пам'ять

```bash
# Пам'ять проекту
cp 02-memory/project-CLAUDE.md ./CLAUDE.md

# Персональна пам'ять
cp 02-memory/personal-CLAUDE.md ~/.claude/CLAUDE.md
```

### Навички (Skills)

```bash
# Персональні навички
cp -r 03-skills/code-review-specialist ~/.claude/skills/

# Навички проекту
cp -r 03-skills/code-review-specialist .claude/skills/
```

### Субагенти

```bash
# Встановити всі
cp 04-subagents/*.md .claude/agents/

# Встановити конкретного
cp 04-subagents/code-reviewer.md .claude/agents/
```

### MCP

```bash
# Встановити облікові дані
export GITHUB_TOKEN="your_token"
export DATABASE_URL="postgresql://..."

# Встановити конфігурацію (рівень проекту)
cp 05-mcp/github-mcp.json .mcp.json

# Або рівень користувача: додати в ~/.claude.json
```

### Хуки

```bash
# Встановити хуки
mkdir -p ~/.claude/hooks
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh

# Налаштувати в settings (~/.claude/settings.json)
```

### Плагіни

```bash
# Встановити з прикладів (якщо опубліковані)
/plugin install pr-review
/plugin install devops-automation
/plugin install documentation
```

### Контрольні точки

```bash
# Контрольні точки створюються автоматично з кожним промптом
# Для відкату натисніть Esc двічі або скористайтесь:
/rewind

# Потім оберіть: Відновити код і розмову, Відновити розмову,
# Відновити код, Підсумувати звідси, або Скасувати
```

### Розширені функції

```bash
# Налаштувати в settings (.claude/settings.json)
# Див. 09-advanced-features/config-examples.json

# Режим планування
/plan Task description

# Режими дозволів (прапорець --permission-mode)
# default        - Запитувати дозвіл на ризиковані дії
# acceptEdits    - Автоприйняття редагувань, запит на інше
# plan           - Лише аналіз, без змін (тільки читання)
# dontAsk        - Приймати все, крім ризикованого
# auto           - Фоновий класифікатор вирішує автоматично
# bypassPermissions - Приймати все (потребує --dangerously-skip-permissions)

# Управління сесіями
/resume                # Відновити попередню розмову
/rename "name"         # Назвати поточну сесію
/fork                  # Розгалужити поточну сесію
claude -c              # Продовжити останню розмову
claude -r "session"    # Відновити сесію за назвою/ID
```

---

## 📋 Шпаргалка по функціях

| Функція | Шлях встановлення | Використання |
|---------|------------------|-------------|
| **Слеш-команди (55+)** | `.claude/commands/*.md` | `/command-name` |
| **Пам'ять** | `./CLAUDE.md` | Автозавантаження |
| **Навички** | `.claude/skills/*/SKILL.md` | Автовиклик |
| **Субагенти** | `.claude/agents/*.md` | Автоделегування |
| **MCP** | `.mcp.json` (проект) або `~/.claude.json` (користувач) | `/mcp__server__action` |
| **Хуки (25 подій)** | `~/.claude/hooks/*.sh` | Тригер на подію (4 типи) |
| **Плагіни** | Через `/plugin install` | Пакет всього |
| **Контрольні точки** | Вбудовано | `Esc+Esc` або `/rewind` |
| **Режим планування** | Вбудовано | `/plan <завдання>` |
| **Режими дозволів (6)** | Вбудовано | `--allowedTools`, `--permission-mode` |
| **Сесії** | Вбудовано | `/session <команда>` |
| **Фонові завдання** | Вбудовано | Run in background |
| **Віддалене керування** | Вбудовано | WebSocket API |
| **Веб-сесії** | Вбудовано | `claude web` |
| **Git Worktrees** | Вбудовано | `/worktree` |
| **Автопам'ять** | Вбудовано | Автозбереження в CLAUDE.md |
| **Список завдань** | Вбудовано | `/task list` |
| **Вбудовані навички (5)** | Вбудовано | `/simplify`, `/loop`, `/claude-api`, `/voice`, `/browse` |

---

## 🎯 Типові сценарії використання

### Ревʼю коду

```bash
# Спосіб 1: Слеш-команда
cp 01-slash-commands/optimize.md .claude/commands/
# Використання: /optimize

# Спосіб 2: Субагент
cp 04-subagents/code-reviewer.md .claude/agents/
# Використання: Автоделегування

# Спосіб 3: Навичка
cp -r 03-skills/code-review-specialist ~/.claude/skills/
# Використання: Автовиклик

# Спосіб 4: Плагін (найкращий)
/plugin install pr-review
# Використання: /review-pr
```

### Документація

```bash
# Слеш-команда
cp 01-slash-commands/generate-api-docs.md .claude/commands/

# Субагент
cp 04-subagents/documentation-writer.md .claude/agents/

# Навичка
cp -r 03-skills/doc-generator ~/.claude/skills/

# Плагін (комплексне рішення)
/plugin install documentation
```

### DevOps

```bash
# Повний плагін
/plugin install devops-automation

# Команди: /deploy, /rollback, /status, /incident
```

### Командні стандарти

```bash
# Пам'ять проекту
cp 02-memory/project-CLAUDE.md ./CLAUDE.md

# Відредагуйте під вашу команду
vim CLAUDE.md
```

### Автоматизація та хуки

```bash
# Встановити хуки (25 подій, 4 типи: command, http, prompt, agent)
mkdir -p ~/.claude/hooks
cp 06-hooks/*.sh ~/.claude/hooks/
chmod +x ~/.claude/hooks/*.sh

# Приклади:
# - Тести перед комітом: pre-commit.sh
# - Автоформатування коду: format-code.sh
# - Сканування безпеки: security-scan.sh

# Auto Mode для повністю автономних процесів
claude --enable-auto-mode -p "Refactor and test the auth module"
# Або циклічна зміна режимів інтерактивно з Shift+Tab
```

### Безпечний рефакторинг

```bash
# Контрольні точки створюються автоматично перед кожним промптом
# Спробуйте рефакторинг
# Якщо вдалось: продовжуйте
# Якщо не вдалось: натисніть Esc+Esc або /rewind для відкату
```

### Складна реалізація

```bash
# Використайте режим планування
/plan Implement user authentication system

# Claude створить детальний план
# Перегляньте та затвердіть
# Claude реалізує систематично
```

### Інтеграція з CI/CD

```bash
# Запуск у headless-режимі (неінтерактивно)
claude -p "Run all tests and generate report"

# З режимом дозволів для CI
claude -p "Run tests" --permission-mode dontAsk

# З Auto Mode для повністю автономних CI-завдань
claude --enable-auto-mode -p "Run tests and fix failures"

# З хуками для автоматизації
# Див. 09-advanced-features/README.md
```

### Навчання та експериментування

```bash
# Режим plan для безпечного аналізу
claude --permission-mode plan

# Експериментуйте безпечно — контрольні точки створюються автоматично
# Для відкату: натисніть Esc+Esc або /rewind
```

### Команди агентів

```bash
# Увімкнути команди агентів
export CLAUDE_AGENT_TEAMS=1

# Або в settings.json
{ "agentTeams": { "enabled": true } }

# Почніть з: "Implement feature X using a team approach"
```

### Заплановані завдання

```bash
# Запускати команду кожні 5 хвилин
/loop 5m /check-status

# Одноразове нагадування
/loop 30m "remind me to check the deploy"
```

---

## 📁 Довідник розташування файлів

```
Ваш проект/
├── .claude/
│   ├── commands/              # Слеш-команди тут
│   ├── agents/                # Субагенти тут
│   ├── skills/                # Навички проекту тут
│   └── settings.json          # Налаштування проекту (хуки тощо)
├── .mcp.json                  # Конфігурація MCP (рівень проекту)
├── CLAUDE.md                  # Пам'ять проекту
└── src/
    └── api/
        └── CLAUDE.md          # Пам'ять для конкретного каталогу

Домашній каталог/
├── .claude/
│   ├── commands/              # Персональні команди
│   ├── agents/                # Персональні агенти
│   ├── skills/                # Персональні навички
│   ├── hooks/                 # Скрипти хуків
│   ├── settings.json          # Налаштування користувача
│   ├── managed-settings.d/    # Керовані налаштування (enterprise/org)
│   └── CLAUDE.md              # Персональна пам'ять
└── .claude.json               # Персональна конфігурація MCP (рівень користувача)
```

---

## 🔍 Пошук прикладів

### За категорією

- **Слеш-команди**: `01-slash-commands/`
- **Пам'ять**: `02-memory/`
- **Навички**: `03-skills/`
- **Субагенти**: `04-subagents/`
- **MCP**: `05-mcp/`
- **Хуки**: `06-hooks/`
- **Плагіни**: `07-plugins/`
- **Контрольні точки**: `08-checkpoints/`
- **Розширені функції**: `09-advanced-features/`
- **CLI**: `10-cli/`

### За сценарієм

- **Продуктивність**: `01-slash-commands/optimize.md`
- **Безпека**: `04-subagents/secure-reviewer.md`
- **Тестування**: `04-subagents/test-engineer.md`
- **Документація**: `03-skills/doc-generator/`
- **DevOps**: `07-plugins/devops-automation/`

### За складністю

- **Просто**: Слеш-команди
- **Середньо**: Субагенти, Пам'ять
- **Просунуто**: Навички, Хуки
- **Комплексно**: Плагіни

---

## 🎓 Навчальний шлях

### День 1

```bash
# Прочитати огляд
cat README.md

# Встановити команду
cp 01-slash-commands/optimize.md .claude/commands/

# Спробувати
/optimize
```

### Дні 2-3

```bash
# Налаштувати пам'ять
cp 02-memory/project-CLAUDE.md ./CLAUDE.md
vim CLAUDE.md

# Встановити субагента
cp 04-subagents/code-reviewer.md .claude/agents/
```

### Дні 4-5

```bash
# Налаштувати MCP
export GITHUB_TOKEN="your_token"
cp 05-mcp/github-mcp.json .mcp.json

# Спробувати MCP-команди
/mcp__github__list_prs
```

### Тиждень 2

```bash
# Встановити навичку
cp -r 03-skills/code-review-specialist ~/.claude/skills/

# Дозвольте автовиклик
# Просто скажіть: "Review this code for issues"
```

### Тиждень 3+

```bash
# Встановити повний плагін
/plugin install pr-review

# Використати вбудовані функції
/review-pr
/check-security
/check-tests
```

---

## Нові функції (березень 2026)

| Функція | Опис | Використання |
|---------|------|-------------|
| **Auto Mode** | Повністю автономна робота з фоновим класифікатором | Прапорець `--enable-auto-mode`, `Shift+Tab` для зміни режимів |
| **Канали** | Інтеграція з Discord та Telegram | Прапорець `--channels`, боти Discord/Telegram |
| **Голосовий ввід** | Голосові команди та контекст для Claude | Команда `/voice` |
| **Хуки (26 подій)** | Розширена система хуків з 4 типами | Типи: command, http, prompt, agent |
| **MCP Elicitation** | MCP-сервери можуть запитувати ввід під час виконання | Автозапит при потребі сервера |
| **Plugin LSP** | Підтримка Language Server Protocol для плагінів | `userConfig`, змінна `${CLAUDE_PLUGIN_DATA}` |
| **Віддалене керування** | Керування Claude Code через WebSocket API | `claude --remote` для зовнішніх інтеграцій |
| **Веб-сесії** | Браузерний інтерфейс Claude Code | `claude web` для запуску |
| **Десктопний застосунок** | Нативний десктопний застосунок | Завантаження з claude.ai/download |
| **Список завдань** | Управління фоновими завданнями | `/task list`, `/task status <id>` |
| **Автопам'ять** | Автоматичне збереження з розмов | Claude автозберігає контекст у CLAUDE.md |
| **Git Worktrees** | Ізольовані робочі простори для паралельної розробки | `/worktree` для створення |
| **Вибір моделі** | Перемикання між Sonnet 4.6 та Opus 4.6 | `/model` або прапорець `--model` |
| **Команди агентів** | Координація кількох агентів | Увімкнути з `CLAUDE_AGENT_TEAMS=1` |
| **Заплановані завдання** | Повторювані завдання з `/loop` | `/loop 5m /command` або CronCreate |
| **Інтеграція з Chrome** | Автоматизація браузера | Прапорець `--chrome` або `/chrome` |
| **Кастомізація клавіатури** | Налаштування клавіш | Команда `/keybindings` |

---

## Поради та хитрощі

### Кастомізація

- Почніть з прикладів як є
- Модифікуйте під ваші потреби
- Тестуйте перед поширенням в команді
- Тримайте конфігурації під контролем версій

### Найкращі практики

- Використовуйте пам'ять для командних стандартів
- Використовуйте плагіни для комплексних процесів
- Використовуйте субагентів для складних завдань
- Використовуйте слеш-команди для швидких завдань

### Усунення неполадок

```bash
# Перевірити розташування файлів
ls -la .claude/commands/
ls -la .claude/agents/

# Перевірити YAML-синтаксис
head -20 .claude/agents/code-reviewer.md

# Перевірити MCP-з'єднання
echo $GITHUB_TOKEN
```

---

## 📊 Матриця функцій

| Потреба | Використовуйте | Приклад |
|---------|---------------|---------|
| Швидкий ярлик | Слеш-команда (55+) | `01-slash-commands/optimize.md` |
| Командні стандарти | Пам'ять | `02-memory/project-CLAUDE.md` |
| Автоматичний процес | Навичка | `03-skills/code-review-specialist/` |
| Спеціалізоване завдання | Субагент | `04-subagents/code-reviewer.md` |
| Зовнішні дані | MCP (+ Elicitation) | `05-mcp/github-mcp.json` |
| Автоматизація подій | Хук (26 подій, 4 типи) | `06-hooks/pre-commit.sh` |
| Комплексне рішення | Плагін (+ LSP) | `07-plugins/pr-review/` |
| Безпечний експеримент | Контрольна точка | `08-checkpoints/checkpoint-examples.md` |
| Повна автономія | Auto Mode | `--enable-auto-mode` або `Shift+Tab` |
| Чат-інтеграції | Канали | `--channels` (Discord, Telegram) |
| CI/CD-пайплайн | CLI | `10-cli/README.md` |

---

## 🔗 Швидкі посилання

- **Головний посібник**: `README.md`
- **Повний покажчик**: `INDEX.md`
- **Каталог**: `CATALOG.md`
- **Оригінальний посібник**: `claude_concepts_guide.md`

---

## 📞 Поширені запитання

**П: Що обрати?**
В: Почніть зі слеш-команд, додавайте функції за потребою.

**П: Чи можна комбінувати функції?**
В: Так! Вони працюють разом. Пам'ять + Команди + MCP = потужна зв'язка.

**П: Як поділитися з командою?**
В: Закомітьте каталог `.claude/` до git.

**П: А що з секретами?**
В: Використовуйте змінні оточення, ніколи не хардкодьте.

**П: Чи можна змінювати приклади?**
В: Безумовно! Це шаблони для кастомізації.

---

## ✅ Чекліст

Чекліст для початку роботи:

- [ ] Прочитати `README.md`
- [ ] Встановити 1 слеш-команду
- [ ] Спробувати команду
- [ ] Створити `CLAUDE.md` проекту
- [ ] Встановити 1 субагента
- [ ] Налаштувати 1 MCP-інтеграцію
- [ ] Встановити 1 навичку
- [ ] Спробувати повний плагін
- [ ] Кастомізувати під свої потреби
- [ ] Поділитися з командою

---

**Швидкий старт**: `cat README.md`

**Повний покажчик**: `cat INDEX.md`

**Ця картка**: Тримайте під рукою для швидкого довідника!

---

**Останнє оновлення**: 9 квітня 2026
**Версія Claude Code**: 2.1.97
