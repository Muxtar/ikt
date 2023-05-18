from rest_framework import serializers
from home.models import Categorie, Tag, Storie
from django.contrib.auth import get_user_model

User = get_user_model()


class SerialTag(serializers.Serializer):
    id  = serializers.IntegerField(read_only = True)
    name = serializers.CharField()
    slug = serializers.SlugField(read_only = True)

    def create(self, validated_data):
        data = Tag.objects.create(**validated_data)
        return data
    
    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

class SerialUser(serializers.ModelSerializer):
    class Meta:
        model = User
        # fields = ['username', 'email', 'first_name', 'last_name']
        fields = '__all__'
        # exclude = ['password', 'is_superuser', 'is_staff', 'is_active']
        # read_only_fields = ['username', 'email']

class SerialCategory(serializers.ModelSerializer):
    class Meta:
        model = Categorie()
        fields = ['name', 'image', 'slug']

class CreateSerialStory(serializers.ModelSerializer):
    class Meta:
        model = Storie
        fields = '__all__'
        read_only_fields = ['id', 'slug', 'create_date', 'update_date']

class SerialStory(serializers.ModelSerializer):
    user  = SerialUser()
    category = SerialCategory()
    tag = SerialTag()

    class Meta:
        model = Storie
        fields = '__all__'
        read_only_fields = ['id', 'slug', 'create_date', 'update_date']

class CategorySerial(serializers.ModelSerializer):
    image = serializers.FileField(required=False)
    class Meta:
        model = Categorie
        fields = ['name', 'image', 'slug']
        read_only_fields = ['id', 'slug']


# class SerialStory(serializers.Serializer):
#     title = serializers.CharField()
#     desc = serializers.CharField()

#     def create(self, validated_data):
#         data = Storie.objects.create(**validated_data)
#         return data