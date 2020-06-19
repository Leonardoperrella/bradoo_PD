from django.contrib import admin
from django.urls import path, include
from bradoo.router import router
from bradoo.core.views import (
    home,
    products_list,
    create_product,
    delete_product,
    delete_product_section,
    edit_product,
    vendors_list,
    create_vendor,
    delete_vendor,
    delete_vendor_section,
    edit_vendor,
)

urlpatterns = [
    path('', home, name='home'),
    path('vendors/', vendors_list, name='vendors'),
    path('create_vendor/', create_vendor, name='create-vendor'),
    path('edit/<int:vendor_id>', edit_vendor, name='edit-vendor'),
    path('delete_vendor/<int:vendor_id>', delete_vendor, name='delete-vendor'),
    path('delete_vendor_section/', delete_vendor_section, name='delete_vendor_section'),
    path('products/', products_list, name='products'),
    path('create_product/', create_product, name='create-product'),
    path('edit_product/<int:product_id>', edit_product, name='edit-product'),
    path('delete_product/<int:product_id>', delete_product, name='delete-product'),
    path('delete_product_section/', delete_product_section, name='delete_product_section'),
    path('api/', include(router.urls))
]
