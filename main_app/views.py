from django.shortcuts import render

# Create your views here.

def index(request):
    return render(request, 'index.html')


def products(request):
    return render(request, 'products.html')

#to change
def product(request): 
    return render(request, 'product.html')


def contact(request):
    return render(request, 'contact.html')