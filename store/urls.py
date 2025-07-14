from django.urls import path
from .views import *

app_name = "store"

urlpatterns = [
    path('', dashboard, name="dashboard"),
    path('search-func/', search_func, name='search_func'),
    path('add-category/', add_category, name="add_category"),
    path('add-colour/', add_colour, name="add_colour"),
    path('add-product/', AddProduct.as_view(), name="add_product"),
]
