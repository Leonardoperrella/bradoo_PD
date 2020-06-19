from rest_framework import serializers
from drf_writable_nested import WritableNestedModelSerializer
from bradoo.core.models import Vendors, Products


class ProductsSerializer(serializers.ModelSerializer):
    class Meta:
        model = Products
        fields = ('name', 'code', 'price')


class VendorsSerializer(WritableNestedModelSerializer,
                        serializers.ModelSerializer):
    products = ProductsSerializer(source='vendor', many=True)
    class Meta:
        model = Vendors
        fields = ('name', 'cnpj', 'city', 'products')
