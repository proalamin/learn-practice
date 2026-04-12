from django.shortcuts import render
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin
from order.models import Cart
from order.serializers import CartSerializers

# Create your views here.
class CartViewSet(CreateModelMixin, RetrieveModelMixin, GenericViewSet):
    queryset = Cart.objects.all()
    serializer_class = CartSerializers
    
    