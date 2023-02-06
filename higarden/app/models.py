from django.db import models

# Create your models here.

class Person(models.Model):
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100)
    subject = models.CharField(max_length=200)
    msg = models.TextField()
    

class Product(models.Model):
    name = models.CharField(max_length=200)
    img = models.ImageField(upload_to='product/')
    description = models.TextField(max_length=200)