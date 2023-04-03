from django.db import models

from . import BaseModel


class MetricUnit(BaseModel):
    WEIGHT = 'weight'
    DIMENSION = 'dimension'
    COUNT = 'count'

    category = models.CharField(max_length=20, choices=(
        (WEIGHT, 'Weight'),
        (DIMENSION, 'Dimension'),
        (COUNT, 'Count'),
    ))
    name = models.CharField(max_length=30, null=False, blank=False)
    code = models.CharField(max_length=10, null=False, blank=False, unique=True)
    symbol = models.CharField(max_length=3, null=False, blank=False, unique=True)

    class Meta:
        indexes = [
            models.Index(fields=['name', 'code', 'category'])
        ]

    def __str__(self):
        return f'{self.name}'
