from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from product.models import Product, Category
from product.serializers import ProductSerializers, CategorySerializer
from django.db.models import Count

@api_view(['GET', 'POST'])
def view_products(request):
    if request.method == 'GET':
        products = Product.objects.select_related('category').all()
        serializer= ProductSerializers(products, many=True, context={'request': request})
        
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer = ProductSerializers(data=request.data)  # Deserializer
        if serializer.is_valid():
            print(serializer.validated_data)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        


@api_view(['GET', 'PUT', 'DELETE'])
def view_specific_products(request, id):
    if request.method =='GET':
        product = get_object_or_404(Product, pk=id)
        serializer = ProductSerializers(product)
        return Response(serializer.data)
    if request.method =='PUT':
        product = get_object_or_404(Product, pk=id)
        serializer = ProductSerializers(product, data= request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    if request.method =='DELETE':
        product = get_object_or_404(Product, pk=id)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['GET', 'POST'])
def view_categories(request):
    if request.method == 'GET':
        # return Response({"msg": "view_categories"})
        # category = Category.objects.all()
        category = Category.objects.annotate(product_Count=Count('products'))
        serializer= CategorySerializer(category, many=True)
        
        return Response(serializer.data)
    
    if request.method == 'POST':
        serializer=CategorySerializer(data=request.data)
        
        # if serializer.is_valid():
        #     serializer.save()
        #     return Response(serializer.data, status=status.HTTP_201_CREATED)
        # else:
        #     return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        


@api_view()
def view_specific_categories(request, pk):
    category = get_object_or_404(Category, pk=pk)
    serializer= CategorySerializer(category)
    return Response(serializer.data)