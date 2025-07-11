"""
URL configuration for spark project.
"""
from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path('admin/', admin.site.urls),
    path('store/', include('store.urls', namespace="store")),
    path('', include('accounts.urls', namespace="user")),
]

