from django.urls import path
from home.views import index

# 127.0.0.1:8000

urlpatterns = [
   path('', index),
]