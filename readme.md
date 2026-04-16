# performance_test_django (Django Ninja)

Simple JWT benchmark backend.

## Role in project

- Handles `/api/login` and `/api/userinfo` for backend tag `django_ninja`.
- Uses shared PostgreSQL 17 data from `performance_test_db`.

## Endpoints

- `POST /api/login` -> returns `{ "token": "..." }`
- `GET /api/userinfo` -> accepts `DjangoToken` or `Authorization: Bearer <token>`

## Repository map and clone URLs

- `performance_test_angular` (frontend): `git@github.com:Khroxx/performance_test_angular.git`
- `performance_test_go` (Go backend): `git@github.com:Khroxx/performance_test_go.git`
- `performance_test_django` (Django Ninja backend): `git@github.com:Khroxx/performance_test__django`
- `performance_test_java` (Spring Boot backend): `git@github.com:Khroxx/performance_test__java`
- `performance_test_db` (shared PostgreSQL 17): `git@github.com:Khroxx/performance_test__db`

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
