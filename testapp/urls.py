
from django.urls import path

from .views import products, product

urlpatterns = [
    path('', products, name="products"),
    path('product/<str:id>', product, name = "product"),
]

