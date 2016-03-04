#!/usr/bin/env python
import os
import sys

if __name__ == "__main__":
    if os.path.exists('config/keys/production.py'):
        DJANGO_SETTINGS_MODULE = 'config.settings.production'
    else:
        DJANGO_SETTINGS_MODULE = 'config.settings.development'

    os.environ.setdefault('DJANGO_SETTINGS_MODULE', DJANGO_SETTINGS_MODULE)

    from django.core.management import execute_from_command_line

    execute_from_command_line(sys.argv)
