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

def index(request):
    # html  = myLoader.get_template('index.html')
    # return HttpResponse(html.render())
    # html = loader.get_template('index.html')
    # return HttpResponse(html.render())
    context = {
        'categories': Categorie.objects.all(),
        'stories':Storie.objects.all()
    }
    return render(request, 'index.html', context=context)

def single(request, id):
    context = {
        'storie':Storie.objects.get(id = id)
        }
    return render(request, 'single.html', context=context)

