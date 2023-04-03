from rest_framework import serializers

from stock.models.inventory import Inventory
from stock.serializers.product_serializer import ProductSerializer
from stock.serializers.product_unit_serializer import ProductUnitSerializer


class InventorySerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    stock_unit = ProductUnitSerializer()
    class Meta:
        model = Inventory
        fields = '__all__'
