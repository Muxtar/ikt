from django.contrib import admin
from home.models import Categorie, Tag, Storie, Comment, Subcribe

# Register your models here.

@admin.register(Storie)
class StorieAdmin(admin.ModelAdmin):
    fields = ['user', 'category', 'image', 'cover_image', 'tag', 'title', 'desc', 'slug']
    
    # search_fields = ['category__name', 'title']
    # list_filter = ['category']    
    

@admin.register(Tag)
class TagAdmin(admin.ModelAdmin):
    fields = ['name']


admin.site.register([Categorie, Comment, Subcribe])