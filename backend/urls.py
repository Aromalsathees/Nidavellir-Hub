from django.contrib import admin
from django.urls import path,include
from .views import *
from store.models import *

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    
    path('admin/', admin.site.urls),
    path('store/',include('store.urls')),
    path('cart/',include('cart.urls')),
    path('account/',include('account.urls')),

    path('',home,name='home'),
    path('search/',search_product,name='search_product'),


    path('<slug:slug>/',product_detail,name='get-product-details'),

    
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
