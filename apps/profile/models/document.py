from django.db import models

from apps.common.models import BaseModel
from apps.common.models.document_type import DocumentType
from doco.settings import DOCUMENT_MEDIA_ROOT


class Document(BaseModel):
    file_root = DOCUMENT_MEDIA_ROOT

    type = models.ForeignKey(DocumentType, null=False, blank=False, on_delete=models.DO_NOTHING)
    file = models.FileField(upload_to=file_root, null=False, blank=False)
    identification_number = models.TextField(null=True, blank=True)
    expiry_date = models.DateField(null=True, blank=True)
    notes = models.TextField(null=True, blank=True)

    class Meta:
        indexes = [
            models.Index(fields=['identification_number'])
        ]

    def __str__(self):
        return f'{self.type}'
