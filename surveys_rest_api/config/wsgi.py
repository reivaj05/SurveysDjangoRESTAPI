"""
WSGI config for surveys_rest_api project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/1.9/howto/deployment/wsgi/
"""

import os

from django.core.wsgi import get_wsgi_application
if os.path.exists('config/keys/production.py'):
    DJANGO_SETTINGS_MODULE = 'config.settings.production'
else:
    DJANGO_SETTINGS_MODULE = 'config.settings.development'

os.environ.setdefault('DJANGO_SETTINGS_MODULE', DJANGO_SETTINGS_MODULE)

application = get_wsgi_application()
