from rest_framework import serializers

from models.invoice import Invoice

from .order import OrderSerializer


class InvoiceSerializer(serializers.ModelSerializer):
    order = OrderSerializer()
    class Meta:
        model = Invoice
        fields = '__all__'
