from django.shortcuts import render

# Create your views here.
from rest_framework import viewsets, status
from carts.models import Cart, CartLine
from carts.serializers import CartLineSerializer
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from products.models import ProductVariant


class CartLineViewSet(viewsets.ModelViewSet):
    queryset = CartLine.objects.all()
    serializer_class = CartLineSerializer

    def create(self, request, *args, **kwargs):
        cart, _ = Cart.objects.get_or_create(user=request.user)
        