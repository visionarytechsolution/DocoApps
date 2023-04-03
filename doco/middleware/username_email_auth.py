from django.contrib.auth import get_user_model
from django.contrib.auth.backends import ModelBackend
from django.contrib.auth.hashers import check_password

from apps.profile.utils import get_doco_user


class UsernameEmailSettingsBackend(ModelBackend):

    def authenticate(self, request, username=None, password=None, **kwargs):
        user = get_doco_user(username)

        if user and check_password(password, user.password):
            return user

        return None

    def get_user(self, user_id):
        UserModel = get_user_model()
        try:
            return UserModel.objects.get(pk=user_id)
        except UserModel.DoesNotExist:
            return None
