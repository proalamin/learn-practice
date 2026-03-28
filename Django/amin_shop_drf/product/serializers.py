from rest_framework import serializers
from decimal import Decimal
from product.models import Category, Product


# class CategorySerializer(serializers.Serializer):
#     id= serializers.IntegerField()
#     name= serializers.CharField()
#     description= serializers.CharField()

class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model= Category
        fields= ['id', 'name', 'description', 'product_Count']
        
    product_Count = serializers.IntegerField(read_only=True)
        
    # product_Count = serializers.SerializerMethodField(method_name='productCount')
        
    # def productCount(self, category):
    #     count = Product.objects.filter(category=category).count()
    #     return count


# class ProductSerializers(serializers.Serializer):
#     id = serializers.IntegerField()
#     name= serializers.CharField()
#     unit_price = serializers.DecimalField(max_digits=10, decimal_places=2, source='price')
    
#     price_with_tax= serializers.SerializerMethodField(method_name='cal_tax')
    
#     # category= serializers.PrimaryKeyRelatedField(
#     #     queryset= Category.objects.all()
#     # )
#     # category = CategorySerializer()
#     category = serializers.HyperlinkedRelatedField(
#         queryset= Category.objects.all(),
#         view_name = 'specific-category',
#     )
    
    # def cal_tax(self, product):
    #     return round(product.price * Decimal(1.1), 2)

class ProductSerializers(serializers.ModelSerializer):
    class Meta:
        model = Product
        # fields= '__all__'
        fields= ['id', 'name', 'description', 'price','price_with_tax', 'stock', 'category']
    
    price_with_tax = serializers.SerializerMethodField(
        method_name='cal_tax'
    )
    
    # category = serializers.HyperlinkedRelatedField(
    #     queryset= Category.objects.all(),
    #     view_name = 'specific-category',
    # )
    
    
    def cal_tax(self, product):
        return round(product.price * Decimal(1.1), 2)
    
    
    def validate_price(self, price):
        if price < 0:
            raise serializers.ValidationError("Price cloud not be negative")
        return price
    
    
    