from django.contrib.auth.models import AbstractUser
from django.db import models


class DocoUserType(models.TextChoices):
    UNSPECIFIED = "UNSPECIFIED", "Unspecified"
    DISTRIBUTOR = "DISTRIBUTOR", "Distributor"
    RETAILER = "RETAILER", "Retailer"
    EMPLOYEE = "EMPLOYEE", "Employee"
    BUSINESS_ADMIN = "BUSINESS_ADMIN", "Business Admin"
    DOCO_ADMIN = "DOCO_ADMIN", "Doco Admin"


class DocoUser(AbstractUser):
    base_type = DocoUserType.UNSPECIFIED
    type = models.CharField(max_length=20, choices=DocoUserType.choices, blank=False, null=False,
                            default=base_type)

    def __str__(self):
        return f'{self.username}'


class Distributor(DocoUser):
    base_type = DocoUserType.DISTRIBUTOR

    class Meta:
        proxy = True


class Retailer(DocoUser):
    base_type = DocoUserType.RETAILER

    class Meta:
        proxy = True


class Employee(DocoUser):
    base_type = DocoUserType.EMPLOYEE

    class Meta:
        proxy = True


class BusinessAdmin(DocoUser):
    base_type = DocoUserType.BUSINESS_ADMIN

    class Meta:
        proxy = True


class DocoAdmin(DocoUser):
    base_type = DocoUserType.DOCO_ADMIN

    class Meta:
        proxy = True
