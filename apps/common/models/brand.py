from django.db import models

from apps.common.models import BaseModel
from doco.settings import LOGO_MEDIA_ROOT


class Brand(BaseModel):
    name = models.CharField(max_length=50, null=False)
    code = models.CharField(max_length=10, null=False)
    logo = models.FileField(null=True, upload_to=LOGO_MEDIA_ROOT)

    class Meta:
        indexes = [
            models.Index(fields=['name', 'code'])
        ]

    def __str__(self):
        return f'{self.name}'
