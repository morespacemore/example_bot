# example_bot

Шаблон бота на Aiogram c базой данных MongoDB.

## Установка

1. Клонируйте репозиторий;
2. Перейдите (`cd`) в клонированный каталог и создайте виртуальное окружение Python (Virtual environment, venv);
3. Активируйте venv и установите все зависимости из `requirements.txt`;
4. Переименуйте файл `env_dist` в `.env` (с точкой в начале), откройте и заполните переменные;
5. Внутри активированного venv введите `python -m app`;

## Используемые технологии

- Python 3.10;
- Aiogram 3.x (работа с Telegram Bot API);
- MongoDB 6.x (база данных);
- Beanie 1.20.x (работа с базой данных);
- Fluentogram 1.1.x (локализация бота);
