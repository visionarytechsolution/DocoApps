from rest_framework import serializers

from models.area import Area

from .province import ProvinceSerializer


class AreaSerializer(serializers.ModelSerializer):
    province = ProvinceSerializer()
    class Meta:
        model = Area
        fields = '__all__'
