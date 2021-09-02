from django.db import models

# Create your models here.
class post(models.Model):
    title= models.CharField(max_length=100)
    mini_title=models.CharField(max_length=50)
    date=models.DateField(auto_now_add=True)
    description=models.CharField(max_length=10000)
    author=models.CharField(max_length=100)
    catagory=models.CharField(max_length=100)

    def __str__(self):
        return '%s' %(self.title) 

class comment(models.Model):
    post=models.ForeignKey(post, on_delete=models.CASCADE,related_name='comments')
    user=models.CharField(max_length=100)
    content=models.TextField()
    date_added=models.DateField(auto_now_add=True)

    def __str__(self):
        return '%s - %s| %s' %(self.content, self.user, self.post.title) 

class catagory(models.Model):
    catagory_name=models.CharField(max_length=100)
    image=models.ImageField(blank=True,null=True,upload_to="images/catagory/")

    def __str__(self):
        return '%s' %(self.catagory_name)

class users(models.Model):
    first_name=models.CharField(max_length=100,blank=True)
    last_name=models.CharField(max_length=100,blank=True)
    user_id=models.CharField(max_length=100,blank=False,null=False)
    gender=models.CharField(max_length=20,blank=True)
    age=models.IntegerField()
    profile_pic=models.ImageField(default="images\profile_pic\default-avatar.jpg", upload_to="images/profile_pic/")

