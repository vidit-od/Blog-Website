from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import auth,User
from django.contrib import messages
from datetime import datetime
from .models import post
# Create your views here.
def index(request):
    return render(request, 'index.html')

def login(request):
    if request.method=='POST':
        username=request.POST['username']
        password=request.POST['password']

        user=auth.authenticate(username=username,password=password)
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        else:
            messages.info(request, 'Invalid Details')
            return redirect('login')
    return render(request, 'login.html')

def signup(request):
    if request.method=='POST':
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        re_password=request.POST['re_password']

        if User.objects.filter(username=username).exists():
            messages.info(request, 'This user name is occpied')
            return redirect('signup')
        elif User.objects.filter(email=email).exists():
            messages.info(request, 'Use Other Email Addess')
            return redirect('signup')
        elif password !=re_password:
            messages.info(request, 'Password Do not math')
            return redirect('signup')
        else:
            user=User.objects.create_user(username=username,email=email,password=password)
            user.save()
            messages.info(request, 'saved')
            return redirect('login')

    return render(request, 'signup.html')

def logout(request):
    auth.logout(request)
    return redirect('/')

def blogs(request):
    posts=post.objects.all()
    return render(request, 'blogs.html',{'posts':posts})

def write_blog(request):
    if request.method=="POST":
        title=request.POST["title"]
        author=request.user.username
        date=(str(datetime.now()))[0:10]
        catagory=request.POST['catagory']
        Description=request.POST['Description']
        if title=='' or author=='' or date=='' or catagory=='' or Description=='':
           messages.info(request, 'empty fields')
           return redirect('write_blog')

        elif post.objects.filter(title="title").exists():
            messages.info(request, 'choose different title')
            return redirect('write_blog')

        elif len(Description)<40 :
            messages.info(request, 'Blog should be descriptive')
            return redirect('write_blog')
        else:
            data= post.objects.create(title=title,author=author,date=date,catagory=catagory,description=Description)
            data.save()
            return redirect('blogs')


    return render(request,'write_blog.html')