from django.db import models

from apps.common.models import BaseModel


class DocumentType(BaseModel):
    name = models.CharField(max_length=30, null=False, blank=False)
    has_unique_number = models.BooleanField(default=True)
    has_back_image = models.BooleanField(default=False)
    has_expiry_date = models.BooleanField(default=True)

    def __str__(self):
        return f'{self.name}'
