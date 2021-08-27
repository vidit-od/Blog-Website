from django.db import models

# Create your models here.
class post(models.Model):
    title= models.CharField(max_length=100)
    mini_title=models.CharField(max_length=50)
    date=models.CharField(max_length=50)
    description=models.CharField(max_length=10000)
    author=models.CharField(max_length=100)
    catagory=models.CharField(max_length=100)

class comment(models.Model):
    post=models.ForeignKey(post, on_delete=models.CASCADE,related_name='comments')
    user=models.CharField(max_length=100)
    content=models.TextField()

    def __str__(self):
        return '%s - %s' %(self.post.title, self.user) 