from django.db import models

from apps.profile.models.business_profile import BusinessProfile, BusinessType
from apps.profile.models.doco_user import DocoUser, DocoUserType
from apps.common.models import BaseModel


class RetailerProfile(BaseModel):
    business_profile = models.OneToOneField(BusinessProfile, on_delete=models.CASCADE, null=False,
                                            limit_choices_to={'type': BusinessType.RETAILER})
    admin_user = models.OneToOneField(DocoUser, on_delete=models.DO_NOTHING, null=True,
                                      limit_choices_to={'type': DocoUserType.RETAILER})

    def __str__(self):
        return f'{self.business_profile.name}'
