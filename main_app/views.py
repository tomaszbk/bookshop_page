from django.shortcuts import render
from users_app.models import Product, User_data
from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.urls import reverse
from django.db.models import F

# Create your views here.

def index(request):
    return render(request, 'index.html')


def products(request):
    
    return render(request, 'products.html', {'products': Product.objects.all(),
    'url_start':"url 'main_app:products/" })

#to change
def product(request, product_id):
    return render(request, 'product.html',{'product':Product.objects.get(pk= product_id  )})


def contact(request):
    return render(request, 'contact.html')


def add_cart(request, product_id):
    user_data = User_data.objects.get(pk= request.user.id)

    print(f"user_data is {user_data}")
    print(f"user_cart raw is {user_data.cart}")

    user_cart = sql_to_list( user_data.cart ) #list of cart

    print(f"user_cart transformed is {user_cart}")
    if product_id in user_cart:
        return HttpResponseRedirect(reverse('main_app:products/' + str(product_id) ))
    print(f"product_id es {product_id}")
    user_cart.append(product_id)
    user_cart = str(user_cart)
    print(f"user_cart con item agregado es {user_cart}")
    user_data.cart = user_cart
    user_data.save()
    return HttpResponseRedirect(reverse('main_app:index'))



def update_rating(request, product_id): #pendiente: check if already liked
    product = Product.objects.get(pk= product_id )
    user_data = User_data.objects.get(pk= request.user.id)
    user_likes =  sql_to_list( user_data.liked_books )
    print(f"user_likes made list: {user_likes}")
    print(f"product_id es {product_id}")
    print(f"product type: {type(product_id)}")
    print(f"user_likes type: {type(user_likes[0])}")
    if str(product_id) in user_likes:
        return HttpResponseRedirect(reverse('main_app:products'))
    
    product.likes = F('likes') + 1
    product.save()   
    user_likes.append(product_id)
    print(f"user_likes w item appended: {user_likes}")
    user_likes = str(user_likes)
    user_data.liked_books = user_likes
    user_data.save()
    return HttpResponseRedirect(reverse('main_app:products'))


def sql_to_list(x):
    x = x.replace("'", "")
    x = x.replace("[", "")
    x = x.replace("]", "")
    x = x.replace(",", "")
    return x.split()
