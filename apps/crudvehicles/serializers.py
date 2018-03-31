from rest_framework import serializers
from .models import AutoMaker


class AutoMakerSerializer(serializers.ModelSerializer):
    repr = serializers.SerializerMethodField()

    class Meta:
        model = AutoMaker
        fields = ('id', 'name', 'repr')
    
    def get_repr(self, obj):
        return str(obj)