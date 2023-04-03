from django.db import models
from apps.common.models import TenantBaseModel
from apps.profile.models import DistributorProfile, Address


class Warehouse(TenantBaseModel):
    distributor = models.ForeignKey(DistributorProfile, null=False, blank=False, on_delete=models.CASCADE,
                                    related_name='warehouse_owner')
    address = models.ForeignKey(Address, null=False, blank=False, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('distributor', 'address')

    # def save(self, *args, **kwargs):
    #     if self.pk is None:
    #         if self.distributor is not None:
    #             self.tenant = self.distributor
    #     super(Warehouse, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.distributor} - {self.address}'
