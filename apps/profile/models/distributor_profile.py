import uuid

from django.db import models
from django.utils.crypto import get_random_string

from apps.profile.models.business_profile import BusinessProfile, BusinessType
from apps.profile.models.doco_user import DocoUser, DocoUserType
from apps.common.models import BaseModel
from doco.settings import DISTRIBUTOR_CODE_STRING_CHARS


class DistributorManager(models.Manager):

    def get_distributor_for_tenant_id(self, tenant_id):
        distributor = super().get_queryset().filter(tenant_id__iexact=tenant_id).first()
        return distributor

    def get_distributor_for_admin_user(self, user):
        distributor = super().get_queryset().filter(admin_user=user).first()
        return distributor

    def get_distributor_for_business_profile(self, business):
        distributor = super().get_queryset().filter(business_profile=business).first()
        return distributor


class DistributorProfile(BaseModel):
    business_profile = models.OneToOneField(BusinessProfile, on_delete=models.CASCADE, 
                                            limit_choices_to={'type': BusinessType.DISTRIBUTOR})
    admin_user = models.OneToOneField(DocoUser, on_delete=models.DO_NOTHING, 
                                      limit_choices_to={'type': DocoUserType.DISTRIBUTOR}, related_name='admin_user')
    tenant_id = models.UUIDField(max_length=32, editable=False, default=uuid.uuid4, unique=True)
    code = models.CharField(max_length=4, null=False, editable=True)

    objects = DistributorManager()

    def __str__(self):
        return f'{self.business_profile.name}'

    def save(self, *args, **kwargs):
        if self.pk is None and self.code is None or self.code == "":
            self.code = get_random_string(length=4, allowed_chars=DISTRIBUTOR_CODE_STRING_CHARS).upper()
        super(DistributorProfile, self).save(*args, **kwargs)
