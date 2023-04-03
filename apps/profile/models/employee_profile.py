from django.db import models

from apps.profile.models import Address, DistributorProfile
from apps.profile.models.business_profile import BusinessProfile, BusinessType
from apps.profile.models.doco_user import DocoUser
from apps.common.models import BaseModel
from apps.profile.models.document import Document


class EmployeeProfileManager(models.Manager):

    def get_employee_profile_for_user(self, user):
        distributor = super().get_queryset().filter(user=user).first()
        return distributor

    def get_tenant_id_for_employee(self, employee):
        employer = employee.employer
        if employer.type == BusinessType.DISTRIBUTOR:
            distributor = DistributorProfile.objects.get_distributor_for_business_profile(employer)
            return distributor.tenant_id
        return None


class EmployeeProfile(BaseModel):
    user = models.OneToOneField(DocoUser, on_delete=models.CASCADE, related_name='auth_user',
                                limit_choices_to={'type': 'EMPLOYEE'})
    employee_code = models.CharField(max_length=30, null=True, blank=True)
    joining_date = models.DateField(null=True)
    primary_number = models.CharField(max_length=15, null=False, blank=False)
    whatsapp_number = models.CharField(max_length=15, null=True, blank=True)
    number_verified = models.BooleanField(default=False)
    email_verified = models.BooleanField(default=False)
    address = models.ForeignKey(Address, null=True, blank=True, on_delete=models.DO_NOTHING)
    id_proof = models.ForeignKey(Document, null=True, on_delete=models.DO_NOTHING,
                                 related_name='employee_id_proof')
    address_proof = models.ForeignKey(Document, null=True, on_delete=models.DO_NOTHING,
                                      related_name='employee_address_proof')
    # employer = models.OneToOneField(BusinessProfile, on_delete=models.CASCADE)
    employer = models.ForeignKey(BusinessProfile, on_delete=models.CASCADE)

    objects = EmployeeProfileManager()

    class Meta:
        indexes = [
            models.Index(fields=['employee_code', 'primary_number', 'employer'])
        ]

    def __str__(self):
        return f'{self.user.username}'
