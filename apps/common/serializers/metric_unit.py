from rest_framework import serializers

from models.metric_unit import MetricUnit


class MetricUnitSerializer(serializers.ModelSerializer):
    class Meta:
        model = MetricUnit
        fields = '__all__'
