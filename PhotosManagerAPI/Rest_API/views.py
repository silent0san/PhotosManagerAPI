import requests
from rest_framework import status
from rest_framework.generics import (
    ListCreateAPIView,
    RetrieveUpdateDestroyAPIView,
    GenericAPIView)
from rest_framework.mixins import CreateModelMixin
from rest_framework.response import Response

from .models import Photo
from .serializers import PhotoSerializer, WriteOnlySerializer


class PhotoListCreateAPIView(ListCreateAPIView):
    queryset = Photo.objects.all()
    paginate_by = 50
    serializer_class = PhotoSerializer
    lookup_field = 'uuid'


class PhotoRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Photo.objects.all()
    serializer_class = PhotoSerializer
    lookup_field = 'uuid'


class PhotoImportAPIViewFromJson(CreateModelMixin, GenericAPIView):
    """
    Concrete view for creating a model instance from JSON.
    """

    def post(self, request, *args, **kwargs):
        listed_data = request.data
        if listed_data is not list:
            listed_data = list(listed_data)

        serializer = WriteOnlySerializer(data=request.data, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({'Added objects': len(serializer.data)}, status=status.HTTP_201_CREATED)


class PhotoImportAPIViewFromUrl(CreateModelMixin, GenericAPIView):
    """
    Concrete view for creating a model instance from API Url.
    """
    def post(self, request, *args, **kwargs):
        if 'api_url' in request.data.keys():
            response = requests.get(request.data["api_url"]).json()
            return self.create(response, *args, **kwargs)

    def create(self, request, *args, **kwargs):
        serializer = WriteOnlySerializer(data=request, many=True)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        return Response({'Added objects': len(serializer.data)}, status=status.HTTP_201_CREATED)
