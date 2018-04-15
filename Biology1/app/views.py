"""
Definition of views.
"""

from django.shortcuts import render
from django.http import HttpRequest
from django.template import RequestContext
from datetime import datetime
from django.db import models
from .models import Blog


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

