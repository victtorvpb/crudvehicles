from django.test import TestCase
from apps.crudvehicles.models import AutoMaker
from apps.crudvehicles.serializers import AutoMakerSerializer
from django.urls import reverse
from rest_framework import status
from django.utils.http import urlencode


class TestAutoMakerListApi(TestCase):
    def setUp(self):

        print('---------------------------')
        for i in range(1, 4):
            AutoMaker.objects.create(
                name='Renault {}'.format(i))

        AutoMaker.objects.create(
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
