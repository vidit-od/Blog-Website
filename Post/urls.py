from django.urls import path
from . import views
urlpatterns=[
    path('',views.index,name='index'),
    path('login',views.login,name='login'),
    path('signup',views.signup,name='signup'),
    path('logout',views.logout,name='logout'),
    path('blogs',views.blogs,name='blogs'),
    path('write_blog',views.write_blog,name='write_blog'),
    path('read_blog/<str:pk>',views.read_blog,name='read_blog'),
    path('like/<int:pk>',views.like,name='like'),
    path('Edit_Profile/<str:pk>',views.profile,name='profile')
]