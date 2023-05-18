from django.urls import path
from home.views import * #index, single

# 127.0.0.1:8000

urlpatterns = [
   path('', index, name = 'index'),
   path('<slug:slug>', index, name = 'index_categories'),

   path('about/', about, name = 'about'),

   path('stories/', stories, name = 'stories'),
   path('stories/<slug:slug>/', stories, name = 'stories_categories'),

   path('recipes/', recipes, name = 'recipes'),
   path('single/<slug:slug>', single, name = 'single'),
   path('subcribe/', subcribe, name = 'subcribe')
]