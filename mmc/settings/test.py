from .base import *  # noqa

DEBUG = True
TEMPLATE_DEBUG = True

ITEMS_PER_PAGE = 10

SECRET_KEY = "test"

CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.db.DatabaseCache",
        "LOCATION": "cache",
    }
}

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
    },
}

PASSWORD_HASHERS = [
    "django.contrib.auth.hashers.MD5PasswordHasher",
]
