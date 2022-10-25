from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView
)
from rest_framework.permissions import IsAuthenticated
from .models import Photo
from .serializers import PhotoSerializer


class PhotoListCreateAPIView(ListCreateAPIView):
    queryset = Photo.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = PhotoSerializer
    lookup_field = 'uuid'


class PhotoRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Photo.objects.all()
    permission_classes = (IsAuthenticated,)
    serializer_class = PhotoSerializer
    lookup_field = 'uuid'

