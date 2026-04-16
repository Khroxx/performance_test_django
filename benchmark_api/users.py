from dataclasses import dataclass

from django.db import connection


@dataclass(frozen=True)
class User:
    email: str
    password: str
    values: int


DJANGO_BACKEND_TAG = "django_ninja"


def find_user(email: str, password: str | None = None) -> User | None:
    sql = """
        SELECT email, password, values_count
        FROM benchmark_users
        WHERE email = %s AND backend_tag = %s
    """
    params: list[object] = [email, DJANGO_BACKEND_TAG]

    if password is not None:
        sql += " AND password = %s"
        params.append(password)

    with connection.cursor() as cursor:
        cursor.execute(sql, params)
        row = cursor.fetchone()

    if row is None:
        return None

    return User(email=row[0], password=row[1], values=row[2])
