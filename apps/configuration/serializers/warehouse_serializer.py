from rest_framework import serializers

from configuration.models.warehouse import Warehouse

from apps.profile.serializer.address_serializer import AddressSerializer
from apps.profile.serializer.distributor_profile_serializer import DistributorProfileSerializer


class WarehouseSerializer(serializers.ModelSerializer):
    distributor = DistributorProfileSerializer()
    address = AddressSerializer()
    class Meta:
        model = Warehouse
        fields = '__all__'
