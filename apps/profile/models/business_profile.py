import uuid

from django.db import models

from apps.common.models import BaseModel
from apps.profile.models import Address


class BusinessType(models.TextChoices):
    UNKNOWN = "UNKNOWN", "Unknown"
    DISTRIBUTOR = "DISTRIBUTOR", "Distributor"
    RETAILER = "RETAILER", "Retailer"


class BusinessProfile(BaseModel):
    profile_id = models.UUIDField(max_length=32, editable=False, default=uuid.uuid4)
    type = models.CharField(max_length=20, choices=BusinessType.choices, default=BusinessType.UNKNOWN)

    name = models.CharField(max_length=200)
    address = models.ForeignKey(Address, null=True, blank=True, on_delete=models.DO_NOTHING)

    contact_person_name = models.CharField(max_length=50, null=False, blank=False)
    contact_person_designation = models.CharField(max_length=50, null=False, blank=False)
    phone_number = models.CharField(max_length=15, null=False, blank=False, unique=True)
    email = models.EmailField(null=True, blank=True)
    number_verified = models.BooleanField(default=False)
    email_verified = models.BooleanField(default=False)

    class Meta:
        indexes = [
            models.Index(fields=['name', 'contact_person_name', 'type', 'profile_id'])
        ]

    def __str__(self):
        return f'{self.name}'
