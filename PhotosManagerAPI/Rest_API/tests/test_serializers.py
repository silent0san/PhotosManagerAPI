from django.test import TestCase
from ..serializers import PhotoSerializer, WriteOnlySerializer
from ..models import Photo


class PhotoSerializerTestCase(TestCase):
    def setUp(self):
        self.photo_attributes = {'title': 'Model Test object 3',
                                 'albumId': 2002,
                                 'url': 'https://via.placeholder.com/600/92c952'
                                 }

        self.photo = Photo.objects.create(**self.photo_attributes)
        self.serializer = PhotoSerializer(instance=self.photo)

    def test_contains_expected_fields(self):
        data = self.serializer.data

        self.assertCountEqual(data.keys(), ['uuid', 'title', 'albumId', 'width', 'height', 'dominant_color', 'url'])

    def test_dominant_color_field_content(self):
        data = self.serializer.data

        self.assertEqual(data['dominant_color'], '92c952')

    def test_width_height_field_content(self):
        data = self.serializer.data

        self.assertEqual(data['width'], 600)
        self.assertEqual(data['height'], 600)


class WriteOnlySerializerTestCase(TestCase):
    def setUp(self):
        self.photo_attributes = {'title': 'Model Test object 4',
                                 'albumId': 2003,
                                 'url': 'https://via.placeholder.com/600/92c952'
                                 }

        self.photo = Photo.objects.create(**self.photo_attributes)
        self.serializer = WriteOnlySerializer(instance=self.photo)

    def test_contains_expected_fields(self):
        data = self.serializer.data

        self.assertCountEqual(data.keys(), ['title', 'albumId', 'url'])
