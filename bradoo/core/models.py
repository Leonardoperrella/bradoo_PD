from django.db import models    
from django.core.validators import MinValueValidator
from decimal import Decimal
from localflavor.br.models import BRCNPJField
from bradoo.core.validators import validate_cnpj


class Vendors(models.Model):
    name = models.CharField('Name', max_length=50)
    cnpj = BRCNPJField(validators=[validate_cnpj])
    city = models.CharField('City', max_length=100, blank=True)

    class Meta:
        verbose_name = "Vendor"
        verbose_name_plural = "Vendors"

    def __str__(self):
        return self.name


class Products(models.Model):
    name = models.CharField('Name', max_length=60)
    code = models.CharField('Code', max_length=13)
    price = models.DecimalField('Price',
                                max_digits=15,
                                decimal_places=2,
                                default=0.00,
                                validators=[MinValueValidator(Decimal("0.01"))
                            ])
    vendor = models.ForeignKey('Vendors', on_delete=models.CASCADE,
                                related_name='vendor')

    class Meta:
        verbose_name = "Product"
        verbose_name_plural = "Products"

    def __str__(self):
        return self.name
