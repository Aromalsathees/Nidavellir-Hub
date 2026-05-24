from django.urls import path  
from .views import *

urlpatterns = [
    path('register/',register,name='register_account'),
    path('login/',login,name='login_account'),
    path('logout/',logout,name='logout_account'),

]