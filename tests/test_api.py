import jwt
from django.conf import settings
from django.test import Client, TestCase


class ApiTests(TestCase):
    def setUp(self) -> None:
        self.client = Client()

    def test_login_success_returns_token(self) -> None:
        response = self.client.post(
            "/api/login",
            data={"email": "user10@test.com", "password": "test"},
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 200)
        payload = response.json()
        self.assertIn("token", payload)

    def test_login_failure_returns_401(self) -> None:
        response = self.client.post(
            "/api/login",
            data={"email": "user10@test.com", "password": "wrong"},
            content_type="application/json",
        )

        self.assertEqual(response.status_code, 401)

    def test_userinfo_accepts_authorization_bearer(self) -> None:
        token = jwt.encode({"email": "user10@test.com"}, settings.SECRET_KEY, algorithm="HS256")
        response = self.client.get(
            "/api/userinfo",
            HTTP_AUTHORIZATION=f"Bearer {token}",
        )

        self.assertEqual(response.status_code, 200)
        payload = response.json()
        self.assertEqual(payload["email"], "user10@test.com")
