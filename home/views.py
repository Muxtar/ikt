from django.shortcuts import render
from django.http import (   HttpResponse,
                            JsonResponse)

from django.template import loader
from home.models import Categorie,Storie
# Create your views here.


class myLoader():
    def __init__(self, template_name) -> None:
        from django.conf import settings
        self.template_name = template_name
        self.BASE_DIR = settings.TEMPLATES[0]['DIRS'][0]/self.template_name

    @classmethod
    def get_template(cls, template_name):
        return cls(template_name)

    def render(self):
        with open(self.BASE_DIR, 'r') as f:
            return f.read()

def index(request, slug = None):
    # html  = myLoader.get_template('index.html')
    # return HttpResponse(html.render())
    # html = loader.get_template('index.html')
    # return HttpResponse(html.render())
    stories = Storie.objects.all()

    if slug:
        stories = stories.filter(category__slug = slug)
   
    context = {
        'stories':stories
    }
    return render(request, 'index.html', context=context)

def about(request):
    return render(request, 'about.html')

def recipes(request):
    return render(request, 'recipes.html')

def stories(request, slug = None):
    stories = Storie.objects.all()
    if slug:
        tag = request.GET.get('tag')
        if not tag:
            stories = stories.filter(category__slug = slug)
        else:
            stories = stories.filter(tag__slug = slug)

    context = {
        'stories': stories
    }
    return render(request, 'stories.html', context=context)

def single(request, slug):
    context = {
        'storie':Storie.objects.get(slug = slug)
        }
    return render(request, 'single.html', context=context)

