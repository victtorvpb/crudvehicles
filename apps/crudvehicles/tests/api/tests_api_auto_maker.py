from django.test import TestCase
from apps.crudvehicles.models import AutoMaker
from apps.crudvehicles.serializers import AutoMakerSerializer
from django.urls import reverse
from rest_framework import status
from django.utils.http import urlencode
import json
from annoying.functions import get_object_or_None

class TestAutoMakerListApi(TestCase):
    def setUp(self):

        for i in range(1, 4):
            AutoMaker.objects.create(
                name='Renault {}'.format(i))

        self.object_get = AutoMaker.objects.create(
            name='Ford'
        )

        self.objects_list = AutoMaker.objects.all()
        self.objects_filter = AutoMaker.objects.filter(
            name__contains='Renault')

    def test_list_auto_maker(self):
        url = reverse('vehicles:AutoMaker-list')
        response = self.client.get(url)
        auto_maker = self.objects_list
        serializer = AutoMakerSerializer(auto_maker, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_filter_auto_maker(self):
        url = reverse('vehicles:AutoMaker-list')

        query = urlencode({
            'name__contains': 'Renault'
        })

        url = '{}?{}'.format(url, query)
        response = self.client.get(url)
        auto_maker = self.objects_filter
        serializer = AutoMakerSerializer(auto_maker, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_auto_maker(self):
        url = reverse('vehicles:AutoMaker-detail',
                      kwargs={'pk': self.object_get.pk})

        response = self.client.get(url)
        auto_maker = self.object_get
        serializer = AutoMakerSerializer(auto_maker)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)


class TestAutoMakerCreateApi(TestCase):

    def setUp(self):

        AutoMaker.objects.create(
            name='Ford'
        )

    def test_create_auto_maker(self):
        data = {
            "name": "Ferrari"
        }

        url = reverse('vehicles:AutoMaker-list')

        response = self.client.post(url, data=data)

        auto_maker = AutoMaker.objects.get(name=data.get('name'))
        serializer = AutoMakerSerializer(auto_maker)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, serializer.data)

    def test_create_not_unique_auto_maker(self):
        data = {
            "name": "Ford"
        }

        url = reverse('vehicles:AutoMaker-list')

        response = self.client.post(url, data=data)
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)


class TestAutoMakerUpdateApi(TestCase):

    def setUp(self):

        self.automaker_update = AutoMaker.objects.create(
            name='Ford'
        )

    def test_update_auto_maker(self):
        data = {
            "name": "Honda"
        }
        new_data = json.dumps(data)
        url = reverse('vehicles:AutoMaker-detail',
                      kwargs={'pk': self.automaker_update.pk})

        response = self.client.put(
            url, data=new_data, content_type='application/json')

        auto_maker = AutoMaker.objects.get(name=data.get('name'))
        serializer = AutoMakerSerializer(auto_maker)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)


class TestAutoMakerDeleteApi(TestCase):

    def setUp(self):

        self.automaker_delete = AutoMaker.objects.create(
            name='Ford'
        )

    def test_update_auto_maker(self):
 
        url = reverse('vehicles:AutoMaker-detail',
                      kwargs={'pk': self.automaker_delete.pk})

        response = self.client.delete(url)

        auto_maker = get_object_or_None(AutoMaker, id=self.automaker_delete.pk)
        
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(None, auto_maker)

        response = self.client.get(url)

        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
