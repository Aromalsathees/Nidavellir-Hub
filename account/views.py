from django.shortcuts import render,redirect
from .forms import RegistrationForm
from .models import *
from django.contrib import messages,auth
from django.contrib.auth.decorators import login_required
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
                password=password,
                phone_number=phone_number,
            )
            user.save()

            return redirect('home')

    return render(
        request,
        'accounts/register.html',
        {'form': form}
    )

def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = auth.authenticate(
            email=email,password=password
        )
        if user is not None:
            auth.login(request,user)
            # messages.success(request,'you are now logged in')
            return redirect('home') 
        else:
            messages.error(request,'invalid login credentials')
            return redirect('login_account')
        
    return render(request,'accounts/login.html')

@login_required(login_url = 'login_account')
def logout(request):
    auth.logout(request)
    messages.success(request,'you are logged out.')
    return redirect('login_account')