from rest_framework import serializers

from apps.profile.models.retailer_profile import RetailerProfile
from apps.profile.serializer.business_profile_serializer import BusinessProfileSerializer
from apps.profile.serializer.doco_user_serializer import DocoUserSerializer


class RetailerProfileSerializer(serializers.ModelSerializer):
    business_profile = BusinessProfileSerializer()
    admin_user = DocoUserSerializer()
    class Meta:
        model = RetailerProfile
        fields = '__all__'