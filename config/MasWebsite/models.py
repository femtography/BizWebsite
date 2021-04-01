from django.db import models

class Product(models.Model):

    name = models.CharField(max_length=30)
    short_d = models.CharField(max_length=120)
    category = models.CharField(max_length=15)
    url = models.CharField(max_length=100)
