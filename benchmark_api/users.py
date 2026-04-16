from dataclasses import dataclass


@dataclass(frozen=True)
class User:
    email: str
    password: str
    values: int


USERS = [
    User(email="user10@test.com", password="test", values=10),
    User(email="user25@test.com", password="test", values=25),
    User(email="user50@test.com", password="test", values=50),
    User(email="user100@test.com", password="test", values=100),
    User(email="user200@test.com", password="test", values=200),
]


def find_user(email: str, password: str | None = None) -> User | None:
    for user in USERS:
        if user.email != email:
            continue
        if password is not None and user.password != password:
            continue
        return user
    return None
