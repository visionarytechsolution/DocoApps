from django.db import models

from . import BaseModel
from . import Province


class Area(BaseModel):
    name = models.CharField(max_length=60, null=False)
    code = models.CharField(max_length=20, null=True, blank=True)
    zip_code = models.CharField(max_length=10, null=True, blank=True)
    province = models.ForeignKey(Province, on_delete=models.DO_NOTHING)

    class Meta:
        indexes = [
            models.Index(fields=['zip_code', 'name', 'province'])
        ]

    def __str__(self):
        return f'{self.name}'
