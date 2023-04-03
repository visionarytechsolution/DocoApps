import uuid

from rest_framework import serializers

from apps.common.models import Area
from apps.profile.models import Address
from apps.profile.models import BusinessProfile
from apps.profile.models import DocoUser
from apps.profile.models import RetailerProfile


class AddressSerializer(serializers.ModelSerializer):
    area = serializers.IntegerField()

    class Meta:
        model = Address
        fields = (
            'address_line1',
            'address_line2',
            'area',
            'latitude',
            'longitude',
        )


class BusinessProfileSerializer(serializers.ModelSerializer):
    address = AddressSerializer(many=False)

    class Meta:
        model = BusinessProfile
        fields = (
            'profile_id',
            'type',
            'name',
            'address',
            'contact_person_name',
            'contact_person_designation',
            'phone_number',
            'email',
        )

    def create(self, validated_data):
        area = Area.objects.get(pk=validated_data['address']['area'])
        validated_data['address']['area'] = area
        address = Address.objects.create(**validated_data.pop('address'))
        validated_data['address'] = address
        validated_data['profile_id'] = uuid.uuid4().hex
        instance = BusinessProfile.objects.create(**validated_data)
        return instance


class DocoUserSerializer(serializers.ModelSerializer):

    class Meta:
        model = DocoUser
        fields = (
            'password',
            'username',
            'first_name',
            'last_name',
            'email',
        )


class RetailerProfileSerializer(serializers.ModelSerializer):

    class Meta:
        model = RetailerProfile
        fields = (
            'business_profile',
            'admin_user',
        )


class RetailerSignupSerializer(serializers.Serializer):
    BDE = 'bde'
    OWN = 'own'

    SOURCE_CHOICES = (
        (BDE, 'BDE'),  # Retailer profile creation by BDE
        (OWN, 'OWN'),  # Retailer profile creation by on their own
    )
    source = serializers.ChoiceField(choices=SOURCE_CHOICES)
