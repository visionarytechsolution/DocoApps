from rest_framework import serializers

from configuration.models.blocked_retailer import BlockedRetailer

from apps.profile.serializer.distributor_profile_serializer import DistributorProfileSerializer
from apps.profile.serializer.retailer_profile_serializer import RetailerProfileSerializer


class BlockedRetailerSerializer(serializers.ModelSerializer):
    retailer = RetailerProfileSerializer()
    distributor = DistributorProfileSerializer()
    class Meta:
        model = BlockedRetailer
        fields = '__all__'
