from enum import Enum

from django.db import models

from apps.profile.models import DocoUser, RetailerProfile
from apps.common.models.tenant_base_model import TenantBaseModel
from apps.profile.models.employee_profile import EmployeeProfile
from apps.sells.service.id_generator_service import generate_order_id


class OrderStatusType(Enum):
    CART = 'CART'
    CREATED = 'CREATED'
    CANCELLED = 'CANCELLED'
    REJECTED = 'REJECTED'
    APPROVED = 'APPROVED'
    PREPARED = 'PREPARED'
    OFD = 'OFD'
    COMPLETED = 'COMPLETED'


class Order(TenantBaseModel):
    ORDER_STATUS_TYPE = (
        (OrderStatusType.CART.value, "CART"),
        (OrderStatusType.CREATED.value, "CREATED"),
        (OrderStatusType.REJECTED.value, "CANCELLED"),
        (OrderStatusType.REJECTED.value, "REJECTED"),
        (OrderStatusType.APPROVED.value, "APPROVED"),
        (OrderStatusType.PREPARED.value, "PREPARED"),
        (OrderStatusType.OFD.value, "OFD"),
        (OrderStatusType.COMPLETED.value, "COMPLETED"),
    )

    created_by = models.ForeignKey(DocoUser, on_delete=models.DO_NOTHING, null=False, blank=False)
    order_id = models.CharField(max_length=40, unique=True, null=False, blank=False, editable=False)
    buyer = models.ForeignKey(RetailerProfile, on_delete=models.DO_NOTHING)

    is_approved = models.BooleanField(default=False)
    approved_by = models.ForeignKey(EmployeeProfile, null=True, blank=True, on_delete=models.DO_NOTHING)
    approved_at = models.DateTimeField(auto_now=True, verbose_name='Approved at')
    comment = models.TextField(null=True, blank=True)
    status = models.CharField(max_length=20, choices=ORDER_STATUS_TYPE, null=False, editable=True, default='CREATED')

    # order_value is total invoice value ** INCLUDING ** taxes, that needs to be paid by buyer
    order_value = models.DecimalField(max_digits=10, decimal_places=2, null=False)

    # TODO - [Tally] : Other attributes to support tally sync

    class Meta:
        indexes = [
            models.Index(fields=['created_by', 'order_id', 'buyer', 'tenant'])
        ]

    def __str__(self):
        return f'{self.order_id}'

    def save(self, *args, **kwargs):
        if self.order_id is None or self.order_id == '':
            self.order_id = generate_order_id(self.tenant.tenant_id)
        super(Order, self).save(*args, **kwargs)

