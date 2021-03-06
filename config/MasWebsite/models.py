from django.db import models

class Product(models.Model):
    def __str__(self):
         return self.name

    name = models.CharField(max_length=30)
    short_d = models.CharField(max_length=120)
    category = models.CharField(max_length=15)
    url = models.CharField(max_length=100)
    is_featured = models.BooleanField(default=False)

class Sale(models.Model):
    def __str__(self):
         return self.name

    name = models.CharField(max_length=30)
    url = models.CharField(max_length=100)
