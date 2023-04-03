from rest_framework import status
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework_simplejwt.exceptions import InvalidToken
from rest_framework_simplejwt.exceptions import TokenError
from rest_framework_simplejwt.views import TokenObtainPairView

from apps.api.v1.auth.serializers import BusinessProfileSerializer
from apps.api.v1.auth.serializers import DocoUserSerializer
from apps.api.v1.auth.serializers import RetailerSignupSerializer
from apps.api.v1.constants import DEFAULT_OTP
from apps.profile.models import RetailerProfile
from apps.profile.utils import get_doco_user, get_doco_user_profile


class DocoTokenObtainPairView(TokenObtainPairView):

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        try:
            serializer.is_valid(raise_exception=True)
        except TokenError as e:
            raise InvalidToken(e.args[0])

        profile_details = get_doco_user_profile(request.data['username'])
        data = serializer.validated_data
        data["profile"] = profile_details
        return Response(data, status=status.HTTP_200_OK)


class RetailerSignupAPIView(APIView):
    """
    API to create retailer profile
    """

    authentication_classes = []
    permission_classes = []

    def post(self, request):
        source_serializer = RetailerSignupSerializer(data=request.data)
        if not source_serializer.is_valid():
            return Response(source_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

        # When BDE create profile for retailer, docouser will be none
        if source_serializer.data['source'] == RetailerSignupSerializer.BDE:
            user = None
        else:
            docouser_serializer = DocoUserSerializer(data=request.data)
            if docouser_serializer.is_valid():
                user = docouser_serializer.save()
            else:
                return Response(
                    docouser_serializer.errors,
                    status=status.HTTP_400_BAD_REQUEST
                )

        business_profile_serializer = BusinessProfileSerializer(data=request.data)
        if business_profile_serializer.is_valid():
            business_profile = business_profile_serializer.save()
            retailer_profile = RetailerProfile.objects.create(
                business_profile=business_profile,
                admin_user=user,
            )
            return Response({'id': retailer_profile.id}, status=status.HTTP_201_CREATED)
        else:
            return Response(
                business_profile_serializer.errors,
                status=status.HTTP_400_BAD_REQUEST
            )


class UserPhoneNumberView(APIView):

    authentication_classes = []
    permission_classes = []

    def get(self, request, *args, **kwargs):
        phone_number = request.query_params.get('phone_number')
        user = get_doco_user(phone_number)
        return Response(
            {
                'phone_number': phone_number,
                'user_id': user.id if user else None,
                'is_found': True if user else False
            },
            status=status.HTTP_200_OK
        )


class OTPView(APIView):

    authentication_classes = []
    permission_classes = []

    def get(self, request, *args, **kwargs):
        phone_number = request.query_params.get('phone_number')
        return Response(
            {
                'phone_number': phone_number,
                'otp': DEFAULT_OTP,
            },
            status=status.HTTP_200_OK
        )


class VerifyOTPView(APIView):

    authentication_classes = []
    permission_classes = []

    def post(self, request, *args, **kwargs):
        phone_number = request.data.get('phone_number')
        otp = request.data.get('otp')
        return Response(
            {
                'phone_number': phone_number,
                'otp_verified': otp == DEFAULT_OTP,
            },
            status=status.HTTP_200_OK
        )
