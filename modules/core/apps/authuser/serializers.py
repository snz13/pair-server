from rest_framework.serializers import ModelSerializer

from modules.core.apps.authuser import models


class CustomUserSerializer(ModelSerializer):
    class Meta:
        model = models.CustomUser
        fields = ('username', 'email', 'first_name', 'last_name', 'date_of_birth', )
