from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import auth,User
from django.contrib import messages
from datetime import datetime
from .models import post,comment,catagory as catagory_model
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
    posts=post.objects.all().order_by('id').reverse()
    all_catagory=catagory_model.objects.all()
    if request.method=='POST':
        catagory=request.POST['catagory_select']
        sort=request.POST['sort']
        author=request.POST['author']

        if sort=="Latest at Top":
            if catagory!="All" and author=="":
                posts=post.objects.filter(catagory=catagory).order_by('id').reverse()
                return render(request, 'blogs.html',{'posts':posts ,'all_catagory':all_catagory,'selected_catagory':catagory})

            elif catagory=="All" and author!="":
                posts=post.objects.filter(author=author).order_by('id').reverse()
                return render(request, 'blogs.html',{'posts':posts,'all_catagory':all_catagory,'selected_author':author})
        
            elif catagory!="All" and author!="":
                posts=post.objects.filter(catagory=catagory , author=author).order_by('id').reverse()
                return render(request, 'blogs.html',{'posts':posts,'all_catagory':all_catagory,'selected_catagory':catagory,'selected_author':author})
        else:
            if catagory!="" and author=="":
                posts=post.objects.filter(catagory=catagory).order_by('id')
                return render(request, 'blogs.html',{'posts':posts,'all_catagory':all_catagory,'selected_catagory':catagory,'selected_sort':sort})

            elif catagory=="" and author!="":
                posts=post.objects.filter(author=author).order_by('id')
                return render(request, 'blogs.html',{'posts':posts,'all_catagory':all_catagory,'selected_author':author,'selected_sort':sort})
        
            elif catagory!="" and author!="":
                posts=post.objects.filter(catagory=catagory , author=author).order_by('id')
                return render(request, 'blogs.html',{'posts':posts,'all_catagory':all_catagory,'selected_catagory':catagory,'selected_author':author,'selected_sort':sort})
    return render(request, 'blogs.html',{'posts':posts,'all_catagory':all_catagory})

def write_blog(request):
    if request.method=="POST":
        title=request.POST["title"]
        mini_title=request.POST["mini_title"]
        author=request.user.username
        date=(str(datetime.now()))[0:10]
        catagory=request.POST['catagory']
        Description=request.POST['Description']
        if title=='' or author=='' or date=='' or catagory=='' or Description=='' or mini_title=='':
           messages.info(request, author)
           return redirect('write_blog')

        elif post.objects.filter(title=title).exists():
            messages.info(request, 'choose different title')
            return redirect('write_blog')

        elif len(Description)<150 :
            messages.info(request, 'Blog should be descriptive')
            return redirect('write_blog')
        else:
            data= post.objects.create(title=title,mini_title=mini_title,author=author,date=date,catagory=catagory,description=Description)
            data.save()
            return redirect('blogs')


    return render(request,'write_blog.html')

def read_blog(request,pk):
    blog=post.objects.get(id=pk)
    all_blog=post.objects.all()
    catagory_blog=[]
    for i in all_blog:
        if i.catagory==blog.catagory:
            catagory_blog.append(i)
    if request.method=='POST':
        content=request.POST['comment']
        user=request.user.username

        if content=="":
            messages.info(request, "Empty Comment not allowed")
            return redirect(f'/read_blog/{pk}')
        
        else:
            new_comment=comment.objects.create(post=blog,user=user,content=content)
            new_comment.save
            return redirect(f'/read_blog/{pk}')
            
        
    return render(request,'read_blog.html',{'blog':blog, 'all_blogs':catagory_blog })