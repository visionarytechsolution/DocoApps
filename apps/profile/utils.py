from django.contrib.auth import get_user_model
from django.db.models import Q

from apps.profile.models import BusinessProfile, DocoUser, EmployeeProfile
from apps.profile.models import DistributorProfile
from apps.profile.models import RetailerProfile
from apps.profile.models.doco_user import DocoUserType
from rest_framework.permissions import BasePermission


def get_doco_user(username):
    UserModel = get_user_model()
    user = UserModel.objects.filter(Q(username__iexact=username) | Q(email__iexact=username)).first()
    # todo: change this logic to check whether username is phonenumber first
    if not user:
        try:
            business_profile = BusinessProfile.objects.get(phone_number=username, number_verified=True)
        except BusinessProfile.DoesNotExist:
            return None

        distributor = DistributorProfile.objects.filter(business_profile=business_profile).first()
        retailer_profile = RetailerProfile.objects.filter(business_profile=business_profile).first()
        if distributor:
            user = distributor.admin_user
        elif retailer_profile:
            user = retailer_profile.admin_user

    return user


def get_doco_user_profile(username):
    user = DocoUser.objects.filter(username__iexact=username).first()
    if not user:
        return None
    profile_details = {'user_id': user.pk}
    if user.type == DocoUserType.RETAILER:
        try:
            retailer_profile = RetailerProfile.objects.get(admin_user=user)
            business_profile = retailer_profile.business_profile
            profile_details['profile_id'] = business_profile.profile_id
            profile_details['name'] = business_profile.name
            profile_details['role'] = DocoUserType.RETAILER
            profile_details['profile_picture'] = "http://placeimg.com/640/480"
        except RetailerProfile.DoesNotExist:
            profile_details['role'] = DocoUserType.UNSPECIFIED
            return profile_details
        return business_profile
    elif user.type == DocoUserType.DISTRIBUTOR:
        try:
            distributor_profile = DistributorProfile.objects.get(admin_user=user)
            business_profile = distributor_profile.business_profile
            profile_details['profile_id'] = business_profile.profile_id
            profile_details['name'] = business_profile.name
            profile_details['role'] = DocoUserType.DISTRIBUTOR
            profile_details['tenant_id'] = distributor_profile.tenant_id
            profile_details['profile_picture'] = "http://placeimg.com/640/480"
        except DistributorProfile.DoesNotExist:
            profile_details['role'] = DocoUserType.UNSPECIFIED
            return profile_details
    elif user.type == DocoUserType.EMPLOYEE:
        try:
            employee_profile = EmployeeProfile.objects.get(user=user)
            business_profile = employee_profile.employer
            distributor_profile = DistributorProfile.objects.get(business_profile=business_profile)
            profile_details['business_profile_id'] = business_profile.profile_id
            profile_details['name'] = employee_profile.user.get_full_name()
            profile_details['role'] = DocoUserType.EMPLOYEE
            profile_details['tenant_id'] = distributor_profile.tenant_id
            profile_details['profile_picture'] = "http://placeimg.com/640/480"
        except EmployeeProfile.DoesNotExist:
            profile_details['role'] = DocoUserType.UNSPECIFIED
            return profile_details
    else:
        profile_details['role'] = DocoUserType.UNSPECIFIED
    return profile_details


class IsBDE(BasePermission):
    """
    Allows access only to BDE users.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.type == DocoUserType.EMPLOYEE)


class IsDistributor(BasePermission):
    """
    Allows access only to DISTRIBUTOR users.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.type == DocoUserType.DISTRIBUTOR)


class IsRetailer(BasePermission):
    """
    Allows access only to DISTRIBUTOR users.
    """

    def has_permission(self, request, view):
        return bool(request.user and request.user.is_authenticated and request.user.type == DocoUserType.RETAILER)
