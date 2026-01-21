# linkClipper — backend (FastAPI)

Backend-сервис для регистрации/логина пользователей и создания коротких ссылок.

## Стек

- **FastAPI** + **Uvicorn**
- **PostgreSQL**
- **SQLAlchemy 2 (async)** + **Alembic**
- **JWT**

## Быстрый старт
### Установка

```bash
git clone https://github.com/r0manb/fastapi-url-shortener.git
cd fastapi-url-shortener

pip install -r requirements.txt
```

### Настройка конфигурации

Создайте файл `.env` в корне
```env
DB_URL=postgresql+asyncpg://postgres:postgres@localhost:5432/link_clipper
JWT_ACCESS_SECRET_KEY=change_me
```

также в `app/config.py` можно настроить
```python
# опционально
JWT_ACCESS_EXP={"minutes": 30}
SHORT_CODE_LEN=8
```

### Примение миграций
```bash
alembic upgrade head
```

### Запуск

```bash
uvicorn app.main:app --reload
```

Swagger UI будет доступен по `http://127.0.0.1:8000/docs`, а ReDoc — по `http://127.0.0.1:8000/redoc`.

## Переменные окружения

- **`DB_URL`**: строка подключения SQLAlchemy (ожидается `postgresql+asyncpg://...`)
- **`JWT_ACCESS_SECRET_KEY`**: секрет для подписи JWT access-токенов
- **`JWT_ACCESS_EXP`** *(опционально)*: объект с параметрами `timedelta` (по умолчанию `{"minutes": 30}`)
- **`SHORT_CODE_LEN`** *(опционально)*: длина short-code (по умолчанию `8`)

## API

### Auth

- `POST /auth/register` — регистрация
- `POST /auth/login` — логин, возвращает JWT токен

### Links
Авторизация: заголовок `Authorization: Bearer <token>`

- `POST /links/` — создать короткую ссылку
- `GET /links/` — получить список ссылок текущего пользователя

### Redirect
- `GET /to/{short_code}` — редирект на `original_url` и инкремент счётчика `clicks`


