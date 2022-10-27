from django.core.management.base import BaseCommand
from PhotosManagerAPI.Rest_API.serializers import WriteOnlySerializer
import requests


class Command(BaseCommand):
    def handle(self, *args, **options):
        api_url = 'https://jsonplaceholder.typicode.com/photos'

        json_data = requests.get(api_url).json()
        serializer = WriteOnlySerializer(data=json_data, many=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
