from django.db import models

from .country import Country
from .state import State


class Province(models.Model):
    name = models.CharField(max_length=60, null=False)
    code = models.CharField(max_length=4, null=True)
    country = models.ForeignKey(Country, on_delete=models.CASCADE)
    state = models.ForeignKey(State, on_delete=models.CASCADE)

    class Meta:
        indexes = [
            models.Index(fields=['name', 'code'])
        ]

    def __str__(self):
        return f'{self.name}'
