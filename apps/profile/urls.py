from django.urls import path

from apps.profile.views.api_views.auth_api_view import RegisterAPIView, LoginAPIView
from apps.profile.views.api_views.business_profile_api_view import BusinessProfileAPIView, BusinessProfileListView
from apps.profile.views.template_view import user_login

# urlpatterns = [
    # path('register', RegisterAPIView.as_view())
    # path('register/business', BusinessProfileAPIView.as_view()),
    # path('businesses/', BusinessProfileListView.as_view()),
    # path('login', LoginAPIView.as_view()),
# ]
