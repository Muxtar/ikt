from django.urls import path
from home.api.views import CategoryView

urlpatterns = [
    path('category/', CategoryView.as_view(), name = 'category-api')
]