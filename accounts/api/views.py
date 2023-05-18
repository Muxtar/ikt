from rest_framework.views import APIView
from accounts.api.serializers import RegisterSerial
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User


class RegisterView(APIView):
    def get(self, request, *args, **kwargs):
        users = User.objects.all()
        serial = RegisterSerial(users, many = True)
        return Response(data=serial.data, status = status.HTTP_200_OK)
    
    def post(self, request, *args, **kwargs):
        data = request.data
        serial = RegisterSerial(data=data)
        if serial.is_valid():
            serial.save()
            return Response(data=serial.data, status=status.HTTP_201_CREATED)  
        return Response(data = serial.errors, status=status.HTTP_400_BAD_REQUEST )