from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import CreationForm, UserCreationForm
from django.contrib.auth import authenticate, logout
from django.contrib.auth import login as auth_login
from django.contrib.auth.forms import AuthenticationForm


# Create your views here.

def user_index(request):
    if request.user.is_authenticated:
        return render(request, 'user_index.html', {"user":request})
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
    logout(request)
    return HttpResponseRedirect(reverse('main_app:index'))


def sign_up(request):
    if request.method == 'POST':
        form = CreationForm(request.POST)
        if form.is_valid():
            form.save()
            return HttpResponseRedirect(reverse('users_app:login'))

    else:
        form = CreationForm()
    return render(request, 'sign_up.html', {'form':form})
    
