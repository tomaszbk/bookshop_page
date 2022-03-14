from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

# Create your models here.

CHOICES = (
    (1,"ACTION"),
    (2,"HORROR"),
    (3,"ADVENTURE"),
    (4,"COMEDY"),
    (5,"KIDS")
)

class Product(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=30)
    price = models.IntegerField()
    genre = models.IntegerField(max_length=20, choices=CHOICES)
    description = models.CharField(max_length=500, default='null')
    image = models.CharField(max_length=100,default='no-img')
    likes = models.IntegerField(default=0) #nuevo

    def __str__(self):
        return self.title


class User_data(models.Model):
    liked_books = models.CharField(max_length=500,default='[]')
    cart = models.CharField(max_length=500, default='[]')