from django.db import models

from apps.common.models import BaseModel
from apps.common.models.area import Area


class Address(BaseModel):
    address_line1 = models.TextField(null=False)
    address_line2 = models.TextField()
    is_verified = models.BooleanField(default=False)
    area = models.ForeignKey(Area, null=False, on_delete=models.DO_NOTHING)
    latitude = models.TextField(null=True, blank=True)
    longitude = models.TextField(null=True, blank=True)

    class Meta:
        indexes = [
            models.Index(fields=['area'])
        ]

    def __str__(self):
        return f'{self.address_line1}'
