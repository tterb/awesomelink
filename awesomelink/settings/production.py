"""
Django settings for the production version of test_drive
"""
import django_heroku
import dj_database_url
from decouple import config
from .base import *


# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = [
    'awesomel.ink',
    'awesomelink.netlify.com',
    'awesomelink.onrender.com',
    'awesomelink.up.railway.app'
]

INSTALLED_APPS += []

DATABASES = {
    'default': dj_database_url.config
}

MIDDLEWARE += [
    'whitenoise.middleware.WhiteNoiseMiddleware',
]

SECRET_KEY = config('SECRET_KEY')

# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator'},
    {'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator'},
    {'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator'},
    {'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator'},
]

STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'

# Activate Django-Heroku.
django_heroku.settings(locals())
