from django.shortcuts import render
from rest_framework.mixins import CreateModelMixin, RetrieveModelMixin, DestroyModelMixin
from rest_framework.viewsets import ModelViewSet, GenericViewSet
from order.models import Cart, CartItem
from order.serializers import CartSerializers, CartItemSerializer

# Create your views here.
class CartViewSet(CreateModelMixin, RetrieveModelMixin, GenericViewSet, DestroyModelMixin):
    queryset = Cart.objects.all()
    serializer_class = CartSerializers
    

class CartItemViewSet(ModelViewSet):
    # queryset = CartItem.objects.all()
    serializer_class = CartItemSerializer
    
    def get_queryset(self):
        return CartItem.objects.filter(cart_id=self.kwargs['cart_pk'])
    
    
    