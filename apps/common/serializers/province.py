from rest_framework import serializers

from models.province import Province

from .country import CountrySerializer
from .state import StateSerializer


class ProvinceSerializer(serializers.ModelSerializer):
    country = CountrySerializer()
    state = StateSerializer()
    class Meta:
        model = Province
        fields = '__all__'
