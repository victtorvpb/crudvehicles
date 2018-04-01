import rest_framework_filters as filters
from .models import AutoMaker, VehicleModel, Vehicle


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


class VehicleFilter(filters.FilterSet):

    color = filters.AllLookupsFilter(name="color")
    mileage = filters.AllLookupsFilter(name="mileage")
    model = filters.RelatedFilter(
        VehicleModelFilter, name="model", queryset=VehicleModel.objects.all())

    class Meta:
        model = Vehicle
        fields = ["id", "model", "color", "mileage"]
