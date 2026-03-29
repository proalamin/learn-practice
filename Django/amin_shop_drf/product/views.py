from django.shortcuts import get_object_or_404
from django.http import HttpResponse
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from product.models import Product, Category
from product.serializers import ProductSerializers, CategorySerializer
from django.db.models import Count

from rest_framework.views import APIView
from rest_framework.mixins import CreateModelMixin, ListModelMixin
from rest_framework.generics import ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.viewsets import ModelViewSet


@api_view(['GET', 'POST'])
def view_products(request):
    if request.method == 'GET':
        products = Product.objects.all()
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
        
        
# class based view        
class ViewProduct(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer= ProductSerializers(products, many=True, context={'request': request})
        return Response(serializer.data)
    
    def post(self, request):
        serializer = ProductSerializers(data=request.data)  # Deserializer
        if serializer.is_valid():
            print(serializer.validated_data)
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# Generic views 
class ProductList(ListCreateAPIView):
    # serializer_class = ProductSerializers

    # def get_queryset(self):
    #     return  Product.objects.select_related('category').all()
    
    queryset= Product.objects.all()
    serializer_class= ProductSerializers
    
    # def get_serializer_context(self):
    #     return {'request': self.request}

# Model View set
class ProductViewSet(ModelViewSet):
    queryset = Product.objects.all()
    serializer_class= ProductSerializers
    
    def destroy(self, request, *args, **kwargs):
        product= self.get_object()
        if product.stock > 0:
            return Response({'msg': 'Product with stock more than 0 could not deleted'})
        self.perform_destroy(product)
        return Response(status=status.HTTP_204_NO_CONTENT)



 
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

# class based views
class ViewSpecificProduct(APIView):
    def get(self, request, id):
        product = get_object_or_404(Product, pk=id)
        serializer = ProductSerializers(product)
        return Response(serializer.data)
    
    def put(self, request, id):
        product = get_object_or_404(Product, pk=id)
        serializer = ProductSerializers(product, data= request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, id):
        product = get_object_or_404(Product, pk=id)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Generic views
class ProductDetails(RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class= ProductSerializers
    lookup_field = 'id'
    
    def delete(self, request, id):
        product = get_object_or_404(Product, pk=id)
        if product.stock > 0:
            return Response({'msg': 'Product with stock more than 10 could not deleted'})
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
        
class ViewCategories(APIView):
    def get(self, request):
        category = Category.objects.annotate(product_Count=Count('products')).all()
        serializer= CategorySerializer(category, many=True)
        return Response(serializer.data)
       
    def post(self, request):
        serializer=CategorySerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)

# Generic views
class CategoryList(ListCreateAPIView):
    queryset= Category.objects.annotate(product_Count=Count('products'))
    serializer_class= CategorySerializer

# Model View set
class CategoryViewSets(ModelViewSet):
    queryset = Category.objects.annotate(product_Count=Count('products')).all()
    serializer_class = CategorySerializer


@api_view()
def view_specific_categories(request, pk):
    category = get_object_or_404(Category, pk=pk)
    serializer= CategorySerializer(category)
    return Response(serializer.data)

class ViewSpecific_categories(APIView):
    def get(self, request, id):
        category = get_object_or_404(
            Category.objects.annotate(product_Count=Count('products')).all(), pk=id
        )
        serializer= CategorySerializer(category)
        return Response(serializer.data)
    
    def put(self, request, id):
        category = get_object_or_404(
            Category.objects.annotate(product_Count=Count('products')).all(), pk=id
        )
        serializer= CategorySerializer(category, data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    
    def delete(self, request, id):
        category = get_object_or_404(
            Category.objects.annotate(product_Count=Count('products')).all(), pk=id
        )
        category.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)

# Generic views
class CategoryDetails(RetrieveUpdateDestroyAPIView):
    queryset = Category.objects.annotate(product_Count=Count('products')).all()
    serializer_class= CategorySerializer
    lookup_field = 'id'