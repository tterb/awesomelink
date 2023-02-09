"""
Django settings for the development version of test_drive
"""

from .base import *

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# Minify static assets
# COMPRESS_ENABLED = True
# COMPRESS_CSS_FILTERS = ["compressor.filters.cssmin.CSSMinFilter"]
# COMPRESS_JS_FILTERS = ["compressor.filters.jsmin.JSMinFilter"]

# if 'pytest' in sys.argv or 'test_coverage' in sys.argv: #Covers regular testing and django-coverage
#     DATABASES['default']['ENGINE'] = 'django.db.backends.sqlite3'

ALLOWED_HOSTS += [
    'localhost',
    '127.0.0.1',
]

INSTALLED_APPS += [
    'debug_toolbar',
]

MIDDLEWARE += [
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

INTERNAL_IPS = [
    '127.0.0.1',
]

DATABASES = {
    'default': {
        # 'ENGINE': 'django.db.backends.sqlite3',
        # 'NAME': BASE_DIR / 'db.sqlite3',
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'brettstevenson',
        'USER': 'admin',
        'PASSWORD': 'password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

CORS_ORIGIN_WHITELIST = [
    'http://localhost:3000',
    'http://localhost:8080',
]
CORS_ORIGIN_ALLOW_ALL = True

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = []

ACCOUNT_EMAIL_VERIFICATION = 'none'
