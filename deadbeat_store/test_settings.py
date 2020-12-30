from . settings import *

DATABASES = {
    "default": {
        "ENGINE": "django.db.backends.sqlite3",
        "NAME": ":memory:",
    }
}

#SET UP EMAIL BACKEND

EMAIL_BACKEND = 'django.core.mail.backends.locmem.EmailBackend'