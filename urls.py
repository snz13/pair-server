from django.contrib import admin
from django.urls import path, include
from settings import yasg_settings

urlpatterns = [
    path('swagger/', yasg_settings.schema_view.with_ui('swagger', cache_timeout=0), name="swagger"),
    path('admin/', admin.site.urls),
    path('core/api/', include('modules.core.urls')),
]
