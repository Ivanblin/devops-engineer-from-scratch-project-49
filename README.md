### Hexlet tests and linter status:
[![Actions Status](https://github.com/Ivanblin/devops-engineer-from-scratch-project-49/actions/workflows/hexlet-check.yml/badge.svg)](https://github.com/Ivanblin/devops-engineer-from-scratch-project-49/actions)
[![Maintainability Rating](https://sonarcloud.io/api/project_badges/measure?project=Ivanblin_devops-engineer-from-scratch-project-49&metric=alert_status)](https://sonarcloud.io/summary/new_code?id=Ivanblin_devops-engineer-from-scratch-project-49)

## Описание

«Игры разума» — набор из пяти консольных математических игр. В каждой нужно дать три правильных ответа подряд; при ошибке игра предлагает попробовать снова.

### Игры

- **brain-even** — чётное ли число? (ответы `yes` / `no`)
- **brain-calc** — значение арифметического выражения (`+`, `-`, `*`)
- **brain-gcd** — наибольший общий делитель двух чисел
- **brain-progression** — пропущенный член арифметической прогрессии
- **brain-prime** — простое ли число? (`yes` / `no`)

Команда **brain-games** только приветствует и спрашивает имя.

## Требования

- Python 3.10+
- [uv](https://docs.astral.sh/uv/) для зависимостей и запуска

## Установка

```bash
git clone https://github.com/Ivanblin/devops-engineer-from-scratch-project-49.git
cd devops-engineer-from-scratch-project-49
make install
```

## Запуск

Примеры:

```bash
uv run brain-games
uv run brain-even
uv run brain-progression
```

Или через Makefile: `make brain-even`, `make brain-calc` и т.д.

## Разработка

```bash
make lint      # проверка стиля (ruff)
make build     # сборка дистрибутива
make publish   # пробная публикация (dry-run)
```

## Демонстрация

После записи прохождения игры в [asciinema](https://asciinema.org/) вставьте сюда ссылку на ролик и при необходимости бейдж, как указано в задании на Hexlet.
