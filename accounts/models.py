from django.db import models
from django.contrib.auth.models import AbstractUser
from django.contrib.auth.models import User

# Create your models here.

# class User(AbstractUser):
#     image = models.ImageField(upload_to='users/', blank=True)


class Profile(models.Model):
    user = models.OneToOneField(User, related_name='profile', on_delete=models.CASCADE)
    img = models.ImageField(upload_to='profile/', default='profile/default.png')

    def __str__(self) -> str:
        return self.user.username