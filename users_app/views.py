from http.client import HTTPResponse
from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from .forms import CreationForm, UserCreationForm
# Create your views here.

def user_index(request):
    return HttpResponseRedirect(reverse('users_app:login'))
    if request.user.is_authenticated:
        return render(request, 'user_index.html')
    return HttpResponseRedirect(reverse('login'))


def login(request):
    return render(request, 'login.html')


def logout(request):
    pass


def sign_up(request):
    if request.method == 'POST':
        pass
    else:
        form = CreationForm
        return render(request, 'sign_up.html', {'form':form})
    
