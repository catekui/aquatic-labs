
from django.shortcuts import render
from django.http import HttpResponse
from .models import Publications, Blog


publications = [
    {
        'author': 'publications author',
        'title': 'publication title1',
        

    }
]
# Create your views here.

def home(request):
    return render(request, 'home.html', {'navbar': 'home'})

    # return render(request, 'navbar.html')

def publications(request):
    context = {
        'posts': Posts.all()
    }
    return render(request, 'publications.html', {'navbar': 'publications'})


def people(request):
    return render(request, 'people.html',  {'navbar': 'people'})

def blog(request):
    return render(request, 'blog.html',  {'navbar': 'blog'})
