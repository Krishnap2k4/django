"""
ASGI config for TaskFlow project.
Uses production settings by default (overridden in manage.py for dev).
"""

import os

from django.core.asgi import get_asgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.production')

application = get_asgi_application()
