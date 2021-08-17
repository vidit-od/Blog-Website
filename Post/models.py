from django.db import models

# Create your models here.
class post(models.Model):
    title= models.CharField(max_length=100)
    date=models.CharField(max_length=50)
    description=models.CharField(max_length=10000)
    author=models.CharField(max_length=100)
    catagory=models.CharField(max_length=100)
