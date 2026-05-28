from django.urls import path  
from .views import *

urlpatterns = [
    path('register/',register,name='register_account'),
    path('login/',login,name='login_account'),
    path('logout/',logout,name='logout_account'),
    path('dashboard/',dashboard),

    path('activate/<uidb64>/<token>/',activate, name='activate'),
    path('reset_password_validate/<uidb64>/<token>/',reset_password_validate, name='reset_password_validate'),
    path('forgotpassword/',ForgotPassword,name='forgotpassword'),
    path('resetpassword/',ResetPassword,name='resetpassword')

]