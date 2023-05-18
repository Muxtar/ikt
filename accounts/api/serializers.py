from rest_framework import serializers
from django.contrib.auth.models import User
  

class RegisterSerial(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['username', 'email', 'password']


    def create(self, validated_data):
        return super().create(validated_data)