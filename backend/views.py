from django.shortcuts import render,redirect  
from store.models import * 
from cart.models import *

def home(request):
    try:
        products = Products.objects.all().filter(is_available=True)
    except Products.DoesNotExist:
        return redirect('/')
        
    context = {
        'products':products,
    }
    return render(request,'home.html',context)

def product_detail(request,slug):
    product = Products.objects.get(slug=slug)
    context = {
        'product':product
    }
    return render(request,'product_detail/product_detail.html',context)

def search_product(request):
    q = request.GET.get('q')
    if not q:
        return redirect('/')
    product = Products.objects.filter(product_name__icontains=q)
    product_count = product.count()
    context = {
        'product':product,
        'product_count':product_count
    }
    return render(request,'search/search.html',context)