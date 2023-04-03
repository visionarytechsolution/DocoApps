from django.db import models

from apps.common.models.tenant_base_model import TenantBaseModel


class Offer(TenantBaseModel):
    class AppliedOnType(models.TextChoices):
        COUNT = 'COUNT', "On Count"
        VALUE = 'VALUE', "On Value"

    class DeductionType(models.TextChoices):
        VALUE = 'VALUE', 'Value'
        PERCENTAGE = 'PERCENTAGE', 'Percentage'

    applied_on = models.CharField(max_length=20, choices=AppliedOnType.choices, default=AppliedOnType.VALUE)
    deduction_type = models.CharField(max_length=20, choices=AppliedOnType.choices, default=DeductionType.VALUE)
    applicable_from = models.DateField(null=False, auto_now_add=True)
    expire_after = models.DateField(null=True)
    value = models.DecimalField(max_digits=10, decimal_places=3, null=False, default=0)

    def __str__(self):
        return f'{self.applied_on}-{self.deduction_type}-{self.value}'
