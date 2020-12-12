from rest_framework import serializers
from carts.models import CartLine

from products.serializers import ProductVariantSerializer


class CartLineSerializer(serializers.ModelSerializer):
    product_variant_details = ProductVariantSerializer(source='product_variant', read_only=True)
    total = serializers.DecimalField(max_digits=6, decimal_places=2, source='get_total', read_only=True)

    class Meta:
        model = CartLine
        fields = '__all__'


