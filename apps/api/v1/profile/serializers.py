from rest_framework import serializers

from apps.profile.models import BusinessProfile


class BusinessProfilePhonumberSerializer(serializers.ModelSerializer):

    class Meta:
        model = BusinessProfile
        fields = ('phone_number',)
