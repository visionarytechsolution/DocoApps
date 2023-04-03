from django.db import models

from apps.common.models import ProductTaxCategory
from apps.common.models.brand import Brand
from apps.common.models.tenant_base_model import TenantBaseModel
from doco.settings import PRODUCT_MEDIA_ROOT


class Product(TenantBaseModel):
    name = models.CharField(max_length=50, null=False)
    hsn_code = models.CharField(max_length=20, null=True)
    description = models.TextField(null=False)
    image = models.FileField(null=True, upload_to=PRODUCT_MEDIA_ROOT)
    brand = models.ForeignKey(Brand, null=False, on_delete=models.DO_NOTHING)

    reference_number = models.CharField(max_length=30, null=True)
    barcode = models.CharField(max_length=30, null=False, unique=True)

    # purchase_price is actual price paid for this product including tax
    purchase_price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    # selling price does not include tax, its minimum price on which this should be sold
    selling_price = models.DecimalField(max_digits=10, decimal_places=2, null=False)
    tax_category = models.ForeignKey(ProductTaxCategory, null=False, on_delete=models.DO_NOTHING)

    # TODO: Tax calculation or buying price and other values related to finance
    # TODO - [Tally] : Other attributes to support tally sync

    class Meta:
        indexes = [
            models.Index(fields=['name', 'reference_number', 'barcode'])
        ]
        unique_together = ('name', 'tenant', 'brand')

    def __str__(self):
        return f'{self.name}'
