from django.urls import path, include

urlpatterns = [
    path('authuser/', include('modules.core.apps.authuser.urls')),
]
