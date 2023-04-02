from django.contrib import admin
from home.models import Categorie, Tag, Storie,Comment

# Register your models here.

@admin.register(Storie)
class StorieAdmin(admin.ModelAdmin):
    fields = ['title', 'image', 'cover_image', 'category', 
              'tag', 'desc']
    
    search_fields = ['category__name', 'tag__name', 'title']
    list_filter = ['category', 'tag']    
    
admin.site.register([Categorie, Tag, Comment])