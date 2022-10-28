from django.contrib.auth.models import User
from django.urls import reverse
from ..serializers import PhotoSerializer
from ..models import Photo
from rest_framework.test import APITestCase, APIClient
from rest_framework import status


class TestPhotoListCreate(APITestCase):
    def setUp(self):
        self.photo_attributes = {'title': 'Model Test object 5',
                                 'albumId': 2004,
                                 'url': 'https://via.placeholder.com/600/92c952'
                                 }

        self.photo = Photo.objects.create(**self.photo_attributes)
        self.serializer = PhotoSerializer(instance=self.photo)

        self.password = '123456'
        self.my_user = User.objects.create_superuser('myuser', 'myemail@test.com', password=self.password)

        client = APIClient()

    def test_create_photo_failure(self):
        data = self.serializer.data
        response = self.client.post(reverse('photo_rest_api'), data)

        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_create_photo(self):
        self.quantity_of_photos = Photo.objects.all().count()
        self.client.login(username=self.my_user.username, password=self.password)
        data = self.serializer.data
        response = self.client.post(reverse('photo_rest_api'), data)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(data['title'], 'Model Test object 5')
        self.assertEqual(data['albumId'], 2004)
        self.assertEqual(data['url'], 'https://via.placeholder.com/600/92c952')
        self.assertEqual(self.quantity_of_photos, 1)

    def test_retrieve_all_photos(self):
        self.quantity_of_photos = Photo.objects.all().count()
        self.client.login(username=self.my_user.username, password=self.password)
        response = self.client.get(reverse('photo_rest_api'))
        self.photos_amount = len(response.json())

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertIsInstance(response.json(), list)
        self.assertEqual(self.photos_amount, self.quantity_of_photos)
        self.assertEqual(response.json()[0]['title'], 'Model Test object 5')
        self.assertEqual(response.json()[0]['albumId'], 2004)
        self.assertEqual(response.json()[0]['url'], 'https://via.placeholder.com/600/92c952')


class TestPhotoRetrieveUpdateDestroyAPIView(APITestCase):
    def setUp(self):
        self.photo_attributes = {'title': 'Model Test object 6',
                                 'albumId': 2005,
                                 'url': 'https://via.placeholder.com/600/92c952'
                                 }

        self.photo = Photo.objects.create(**self.photo_attributes)
        self.serializer = PhotoSerializer(instance=self.photo)

        self.password = '123456'
        self.my_user = User.objects.create_superuser('myuser', 'myemail@test.com', password=self.password)

        client = APIClient()

    def test_retrieve_single_photo(self):
        data = self.serializer.data
        self.client.login(username=self.my_user.username, password=self.password)
        response = self.client.get(reverse('photo_rest_api', kwargs={'uuid': data['uuid']}))
        photo = Photo.objects.get(uuid=response.json()['uuid'])

        self.assertEqual(photo.title, response.data['title'])
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_update_photo(self):
        data = self.serializer.data
        self.client.login(username=self.my_user.username, password=self.password)
        response = self.client.patch(
            reverse('photo_rest_api', kwargs={'uuid': data['uuid']}), {
                "title": "New Model Test name",
                'albumId': 3005
            })

        updated_photo = Photo.objects.get(uuid=response.json()['uuid'])

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(updated_photo.title, "New Model Test name")
        self.assertEqual(updated_photo.albumId, 3005)

    def test_delete_photo(self):
        data = self.serializer.data
        self.client.login(username=self.my_user.username, password=self.password)
        objects_in_db = Photo.objects.all().count()

        self.assertGreater(objects_in_db, 0)
        self.assertEqual(objects_in_db, 1)

        response = self.client.delete(
            reverse('photo_rest_api', kwargs={'uuid': data['uuid']}))
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        self.assertEqual(Photo.objects.all().count(), 0)
