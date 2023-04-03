from django.contrib.auth.models import User
from rest_framework.exceptions import AuthenticationFailed
from rest_framework.response import Response
from rest_framework.views import APIView

from apps.profile.models import DocoUser
from apps.profile.serializer.doco_user_serializer import DocoUserSerializer


class RegisterAPIView(APIView):
    def post(self, request):
        # serializer = DocoUserSerializer(data=request.data)
        # serializer.is_valid(raise_exception=True)
        # serializer.save()
        return Response(request.data)


class LoginAPIView(APIView):
    def post(self, request):
        username = request.data['username']
        password = request.data['password']
        user = User.objects.filter(username=username).first()
        if user is None:
            raise AuthenticationFailed('User not found')

        if not user.check_password(password):
            raise AuthenticationFailed('Incorrect password')

        docouser = DocoUser.object.get_docouser_for_user(user)
        serializer = DocoUserSerializer(docouser)
        return Response(serializer.data)
