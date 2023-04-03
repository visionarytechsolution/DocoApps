import factory

from apps.common.models import Area
from apps.common.models import Country
from apps.common.models import Province
from apps.common.models import State
from apps.profile.models import BusinessProfile
from apps.profile.models import RetailerProfile
from apps.profile.models import DocoUser

USER_PASSWORD = 'adm1n'


class BusinessProfileFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = BusinessProfile


class RetailerProfileFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = RetailerProfile


class DocoUserFactory(factory.django.DjangoModelFactory):
    password = factory.PostGenerationMethodCall('set_password', USER_PASSWORD)
    is_superuser = False
    is_staff = True
    is_active = True

    class Meta:
        model = DocoUser


class ProvinceFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Province


class CountryFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Country


class StateFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = State


class AreaFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Area
