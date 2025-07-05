from django.db import models
from django.db import models
from django.conf import settings
from phonenumber_field.modelfields import PhoneNumberField


# Create your models here.

class ProductCategory(models.Model):
    category = models.CharField(max_length=300)
    quantity = models.IntegerField(default=0)

    def __str__(self):
        return self.category
#
#
# category_list = ProductCategory.objects.all().values_list('category', 'category')
# product_cat_choice = []
# for item in category_list:
#     product_cat_choice.append(item)
#
#
# class Product(models.Model):
#     name = models.CharField(max_length=300)
#     color = models.CharField(max_length=300)
#     type = models.CharField(max_length=300, choices=product_cat_choice)
#     serial_no = models.IntegerField()
#     spec = models.CharField(max_length=300)
#     quantity = models.IntegerField()
#     checked_in = models.BooleanField(default=False)
#     sold_out = models.BooleanField(default=False)
#
#     def __str__(self):
#         return self.name
