from rest_framework import serializers

from apps.profile.models import DocoUser
from apps.profile.serializer.user_serializer import UserSerializer


class DocoUserSerializer(serializers.ModelSerializer):
    user = UserSerializer(read_only=True, many=False)

    class Meta:
        model = DocoUser
        fields = ['user', 'type']
