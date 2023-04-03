from django.db import models

from apps.common.models.tenant_base_model import TenantBaseModel
from apps.sells.models import Order
from apps.stock.models import ProductUnit
from apps.stock.models.product import Product


class OrderItem(TenantBaseModel):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, null=False, blank=False)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, null=False, blank=False)
    quantity = models.PositiveIntegerField(null=False)
    unit = models.ForeignKey(ProductUnit, null=False, on_delete=models.DO_NOTHING)

    class Meta:
        indexes = [
            models.Index(fields=['order', 'product'])
        ]
        unique_together = ('order', 'product')

    def __str__(self):
        return f'{self.order} - ({self.product.name})'
