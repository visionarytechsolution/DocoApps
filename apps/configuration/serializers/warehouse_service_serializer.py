from rest_framework import serializers

from configuration.models.warehouse_serviceability import WarehouseServiceability
from configuration.serializers.warehouse_serializer import WarehouseSerializer

from apps.common.serializers.area import AreaSerializer


class WarehouseServiceabilitySerializer(serializers.ModelSerializer):
    warehouse = WarehouseSerializer()
    area = AreaSerializer()
    class Meta:
        model = WarehouseServiceability
        fields = '__all__'
