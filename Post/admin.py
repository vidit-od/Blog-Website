from django.contrib import admin
from .models import post,comment,catagory,users
# Register your models here.
admin.site.register(post)
admin.site.register(comment)
admin.site.register(catagory)
admin.site.register(users)