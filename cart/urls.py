from django.urls import path  
from .views import *

urlpatterns = [
    path('',cart,name='cart'),
    path('add_to_cart/<int:product_id>/',add_to_cart,name='add-to-cart'),
    path('remove_product/<int:product_id>/',remove_cart_item,name='remove_cart_item'),
    path('count_decrease/<int:product_id>/',count_decrease,name='count_decrease'),
]