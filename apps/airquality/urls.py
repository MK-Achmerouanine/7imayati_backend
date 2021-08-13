from django.contrib import admin
from django.urls import path
from .views import AirQualityViewSet
urlpatterns = [
    path('', AirQualityViewSet.as_view(), name="quality_list" ),
]
