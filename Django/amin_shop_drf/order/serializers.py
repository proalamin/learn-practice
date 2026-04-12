from rest_framework import serializers
from order.models import Cart, CartItem
from product.models import Product
from product.serializers import ProductSerializers


class ProductSerializerForCart(serializers.ModelSerializer):
    class Meta:
        model =Product
        fields = [ 'id', 'name', 'price']

    
class CartItemSerializer(serializers.ModelSerializer):
    # product = ProductSerializers()
    product = ProductSerializerForCart()
    
    # product_price=serializers.SerializerMethodField(method_name='get_product_price')
    
    class Meta:
        model= CartItem
        fields = ['id', 'product', 'quantity', 'product']
    
    # def get_product_price(self, cart_item):
    #     return cart_item.product.price
        
        
class CartSerializers(serializers.ModelSerializer):
    items = CartItemSerializer(many=True)
    
    class Meta:
        model =Cart
        fields = ['id', 'user', 'items']
        
    