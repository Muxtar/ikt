from django.urls import path
from home.views import index, single

# 127.0.0.1:8000

urlpatterns = [
   path('', index, name = 'index'),
   path('single/<int:id>', single, name = 'single')
]