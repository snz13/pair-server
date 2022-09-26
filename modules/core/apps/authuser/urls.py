from django.urls import path, include
from rest_framework import routers

from modules.core.apps.authuser import views

router = routers.DefaultRouter()

router.register('user', views.CustomUserModelViewSet)

urlpatterns = [

] + router.urls
