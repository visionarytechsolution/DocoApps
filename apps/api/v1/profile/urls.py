from django.urls import path

from apps.api.v1.profile.views import PhoneNumberRegisteredAPIView

urlpatterns = [
    path(
        'phone-number-registered/', PhoneNumberRegisteredAPIView.as_view(),
        name='phone_number_registered'
    ),
]
