from django.contrib import admin
from products.models import (
    Category, ProductType, Attribute, AttributeValue,
    Product, ProductVariant
)
# Register your models here.

admin.site.register([
    ProductType, Attribute, AttributeValue
])

from mptt.admin import MPTTModelAdmin

admin.site.register(Category, MPTTModelAdmin)


class ProductVariantInline(admin.TabularInline):
    model = ProductVariant
    fields = ['sku', 'name', 'price']


class ProductAdmin(admin.ModelAdmin):
    inlines = [
        ProductVariantInline,
    ]


admin.site.register(Product, ProductAdmin)
