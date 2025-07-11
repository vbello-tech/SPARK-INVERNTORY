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


class Colour(models.Model):
    colour = models.CharField(max_length=300)

    def __str__(self):
        return self.colour


Type_Choice = [
    ('Used', 'Used'),
    ('UK', 'UK'),
    ('China', 'China'),
]


class Product(models.Model):
    name = models.CharField(max_length=300)
    colour = models.ManyToManyField('Colour', related_name="color")
    category = models.ForeignKey('ProductCategory', related_name="product_category", on_delete=models.CASCADE, blank=True, null=True)
    serial_no = models.CharField(max_length=20)
    ram = models.CharField(max_length=5, blank=True, null=True)
    rom = models.CharField(max_length=10, blank=True, null=True)
    type = models.CharField(max_length=8, choices=Type_Choice, blank=True, null=True)
    quantity = models.IntegerField()
    checked_in = models.BooleanField(default=False)
    sold_out = models.BooleanField(default=False)

    def __str__(self):
        return self.name
