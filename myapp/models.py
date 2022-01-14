from django.db import models
from django.db.models.base import Model


class product(models.Model):
    type = models.CharField(max_length=50)
    product_name = models.CharField(max_length=30)
    description = models.TextField()
    price = models.IntegerField(default=0)
    offer = models.BooleanField(default=False)
    image = models.ImageField(upload_to='img/pics', default=" ")

    def __str__(self):
        return self.product_name

class Contact(models.Model):
    location = models.CharField(max_length=150)
    phone = models.CharField(max_length=15)
    mobile = models.CharField(max_length=12)
    email = models.EmailField()

class Cloth(models.Model):
    product_name = models.CharField(max_length=150)
    price = models.IntegerField(default=0)
    offer = models.BooleanField(default=False)
    image = models.ImageField(upload_to='img/pics', default=" ")

    def __str__(self):
        return self.product_name



