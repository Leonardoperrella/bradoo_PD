from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from django.http import Http404
from rest_framework import status, viewsets, mixins
from rest_framework.response import Response
from rest_framework.views import APIView
from bradoo.core.models import Products, Vendors
from bradoo.core.forms import ProductsModelForm, VendorsModelForm
from bradoo.core.serializers import VendorsSerializer


def home(request):
    return render(request, 'core/home.html')


def products_list(request):
    products = Products.objects.all()
    paginator = Paginator(products, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj
    }

    return render(request, 'core/products_list.html', context=context)


def create_product(request):

    if not request.method == 'POST':
        return render(request,
                        'core/create_product.html',
                        {'form': ProductsModelForm()})

    form = ProductsModelForm(request.POST)
    if not form.is_valid():
        return render(request, 'core/create_product.html', {'form': form})

    form.save()
    return redirect('products')


def delete_product(request, product_id):
    product = Products.objects.get(pk=product_id)
    product.delete()
    return redirect('products')


def delete_product_section(request, id=None):
    if request.method == 'POST':
        id_list = request.POST.getlist('products')
        for agent_id in id_list:
            Products.objects.get(id=agent_id).delete()
    return redirect('products')


def edit_product(request, product_id):
    product = Products.objects.get(pk=product_id)

    if not request.method == 'POST':
        return render(request,
                        'core/edit_product.html',
                        {'form': ProductsModelForm(instance=product)})
      
    form = ProductsModelForm(data=request.POST, instance=product)
    if not form.is_valid():
        return render(request, 'core/edit_product.html', {'form': form})
    form.save()
    return redirect('products')
  

def vendors_list(request):
    vendors = Vendors.objects.all()
    name = request.GET.get('name', False)
    cnpj = request.GET.get('cnpj', False) 
    city = request.GET.get('city', False)
    
    if name:
        vendors = vendors.filter(name=name)
    if cnpj:
        vendors = vendors.filter(cnpj=cnpj)
    if city:
        vendors = vendors.filter(city=city)           

    paginator = Paginator(vendors, 2)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    
    context = {
        'page_obj': page_obj
    }
    return render(request, 'core/vendors_list.html', context=context)


def create_vendor(request):

    if not request.method == 'POST':
        return render(request,
                        'core/create_vendor.html',
                        {'form': VendorsModelForm()})

    form = VendorsModelForm(request.POST)
    if not form.is_valid():
        return render(request, 'core/create_vendor.html', {'form': form})

    form.save()
    return redirect('vendors')


def delete_vendor(request, vendor_id):
    vendor = Vendors.objects.get(pk=vendor_id)
    vendor.delete()
    return redirect('vendors')


def delete_vendor_section(request, id=None):
    if request.method == 'POST':
        id_list = request.POST.getlist('vendors')
        for agent_id in id_list:
            Vendors.objects.get(id=agent_id).delete()
    return redirect('vendors')


def edit_vendor(request, vendor_id):
    vendor = Vendors.objects.get(pk=vendor_id)

    if not request.method == 'POST':
        return render(request,
                        'core/edit_vendor.html',
                        {'form': VendorsModelForm(instance=vendor)})
      
    form = VendorsModelForm(data=request.POST, instance=vendor)
    if not form.is_valid():
        return render(request, 'core/edit_vendor.html', {'form': form})
    form.save()
    return redirect('vendors')


class VendorsViewSet(viewsets.ModelViewSet):
    queryset = Vendors.objects.all()
    serializer_class = VendorsSerializer

    def get_queryset(self):
        qs = super(VendorsViewSet, self).get_queryset()
        pk = self.request.query_params.get('id')
        cnpj = self.request.query_params.get('cnpj')
        name = self.request.query_params.get('name')
        print(self.request.GET)
        if pk:
            qs = qs.filter(pk=pk)
            print('entrou pk')
            print(qs)
        if cnpj:
            qs = qs.filter(cnpj=cnpj)
            print('entrou cnpj')
            print(qs)
        if name:
            qs = qs.filter(name=name)
            print('entrou name')
            print(qs)
        return qs

    def list(self, request, *args, **kwargs):
        queryset = self.filter_queryset(self.get_queryset())
        if not queryset:
            return Response(status=status.HTTP_204_NO_CONTENT)
        page = self.paginate_queryset(queryset)
        if page is not None:
            serializer = self.get_serializer(page, many=True)
            return self.get_paginated_response(serializer.data)

        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)    