from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import CreationForm, UserCreationForm
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib.auth.forms import AuthenticationForm
from .models import Product, User_data
from main_app.views import sql_to_list


# Create your views here.

def user_index(request):
    if request.user.is_authenticated:      
        raw_cart = User_data.objects.get(pk=request.user.id)
        cart = sql_to_list(raw_cart.cart)
        print(f"carrito es {cart}")
        print(f"len de cart es {len(cart)}")
        products = []
        if len(cart) >0:
            for id in cart:
                products.append( Product.objects.get(pk = int(id)) )

        return render(request, 'user_index.html', {"user":request, "products":products})
    return HttpResponseRedirect(reverse('users_app:login'))


def login(request):
    if request.method == "POST":
        form = AuthenticationForm(data=request.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(username=username, password=password)
            if user is not None:
                auth_login(request, user) # si usaba login, conflicto de nombres
                return HttpResponseRedirect(reverse('users_app:user_index'))
    form = AuthenticationForm()
    return render(request, 'login.html', {'form':form})


def logout(request):
    auth_logout(request)
    return HttpResponseRedirect(reverse('main_app:index'))


def sign_up(request):
    if request.method == 'POST':
        form = CreationForm(request.POST)
        if form.is_valid():
            form.save()
            user_data = User_data()
            user_data.save()
            return HttpResponseRedirect(reverse('users_app:login'))

    else:
        form = CreationForm()
    return render(request, 'sign_up.html', {'form':form})
    
