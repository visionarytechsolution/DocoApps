from rest_framework_simplejwt.serializers import TokenObtainPairSerializer

from apps.profile.models import DistributorProfile, EmployeeProfile
from apps.profile.models.doco_user import DocoUserType
from apps.profile.serializer.employee_profile_serializer import EmployeeProfileSerializer


class DocoTokenObtainPairSerializer(TokenObtainPairSerializer):

    def update(self, instance, validated_data):
        pass

    def create(self, validated_data):
        pass

    @classmethod
    def get_token(cls, user):
        token = super(DocoTokenObtainPairSerializer, cls).get_token(user)

        # Add custom claims
        token['username'] = user.username
        token['type'] = user.type

        if user.type == DocoUserType.EMPLOYEE:
            employee = EmployeeProfile.objects.get_employee_profile_for_user(user)
            if employee:
                tenant_id = EmployeeProfile.objects.get_tenant_id_for_employee(employee)
                if tenant_id is not None:
                    token['tenant'] = f'{tenant_id}'
                token['profile_id'] = EmployeeProfileSerializer(instance=employee).data
        if user.type == DocoUserType.DISTRIBUTOR:
            distributor = DistributorProfile.objects.get_distributor_for_admin_user(user)
            token['tenant'] = f'{distributor.tenant_id}'
            token['profile_id'] = distributor.pk

        return token
