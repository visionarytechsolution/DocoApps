from django.db import models

from apps.common.models import BaseModel


class ProductCategory(BaseModel):
    name = models.CharField(max_length=30, null=False, blank=False, unique=True)
    code = models.CharField(max_length=10, null=False, blank=False)

    def __str__(self):
        return f'{self.name}'
