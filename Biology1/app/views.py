"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from django.db import models
from .models import Blog
from .models import Comment
from .forms import CommentForm
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm


def home(request):
    """Renders the home page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/index.html',
        {
            'title':'Главная',
            'year':datetime.now().year,
        }
    )


def blog(request):
    """Renders the blog page."""
    posts = Blog.objects.order_by('-posted')

    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/blog.html',
        {
            'title':'Блог о генетике',
            'message':'Посты о генетике',
            'posts': posts,
            'year':datetime.now().year,
        }
    )


def blogpost(request, parametr):
    """Renders the blogpost page."""
    post_1 = Blog.objects.get(id=parametr)
    comments = Comment.objects.filter(post=parametr)
    
    if request.method == "POST":
        form = CommentForm(request.POST)
        if form.is_valid():
            comment_f = form.save(commit=False)
            comment_f.author = request.user
            comment_f.date = datetime.now()                       
            comment_f.post = Blog.objects.get(id=parametr)    
            comment_f.save() 
       
            return redirect('blogpost', parametr=post_1.id)
    else:                                           
        form = CommentForm()
   
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/blogpost.html',
        {                                           
            'post_1': post_1, 
            'comments': comments, 
            'form': form, 

            'year':datetime.now().year,
        }
    )


def registration(request):
    """Renders the registration page."""
      
    if request.method == "POST":
        regform = UserCreationForm(request.POST) 
        if regform.is_valid():                           
            reg_f = regform.save(commit=False)                  
            reg_f.is_staff = False
            reg_f.is_active = True
            reg_f.is_superuser = False
            reg_f.date_joined = datetime.now()                       
            reg_f.last_login = datetime.now()
            
            reg_f.save() 
       
            return redirect('blog')
    else:                                           
        regform = UserCreationForm()
   
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/registration.html',
        {                                           
            
            'regform': regform, 
            
            'year':datetime.now().year,
        }
    )


def sections(request):
    """Renders the sections page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/sections.html',
        {
            'title':'Разделы биологии',
            'message':' ',
            'year':datetime.now().year,
        }
    )


def contact(request):
    """Renders the contact page."""
    assert isinstance(request, HttpRequest)
    return render(
        request,
        'app/contact.html',
        {
            'title':'Контакты со мной',
            'message':'Контакты со мной',
            'year':datetime.now().year,
        }
    )

