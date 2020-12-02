from django.shortcuts import get_object_or_404
from django.template.response import TemplateResponse
# Create your views here.
from products.models import Product, Category, Attribute
from django.core.paginator import Paginator


def get_category(request, category_id):
    category = get_object_or_404(Category, id=category_id)
    categories = category.get_descendants(include_self=True)
    products = Product.objects.filter(category__in=categories)
    print('*'*77)
    print(len(products))
    print('*'*77)
    paginator = Paginator(products, 1)
    page = request.GET.get('page')
    products = paginator.get_page(page)
    ctx = {
        'category': category,
        'products': products
    }
    return TemplateResponse(request, 'products/get_category.html', ctx)


def get_product(request, product_id):
    product = get_object_or_404(Product, id=product_id)
    attributes = Attribute.objects.filter(product_type=product.product_type)
    ctx = {
        'product': product,
        'attributes': attributes
    }
    return TemplateResponse(request, 'products/get_product.html', ctx)


from rest_framework import generics
from products.serializers import ProductSerializer


class ProductAPIView(generics.RetrieveAPIView):
    lookup_field = 'id'
    queryset = Product.objects.all()
    serializer_class = ProductSerializer




