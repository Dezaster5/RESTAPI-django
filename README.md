"# RESTAPI-django" 
# Django CRUD API Project

## Описание проекта

Этот проект представляет собой REST API для управления объектами **Item**, предоставляя базовые CRUD-операции (создание, чтение, обновление и удаление). API построен на Django с использованием Django REST Framework и включает авто-сгенерированную документацию с помощью **Swagger** и **ReDoc**.

## Возможности

- **Создание** нового объекта (`POST /api/items/`)
- **Чтение** списка всех объектов (`GET /api/items/`) или одного объекта по ID (`GET /api/items/{id}/`)
- **Обновление** существующего объекта (`PUT /api/items/{id}/` или `PATCH /api/items/{id}/`)
- **Удаление** объекта (`DELETE /api/items/{id}/`)
- **Документация API** через **Swagger** и **ReDoc**

## Технологии

- **Django** — основной фреймворк
- **Django REST Framework (DRF)** — для создания REST API (pip install django djangorestframework)
- **Sqlite3** — база данных
- **Swagger** — для документации API
- **ReDoc** — альтернатива для документации API

## Установка

### Шаг 1: Клонирование репозитория

```bash
git clone https://github.com/your_username/your_project_name.git
cd your_project_name

# Настройка виртуального окружения

### Шаг 2

# На Windows
python -m venv venv
venv\Scripts\activate

# На macOS/Linux
python3 -m venv venv
source venv/bin/activate

### Шаг 3: Установка зависимостей
# Установите зависимости, указанные в файле requirements.txt:

```bash

pip install -r requirements.txt

### Шаг 4

# Запуск сервера

python manage.py runserver

Теперь вы можете получить доступ к приложению по адресу http://127.0.0.1:8000.

# Документация API
Документация доступна по следующим URL-адресам:

- Swagger UI: http://127.0.0.1:8000/swagger/
- ReDoc UI: http://127.0.0.1:8000/redoc/
- OpenAPI (YAML): http://127.0.0.1:8000/swagger.yaml/

# Примеры запросов
### Создание нового объекта

```bash

POST /api/items/
Content-Type: application/json

{
    "name": "Новый предмет",
    "description": "Описание предмета",
    "price": 100.50
    "created_at": "Новая Дата и время"
}

# Чтение всех объектов

```bash

GET /api/items/

# Чтение объекта по ID

```bash

GET /api/items/1/

# Обновление объекта

```bash

PUT /api/items/1/
Content-Type: application/json

{
    "name": "Обновленное название",
    "description": "Обновленное описание",
    "price": 150.00
    "created_at": "Обновленное Дата и время"
}

# Удаление объекта

```bash

DELETE /api/items/1/

# Как внести изменения

- Сделайте форк проекта.
- Создайте новую ветку (git checkout -b new-feature).
- Внесите изменения и сделайте коммит (git commit -am 'Добавил новую функцию').
- Отправьте изменения в вашу ветку (git push origin new-feature).
- Создайте Pull Request.