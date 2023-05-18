from django.shortcuts import render
from django.http import JsonResponse
from home.models import Categorie, Tag, Storie
from home.api.serializers import (SerialTag, SerialStory, CreateSerialStory, 
                                  CategorySerial)
from rest_framework.views import APIView

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from rest_framework import permissions
from home.api.permissions import MyPermissions



@api_view(['GET', 'POST'])
def tagView(request):
    if request.method == 'GET':
        tags = Tag.objects.all()
        serial = SerialTag(tags, many = True)
        return Response(serial.data, status=status.HTTP_200_OK)
    
    elif request.method == 'POST':
        data = SerialTag(data=request.data)
        if data.is_valid():
            data.save()
            return Response(data=data.data, status=status.HTTP_201_CREATED)

@api_view(['GET', 'PUT', 'DELETE'])
def tagViewId(request, id):
    try:
        tags = Tag.objects.get(id = id)
    except:
        return Response(data={
                'error':'Tag not found'
            }, status=status.HTTP_204_NO_CONTENT)
    
    if request.method == 'GET':
        serial = SerialTag(tags)
        return Response(serial.data, status=status.HTTP_200_OK)
    
    elif request.method == 'PUT':
        serial = SerialTag(tags, request.data)
        if serial.is_valid():
            serial.save()
            return Response(serial.data, status.HTTP_200_OK)

    elif request.method == 'DELETE':
        tags.delete()
        return Response(data={'delete':'Success'}, status=status.HTTP_200_OK)

class CategoryView(APIView):
    def get(self, request, *args, **kwargs):
        categories = Categorie.objects.all()
        # print(categories)
        # return Response({"salam":'salam'})
        serial = CategorySerial(categories, many = True,context = {'request':request})
        return Response(data=serial.data, status=status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        data = CategorySerial(data = request.data)
        if data.is_valid():
            data.save()
            return Response(data=data.data, status=status.HTTP_201_CREATED)
        return Response(data=data.errors, status=status.HTTP_400_BAD_REQUEST)
    
class StorieViewApi(APIView):
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def get(self, request, *args, **kwargs):
        stories = Storie.objects.all()
        serial = SerialStory(stories, many = True)
        return Response(data=serial.data, status=status.HTTP_200_OK)


    def post(self, request, *args, **kwargs):
        data = CreateSerialStory(data = request.data)
        if data.is_valid():
            data.save()
            return Response(data = data.data, status=status.HTTP_201_CREATED)
        return Response({'error':data.errors})
    
        #     return Response(data=data.data, status=status.HTTP_201_CREATED)
        # return Response(data=data.errors, status=status.HTTP_400_BAD_REQUEST)


class StorieViewApiId(APIView):
    permission_classes = [MyPermissions]
    def get(self, request, id, *args, **kwargs):
        stories = Storie.objects.get(id = id)
        serial = SerialStory(stories,  context = {'request':request})
        return Response(data=serial.data, status=status.HTTP_200_OK)

    def put(self, request, id, *args, **kwargs):
        obj = Storie.objects.get(id = id)
        serial = CreateSerialStory(obj, data = request.data)
        if serial.is_valid():
            serial.save()
            return Response(data=serial.data, status=status.HTTP_200_OK)
        return Response(data=serial.errors, status=status.HTTP_400_BAD_REQUEST)
    

    # def post(self, request, *args, **kwargs):
    #     data = CreateSerialStory(data = request.data)
    #     if data.is_valid():
    #         data.save()
    #         return Response(data = data.data, status=status.HTTP_201_CREATED)
    #     return Response({'error':data.errors})
    
    # return Response(data=data.data, status=status.HTTP_201_CREATED)
    # return Response(data=data.errors, status=status.HTTP_400_BAD_REQUEST)


# def categoryApi(request):
#     js = []
#     data = Categorie.objects.all()
#     for i in data:
#         js.append({'name':i.name, 'image':i.image.url, 'slug':i.slug})
#     return JsonResponse(js, safe=False)
