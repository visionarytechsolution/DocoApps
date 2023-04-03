from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import AllowAny
from ...serializer.doco_token_obtain_pair_serializer import DocoTokenObtainPairSerializer


class DocoObtainTokenPairView(TokenObtainPairView):
    permission_classes = (AllowAny,)
    serializer_class = DocoTokenObtainPairSerializer
