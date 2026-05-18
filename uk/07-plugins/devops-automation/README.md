<picture>
  <source media="(prefers-color-scheme: dark)" srcset="../../../resources/logos/claude-howto-logo-dark.svg">
  <img alt="Claude How To" src="../../../resources/logos/claude-howto-logo.svg">
</picture>

# Плагін DevOps Automation

Повна автоматизація DevOps для розгортання, моніторингу та реагування на інциденти.

## Функції

✅ Автоматизовані розгортання
✅ Процедури відкату
✅ Моніторинг стану системи
✅ Робочі процеси реагування на інциденти
✅ Інтеграція з Kubernetes

## Встановлення

```bash
/plugin install devops-automation
```

## Що включено

### Слеш-команди
- `/deploy` — Розгортання на продакшен або стейджинг
- `/rollback` — Відкат до попередньої версії
- `/status` — Перевірка стану системи
- `/incident` — Обробка інцидентів на продакшені

### Субагенти
- `deployment-specialist` — Операції розгортання
- `incident-commander` — Координація інцидентів
- `alert-analyzer` — Аналіз стану системи

### MCP-сервери
- Інтеграція з Kubernetes

### Скрипти
- `deploy.sh` — Автоматизація розгортання
- `rollback.sh` — Автоматизація відкату
- `health-check.sh` — Утиліти перевірки стану

### Хуки
- `pre-deploy.js` — Передрозгортальна валідація
- `post-deploy.js` — Післярозгортальні завдання

## Використання

### Розгортання на стейджинг
```
/deploy staging
```

### Розгортання на продакшен
```
/deploy production
```

### Відкат
```
/rollback production
```

### Перевірка стану
```
/status
```

### Обробка інциденту
```
/incident
```

## Вимоги

- Claude Code 1.0+
- Kubernetes CLI (kubectl)
- Налаштований доступ до кластера

## Конфігурація

Налаштуйте конфіг Kubernetes:
```bash
export KUBECONFIG=~/.kube/config
```

## Приклад робочого процесу

```
User: /deploy production

Claude:
1. Запускає pre-deploy хук (валідація kubectl, з'єднання з кластером)
2. Делегує субагенту deployment-specialist
3. Запускає скрипт deploy.sh
4. Моніторить прогрес розгортання через Kubernetes MCP
5. Запускає post-deploy хук (очікування подів, smoke-тести)
6. Надає підсумок розгортання

Результат:
✅ Розгортання завершено
📦 Версія: v2.1.0
🚀 Поди: 3/3 готові
⏱️  Час: 2хв 34с
```
