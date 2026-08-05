<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../../resources/logos/claude-howto-logo.svg">
</picture>

# Скрипт збірки EPUB

Збірка EPUB-книги з markdown-файлів Claude How-To.

## Функції

- Організує розділи за структурою каталогів (01-slash-commands, 02-memory тощо)
- Рендерить Mermaid-діаграми як PNG-зображення через локальний `mmdc` CLI (без мережі)
- Кешує однакові діаграми — кожна унікальна діаграма рендериться лише раз
- Генерує обкладинку з логотипу проєкту
- Конвертує внутрішні markdown-посилання у посилання на розділи EPUB
- Суворий режим помилок — падає, якщо діаграма не може бути відрендерена

## Вимоги

- Python 3.10+
- [uv](https://github.com/astral-sh/uv)
- Інтернет-з'єднання для рендерингу Mermaid-діаграм

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
                     [--mmdc-path MMDC_PATH] [--lang {en,vi,zh,ja}]
                     [--puppeteer-config PUPPETEER_CONFIG]

options:
  -h, --help            show this help message and exit
  --root, -r ROOT       Root directory (default: repo root)
  --output, -o OUTPUT   Output path (default: claude-howto-guide.epub)
  --verbose, -v         Enable verbose logging
  --mmdc-path PATH      Path to mmdc binary (default: mmdc from PATH)
  --lang {en,vi,zh,ja}  Language to build (default: en)
  --puppeteer-config P  Puppeteer config JSON passed to mmdc via -p
```

## Приклади

```bash
# Build with verbose output
uv run scripts/build_epub.py --verbose

# Custom output location
uv run scripts/build_epub.py --output ~/Desktop/claude-guide.epub

# Build a translated edition
uv run scripts/build_epub.py --lang vi

# Point at an mmdc that is not on PATH
uv run scripts/build_epub.py --mmdc-path ./node_modules/.bin/mmdc
```

## Вивід

Створює `claude-howto-guide.epub` у кореневому каталозі репозиторію.

EPUB включає:
- Обкладинку з логотипом проєкту
- Зміст з вкладеними секціями
- Весь markdown-контент, конвертований у EPUB-сумісний HTML
- Mermaid-діаграми, відрендерені як PNG-зображення

## Запуск тестів

```bash
# With virtual environment
source .venv/bin/activate
pytest scripts/tests/ -v

# Or with uv directly
uv run --with pytest --with pytest-asyncio \
    --with ebooklib --with markdown --with beautifulsoup4 \
    --with httpx --with pillow --with tenacity \
    pytest scripts/tests/ -v
```

## Залежності

Керуються через PEP 723 inline script metadata:

| Пакет | Призначення |
|-------|-------------|
| `ebooklib` | Генерація EPUB |
| `markdown` | Конвертація Markdown → HTML |
| `beautifulsoup4` | Парсинг HTML |
| `httpx` | Асинхронний HTTP-клієнт |
| `pillow` | Генерація обкладинки |
| `tenacity` | Логіка повторних спроб |

## Усунення проблем

**Збірка падає з `mmdc not found`**: Встановіть Mermaid CLI (`npm install -g @mermaid-js/mermaid-cli`) або вкажіть шлях через `--mmdc-path`. На arm64 вбудований Chromium не працює — збирайте EPUB у CI (джоб `build-epub` у `.github/workflows/test.yml`).

**`mmdc` падає в CI або контейнері**: Chromium потребує профілю без пісочниці. Запишіть `{"args":["--no-sandbox","--disable-setuid-sandbox"]}` у файл і передайте його через `--puppeteer-config`.

**Відсутній логотип**: Скрипт генерує текстову обкладинку, якщо `claude-howto-logo.png` не знайдено.
