from rest_framework import serializers

from stock.models.product_unit import ProductUnit

from apps.common.models.tenant_base_model import TenantBaseModel
from apps.common.serializers.metric_unit import MetricUnitSerializer
from apps.stock.serializers.product_serializer import ProductSerializer


class ProductUnitSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    unit = MetricUnitSerializer()
    class Meta:
        model = ProductUnit
        fields = '__all__'
