from django.contrib import admin
from bradoo.core.models import Vendors, Products


class VendorsAdmin(admin.ModelAdmin):
    list_display = ("name", "cnpj", "city")


class ProductsAdmin(admin.ModelAdmin):
    list_display = ("name", "code", "price", "vendor")


admin.site.register(Vendors, VendorsAdmin)
admin.site.register(Products, ProductsAdmin)