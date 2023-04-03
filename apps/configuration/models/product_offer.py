from django.db import models

from apps.common.models.tenant_base_model import TenantBaseModel
from apps.configuration.models.offer import Offer
from apps.stock.models import Product


class ProductOffer(TenantBaseModel):
    product = models.ForeignKey(Product, null=False, blank=False, on_delete=models.CASCADE)
    offer = models.ForeignKey(Offer, null=False, blank=False, on_delete=models.CASCADE)

    class Meta:
        unique_together = ('product', 'offer')
    
    def __str__(self):
        return f'{self.product}-{self.offer}'
