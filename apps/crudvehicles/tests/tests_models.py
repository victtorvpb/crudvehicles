from django.test import TestCase

from apps.crudvehicles.models import AutoMaker, VehicleModel
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
            name='Civic',
            model=ModelsTypesChoices.car,
            engine=1.0,
            automaker=self.auto_maker
        )

        self.vehicle_model_car = VehicleModel.objects.create(
            name='CG',
            model=ModelsTypesChoices.car,
            engine=150,
            automaker=self.auto_maker
        )

    def test_insert_model_auto_maker(self):

        self.assertEqual(self.auto_maker.name, 'Ford')

    def test_insert_model_vehicle_model_car(self):

        self.assertEqual(self.auto_maker.name, 'Civic')
        self.assertEqual(self.auto_maker.engine, 1.0)
        self.assertEqual(self.auto_maker.model, ModelsTypesChoices.car)

    def test_insert_model_vehicle_model_motorcycle(self):

        self.assertEqual(self.auto_maker.name, 'CG')
        self.assertEqual(self.auto_maker.engine, 150)
        self.assertEqual(self.auto_maker.model, ModelsTypesChoices.motorcycle)
