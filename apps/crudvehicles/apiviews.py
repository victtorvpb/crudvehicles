from rest_framework import viewsets
from .filtersapi import AutomMakerFilter
from .models import AutoMaker
from .serializers import AutoMakerSerializer

class AutoMakerView(viewsets.ModelViewSet):
    queryset = AutoMaker.objects.all()
    serializer_class = AutoMakerSerializer
    filter_class = AutomMakerFilter

