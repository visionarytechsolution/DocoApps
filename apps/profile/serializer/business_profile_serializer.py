from rest_framework import serializers

from apps.profile.models import BusinessProfile


class BusinessProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusinessProfile
        fields = ['profile_id', 'name', 'type', 'address', 'contact_person_name', 'contact_person_designation', 'primary_number',
                  'number_verified', 'whatsapp_number', 'primary_email', 'email_verified']
