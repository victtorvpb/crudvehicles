from django.test import TestCase
from apps.crudvehicles.models import VehicleModel, AutoMaker
from apps.crudvehicles.choices import ModelsTypesChoices
from apps.crudvehicles.serializers import VehicleModelSerializer
from django.urls import reverse
from rest_framework import status
from django.utils.http import urlencode

class TestVehicleModelMotorcycleListApi(TestCase):
    def setUp(self):

        for i in range(1, 4):
            auto_maker = AutoMaker.objects.create(
                name='Renault {}'.format(i))

            VehicleModel.objects.create(
                name='Clio {}'.format(i),
                model=ModelsTypesChoices.motorcycle,
                engine=i*1.2,
                automaker=auto_maker,
            )

        auto_maker = AutoMaker.objects.create(
            name='Ford'
        )

        self.object_get = VehicleModel.objects.create(
            name='Ka',
            model=ModelsTypesChoices.motorcycle,
            engine=1.0,
            automaker=auto_maker
        )

        self.objects_list = VehicleModel.objects.all()
        self.objects_filter = VehicleModel.objects.filter(
            name__contains='Clio')

    def test_list_vehicle_model(self):
        url = reverse('vehicles:VehicleModel-list')
        response = self.client.get(url)
        vehicle_model = self.objects_list
        serializer = VehicleModelSerializer(vehicle_model, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_filter_vehicle_mode(self):
        url = reverse('vehicles:VehicleModel-list')

        query = urlencode({
            'name__contains': 'Clio'
        })

        url = '{}?{}'.format(url, query)
        response = self.client.get(url)
        vehicle_mode = self.objects_filter
        serializer = VehicleModelSerializer(vehicle_mode, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_vehicle_mode(self):
        url = reverse('vehicles:VehicleModel-detail',
                      kwargs={'pk': self.object_get.pk})

        response = self.client.get(url)
        vehicle_mode = self.object_get
        serializer = VehicleModelSerializer(vehicle_mode)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

class TestVehicleModelCarListApi(TestCase):
    def setUp(self):

        for i in range(1, 4):
            auto_maker = AutoMaker.objects.create(
                name='Renault {}'.format(i))

            VehicleModel.objects.create(
                name='Clio {}'.format(i),
                model=ModelsTypesChoices.car,
                engine=i*1.2,
                automaker=auto_maker,
            )

        auto_maker = AutoMaker.objects.create(
            name='Ford'
        )

        self.object_get = VehicleModel.objects.create(
            name='Ka',
            model=ModelsTypesChoices.car,
            engine=1.0,
            automaker=auto_maker
        )

        self.objects_list = VehicleModel.objects.all()
        self.objects_filter = VehicleModel.objects.filter(
            name__contains='Clio')

    def test_list_vehicle_model(self):
        url = reverse('vehicles:VehicleModel-list')
        response = self.client.get(url)
        vehicle_model = self.objects_list
        serializer = VehicleModelSerializer(vehicle_model, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_filter_vehicle_mode(self):
        url = reverse('vehicles:VehicleModel-list')

        query = urlencode({
            'name__contains': 'Clio'
        })

        url = '{}?{}'.format(url, query)
        response = self.client.get(url)
        vehicle_mode = self.objects_filter
        serializer = VehicleModelSerializer(vehicle_mode, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_vehicle_mode(self):
        url = reverse('vehicles:VehicleModel-detail',
                      kwargs={'pk': self.object_get.pk})

        response = self.client.get(url)
        vehicle_mode = self.object_get
        serializer = VehicleModelSerializer(vehicle_mode)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

