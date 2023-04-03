from rest_framework import serializers

from models.package_dimention import PackageDimension

from .metric_unit import MetricUnitSerializer


class PackageDimensionSerializer(serializers.ModelSerializer):
    dimension_unit = MetricUnitSerializer()
    weight_unit = MetricUnitSerializer()
    class Meta:
        model = PackageDimension
        fields = '__all__'
