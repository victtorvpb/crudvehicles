from django.test import TestCase
from apps.crudvehicles.models import AutoMaker
from apps.crudvehicles.serializers import AutoMakerSerializer
from django.core.urlresolvers import reverse
from rest_framework import status


class TestAutoMakerApi(TestCase):
    def setUp(self):
        for i in range(1, 4):
            self.automaker_list = AutoMaker.objects.create(
                name='AutoMaker {}'.format(i))

    def tes_list_auto_maker(self):
        url = reverse('crudvehicles.AutoMaker-list')
        response = self.client.get(url)
        auto_maker = AutoMaker.objects.all()
        serializer = AutoMakerSerializer(auto_maker, many=True)

        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data, serializer.data)
