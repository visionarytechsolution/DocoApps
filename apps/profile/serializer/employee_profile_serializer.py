from rest_framework import serializers

from apps.profile.models import EmployeeProfile


class EmployeeProfileSerializer(serializers.ModelSerializer):
    class Meta:
        model = EmployeeProfile
        fields = ['employee_code', 'joining_date', 'primary_number', 'whatsapp_number', 'employer']
