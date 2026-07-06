"""
Root URL configuration for TaskFlow.
"""

from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    # Django admin
    path('admin/', admin.site.urls),

    # API v1 endpoints (enabled as apps are built)
    # path('api/v1/auth/', include('apps.accounts.urls')),        # Phase 3
    # path('api/v1/tasks/', include('apps.tasks.urls')),          # Phase 5
    # path('api/v1/notifications/', include('apps.notifications.urls')),  # Phase 6
]

# Serve media files in development
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
