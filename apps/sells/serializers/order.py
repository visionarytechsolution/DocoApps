from rest_framework import serializers

from models.order import Order

from apps.profile.serializer.doco_user_serializer import DocoUserSerializer
from apps.profile.serializer.employee_profile_serializer import EmployeeProfileSerializer
from apps.profile.serializer.retailer_profile_serializer import RetailerProfileSerializer


class OrderSerializer(serializers.ModelSerializer):
    created_by =DocoUserSerializer()
    buyer = RetailerProfileSerializer()
    approved_by = EmployeeProfileSerializer()

    class Meta:
        model = Order
        fields = '__all__'