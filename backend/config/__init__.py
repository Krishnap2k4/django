"""
TaskFlow config package.
- Installs PyMySQL as the MySQL adapter
- Ensures Celery app is loaded when Django starts
"""

import pymysql

pymysql.install_as_MySQLdb()

from .celery import app as celery_app

__all__ = ('celery_app',)
