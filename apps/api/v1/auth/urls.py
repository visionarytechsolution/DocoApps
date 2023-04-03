from django.urls import path

from rest_framework_simplejwt.views import TokenRefreshView
from rest_framework_simplejwt.views import TokenVerifyView

from apps.api.v1.auth.views import DocoTokenObtainPairView
from apps.api.v1.auth.views import OTPView
from apps.api.v1.auth.views import RetailerSignupAPIView
from apps.api.v1.auth.views import UserPhoneNumberView
from apps.api.v1.auth.views import VerifyOTPView

urlpatterns = [
    path('login/', DocoTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),
    path('retailer-signup/', RetailerSignupAPIView.as_view(), name='retailer_signup'),
    path('user/', UserPhoneNumberView.as_view(), name='get_user_for_phone_number'),
    path('otp/', OTPView.as_view(), name='get_otp'),
    path('verify-otp/', VerifyOTPView.as_view(), name='get_otp'),
]
