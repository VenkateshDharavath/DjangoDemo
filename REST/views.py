import json
from os import stat
from rest_framework import status
from django.shortcuts import render
from testapp.models import Product
from .serializers import ProductSerializer, TagsSerializer

from rest_framework.decorators import api_view, parser_classes
from rest_framework.parsers import JSONParser
from rest_framework.response import Response

# from rest_framework.renderers import JSONRenderer

# Create your views here.
@api_view(['GET', 'POST'])
@parser_classes([JSONParser])
def get_all_products(request):
    if request.method == 'GET':
        products = Product.objects.all()
        serialized = ProductSerializer(products, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)
    elif request.method == 'POST':
        body = request.body.decode('utf-8')
        body = json.loads(body)
        print(type(body), body)
        prod = Product()
        prod.product_name = body.get("product_name")
        prod.discription = body.get("discription")

        prod.save()

        serialized = ProductSerializer(prod)
        return Response(serialized.data, status=status.HTTP_201_CREATED)

@api_view(['GET'])
def get_product(request, id):
    if request.method == 'GET':
        product = Product.objects.get(id=id)
        serialized = ProductSerializer(product)
        return Response(serialized.data, status=status.HTTP_200_OK)

@api_view(['GET'])
def get_tags(request, id):
    if request.method == 'GET':
        product = Product.objects.get(id=id)
        tags = product.tags_set.all()
        serialized = TagsSerializer(tags, many=True)
        return Response(serialized.data, status=status.HTTP_200_OK)