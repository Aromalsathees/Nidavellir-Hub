from django.shortcuts import render  
from store.models import * 

def home(request):
    products = Products.objects.all()
    context = {
        'products':products
    }
    return render(request,'home.html',context)
