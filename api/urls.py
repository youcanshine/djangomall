from django.urls import path
from products.views import ProductAPIView

urlpatterns = [
    path('products/<id>/', ProductAPIView.as_view())
]
