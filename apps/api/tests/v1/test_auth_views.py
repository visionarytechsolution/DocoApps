import json
import random
from http import HTTPStatus

from django.core.cache import cache

from rest_framework.test import APITestCase

from faker import Faker

from apps.api.tests.factories import USER_PASSWORD
from apps.api.tests.factories import AreaFactory
from apps.api.tests.factories import BusinessProfileFactory
from apps.api.tests.factories import CountryFactory
from apps.api.tests.factories import DocoUserFactory
from apps.api.tests.factories import ProvinceFactory
from apps.api.tests.factories import RetailerProfileFactory
from apps.api.tests.factories import StateFactory
from apps.api.v1.constants import DEFAULT_OTP

fake = Faker()


class AuthAPITestCase(APITestCase):

    def setUp(self):
        cache.clear()

    @classmethod
    def setUpTestData(cls):
        cls.user = DocoUserFactory(
            username='lauren',
            email=fake.email()
        )
        cls.business_profile = BusinessProfileFactory(
            phone_number=random.randint(500000000, 599999000)
        )
        cls.retailer_profile = RetailerProfileFactory(
            business_profile=cls.business_profile,
            admin_user=cls.user
        )
        country = CountryFactory()
        state = StateFactory()
        province = ProvinceFactory(
            country=country,
            state=state
        )
        cls.area = AreaFactory(province=province)

    def test_login_returns_http_status_ok(self):
        # given
        url = '/api/v1/auth/login/'

        # when
        response = self.client.post(
            url,
            {'username': self.user.username, 'password': USER_PASSWORD}
        )

        # then
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_login_with_email_returns_http_status_ok(self):
        # given
        url = '/api/v1/auth/login/'

        # when
        response = self.client.post(
            url,
            {'username': self.user.email, 'password': USER_PASSWORD}
        )

        # then
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_retailer_own_signup(self):
        # given
        url = '/api/v1/auth/retailer-signup/'
        payload = {
            'type': 'RETAILER',
            'source': 'own',
            'name': fake.name(),
            'address': {
                'address_line1': fake.address(),
                'address_line2': fake.address(),
                'area': self.area.id,
                'latitude': str(fake.latitude()),
                'longitude': str(fake.longitude()),
            },
            'contact_person_name': fake.name(),
            'contact_person_designation': fake.job(),
            'phone_number': random.randint(500000000, 599999000),
            'password': fake.password(),
            'username': fake.user_name(),
            'first_name': fake.first_name(),
            'last_name': fake.last_name(),
            'email': fake.email(),
        }

        # when
        response = self.client.post(url, payload, format='json')

        # then
        self.assertEqual(response.status_code, HTTPStatus.CREATED)

    def test_retailer_bde_signup(self):
        # given
        url = '/api/v1/auth/retailer-signup/'
        payload = {
            'type': 'RETAILER',
            'source': 'bde',
            'name': fake.name(),
            'address': {
                'address_line1': fake.address(),
                'address_line2': fake.address(),
                'area': self.area.id,
                'latitude': str(fake.latitude()),
                'longitude': str(fake.longitude()),
            },
            'contact_person_name': fake.name(),
            'contact_person_designation': fake.job(),
            'phone_number': random.randint(500000000, 599999000),
            'email': fake.email(),
        }

        # when
        response = self.client.post(url, payload, format='json')

        # then
        self.assertEqual(response.status_code, HTTPStatus.CREATED)

    def test_get_user_for_phonenumber_status_ok(self):
        # given
        url = f'/api/v1/auth/user/?phone_number={self.business_profile.phone_number}'

        # when
        response = self.client.get(url)

        # then
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_get_otp_for_phonenumber_status_ok(self):
        # given
        url = f'/api/v1/auth/otp/?phone_number={self.business_profile.phone_number}'

        # when
        response = self.client.get(url)

        # then
        self.assertEqual(response.status_code, HTTPStatus.OK)

    def test_verify_otp_for_phonenumber_status_ok(self):
        # given
        url = f'/api/v1/auth/verify-otp/?phone_number={self.business_profile.phone_number}'

        # when
        response = self.client.post(
            url,
            {
                'phone_number': self.business_profile.phone_number,
                'otp': DEFAULT_OTP
            }
        )

        # then
        self.assertEqual(response.status_code, HTTPStatus.OK)
