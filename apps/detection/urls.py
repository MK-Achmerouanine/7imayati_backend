from django.contrib import admin
from django.urls import path
from .views import PictureViewSet

urlpatterns = [
    path('upload/', PictureViewSet.as_view(), name='upload-pictures'),
]
