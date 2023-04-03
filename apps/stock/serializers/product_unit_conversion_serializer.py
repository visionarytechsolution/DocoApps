from rest_framework import serializers

from stock.models.product_unit_conversion import ProductUnitConversion
from stock.serializers.product_unit_serializer import ProductUnitSerializer


class ProductUnitConversionSerializer(serializers.ModelSerializer):
    from_unit = ProductUnitSerializer()
    to_unit = ProductUnitSerializer()
    class Meta:
        model = ProductUnitConversion
        fields = '__all__'
