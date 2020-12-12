from django.urls import path, include
from rest_framework import routers
from products.views import ProductAPIView
from carts.views import CartLineViewSet


router = routers.SimpleRouter()
router.register(r'cartlines', CartLineViewSet, 'cartlines')
urlpatterns = [
    path('', include(router.urls)),
    path('products/<id>/', ProductAPIView.as_view())
]
