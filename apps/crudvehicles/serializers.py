from rest_framework import serializers
from .models import AutoMaker, VehicleModel


class AutoMakerSerializer(serializers.ModelSerializer):
    repr = serializers.SerializerMethodField()

    class Meta:
        model = AutoMaker
        fields = ('id', 'name', 'repr')

    def get_repr(self, obj):
        return str(obj)


class VehicleModelSerializer(serializers.ModelSerializer):

    repr = serializers.SerializerMethodField()
    # model = serializers.SerializerMethodField()

    class Meta:
        model = VehicleModel
        fields = ('id', 'name', 'model', 'engine', 'automaker', 'repr')

    def get_repr(self, obj):
        return 'AutoMaker {} - engine {} - model - {}'.format(
            obj.automaker.name, obj.engine, obj.get_model_display())

