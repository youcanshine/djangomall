from django.db import models
from django.conf import settings

from products.models import ProductVariant
from django.core.validators import MinValueValidator


class Cart(models.Model):
    user = models.ForeignKey(
        settings.AUTH_USER_MODEL, blank=True, null=True, related_name='carts', on_delete=models.CASCADE)

    def __str__(self):
        return self.user.get_username()


class CartLine(models.Model):
    cart = models.ForeignKey(Cart, related_name='lines', on_delete=models.CASCADE)
    product_variant = models.ForeignKey(ProductVariant, related_name='+', on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField(default=0, validators=[MinValueValidator(1)])
    unit_price = models.DecimalField(max_digits=16, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True, editable=True)

    def __str__(self):
        return '{0} {1}({2})'.format(
            self.product_variant.product.name,
            self.product_variant.sku,
            self.quantity
        )

    def get_total(self):
        return self.unit_price * self.quantity

    class Meta:
        unique_together = ('cart', 'product_variant')
        ordering = ['-created_at']




