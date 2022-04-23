from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('products<int:genre>', views.products, name = 'products'),
    path('products', views.products, name = 'products'),
    path('contact', views.contact, name = 'contact'),
    path('products/<int:product_id>', views.product, name = 'products'),
    path('add_cart', views.add_cart, name = 'add_cart'),
    path('products/remove_cart/<int:product_id>', views.remove_cart, name = 'remove_cart'),
    path('like', views.update_rating, name = 'like')
]