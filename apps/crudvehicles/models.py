from django.db import models
from dj.choices.fields import ChoiceField
from .choices import ModelsTypesChoices


class AutoMaker(models.Model):
    name = models.CharField(max_length=100, blank=False,
                            null=False, unique=True)

    def __str__(self):
        return self.name


class VehicleModel(models.Model):
    name = models.CharField(
        max_length=100,
        blank=False,
        null=False)

    model = ChoiceField(
        choices=ModelsTypesChoices,
        default=ModelsTypesChoices.car)

    engine = models.FloatField(
        null=False,
        blank=False)

    automaker = models.ForeignKey(
        AutoMaker,
        related_name='autoMaker',
        on_delete=models.PROTECT)
    
    def __str__(self):
        return self.name
