from django.db import models

# Create your models here.
GenreType = models.TextChoices('GenreType', 'ACTION HORROR ADVENTURE COMEDY KIDS')

class Product(models.Model):
    title = models.CharField(max_length=50)
    author = models.CharField(max_length=30)
    price = models.IntegerField()
    genre = models.CharField(max_length=20, choices=GenreType.choices)
    description = models.CharField(max_length=500, default='null')
    image = models.CharField(max_length=100,default='no-img')

    def __str__(self):
        return self.title
