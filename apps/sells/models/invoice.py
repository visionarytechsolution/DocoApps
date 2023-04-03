from enum import Enum

from django.db import models

from apps.common.models.tenant_base_model import TenantBaseModel
from apps.sells.models import Order
from apps.sells.service.id_generator_service import generate_invoice_id


class InvoiceStatusType(Enum):
    GENERATED = 'GENERATED'
    PENDING = 'PENDING'
    SETTLED = 'SETTLED'


class Invoice(TenantBaseModel):
    INVOICE_STATUS_TYPE = (
        (InvoiceStatusType.GENERATED.value, "GENERATED"),
        (InvoiceStatusType.PENDING.value, "PENDING"),
        (InvoiceStatusType.SETTLED.value, "SETTLED"),
    )

    order = models.OneToOneField(Order, on_delete=models.CASCADE, null=False, blank=False)
    invoice_id = models.CharField(max_length=40, unique=True, null=False, blank=False, editable=False)
    status = models.CharField(max_length=20, choices=INVOICE_STATUS_TYPE, null=False, editable=True,
                              default='GENERATED')
    due_date = models.DateField(null=False, blank=False)
    invoice_value = models.DecimalField(max_digits=10, decimal_places=2, null=False)

    # TODO - [Tally] : Other attributes to support tally sync

    class Meta:
        indexes = [
            models.Index(fields=['order', 'invoice_id'])
        ]

    def __str__(self):
        return f'{self.invoice_id}-{self.invoice_value}'

    def save(self, *args, **kwargs):
        if self.invoice_id is None or self.invoice_id == '':
            self.invoice_id = generate_invoice_id(self.order)
        super(Invoice, self).save(*args, **kwargs)
