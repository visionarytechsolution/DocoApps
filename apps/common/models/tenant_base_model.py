from django.db import models

from apps.profile.models import DistributorProfile
from apps.common.models import BaseModel


class TenantBaseModel(BaseModel):
    tenant = models.ForeignKey(DistributorProfile, to_field='tenant_id', on_delete=models.CASCADE, null=False, blank=False,
                               db_index=True)
    is_active = models.BooleanField(default=True)

    class Meta:
        abstract = True
