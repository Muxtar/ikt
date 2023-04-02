from django.db import models
# from django.contrib.auth.models import User
from django.contrib.auth import get_user_model

User = get_user_model()


# Create your models here.

class Base(models.Model):
    create_date = models.DateTimeField(auto_now_add=True)
    update_date = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True


class Categorie(Base):
    name = models.CharField(max_length=30, unique=True)
    image = models.ImageField(upload_to='images/categories')

    def __str__(self) -> str:
        return self.name    

class Tag(Base):
    name = models.CharField(max_length=30)

    def __str__(self) -> str:
        return self.name
    
class Storie(Base):
    category = models.ForeignKey(Categorie, related_name='story', on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag, related_name='story', blank=True)

    title = models.CharField(max_length=50)
    image = models.ImageField(upload_to='stories/images')
    cover_image = models.ImageField(upload_to='stories/cover')
    desc =  models.TextField()

    def __str__(self) -> str:
        return self.title


class Comment(Base):
    user = models.ForeignKey(User, related_name='comment', on_delete=models.CASCADE)
    storie = models.ForeignKey(Storie, related_name='storie_comment', on_delete=models.CASCADE)
    incomment = models.ForeignKey('self', related_name='incomments', null=True, blank=True, on_delete=models.CASCADE)
    comment = models.TextField()

    def __str__(self) -> str:
        return self.comment[:20]