import json
from django.core.management.base import BaseCommand
from PhotosManagerAPI.Rest_API.serializers import WriteOnlySerializer


class Command(BaseCommand):
    def add_arguments(self, parser):
        parser.add_argument('json_file', type=str, help='Insert JSON file name.')

    def handle(self, *args, **kwargs):
        json_file = kwargs['json_file']
        with open(json_file, 'r') as file:
            request = json.load(file)
            serializer = WriteOnlySerializer(data=request, many=True)
            if serializer.is_valid(raise_exception=True):
                serializer.save()
                return "Import from JSON file finished successfully."
