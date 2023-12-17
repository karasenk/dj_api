from rest_framework import serializers
from .models import Category, Product


class CategorySerializer(serializers.ModelSerializer):
    class Meta:
        model = Category
        fields = ('name')


class ProductSerializer(serializers.ModelSerializer):
    name = serializers.CharField()
    price = serializers.IntegerField()

    class Meta:
        model = Product
        fields = ('name', 'price', 'category')
