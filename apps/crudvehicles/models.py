from django.db import models


class AutoMaker(models.Model):
    name = models.CharField(max_length=100, blank=False,
                            null=False, unique=True)

    def __str__(self):
        return self.name
