from rest_framework import serializers
from decimal import Decimal
from product.models import Category


class CategorySerializer(serializers.Serializer):
    id= serializers.IntegerField()
    name= serializers.CharField()
    description= serializers.CharField()

class ProductSerializers(serializers.Serializer):
    id = serializers.IntegerField()
    name= serializers.CharField()
    unit_price = serializers.DecimalField(max_digits=10, decimal_places=2, source='price')
    
    price_with_tax= serializers.SerializerMethodField(method_name='cal_tax')
    
    # category= serializers.PrimaryKeyRelatedField(
    #     queryset= Category.objects.all()
    # )
    category = CategorySerializer()
    
    def cal_tax(self, product):
        return round(product.price * Decimal(1.1), 2)