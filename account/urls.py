from django.urls import path  
from .views import *

urlpatterns = [
      path('activate/<uidb64>/<token>/',activate, name='activate'),
    path('register/',register,name='register_account'),
    path('login/',login,name='login_account'),
    path('logout/',logout,name='logout_account'),

]