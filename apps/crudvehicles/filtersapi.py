import rest_framework_filters as filters
from .models import AutoMaker


class AutomMakerFilter(filters.FilterSet):

    name = filters.AllLookupsFilter(name='name')

    class Meta:
        model = AutoMaker
        fields = ['id', 'name']
