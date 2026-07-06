"""
Reusable model and view mixins for TaskFlow.
"""

from django.db import models


class TimestampMixin(models.Model):
    """Adds created_at and updated_at timestamps to any model."""
    created_at = models.DateTimeField(auto_now_add=True, db_index=True)
    updated_at = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True
        ordering = ['-created_at']
