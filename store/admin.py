from django.contrib import admin
from .models import ProductCategory, Colour, Product

# Register your models here.

admin.site.register(ProductCategory)
admin.site.register(Colour)
admin.site.register(Product)
