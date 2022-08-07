from drf_yasg import openapi
from drf_yasg.views import get_schema_view as swagger_get_schema_view
from rest_framework import permissions

schema_view = swagger_get_schema_view(
    openapi.Info(
        title="Pair API",
        default_version='1.0.0',
        description="Documentation to app 'Pair'",
    ),
    public=True,
    permission_classes=(permissions.AllowAny,)
)
