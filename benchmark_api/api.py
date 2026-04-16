from datetime import UTC, datetime, timedelta

import jwt
from django.conf import settings
from django.http import HttpRequest
from ninja import NinjaAPI, Schema

from .users import find_user

api = NinjaAPI()

JWT_SECRET = settings.SECRET_KEY
JWT_ALGO = "HS256"
TOKEN_HEADER = "DjangoToken"


class CredentialsIn(Schema):
    email: str
    password: str


class TokenOut(Schema):
    token: str


def _extract_token(request: HttpRequest) -> str | None:
    custom_header = request.headers.get(TOKEN_HEADER)
    if custom_header:
        return custom_header

    auth_header = request.headers.get("Authorization", "")
    if auth_header.startswith("Bearer "):
        return auth_header[7:]

    return None


@api.post("/login", response={200: TokenOut, 401: dict})
def login(request: HttpRequest, payload: CredentialsIn):
    user = find_user(payload.email, payload.password)
    if user is None:
        return 401, {"message": "Unauthorized"}

    exp = datetime.now(UTC) + timedelta(hours=1)
    token = jwt.encode({"email": user.email, "exp": exp.timestamp()}, JWT_SECRET, algorithm=JWT_ALGO)
    return 200, {"token": token}


@api.get("/userinfo", response={200: dict, 401: dict, 404: dict})
def userinfo(request: HttpRequest):
    token = _extract_token(request)
    if not token:
        return 401, {"message": "Missing token"}

    try:
        payload = jwt.decode(token, JWT_SECRET, algorithms=[JWT_ALGO])
    except jwt.PyJWTError:
        return 401, {"message": "Invalid token"}

    email = payload.get("email")
    if not isinstance(email, str):
        return 401, {"message": "Invalid token"}

    user = find_user(email)
    if user is None:
        return 404, {"message": "User not found"}

    return {
        "email": user.email,
        "values": user.values,
    }
