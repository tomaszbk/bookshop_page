from django.shortcuts import render
from users_app.models import Product

# Create your views here.

def index(request):
    return render(request, 'index.html')


def products(request):
    return render(request, 'products.html', {'products': Product.objects.all() })

#to change
def product(request): 
    return render(request, 'product.html')


def contact(request):
    return render(request, 'contact.html')