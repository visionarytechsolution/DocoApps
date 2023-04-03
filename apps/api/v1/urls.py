from django.urls import include
from django.urls import path

urlpatterns = [
    path('auth/', include(('apps.api.v1.auth.urls', 'api'), namespace='auth')),
    path('profile/', include(('apps.api.v1.profile.urls', 'api'), namespace='profiles')),
]
