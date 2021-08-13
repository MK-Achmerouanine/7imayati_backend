from rest_framework.generics import ListAPIView
from django.http import HttpResponse
from .models import Picture
from .serializers import PictureSerializer
import json

class PictureViewSet(ListAPIView):
    queryset = Picture.objects.all()
    serializer_class = PictureSerializer

    def post(self, request, *args, **kwargs):
        file = request.data['file']
        image = Picture.objects.create(image=file)
        return HttpResponse(json.dumps({'message': "Uploaded"}), status=200)