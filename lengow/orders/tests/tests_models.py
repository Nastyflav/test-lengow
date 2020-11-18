#! /usr/bin/env python3
# coding: utf-8

"""
Author: [Nastyflav](https://github.com/Nastyflav) 2020-18-11
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

"""

from django.test import TestCase

from orders.models import Order


class TestModels(TestCase):
    """To test the orders app models"""
    def setUpTestData():
        """Create a temp order to perform tests"""
        Order.objects.create(
            marketplace="Cdiscount",
            customer="User 1",
            payment_date="2020-18-11",
            order_amount="56.13"
        )