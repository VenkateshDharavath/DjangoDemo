from django.shortcuts import render
from .models import Product

def products(request):
    products = Product.objects.all()
    # products =  [1,2,3,4,5]
    return render(request, 'products.html', {"products": products})

def product(request, id):
    return render(request, 'product.html', {"id": id})
