from rest_framework import serializers

from apps.common.serializers.area import AreaSerializer
from apps.profile.models.address import Address


class AddressSerializer(serializers.ModelSerializer):
    area = AreaSerializer()
    class Meta:
        model = Address
        fields = '__all__'
