from django.urls import path
from .views import *

app_name = "store"

urlpatterns = [
    path('', dashboard, name="dashboard"),
    path('search-func/', search_func, name='search_func'),
]
