import os
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = os.getenv("DJANGO_SECRET_KEY", "django-ninja-local-secret")
DEBUG = os.getenv("DEBUG", "1") == "1"
ALLOWED_HOSTS = ["*"]

INSTALLED_APPS = [
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "corsheaders",
]

MIDDLEWARE = [
    "corsheaders.middleware.CorsMiddleware",
    "django.middleware.common.CommonMiddleware",
]

ROOT_URLCONF = "benchmark_api.urls"
TEMPLATES = []
WSGI_APPLICATION = "benchmark_api.wsgi.application"
ASGI_APPLICATION = "benchmark_api.asgi.application"

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.postgresql",
        "NAME": os.getenv("DB_NAME", "testdb"),
        "USER": os.getenv("DB_USER", "testuser"),
        "PASSWORD": os.getenv("DB_PASSWORD", "testpassword"),
        "HOST": os.getenv("DB_HOST", "db"),
        "PORT": os.getenv("DB_PORT", "5432"),
    }
}

LANGUAGE_CODE = "en-us"
TIME_ZONE = "UTC"
USE_I18N = True
USE_TZ = True

CORS_ALLOWED_ORIGINS = [
    "http://localhost:4200",
]

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
