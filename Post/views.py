from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import auth,User
from django.contrib import messages
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

def write_blog(request,pk):
    name=pk
    return render(request,'write_blog.html',{'name':name})