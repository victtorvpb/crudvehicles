from rest_framework import viewsets
from .filtersapi import AutomMakerFilter, VehicleModelFilter,\
    VehicleFilter
from .models import AutoMaker, VehicleModel, Vehicle
from .serializers import AutoMakerSerializer, VehicleModelSerializer,\
    VehicleSerializer

class AutoMakerView(viewsets.ModelViewSet):
    queryset = AutoMaker.objects.all()
    serializer_class = AutoMakerSerializer
    filter_class = AutomMakerFilter


class VehicleModelView(viewsets.ModelViewSet):
    queryset = VehicleModel.objects.all()
    serializer_class = VehicleModelSerializer
    filter_class = VehicleModelFilter

class VehicleView(viewsets.ModelViewSet):
    queryset = Vehicle.objects.all()
    serializer_class = VehicleSerializer
    filter_class = VehicleFilter