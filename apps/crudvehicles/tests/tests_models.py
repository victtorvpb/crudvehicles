from django.test import TestCase

from apps.crudvehicles.models import AutoMaker, VehicleModel,\
    Vehicle
from apps.crudvehicles.choices import ModelsTypesChoices


class TestModels(TestCase):
    '''
        Test all models off app crudvehicles
    '''

    def setUp(self):

        self.auto_maker = AutoMaker.objects.create(
            name='Honda'
        )

        self.vehicle_model_car = VehicleModel.objects.create(
            model=ModelsTypesChoices.car,
            engine=1.0,
            automaker=self.auto_maker
        )

        self.vehicle_model_motorcycle = VehicleModel.objects.create(
            model=ModelsTypesChoices.motorcycle,
            engine=150,
            automaker=self.auto_maker
        )

        self.vehicle_motorcycle = Vehicle.objects.create(
            name='CG',
            color='Black',
            model=self.vehicle_model_motorcycle,
        )

        self.vehicle_car = Vehicle.objects.create(
            name='Civic',
            color='Red',
            model=self.vehicle_model_car,
        )

    def test_insert_model_auto_maker(self):

        self.assertEqual(self.auto_maker.name, 'Honda')

    def test_insert_model_vehicle_model_car(self):

        self.assertEqual(self.vehicle_model_car.engine, 1.0)
        self.assertEqual(self.vehicle_model_car.model, ModelsTypesChoices.car)

    def test_insert_model_vehicle_model_motorcycle(self):

        self.assertEqual(self.vehicle_model_motorcycle.engine, 150)
        self.assertEqual(self.vehicle_model_motorcycle.model,
                         ModelsTypesChoices.motorcycle)

    def test_insert_vehicle_motorcycle(self):

        self.assertEqual(self.vehicle_motorcycle.name, 'CG')
        self.assertEqual(self.vehicle_motorcycle.color, 'Black')
        self.assertEqual(self.vehicle_motorcycle.model,
                         self.vehicle_model_motorcycle)

    def test_insert_vehicle_car(self):

        self.assertEqual(self.vehicle_car.name, 'Civic')
        self.assertEqual(self.vehicle_car.color, 'Red')
        self.assertEqual(self.vehicle_car.model, self.vehicle_model_car)
    
