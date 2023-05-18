from django.db import models
# from django.contrib.auth.models import User
from django.utils.text import slugify
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
    slug = models.SlugField(blank=True, editable=False  )

    def __str__(self) -> str:
        return self.name    
    
    def save(self, *args) -> None:
        self.slug = slugify(self.name)
        return super().save(args)

class Tag(Base):
    name = models.CharField(max_length=30, unique=True)
    slug = models.SlugField(max_length=100, blank=True, null=True)

    def __str__(self) -> str:
        return self.name
    
class Storie(Base):
    category = models.ForeignKey(Categorie, related_name='story', on_delete=models.CASCADE)
    tag = models.ManyToManyField(Tag, related_name='story', blank=True)
    user = models.ForeignKey(User, related_name='story', on_delete=models.CASCADE)
    image = models.ImageField(upload_to='stories/images', null = True, blank = True)
    cover_image = models.ImageField(upload_to='stories/cover', null = True, blank = True)
    title = models.CharField(max_length=50)
    desc =  models.TextField()
    slug = models.SlugField(max_length=100, blank=True, null=True)

    def __str__(self) -> str:
        return self.title
    
    # def save(self, *args) -> None:
    #     data = '-'.join(self.title.split())
    #     self.slug = str(f"{data}-{self.id}")
    #     return super().save(args)
    
    # def save(self, *args, **kwargs) -> None:
    #     return super.save(args, kwargs)


class Comment(Base):
    user = models.ForeignKey(User, related_name='comment', on_delete=models.CASCADE)
    storie = models.ForeignKey(Storie, related_name='storie_comment', on_delete=models.CASCADE)
    incomment = models.ForeignKey('self', related_name='incomments', null=True, blank=True, on_delete=models.CASCADE)
    comment = models.TextField()

    def __str__(self) -> str:
        return self.comment[:20]

class Subcribe(Base):
    email = models.EmailField(max_length=50, unique=True)
    def __str__(self) -> str:
        return self.email