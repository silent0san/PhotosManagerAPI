from rest_framework import serializers
from .models import Photo


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['uuid', 'title', 'albumId', 'width', 'height', 'dominant_color', 'url']
        read_only_fields = ['width', 'height', 'dominant_color']


class WriteOnlySerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['title', 'albumId', 'url']
