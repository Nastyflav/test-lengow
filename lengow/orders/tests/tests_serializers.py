#! /usr/bin/env python3
# coding: utf-8

"""
Author: [Nastyflav](https://github.com/Nastyflav) 2020-25-11
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

"""

from django.urls import include, path, reverse
from rest_framework.test import APITestCase, URLPatternsTestCase

from orders.models import Order
from orders.serializers import OrderSerializer


class TestOrderSerializer(APITestCase, URLPatternsTestCase):
    urlpatterns = [
        path('api/', include('orders.urls')),
    ]

    def test_create_account(self):
        """
        Ensure we can create a new account object.
        """
        url = reverse('api')
        response = self.client.get(url, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
