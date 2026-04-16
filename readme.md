# performance_test_django (Django Ninja)

Simple JWT benchmark backend.

## Endpoints

- `POST /api/login` -> returns `{ "token": "..." }`
- `GET /api/userinfo` -> accepts `DjangoToken` or `Authorization: Bearer <token>`

## Shared DB dependency

This backend uses the shared PostgreSQL 17 instance from `performance_test_db`.

Start DB first:

```bash
cd ../performance_test_db
cp .env.example .env
docker compose up -d
```

## Run backend with Docker

```bash
docker compose up --build
```

Service runs on `http://localhost:8080`.

## Local run without Docker

```bash
python manage.py runserver 0.0.0.0:8080
```

Default DB config expects:

- host: `localhost`
- port: `5432`
- database: `testdb`
- user: `testuser`
- password: `testpassword`
