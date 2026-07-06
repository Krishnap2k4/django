"""
Development settings for TaskFlow.
Extends base settings with debug-friendly overrides.
"""

from .base import *  # noqa: F401,F403

# =============================================================
# DEBUG
# =============================================================

DEBUG = True
SECRET_KEY = 'django-insecure-dev-only-key-do-not-use-in-production-abc123xyz'

ALLOWED_HOSTS = ['*']

# =============================================================
# REST FRAMEWORK — Add browsable API in dev
# =============================================================

REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'] = (  # noqa: F405
    'rest_framework.renderers.JSONRenderer',
    'rest_framework.renderers.BrowsableAPIRenderer',
)

# Relaxed throttling for development
REST_FRAMEWORK['DEFAULT_THROTTLE_RATES'] = {  # noqa: F405
    'anon': '1000/minute',
    'user': '5000/minute',
}

# =============================================================
# CORS — Allow all in development
# =============================================================

CORS_ALLOW_ALL_ORIGINS = True

# =============================================================
# EMAIL — Print to console
# =============================================================

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# =============================================================
# CACHE — Can switch to local memory for simpler dev setup
# =============================================================

# Uncomment below to use local memory cache instead of Redis
# CACHES = {
#     'default': {
#         'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
#     }
# }

# =============================================================
# LOGGING — More verbose in dev
# =============================================================

LOGGING['loggers']['django.db.backends'] = {  # noqa: F405
    'handlers': ['console'],
    'level': 'DEBUG' if os.environ.get('SQL_DEBUG') else 'WARNING',  # noqa: F405
    'propagate': False,
}
