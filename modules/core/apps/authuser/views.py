from rest_framework.viewsets import ModelViewSet

from modules.core.apps.authuser import models, serializers


class CustomUserModelViewSet(ModelViewSet):
    queryset = models.CustomUser.objects.all()
    serializer_class = serializers.CustomUserSerializer
