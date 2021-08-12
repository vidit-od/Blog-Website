from django.db import models
from datetime import datetime
# Create your models here.
class post(models.Model):
    title= models.CharField(max_length=100)
    date=models.DateField(default=datetime.now,blank=True)
    description=models.CharField(max_length=10000)
    author=models.CharField(max_length=100)
    catagory=models.CharField(max_length=100)
    image=models.ImageField(upload_to='uploads/',null=True)
