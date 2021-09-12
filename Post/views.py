from django.shortcuts import render,redirect,get_object_or_404
from django.http import HttpResponse,HttpResponseRedirect
from django.contrib.auth.models import auth,User
from django.contrib import messages
from datetime import datetime
from django.urls import reverse
from .models import post,comment,catagory as catagory_model,users
import os
from django.conf import settings
import random
# Create your views here.
# for index.html
def index(request):
    user=users.objects.get(user_id=request.user.id)
    max_blogs=random.randint(3, 6)
    all_posts=post.objects.all().order_by('id').reverse()[0:max_blogs]
    return render(request, 'index.html',{'user_pic':user,'all_posts':all_posts})

# for login.html
def login(request):
    if request.method=='POST':
        # collect data from form
        username=request.POST['username']
        password=request.POST['password']
        
        # authenticate the data
        user=auth.authenticate(username=username,password=password)
        # if authentication complete; login
        if user is not None:
            auth.login(request, user)
            return redirect('/')
        # else give error message
        else:
            messages.info(request, 'Invalid Details')
            return redirect('login')
    return render(request, 'login.html')

# for signup.html
def signup(request):
    if request.method=='POST':
        # collect data
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        re_password=request.POST['re_password']

        # username should be unique;give error message if it already exist in db
        if User.objects.filter(username=username).exists():
            messages.info(request, 'This user name is occpied')
            return redirect('signup')

        # email should be unique;give error message if it already exist in db
        elif User.objects.filter(email=email).exists():
            messages.info(request, 'Use Other Email Addess')
            return redirect('signup')
        # if password and confirm password do not match
        elif password !=re_password:
            messages.info(request, 'Password Do not math')
            return redirect('signup')
        # all the possible errors are not present; hencs this profile is ready to be created
        else:
            user=User.objects.create_user(username=username,email=email,password=password)
            user.save()
            user2=users.objects.create(user_id=user)
            user2.save()
            messages.info(request, 'saved')
            return redirect('login')

    return render(request, 'signup.html')

# for logout functionality
def logout(request):
    auth.logout(request)
    return redirect('/')

# for blogs.html
def blogs(request):
    posts=post.objects.all().order_by('id').reverse()
    all_catagory=catagory_model.objects.all()
    user=users.objects.get(user_id=request.user.id)
    # for filteration of data
    if request.method=='POST':
        # catagory has the catagory name sotred in it 
        catagory_name=request.POST['catagory_select']
        # using catagory we find its id; .first() gives the object's first row's result which is its id most of the cases 
        catagory=catagory_model.objects.filter(catagory_name=catagory_name).first()
        sort=request.POST['sort']
        author=request.POST['author']
        # if user wants latest at top; .reverse() will come here
        if sort=="Latest at Top":
            # user request only catagory sort
            if catagory_name!="All" and author=="":
                posts=post.objects.filter(catagory=catagory).order_by('id').reverse()
                messages.info(request,'1')
                return render(request, 'blogs.html',{'posts':posts ,'all_catagory':all_catagory,'selected_catagory':catagory_name,'user_pic':user})

            # user request only author sort
            elif catagory_name=="All" and author!="":
                posts=post.objects.filter(author=author).order_by('id').reverse()
                messages.info(request, '2')
                return render(request, 'blogs.html',{'posts':posts,'all_catagory':all_catagory,'selected_author':author,'user_pic':user})

            # user requests both sort
            elif catagory_name!="All" and author!="":
                posts=post.objects.filter(catagory=catagory , author=author).order_by('id').reverse()
                messages.info(request, '3')
                return render(request, 'blogs.html',{'posts':posts,'all_catagory':all_catagory,'selected_catagory':catagory_name,'selected_author':author,'user_pic':user})
            else:
                posts=post.objects.order_by('id').reverse()
                messages.info(request, '4')
                return render(request, 'blogs.html',{'posts':posts,'all_catagory':all_catagory,'selected_catagory':catagory_name,'selected_author':author,'user_pic':user})
        # if user wants oldest at top;
        else:
            # user request only catagory sort
            if catagory_name!="All" and author=="":
                posts=post.objects.filter(catagory=catagory).order_by('id')
                messages.info(request, '5')
                return render(request, 'blogs.html',{'posts':posts,'all_catagory':all_catagory,'selected_catagory':catagory_name,'selected_sort':sort,'user_pic':user})

            # user request only author sort
            elif catagory_name=="All" and author!="":
                posts=post.objects.filter(author=author).order_by('id')
                messages.info(request, '6')
                return render(request, 'blogs.html',{'posts':posts,'all_catagory':all_catagory,'selected_author':author,'selected_sort':sort,'user_pic':user})

            # user requests both sort
            elif catagory_name!="All" and author!="":
                posts=post.objects.filter(catagory=catagory , author=author).order_by('id')
                messages.info(request, '7')
                return render(request, 'blogs.html',{'posts':posts,'all_catagory':all_catagory,'selected_catagory':catagory_name,'selected_author':author,'selected_sort':sort,'user_pic':user})
            else:
                posts=post.objects.all().order_by('id')
                messages.info(request, '8')
                return render(request, 'blogs.html',{'posts':posts,'all_catagory':all_catagory,'selected_catagory':catagory_name,'selected_author':author,'selected_sort':sort,'user_pic':user})
    return render(request, 'blogs.html',{'posts':posts,'all_catagory':all_catagory,'user_pic':user})

