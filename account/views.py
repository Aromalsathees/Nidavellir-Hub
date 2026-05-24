from django.shortcuts import render,redirect
from .forms import RegistrationForm
from .models import *
# Create your views here.

def register(request):

    form = RegistrationForm(request.POST or None)

    if request.method == 'POST':

        if form.is_valid():

            first_name = form.cleaned_data['first_name']
            last_name = form.cleaned_data['last_name']
            phone_number = form.cleaned_data['phone_number']
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']

            username = email.split("@")[0]

            user = Account.objects.create_user(
                first_name=first_name,
                last_name=last_name,
                email=email,
                username=username,
                password=password
            )

            user.phone_number = phone_number
            user.save()

            return redirect('home')

    return render(
        request,
        'accounts/register.html',
        {'form': form}
    )

def login(request):
    return render(request,'accounts/login.html')

def logout(request):
    return redirect('/login')