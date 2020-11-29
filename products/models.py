from django.db import models

# Create your models here.
from mptt.managers import TreeManager
from mptt.models import MPTTModel


class Category(MPTTModel, models.Model):
    name = models.CharField(max_length=128)
    parent = models.ForeignKey(
        'self', blank=True, null=True, related_name='children',
        on_delete=models.CASCADE
    )
    tree = TreeManager()

    def __str__(self):
        return self.name


class ProductType(models.Model):
    name = models.CharField(max_length=128)

    def __str__(self):
        return self.name


class Attribute(models.Model):
    name = models.CharField(max_length=128)
    product_type = models.ForeignKey(
        ProductType,
        related_name='product_attributes',
        blank=True,
        null=True,
        on_delete=models.CASCADE
    )

    def __str__(self):
        return self.name


class AttributeValue(models.Model):
    attribute = models.ForeignKey(
        Attribute,
        related_name='values',
        on_delete=models.CASCADE
    )
    value = models.CharField(max_length=32)

    def __str__(self):
        return self.value


class Product(models.Model):
    category = models.ForeignKey(
        Category, related_name='products', on_delete=models.CASCADE)
    product_type = models.ForeignKey(
        ProductType, related_name='products', on_delete=models.CASCADE)
    attribute_values = models.ManyToManyField('AttributeValue')
    name = models.CharField(max_length=128)
    
