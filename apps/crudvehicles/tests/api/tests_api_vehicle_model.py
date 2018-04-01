from django.test import TestCase
from apps.crudvehicles.models import VehicleModel, AutoMaker
from apps.crudvehicles.choices import ModelsTypesChoices
from apps.crudvehicles.serializers import VehicleModelSerializer
from django.urls import reverse
from rest_framework import status
from django.utils.http import urlencode
import json
from annoying.functions import get_object_or_None


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

        self.objects_filter_engine_lte = VehicleModel.objects.filter(
            engine__lte=1.2)

        self.objects_filter_engine_gte = VehicleModel.objects.filter(
            engine__gte=1.2)

    def test_list_vehicle_model(self):
        url = reverse('vehicles:VehicleModel-list')
        response = self.client.get(url)
        vehicle_model = self.objects_list
        serializer = VehicleModelSerializer(vehicle_model, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_filter_vehicle_model(self):
        url = reverse('vehicles:VehicleModel-list')

        query = urlencode({
            'name__contains': 'Clio'
        })

        url = '{}?{}'.format(url, query)
        response = self.client.get(url)
        vehicle_model = self.objects_filter
        serializer = VehicleModelSerializer(vehicle_model, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_vehicle_model(self):
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
            'engine__lte': 1.2
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
            'engine__gte': 1.2
        })

        url = '{}?{}'.format(url, query)
        response = self.client.get(url)
        vehicle_model = self.objects_filter_engine_gte
        serializer = VehicleModelSerializer(vehicle_model, many=True)

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
        self.objects_filter_engine_lte = VehicleModel.objects.filter(
            engine__lte=1.2)

        self.objects_filter_engine_gte = VehicleModel.objects.filter(
            engine__gte=1.2)

    def test_list_vehicle_model(self):
        url = reverse('vehicles:VehicleModel-list')
        response = self.client.get(url)
        vehicle_model = self.objects_list
        serializer = VehicleModelSerializer(vehicle_model, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_filter_vehicle_model(self):
        url = reverse('vehicles:VehicleModel-list')

        query = urlencode({
            'name__contains': 'Clio'
        })

        url = '{}?{}'.format(url, query)
        response = self.client.get(url)
        vehicle_model = self.objects_filter
        serializer = VehicleModelSerializer(vehicle_model, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)

    def test_get_vehicle_model(self):
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
            'engine__lte': 1.2
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
            'engine__gte': 1.2
        })

        url = '{}?{}'.format(url, query)
        response = self.client.get(url)
        vehicle_model = self.objects_filter_engine_gte
        serializer = VehicleModelSerializer(vehicle_model, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)


class TestVehicleModelCreateApi(TestCase):

    def setUp(self):
        self.auto_maker = AutoMaker.objects.create(
            name='Honda'
        )

    def test_create_vehicle_model_car(self):

        data = {
            'name': 'Civic',
            'model': ModelsTypesChoices.car.id,
            'engine': 1.0,
            'automaker': self.auto_maker.pk
        }

        url = reverse('vehicles:VehicleModel-list')

        response = self.client.post(url, data=data)

        vehicle_model = VehicleModel.objects.get(name=data.get('name'))
        serializer = VehicleModelSerializer(vehicle_model)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, serializer.data)

    def test_create_vehicle_model_motorcycle(self):

        data = {
            'name': 'CG',
            'model': ModelsTypesChoices.motorcycle.id,
            'engine': 150,
            'automaker': self.auto_maker.pk
        }

        url = reverse('vehicles:VehicleModel-list')

        response = self.client.post(url, data=data)

        vehicle_model = VehicleModel.objects.get(name=data.get('name'))
        serializer = VehicleModelSerializer(vehicle_model)

        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(response.data, serializer.data)


class TestVehicleModelUpdateApi(TestCase):

    def setUp(self):
        auto_maker = AutoMaker.objects.create(
            name='Honda'
        )

        self.auto_maker_update = AutoMaker.objects.create(
            name='yamaha'
        )

        self.model_car_update = VehicleModel.objects.create(
            name='Fit',
            model=ModelsTypesChoices.car,
            engine=1.0,
            automaker=auto_maker
        )

        self.model_motorcycle_update = VehicleModel.objects.create(
            name='Biz',
            model=ModelsTypesChoices.motorcycle,
            engine=150,
            automaker=auto_maker
        )

    def test_update_partial_vehicle_model(self):
        url = reverse('vehicles:VehicleModel-detail',
                      kwargs={'pk': self.model_car_update.pk})

        data = {
            'name': 'Civic',
            'engine': 2.0,
        }

        new_data = json.dumps(data)

        response = self.client.patch(
            url, data=new_data, content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        vehicle_model = VehicleModel.objects.get(name=data.get('name'))
        serializer = VehicleModelSerializer(vehicle_model)

        self.assertEqual(response.data, serializer.data)

    def test_update_vehicle_model(self):
        url = reverse('vehicles:VehicleModel-detail',
                      kwargs={'pk': self.model_car_update.pk})

        data = {
            'name': 'Fazer',
            'engine': 250,
            'model': ModelsTypesChoices.motorcycle.id,
            'automaker': self.auto_maker_update.id
        }

        new_data = json.dumps(data)

        response = self.client.patch(
            url, data=new_data, content_type='application/json')

        self.assertEqual(response.status_code, status.HTTP_200_OK)

        vehicle_model = VehicleModel.objects.get(name=data.get('name'))
        serializer = VehicleModelSerializer(vehicle_model)

        self.assertEqual(response.data, serializer.data)


class TestVehicleModelDeleteApi(TestCase):

    def setUp(self):
        auto_maker = AutoMaker.objects.create(
            name='Honda'
        )

        self.model_car_delete = VehicleModel.objects.create(
            name='Fit',
            model=ModelsTypesChoices.car,
            engine=1.0,
            automaker=auto_maker
        )

        self.model_motorcycle_delete = VehicleModel.objects.create(
            name='Biz',
            model=ModelsTypesChoices.motorcycle,
            engine=150,
            automaker=auto_maker
        )

    def test_update_vehicle_model_car(self):

        url = reverse('vehicles:VehicleModel-detail',
                      kwargs={'pk': self.model_car_delete.pk})

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        vehicle_model = get_object_or_None(
            VehicleModel, id=self.model_car_delete.pk)
        self.assertEqual(None, vehicle_model)

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)

    def test_update_vehicle_model_motorcyle(self):

        url = reverse('vehicles:VehicleModel-detail',
                      kwargs={'pk': self.model_motorcycle_delete.pk})

        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)

        vehicle_model = get_object_or_None(
            VehicleModel, id=self.model_motorcycle_delete.pk)
        self.assertEqual(None, vehicle_model)

        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
