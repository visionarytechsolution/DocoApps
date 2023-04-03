from rest_framework import serializers

from models.bank_details import BankDetail


class BankDetailSerializer(serializers.ModelSerializer):
    class Meta:
        model = BankDetail
        fields = '__all__'
