from rest_framework import status
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework.views import APIView

from rest_framework_simplejwt.authentication import JWTAuthentication

from apps.api.v1.profile.serializers import BusinessProfilePhonumberSerializer
from apps.profile.models import BusinessProfile


class PhoneNumberRegisteredAPIView(APIView):
    """
    Validate whether the incoming phone number is already registered or not
    """

    authentication_classes = ()
    permission_classes = (IsAuthenticated)

    def post(self, request):
        serializer = BusinessProfilePhonumberSerializer(data=request.data)
        if serializer.is_valid():
            registered = BusinessProfile.objects.filter(phone_number=serializer.data['phone_number']).exists()
            return Response({
                'phone_number_registered': registered
            }, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
