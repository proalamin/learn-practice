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
    total_Price=serializers.SerializerMethodField(method_name='get_total_price')
    
    # product_price=serializers.SerializerMethodField(method_name='get_product_price')
    
    class Meta:
        model= CartItem
        fields = ['id', 'product', 'quantity', 'product', 'total_Price']
    
    # def get_product_price(self, cart_item):
    #     return cart_item.product.price
    
    def get_total_price(self, cart_item: CartItem):
        return cart_item.quantity * cart_item.product.price
        
        
class CartSerializers(serializers.ModelSerializer):
    items = CartItemSerializer(many=True, read_only=True)
    total_price= serializers.SerializerMethodField(method_name="get_total_price")
    
    class Meta:
        model =Cart
        fields = ['id', 'user', 'items', 'total_price']
        
    def get_total_price(self, cart: Cart):
        list = sum([item.product.price * item.quantity for item in cart.items.all()])
        # print("list", list)
        return list;
    