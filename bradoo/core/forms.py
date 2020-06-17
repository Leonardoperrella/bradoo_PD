from django import forms
from bradoo.core.models import Products, Vendors
from localflavor.br.forms import BRCNPJField
from input_mask.contrib.localflavor.br.widgets import BRCNPJInput


class ProductsModelForm(forms.ModelForm):
    class Meta:
        model = Products
        fields = ['name', 'code', 'price', 'vendor']


class VendorsModelForm(forms.ModelForm):
    class Meta:
        model = Vendors
        fields = ['name', 'cnpj', 'city']

    #cnpj = BRCNPJField(widget=BRCNPJInput) 