from django.db import models
from apps.common.models import Area, TenantBaseModel
from apps.configuration.models.warehouse import Warehouse


class WarehouseServiceability(TenantBaseModel):
    warehouse = models.ForeignKey(Warehouse, null=False, blank=False, on_delete=models.CASCADE)
    area = models.ForeignKey(Area, null=False, blank=False, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('warehouse', 'area')

    def save(self, *args, **kwargs):
        if self.pk is None:
            if self.warehouse is not None:
                self.tenant = self.warehouse.tenant
        super(WarehouseServiceability, self).save(*args, **kwargs)

    def __str__(self):
        return f'{self.warehouse} - {self.area.zip_code}'
