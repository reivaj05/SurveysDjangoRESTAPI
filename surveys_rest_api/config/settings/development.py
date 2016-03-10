from .base import *
from config.keys import KEYS
# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

# TEMPLATES[0]['OPTIONS']['DEBUG'] = True

SECRET_KEY = KEYS.get('SECRET_KEY', None)
# Database
# https://docs.djangoproject.com/en/1.9/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'vagrant',
        'USER': 'vagrant',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
        'CONN_MAX_AGE': 600,
    }
}

INSTALLED_APPS += (
    'django_extensions',
    'debug_toolbar',
)

MIDDLEWARE_CLASSES += (
    'debug_toolbar.middleware.DebugToolbarMiddleware',
)

# This IP addresses ensure debug toolbar shows development environment
INTERNAL_IPS = ('127.0.0.1', '10.0.2.2')

CORS_ORIGIN_WHITELIST = (
        'localhost:8080',
)
