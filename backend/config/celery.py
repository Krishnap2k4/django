"""
Celery configuration for TaskFlow project.
"""

import os

from celery import Celery

# Set default Django settings module
os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.development')

app = Celery('taskflow')

# Read config from Django settings, using CELERY_ prefix
app.config_from_object('django.conf:settings', namespace='CELERY')

# Auto-discover tasks in all installed apps
app.autodiscover_tasks()

# Task routing — separate queues for different task types
app.conf.task_routes = {
    'apps.notifications.tasks.*': {'queue': 'notifications'},
}

# Task retry defaults
app.conf.task_default_retry_delay = 60  # 1 minute
app.conf.task_max_retries = 3


@app.task(bind=True, ignore_result=True)
def debug_task(self):
    """Debug task to verify Celery is working."""
    print(f'Request: {self.request!r}')
