from rest_framework import serializers

from apps.profile.models.distributor_profile import DistributorProfile
from apps.profile.serializer.business_profile_serializer import BusinessProfileSerializer

from .doco_user_serializer import DocoUserSerializer


class DistributorProfileSerializer(serializers.ModelSerializer):
    business_profile = BusinessProfileSerializer()
    admin_user = DocoUserSerializer()
    class Meta:
        model = DistributorProfile
        fields = '__all__'
