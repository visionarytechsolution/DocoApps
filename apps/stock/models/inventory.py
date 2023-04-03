from django.db import models

from apps.common.models.tenant_base_model import TenantBaseModel
from . import Product, ProductUnit


class Inventory(TenantBaseModel):
    product = models.OneToOneField(Product, null=False, on_delete=models.CASCADE, to_field='barcode')
    current_stock = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    minimum_stock = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    stock_unit = models.ForeignKey(ProductUnit, null=False, blank=False, on_delete=models.DO_NOTHING)

    # TODO: some tag to signify negative inventory is allowed
    # TODO - [Tally] : Other attributes to support tally sync

    class Meta:
        indexes = [
            models.Index(fields=['product'])
        ]
        unique_together = ('product', 'tenant')

    def __str__(self):
        return f'{self.product.name}'
