from django.test import TestCase
from apps.crudvehicles.models import VehicleModel, AutoMaker, Vehicle
from apps.crudvehicles.choices import ModelsTypesChoices
from apps.crudvehicles.serializers import VehicleSerializer
from django.urls import reverse
from rest_framework import status
from django.utils.http import urlencode
import json
from annoying.functions import get_object_or_None


class TestVehicleListApi(TestCase):
    def setUp(self):

        auto_maker = AutoMaker.objects.create(
            name='Renault'
        )
        vehicle_model = VehicleModel.objects.create(
            name='Clio',
            model=ModelsTypesChoices.motorcycle,
            engine=1.2,
            automaker=auto_maker,
        )

        for i in range(1, 4):

            Vehicle.objects.create(
                model=vehicle_model,
                color='Branco',
                mileage=i*100
            )

        self.object_get = Vehicle.objects.create(
            model=vehicle_model,
            color='Preto',
            mileage=1300
        )

        self.objects_list = Vehicle.objects.all()
        # import pdb; pdb.set_trace()
        self.objects_filter_name = Vehicle.objects.filter(
            model__name__contains='Clio')

        self.objects_filter_color = Vehicle.objects.filter(
            color__contains='Branco')

        self.objects_filter_engine_lte = Vehicle.objects.filter(
            model__engine__lte=1.2)

        self.objects_filter_engine_gte = Vehicle.objects.filter(
            model__engine__gte=1.2)

        self.objects_filter_mileage_lte = Vehicle.objects.filter(
            mileage__lte=100)

        self.objects_filter_mileage_gte = Vehicle.objects.filter(
            mileage__gte=200)

    def test_list_vehicle(self):
        url = reverse('vehicles:Vehicle-list')
        response = self.client.get(url)
        vehicle_model = self.objects_list
        serializer = VehicleSerializer(vehicle_model, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_filter_vehicle_name(self):
        url = reverse('vehicles:Vehicle-list')

        query = urlencode({
            'model__name__contains': 'Clio'
        })

        url = '{}?{}'.format(url, query)
        response = self.client.get(url)
        vehicle_model = self.objects_filter_name
        serializer = VehicleSerializer(vehicle_model, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_filter_vehicle_color(self):
        url = reverse('vehicles:Vehicle-list')

        query = urlencode({
            'color__contains': 'Branco'
        })

        url = '{}?{}'.format(url, query)
        response = self.client.get(url)
        vehicle_model = self.objects_filter_color
        serializer = VehicleSerializer(vehicle_model, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_vehicle(self):
        url = reverse('vehicles:Vehicle-detail',
                      kwargs={'pk': self.object_get.pk})

        response = self.client.get(url)
        vehicle_model = self.object_get
        serializer = VehicleSerializer(vehicle_model)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_filter_engine_less(self):
        url = reverse('vehicles:Vehicle-list')
        query = urlencode({
            'model__engine__lte': 1.2
        })

        url = '{}?{}'.format(url, query)
        response = self.client.get(url)
        vehicle_model = self.objects_filter_engine_lte
        serializer = VehicleSerializer(vehicle_model, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_filter_engine_greater(self):
        url = reverse('vehicles:Vehicle-list')
        query = urlencode({
            'model__engine__gte': 1.2
        })

        url = '{}?{}'.format(url, query)
        response = self.client.get(url)
        vehicle_model = self.objects_filter_engine_gte
        serializer = VehicleSerializer(vehicle_model, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_filter_mileage_less(self):
        url = reverse('vehicles:Vehicle-list')
        query = urlencode({
            'mileage__lte': 100
        })

        url = '{}?{}'.format(url, query)
        response = self.client.get(url)
        vehicle_model = self.objects_filter_mileage_lte
        serializer = VehicleSerializer(vehicle_model, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_filter_mileage_greater(self):
        url = reverse('vehicles:Vehicle-list')
        query = urlencode({
            'mileage__gte': 200
        })

        url = '{}?{}'.format(url, query)
        response = self.client.get(url)
        vehicle_model = self.objects_filter_mileage_gte
        serializer = VehicleSerializer(vehicle_model, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)


class TestVehicleCreateApi(TestCase):

    def setUp(self):
        auto_maker = AutoMaker.objects.create(
            name='Renault'
        )
        self.vehicle_model = VehicleModel.objects.create(
            name='Clio',
            model=ModelsTypesChoices.motorcycle,
            engine=1.2,
            automaker=auto_maker,
        )

    def test_create_vehicle(self):

        data = {
            'color': 'red',
            'model': self.vehicle_model.id,
            'mileage': 3000,
        }

        url = reverse('vehicles:Vehicle-list')

        response = self.client.post(url, data=data)

        vehicle = Vehicle.objects.get(color=data.get(
            'color'), model=self.vehicle_model, mileage=data.get('mileage'))
        serializer = VehicleSerializer(vehicle)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, serializer.data)


class TestVehicleUpdateApi(TestCase):

    def setUp(self):
        auto_maker = AutoMaker.objects.create(
            name='Renault'
        )
        vehicle_model = VehicleModel.objects.create(
            name='Clio',
            model=ModelsTypesChoices.motorcycle,
            engine=1.2,
            automaker=auto_maker,
        )

        self.vehicle_update = Vehicle.objects.create(
            model=vehicle_model,
            color='Preto',
            mileage=1300
        )

    def test_update_vehicle(self):

        url = reverse('vehicles:Vehicle-detail',
                      kwargs={'pk': self.vehicle_update.pk})

        data = {
            'color': 'Blanco',
            'mileage': 5000,
        }

        new_data = json.dumps(data)

        response = self.client.patch(
            url, data=new_data, content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        vehicle = Vehicle.objects.get(
            color=data.get('color'),
            mileage=data.get('mileage')
        )
        serializer = VehicleSerializer(vehicle)
        self.assertEqual(response.data, serializer.data)


class TestVehicleDeleteApi(TestCase):

    def setUp(self):
        auto_maker = AutoMaker.objects.create(
            name='Renault'
        )
        vehicle_model = VehicleModel.objects.create(
            name='Clio',
            model=ModelsTypesChoices.motorcycle,
            engine=1.2,
            automaker=auto_maker,
        )

        self.vehicle_delete = Vehicle.objects.create(
            model=vehicle_model,
            color='Preto',
            mileage=1300
        )
    
    def test_delete_vehicle(self):

        url = reverse('vehicles:Vehicle-detail',
                      kwargs={'pk': self.vehicle_delete.pk})

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        vehicle = get_object_or_None(
            Vehicle, id=self.vehicle_delete.pk)
        self.assertEqual(None, vehicle)

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)