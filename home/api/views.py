from django.shortcuts import render
from django.http import JsonResponse
from home.models import Categorie
from rest_framework.views import APIView


# def categoryApi(request):
#     js = []
#     data = Categorie.objects.all()
#     for i in data:
#         js.append({'name':i.name, 'image':i.image.url, 'slug':i.slug})
#     return JsonResponse(js, safe=False)

class CategoryView(APIView):
    def get(self, *args, **kwargs):
        print('get run')
        js = []
        data = Categorie.objects.all()
        for i in data:
            js.append({'name':i.name, 'image':i.image.url, 'slug':i.slug})
        return JsonResponse(js, safe=False)


    def post(self, *args, **kwargs):
        pass