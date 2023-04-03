from rest_framework import serializers

from models.product_tax_category import ProductTaxCategory

from .product_category import ProductCategorySerializer
from .state import StateSerializer


class ProductTaxCategorySerializer(serializers.ModelSerializer):
    category = ProductCategorySerializer()
    state = StateSerializer()
    class Meta:
        model = ProductTaxCategory
        fields = '__all__'
