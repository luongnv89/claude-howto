<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../../../resources/logos/claude-howto-logo.svg">
</picture>

# Плагін Documentation

Комплексна генерація та підтримка документації для вашого проєкту.

## Функції

✅ Генерація API-документації
✅ Створення та оновлення README
✅ Синхронізація документації
✅ Покращення коментарів коду
✅ Генерація прикладів

## Встановлення

```bash
claude --plugin-dir ./07-plugins/documentation
```

Перевірте плагін перед завантаженням:

```bash
claude plugin validate ./07-plugins/documentation
```

## Що включено

### Слеш-команди

Команди плагіна мають простір імен за `name` плагіна з `plugin.json`:

- `/documentation:generate-api-docs` — Генерація API-документації
- `/documentation:generate-readme` — Створення або оновлення README
- `/documentation:sync-docs` — Синхронізація документації зі змінами коду
- `/documentation:validate-docs` — Валідація документації

### Субагенти
- `api-documenter` — Спеціаліст з API-документації
- `code-commentator` — Покращення коментарів коду
- `example-generator` — Створення прикладів коду

### Шаблони
- `api-endpoint.md` — Шаблон документації ендпоінту API
- `function-docs.md` — Шаблон документації функції
- `adr-template.md` — Шаблон Architecture Decision Record

### MCP-сервери

`.mcp.json` оголошує один сервер, `github`: офіційний MCP-сервер GitHub (`ghcr.io/github/github-mcp-server`), що запускається через Docker у режимі лише для читання. Образ закріплено на [релізі v2.1.0](https://github.com/github/github-mcp-server/releases/tag/v2.1.0); щоб оновити, змініть тег у `.mcp.json`. У `/mcp` він відображається як `plugin:documentation:github`.

## Використання

### Генерація API-документації
```text
/documentation:generate-api-docs
```

### Створення README
```text
/documentation:generate-readme
```

### Синхронізація документації
```text
/documentation:sync-docs
```

### Валідація документації
```text
/documentation:validate-docs
```

## Вимоги

- Claude Code 2.1+
- Docker і персональний токен доступу GitHub (опціонально, для MCP-сервера GitHub)

## Приклад робочого процесу

```text
User: /documentation:generate-api-docs

Claude:
1. Сканує всі API-ендпоінти в /src/api/
2. Делегує субагенту api-documenter
3. Витягує сигнатури функцій та JSDoc
4. Організує за модулями/ендпоінтами
5. Використовує шаблон api-endpoint.md
6. Генерує комплексну markdown-документацію
7. Включає приклади curl, JavaScript та Python

Результат:
✅ API-документація згенерована
📄 Створені файли:
   - docs/api/users.md
   - docs/api/auth.md
   - docs/api/products.md
📊 Покриття: 23/23 ендпоінти задокументовано
```

## Використання шаблонів

### Шаблон ендпоінту API
Використовуйте для документування REST API ендпоінтів з повними прикладами.

### Шаблон документації функції
Використовуйте для документування окремих функцій/методів.

### Шаблон ADR
Використовуйте для документування архітектурних рішень.

## Конфігурація

Налаштуйте GitHub-токен для синхронізації документації:
```bash
export GITHUB_TOKEN="your_github_token"
```

`.mcp.json` передає його серверу як `GITHUB_PERSONAL_ACCESS_TOKEN` — змінну, яку читає сервер. Запустіть `/mcp`, щоб перевірити, що `plugin:documentation:github` підключено. Без токена команди все одно працюють з локальними файлами.

## Найкращі практики

- Тримайте документацію близько до коду
- Оновлюйте документацію разом зі змінами коду
- Включайте практичні приклади
- Регулярно валідуйте
- Використовуйте шаблони для консистентності

---

**Останнє оновлення**: 18 жовтня 2026
**Версія Claude Code**: 2.1.302
**Джерела**:
- https://code.claude.com/docs/en/plugins/cli-reference
- https://code.claude.com/docs/en/plugins/install
