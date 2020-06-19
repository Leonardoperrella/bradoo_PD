from django import forms
from bradoo.core.models import Products, Vendors


class ProductsModelForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['name', 'code', 'price', 'vendor']


class VendorsModelForm(forms.ModelForm):
    class Meta:
        model = Vendors
        fields = ['name', 'cnpj', 'city']
