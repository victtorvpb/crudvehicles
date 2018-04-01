from django.test import TestCase
from apps.crudvehicles.models import VehicleModel, AutoMaker, Vehicle
from apps.crudvehicles.choices import ModelsTypesChoices
from apps.crudvehicles.serializers import VehicleModelSerializer
from django.urls import reverse
from rest_framework import status
from django.utils.http import urlencode
import json
from annoying.functions import get_object_or_None


class TestVehicleModelListApi(TestCase):
    def setUp(self):

        auto_maker = AutoMaker.objects.create(
            name='Renault'
        )
        vehicle_model = VehicleModel.objects.create(
            name='Clio',
            model=ModelsTypesChoices.motorcycle,
            engine=i*1.2,
            automaker=auto_maker,
        )

        for i in range(1, 4):
            Vehicle.objects.create(
                color='Branco',
                mileage=i*100
            )

        Vehicle.objects.create(
            color='Preto',
            mileage=1300
        )

        self.objects_list = Vehicle.objects.all()
        self.objects_filter_name = Vehicle.objects.filter(
            vehicle_model__name__contains='Clio')

        self.objects_filter_color = Vehicle.objects.filter(
            color__contains='Branco')

        self.objects_filter_engine_lte = VehicleModel.objects.filter(
            vehicle_model__engine__lte=1.2)

        self.objects_filter_engine_gte = VehicleModel.objects.filter(
            vehicle_model__engine__gte=1.2)

    def test_list_vehicle(self):
        url = reverse('vehicles:VehicleModel-list')
        response = self.client.get(url)
        vehicle_model = self.objects_list
        serializer = VehicleModelSerializer(vehicle_model, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_filter_vehicle_name(self):
        url = reverse('vehicles:VehicleModel-list')

        query = urlencode({
            'vehicle_model__name__contains': 'Clio'
        })

        url = '{}?{}'.format(url, query)
        response = self.client.get(url)
        vehicle_model = self.objects_filter_name
        serializer = VehicleModelSerializer(vehicle_model, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_filter_vehicle_color(self):
        url = reverse('vehicles:VehicleModel-list')

        query = urlencode({
            'color__contains': 'Branco'
        })

        url = '{}?{}'.format(url, query)
        response = self.client.get(url)
        vehicle_model = self.objects_filter_color
        serializer = VehicleModelSerializer(vehicle_model, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_vehicle(self):
        url = reverse('vehicles:VehicleModel-detail',
                      kwargs={'pk': self.object_get.pk})

        response = self.client.get(url)
        vehicle_model = self.object_get
        serializer = VehicleModelSerializer(vehicle_model)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_filter_engine_less(self):
        url = reverse('vehicles:VehicleModel-list')
        query = urlencode({
            'vehicle_model__engine__lte': 1.2
        })

        url = '{}?{}'.format(url, query)
        response = self.client.get(url)
        vehicle_model = self.objects_filter_engine_lte
        serializer = VehicleModelSerializer(vehicle_model, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_filter_engine_greater(self):
        url = reverse('vehicles:VehicleModel-list')
        query = urlencode({
            'vehicle_model__engine__gte': 1.2
        })

        url = '{}?{}'.format(url, query)
        response = self.client.get(url)
        vehicle_model = self.objects_filter_engine_gte
        serializer = VehicleModelSerializer(vehicle_model, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
