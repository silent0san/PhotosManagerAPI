from rest_framework import serializers
from .models import Photo


class PhotoSerializer(serializers.ModelSerializer):
    class Meta:
        model = Photo
        fields = ['uuid', 'title', 'albumID', 'width', 'height', 'dominant_color']
