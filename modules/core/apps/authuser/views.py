from rest_framework.viewsets import ModelViewSet

from modules.core.apps.authuser import models, serializers


class CustomUserModelViewSet(ModelViewSet):
    """
    API для работы со списком пользователей сервиса
    """
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.CustomUserSerializer
