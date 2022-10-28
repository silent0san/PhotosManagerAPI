from django.core.management.base import BaseCommand
from PhotosManagerAPI.Rest_API.serializers import WriteOnlySerializer
import requests


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('api_url', type=str, help='Insert API url.')

    def handle(self, *args, **kwargs):
        api_url = kwargs['api_url']

        json_data = requests.get(api_url).json()
        serializer = WriteOnlySerializer(data=json_data, many=True)
        if serializer.is_valid(raise_exception=True):
            serializer.save()
            return "Import from API finished successfully."
