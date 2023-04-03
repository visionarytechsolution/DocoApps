from rest_framework import serializers

from models.order_item import OrderItem

from apps.sells.serializers.order import OrderSerializer
from apps.stock.serializers.product_serializer import ProductSerializer
from apps.stock.serializers.product_unit_serializer import ProductUnitSerializer


class OrderItemSerializer(serializers.ModelSerializer):
    order = OrderSerializer()
    product = ProductSerializer()
    unit = ProductUnitSerializer()
    class Meta:
        model = OrderItem
        fields = '__all__'