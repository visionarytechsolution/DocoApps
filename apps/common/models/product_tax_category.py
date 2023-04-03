from django.db import models

from apps.common.models import BaseModel
from apps.common.models import ProductCategory
from apps.common.models import State


class ProductTaxCategory(BaseModel):
    category = models.ForeignKey(ProductCategory, null=False, blank=False, on_delete=models.CASCADE)
    state = models.ForeignKey(State, null=False, blank=False, on_delete=models.CASCADE)
    gst = models.DecimalField(max_digits=5, decimal_places=3, default=0)
    sgst = models.DecimalField(max_digits=5, decimal_places=3, default=0)
    igst = models.DecimalField(max_digits=5, decimal_places=3, default=0)

    class Meta:
        unique_together = ('category', 'state')

    def __str__(self):
        return f'{self.category} ({"{:.2f}%".format(self.gst)})'
