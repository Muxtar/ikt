from django.urls import path
from home.api.views import *

urlpatterns = [
    path('tag/', tagView, name = 'tag-view'),
    path('tag/<int:id>/', tagViewId, name = 'tag-view-id'),
    path('stories/', StorieViewApi.as_view(), name = 'stories-api'),
    path('stories/<int:id>/', StorieViewApiId.as_view(), name = 'stories-api-id'),

    path('category/', CategoryView.as_view(), name = 'category')

]