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
