from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name = 'index'),
    path('products', views.products, name = 'products'),
    path('contact', views.contact, name = 'contact'),
    path('products/<int:product_id>', views.product, name = 'products'),
    path('products/add_cart/<int:product_id>', views.add_cart, name = 'add_cart'),
    path('products/like/<int:product_id>', views.update_rating, name = 'like')
]