from django.urls import path

from .views import get_all_products, get_product, get_tags

urlpatterns = [
    path('products/', get_all_products),
    path('products/<str:id>', get_product),
    path('products/<str:id>/tags', get_tags),
]
