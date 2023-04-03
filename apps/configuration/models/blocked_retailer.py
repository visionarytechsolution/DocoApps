from django.db import models

from apps.common.models.tenant_base_model import TenantBaseModel
from apps.profile.models import RetailerProfile, DistributorProfile


class BlockedRetailer(TenantBaseModel):
    retailer = models.ForeignKey(RetailerProfile, null=False, on_delete=models.DO_NOTHING,
                                 related_name='blocked_retailer')
    distributor = models.ForeignKey(DistributorProfile, null=False, on_delete=models.DO_NOTHING,
                                    related_name='blocking_distributor')
    reason = models.TextField()

    class Meta:
        indexes = [
            models.Index(fields=['retailer'])
        ]
        unique_together = ('retailer', 'distributor')

    def __str__(self):
        return f'{self.retailer.name}'
