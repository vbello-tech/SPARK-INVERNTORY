from .settings import *


ALLOWED_HOSTS = [
    '0.0.0.0',
    'localhost',
    'sparkinventory.fly.dev',
    '127.0.0.1'
]

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases
#
# DATABASES = {
#     'default':  dj_database_url.config(
#         default=config('DATABASE_URL')
#     )
# }

# db_from_env = dj_database_url.config(conn_max_age=500, ssl_require=True)
# DATABASES['default'].update(db_from_env)

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('DB_DATABASE'),
        'USER': config('DB_USERNAME'),
        'PASSWORD': config('DB_PASSWORD'),
        'HOST': config('DB_HOST'),
        'PORT': config('DB_PORT'),
    }
}

STORAGES = {
    "default": {
        "BACKEND": "django.core.files.storage.FileSystemStorage",
    },
    "staticfiles": {
        "BACKEND": "whitenoise.storage.CompressedManifestStaticFilesStorage",
    },
}

# PRODUCTION SETTINGS

# SECURE_SSL_REDIRECT = True

CSRF_TRUSTED_ORIGINS = ['https://sparkinventory.fly.dev/']

CORS_ORIGIN_ALLOW_ALL = True

SESSION_COOKIE_SECURE = True

CSRF_COOKIE_SECURE = True

SECURE_BROWSER_XSS_FILTER = True
