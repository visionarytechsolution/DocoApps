from rest_framework import serializers

from stock.models.product import Product

from apps.common.serializers.brand import BrandSerializer
from apps.common.serializers.product_tax_category import ProductCategorySerializer


class ProductSerializer(serializers.ModelSerializer):
    brand = BrandSerializer()
    tax_category = ProductCategorySerializer()
    class Meta:
        model = Product
        fields = '__all__'
