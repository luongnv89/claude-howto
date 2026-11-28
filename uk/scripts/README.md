<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../../resources/logos/claude-howto-logo.svg">
</picture>

# Скрипт збірки EPUB

Збірка EPUB-книги з markdown-файлів Claude How-To.

## Функції

- Організує розділи за структурою каталогів (01-slash-commands, 02-memory тощо)
- Рендерить Mermaid-діаграми як SVG-зображення через [Pele](https://github.com/obsidianmd/pele) — закріплений бандл, який запускає Node.js; CSS-змінні замінюються звичайними кольорами на білому тлі, тож діаграми видно в будь-якій EPUB-читалці
- Кешує однакові діаграми — кожна унікальна діаграма рендериться лише раз
- Генерує обкладинку з логотипу проєкту
- Конвертує внутрішні markdown-посилання у посилання на розділи EPUB
- Суворий режим помилок — падає, якщо діаграма не може бути відрендерена

## Вимоги

- Python 3.10+
- [uv](https://github.com/astral-sh/uv)
- Node.js >= 20 у `PATH` для рендерингу Mermaid-діаграм. Закріплений бандл Pele завантажується під час першого запуску (мережа потрібна лише раз), перевіряється за sha256 і кешується в `scripts/.vendor-cache/pele/`

## Швидкий старт

```bash
# Simplest way - uv handles everything
uv run scripts/build_epub.py
```

## Налаштування розробки

```bash
# Create virtual environment
uv venv

# Activate and install dependencies
source .venv/bin/activate
uv pip install -r requirements-dev.txt

# Run tests
pytest scripts/tests/ -v

# Run the script
python scripts/build_epub.py
```

## Параметри командного рядка

```
usage: build_epub.py [-h] [--root ROOT] [--output OUTPUT] [--verbose]
                     [--lang {en,vi,zh,ja,ko,fa}]

options:
  -h, --help            show this help message and exit
  --root, -r ROOT       Root directory (default: repo root)
  --output, -o OUTPUT   Output path (default: claude-howto-guide.epub)
  --verbose, -v         Enable verbose logging
  --lang {en,vi,zh,ja,ko,fa}  Language to build (default: en)
```

## Приклади

```bash
# Build with verbose output
uv run scripts/build_epub.py --verbose

# Custom output location
uv run scripts/build_epub.py --output ~/Desktop/claude-guide.epub

# Build a translated edition
uv run scripts/build_epub.py --lang vi
```

## Вивід

Створює `claude-howto-guide.epub` у кореневому каталозі репозиторію.

EPUB включає:
- Обкладинку з логотипом проєкту
- Зміст з вкладеними секціями
- Весь markdown-контент, конвертований у EPUB-сумісний HTML
- Mermaid-діаграми, відрендерені як SVG-зображення

## Запуск тестів

```bash
# With virtual environment
source .venv/bin/activate
pytest scripts/tests/ -v

# Or with uv directly
uv run --with pytest --with pytest-asyncio \
    --with ebooklib --with markdown --with beautifulsoup4 \
    --with pillow \
    pytest scripts/tests/ -v
```

## Залежності

Керуються через PEP 723 inline script metadata:

| Пакет | Призначення |
|-------|-------------|
| `ebooklib` | Генерація EPUB |
| `markdown` | Конвертація Markdown → HTML |
| `beautifulsoup4` | Парсинг HTML |
| `pillow` | Генерація обкладинки |

## Усунення проблем

**Збірка падає з `Pele is unavailable`**: Встановіть Node.js >= 20 і переконайтеся, що `node` є у `PATH` (`node --version`).

**Помилка завантаження або контрольної суми бандла Pele**: Перша збірка завантажує закріплений бандл Pele з cdn.jsdelivr.net і перевіряє sha256 кожного файлу. Офлайн або за проксі виконайте одну збірку з доступом до мережі; наступні збірки використовують кеш у `scripts/.vendor-cache/pele/<version>/`. Невідповідність контрольної суми означає, що завантаження змінене або обірване: видаліть цю папку й зберіть знову.

**Відсутній логотип**: Скрипт генерує текстову обкладинку, якщо `claude-howto-logo.png` не знайдено.
