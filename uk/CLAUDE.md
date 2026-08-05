<!-- i18n-source: CLAUDE.md -->
<!-- i18n-source-sha: 63a1416 -->
<!-- i18n-date: 2026-04-10 -->

# CLAUDE.md

Цей файл надає настанови для Claude Code (claude.ai/code) при роботі з кодом у цьому репозиторії.

## Огляд проєкту

Claude How To — це навчальний репозиторій з функцій Claude Code. Це **документація-як-код** — основний продукт — markdown-файли, організовані в пронумеровані навчальні модулі, а не виконуваний додаток.

**Архітектура**: Кожен модуль (01-10) охоплює конкретну функцію Claude Code з готовими шаблонами для копіювання, Mermaid-діаграмами та прикладами. Система збірки валідує якість документації та генерує EPUB-книгу.

## Типові команди

### Перевірки якості pre-commit

Уся документація повинна пройти чотири перевірки якості перед комітами (запускаються автоматично через pre-commit хуки):

```bash
# Install pre-commit hooks (runs on every commit)
pre-commit install

# Run all checks manually
pre-commit run --all-files
```

П'ять перевірок:
1. **markdown-lint** — Структура та форматування Markdown через `markdownlint`
2. **cross-references** — Внутрішні посилання, якорі, синтаксис блоків коду (Python-скрипт)
3. **mermaid-syntax** — Валідація коректного парсингу всіх Mermaid-діаграм (Python-скрипт)
4. **link-check** — Доступність зовнішніх URL (Python-скрипт)
5. **build-epub** — EPUB генерується без помилок (при змінах `.md`)

### Налаштування середовища розробки

```bash
# Install uv (Python package manager)
pip install uv

# Create virtual environment and install Python dependencies
uv venv
source .venv/bin/activate
uv pip install -r scripts/requirements-dev.txt

# Install Node.js tools (markdown linter and Mermaid validator)
npm install -g markdownlint-cli
npm install -g @mermaid-js/mermaid-cli

# Install pre-commit hooks
uv pip install pre-commit
pre-commit install
```

### Тестування

Python-скрипти в `scripts/` мають юніт-тести:

```bash
# Run all tests
pytest scripts/tests/ -v

# Run with coverage
pytest scripts/tests/ -v --cov=scripts --cov-report=html

# Run specific test
pytest scripts/tests/test_build_epub.py -v
```

### Якість коду

```bash
# Lint and format Python code
ruff check scripts/
ruff format scripts/

# Security scan
bandit -c scripts/pyproject.toml -r scripts/ --exclude scripts/tests/

# Type checking
mypy scripts/ --ignore-missing-imports
```

### Збірка EPUB

```bash
# Generate ebook (renders Mermaid diagrams with the local mmdc CLI — no network)
uv run scripts/build_epub.py

# With options
uv run scripts/build_epub.py --verbose --output custom-name.epub --mmdc-path ./node_modules/.bin/mmdc
```

## Структура каталогів

```
├── 01-slash-commands/      # Ярлики, ініційовані користувачем
├── 02-memory/              # Приклади постійного контексту
├── 03-skills/              # Повторно використовувані можливості
├── 04-subagents/           # Спеціалізовані AI-асистенти
├── 05-mcp/                 # Приклади Model Context Protocol
├── 06-hooks/               # Автоматизація на основі подій
├── 07-plugins/             # Пакетні функції
├── 08-checkpoints/         # Знімки сесій
├── 09-advanced-features/   # Планування, мислення, фони
├── 10-cli/                 # Довідник CLI
├── scripts/
│   ├── build_epub.py           # Генератор EPUB (рендерить Mermaid через локальний mmdc)
│   ├── check_cross_references.py   # Валідація внутрішніх посилань
│   ├── check_links.py          # Перевірка зовнішніх URL
│   ├── check_mermaid.py        # Валідація синтаксису Mermaid
│   └── tests/                  # Юніт-тести для скриптів
├── .pre-commit-config.yaml    # Визначення перевірок якості
└── README.md               # Основний довідник (також індекс модулів)
```

## Настанови щодо контенту

### Структура модуля
Кожна пронумерована папка дотримується патерну:
- **README.md** — Огляд функції з прикладами
- **Файли прикладів** — Готові шаблони для копіювання (`.md` для команд, `.json` для конфігурацій, `.sh` для хуків)
- Файли організовані за складністю функцій та залежностями

### Mermaid-діаграми
- Усі діаграми повинні успішно парситися (перевіряється pre-commit хуком)
- Збірка EPUB рендерить діаграми через локальний `mmdc` CLI (інтернет не потрібен, але потрібен `mmdc`)
- Використовуйте Mermaid для блок-схем, діаграм послідовностей та архітектурних візуалізацій

### Перехресні посилання
- Використовуйте відносні шляхи для внутрішніх посилань (напр., `(01-slash-commands/README.md)`)
- Блоки коду повинні вказувати мову (напр., ` ```bash `, ` ```python `)
- Якірні посилання використовують формат `#heading-name`

### Валідація посилань
- Зовнішні URL повинні бути доступні (перевіряється pre-commit хуком)
- Уникайте посилань на тимчасовий контент
- Використовуйте пермалінки де можливо

## Ключові архітектурні рішення

1. **Пронумеровані папки вказують порядок навчання** — Префікс 01-10 відображає рекомендовану послідовність вивчення функцій Claude Code. Ця нумерація навмисна; не реорганізовуйте за алфавітом.

2. **Скрипти — утиліти, а не продукт** — Python-скрипти в `scripts/` підтримують якість документації та генерацію EPUB. Фактичний контент — у пронумерованих папках модулів.

3. **Pre-commit — привратник** — Усі перевірки якості повинні пройти перед прийняттям PR. CI-конвеєр запускає ці ж перевірки як другий прохід.

4. **Рендеринг Mermaid потребує локального `mmdc`** — Збірка EPUB викликає локальний `mmdc` CLI для рендерингу діаграм (мережа не потрібна). Помилки збірки тут зазвичай пов'язані з відсутнім `mmdc` або невалідним синтаксисом Mermaid. Сама збірка EPUB не виконується у pre-commit — лише в CI.

5. **Це туторіал, а не бібліотека** — При додаванні контенту зосереджуйтесь на чітких поясненнях, готових прикладах та візуальних діаграмах. Цінність — у навчанні концепцій, а не у наданні повторно використовуваного коду.

## Конвенції комітів

Дотримуйтесь формату conventional commits:
- `feat(slash-commands): Add API documentation generator`
- `docs(memory): Improve personal preferences example`
- `fix(README): Correct table of contents link`
- `refactor(hooks): Simplify hook configuration examples`

Скоуп повинен відповідати назві папки де можливо.
