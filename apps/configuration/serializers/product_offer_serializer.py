from rest_framework import serializers

from configuration.models.product_offer import ProductOffer
from configuration.serializers.offer_serializer import OfferSerializer
from stock.serializers.product_serializer import ProductSerializer


class ProductOfferSerializer(serializers.ModelSerializer):
    product = ProductSerializer()
    offer = OfferSerializer()
    class Meta:
        model = ProductOffer
        fields = '__all__'
