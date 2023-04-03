from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import generics
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.profile.models import BusinessProfile
from apps.profile.serializer.business_profile_serializer import BusinessProfileSerializer


class BusinessProfileAPIView(APIView):
    def post(self, request):
        serializer = BusinessProfileSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(request.data)


class BusinessProfileListView(generics.ListAPIView):
    queryset = BusinessProfile.objects.all()
    serializer_class = BusinessProfileSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ['profile_id', 'primary_number', 'whatsapp_number', 'primary_email']
