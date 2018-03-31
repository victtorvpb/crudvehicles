from django.test import TestCase

from apps.crudvehicles.models import AutoMaker


class TestModels(TestCase):
    '''
        Test all models off app crudvehicles
    '''

    def setUp(self):

        self.auto_maker = AutoMaker.objects.create(
            name='Ford'
        )

    def test_insert_model_auto_maker(self):

        self.assertEqual(self.auto_maker.name, 'Ford')