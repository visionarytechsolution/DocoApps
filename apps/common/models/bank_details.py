from django.db import models

from apps.common.models import BaseModel


class BankDetail(BaseModel):
    CURRENT_ACCOUNT = 'current-account'
    SAVINGS_ACCOUNT = 'savings-account'

    bank_name = models.CharField(max_length=100)
    beneficiary_name = models.CharField(max_length=100)
    account_number = models.CharField(max_length=30)
    ifsc_code = models.CharField(max_length=20)
    account_type = models.CharField(max_length=20, choices=(
        (CURRENT_ACCOUNT, 'Current Account'),
        (SAVINGS_ACCOUNT, 'Savings Account'),
    ))

    class Meta:
        indexes = [
            models.Index(fields=['account_number', 'beneficiary_name'])
        ]

    def __str__(self):
        return f'{self.account_number}'
