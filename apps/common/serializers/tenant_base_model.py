from rest_framework import serializers

from models.tenant_base_model import TenantBaseModel

from apps.profile.serializer.distributor_profile_serializer import DistributorProfileSerializer


class TenantBaseModelSerializer(serializers.ModelSerializer):
    tenant = DistributorProfileSerializer()
    class Meta:
        model = TenantBaseModel
        fields = '__all__'
