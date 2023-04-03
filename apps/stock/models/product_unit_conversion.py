from django.db import models

from apps.common.models.tenant_base_model import TenantBaseModel
from apps.stock.models.product_unit import ProductUnit


class ProductUnitConversion(TenantBaseModel):
    from_unit = models.ForeignKey(ProductUnit, null=False, on_delete=models.CASCADE, related_name='from_unit')
    to_unit = models.ForeignKey(ProductUnit, null=False, on_delete=models.CASCADE, related_name='to_unit')
    factor = models.DecimalField(max_digits=10, decimal_places=5, null=False)

    class Meta:
        unique_together = ('from_unit', 'to_unit')

    def __str__(self):
        return f'{self.from_unit.unit}->{self.to_unit.unit} '
