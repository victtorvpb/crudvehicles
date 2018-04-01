import rest_framework_filters as filters
from .models import AutoMaker, VehicleModel


class AutomMakerFilter(filters.FilterSet):

    name = filters.AllLookupsFilter(name='name')

    class Meta:
        model = AutoMaker
        fields = ['id', 'name']


class VehicleModelFilter(filters.FilterSet):

    name = filters.AllLookupsFilter(name='name')
    model = filters.AllLookupsFilter(name='model')
    engine = filters.AllLookupsFilter(name='engine')
    automaker = filters.RelatedFilter(
        AutomMakerFilter, name='automaker', queryset=AutoMaker.objects.all())

    class Meta:
        model = VehicleModel
        fields = ['id', 'name', 'model', 'engine', 'automaker']
