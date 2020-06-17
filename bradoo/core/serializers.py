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
    '''
    def create(self, validated_data):
        vendor_validated_data = validated_data.pop('vendor')
        print(vendor_validated_data)
        vendor = Vendors.objects.create(**validated_data)
        vendor_set_serializer = self.fields['products']
        for each in vendor_validated_data:
            each['vendor'] = vendor
        vendor_set_serializer.create(vendor_validated_data)
        return vendor
    '''

