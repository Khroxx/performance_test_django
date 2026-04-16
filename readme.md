# performance_test_django (Django Ninja)

Simple JWT benchmark backend.

## Endpoints

- `POST /api/login` -> returns `{ "token": "..." }`
- `GET /api/userinfo` -> requires `DjangoToken` header or `Authorization: Bearer <token>`

## Local run with Docker

```bash
docker compose up --build
```

Service runs on `http://localhost:8080`.