# for write_blog.html
def write_blog(request):
    all_catagory=catagory_model.objects.all()
    if request.method=="POST":
        # collect data from form
        title=request.POST["title"]
        mini_title=request.POST["mini_title"]
        author=request.user.username
        date=(str(datetime.now()))[0:10]
        catagory=request.POST['catagory']
        Description=request.POST['Description']
        
        # if any field empty give error message
        if title=='' or author=='' or date=='' or catagory=='' or Description=='' or mini_title=='':
           messages.info(request, author)
           return redirect('write_blog')
        # post title should be unique
        elif post.objects.filter(title=title).exists():
            messages.info(request, 'choose different title')
            return redirect('write_blog')
        # blog length should be atleast 150 words
        elif len(Description)<150 :
            messages.info(request, 'Blog should be descriptive')
            return redirect('write_blog')
        # all possible errors checked; save data 
        else:
            data= post.objects.create(title=title,mini_title=mini_title,author=author,date=date,catagory=catagory,description=Description)
            data.save()
            return redirect('blogs')
    return render(request,'write_blog.html',{'all_catagory':all_catagory})

# for read_blog.html
def read_blog(request,pk):
    # collect data from models 
    blog=post.objects.get(id=pk)
    total_like=blog.total_likes()
    all_blog=post.objects.all()
    catagory_blog=[]
    like_status=False
    user=users.objects.get(user_id=request.user.id)
    # for suggestions section; filter out blogs that have similar catagory to current blog
    for i in all_blog:
        if i.catagory==blog.catagory:
            catagory_blog.append(i)
    # to store comments in database
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
    
    # find if we have already liked this post or not
    if blog.like.filter(id=request.user.id).exists():
        like_status=True
    else:
        like_status=False
 
    return render(request,'read_blog.html',{'blog':blog, 'all_blogs':catagory_blog ,'total_like':total_like,'like_status':like_status,'user_pic':user})

# for adding likes functionality
def like(request,pk):
    # get the post we want to add like/unlike
    Post = post.objects.get(id=pk)
    like_status=False
    # if like already exist: then unlike it
    if Post.like.filter(id=request.user.id).exists(): 
        Post.like.remove(request.user.id)
        like_status=False
    # if like doesnot exist; all like
    else:
        Post.like.add(request.user.id)
        like_status=True
    return HttpResponseRedirect(reverse('read_blog',args=[str(pk)]))

# for Edit_Profile.html
def profile(request,pk):
    user_id=User.objects.get(username=pk).pk
    user=users.objects.get(user_id=user_id)
    
    if request.method=='POST':
        profile_pic=request.FILES.get('profile_pic', False)
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        age=request.POST['age']
        gender=request.POST['gender']

        if profile_pic!=False:
            ext="."+str(user.profile_pic).split('.')[-1]
            name = 'profile_pic//'+str(user_id)+ext
            os.remove(os.path.join(settings.MEDIA_ROOT,name))
            user.profile_pic=profile_pic
        user.first_name=first_name
        user.last_name=last_name
        user.age=age
        user.gender=gender
        user.save()
        
        return redirect(f'/Edit_Profile/{pk}')
    return render(request, 'Edit_Profile.html',{'user':user})