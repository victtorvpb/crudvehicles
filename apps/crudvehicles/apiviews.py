from rest_framework import viewsets
from .filtersapi import AutomMakerFilter, VehicleModelFilter
from .models import AutoMaker, VehicleModel
from .serializers import AutoMakerSerializer, VehicleModelSerializer

class AutoMakerView(viewsets.ModelViewSet):
    queryset = AutoMaker.objects.all()
    serializer_class = AutoMakerSerializer
    filter_class = AutomMakerFilter


class VehicleModelView(viewsets.ModelViewSet):
    queryset = VehicleModel.objects.all()
    serializer_class = VehicleModelSerializer
    filter_class = VehicleModelFilter