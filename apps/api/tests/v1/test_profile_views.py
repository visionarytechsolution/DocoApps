import random
from http import HTTPStatus

from django.core.cache import cache

from rest_framework.test import APITestCase

from apps.api.tests.factories import BusinessProfileFactory
from apps.api.tests.factories import DocoUserFactory


class ProfileAPITestCase(APITestCase):

    def setUp(self):
        cache.clear()

    @classmethod
    def setUpTestData(cls):
        cls.business_profile = BusinessProfileFactory(
            phone_number=random.randint(500000000, 599999000)
        )
        cls.user = DocoUserFactory(username='lauren')

    def test_get_phone_number_registered_returns_http_status_ok(self):
        # given
        url = '/api/v1/profile/phone-number-registered/'
        self.client.force_authenticate(user=self.user)

        # when
        response = self.client.post(url, {'phone_number': self.business_profile.phone_number})

        # then
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertTrue(response.data['phone_number_registered'])

    def test_get_phone_number_registered_returns_http_status_bad_request(self):
        # given
        url = '/api/v1/profile/phone-number-registered/'
        self.client.force_authenticate(user=self.user)

        # when
        response = self.client.post(url, {'phone_number': '111222333'})

        # then
        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertFalse(response.data['phone_number_registered'])
