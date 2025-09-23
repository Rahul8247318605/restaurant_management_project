from django.urls import path
from .views import MenuCategoryListAPIView

urlpatterns = [
    path('categories/', MenuCategoryListAPIView.as_view(), name='category-list'),
]