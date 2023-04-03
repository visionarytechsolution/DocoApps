from django.db import models
from django.db.models.signals import pre_save
from django.dispatch import receiver

from apps.common.models import MetricUnit
from apps.common.models.tenant_base_model import TenantBaseModel
from apps.stock.models.product import Product


class ProductUnit(TenantBaseModel):
    product = models.ForeignKey(Product, null=False, on_delete=models.CASCADE)
    unit = models.ForeignKey(MetricUnit, null=False, on_delete=models.CASCADE)
    is_default = models.BooleanField(default=False)

    class Meta:
        indexes = [
            models.Index(fields=['product'])
        ]
        unique_together = ('product', 'unit')

    def __str__(self):
        return f'{self.product.name}-{self.unit.name} '
