"""
WSGI config for TaskFlow project.
Uses production settings by default (overridden in manage.py for dev).
"""

import os

from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.production')

application = get_wsgi_application()
