from rest_framework.generics import ListAPIView
from django.http import HttpResponse
from .models import AirQuality
from .serializers import AirQualitySerializer
import json

class AirQualityViewSet(ListAPIView):
    queryset = AirQuality.objects.all()
    serializer_class = AirQualitySerializer