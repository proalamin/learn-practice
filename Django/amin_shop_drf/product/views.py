from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from product.models import Product, Category
from product.serializers import ProductSerializers, CategorySerializer

@api_view()
def view_products(request):
    products = Product.objects.select_related('category').all()
    serializer= ProductSerializers(products, many=True)
    
    return Response(serializer.data)


@api_view()
def view_specific_products(request, id):
    
        product = get_object_or_404(Product, pk=id)
        serializer = ProductSerializers(product)
        
        return Response(serializer.data)


@api_view()
def view_categories(request):
    # return Response({"msg": "view_categories"})
    products = Category.objects.all()
    serializer= CategorySerializer(products, many=True)
    
    return Response(serializer.data)


