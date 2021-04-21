from rest_framework import serializers
from . models import ProductCategory, Product

#-------------------------------------------------
# КАТЕГОРИЯ
#-------------------------------------------------

class CategoryListSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = ('id','name', 'description')


class CategoryDeteilSerializer(serializers.ModelSerializer):
    class Meta:
        model = ProductCategory
        fields = '__all__'


#-------------------------------------------------
# ПРОДУКТ
#-------------------------------------------------

class ProductDeteilSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = '__all__'


class ProductListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = ('id','name', 'price_now', 'quantity', 'image', 'status', 'short_description')