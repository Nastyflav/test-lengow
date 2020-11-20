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
            payment_date="2020-11-18",
            order_amount="56.13",
            currency="EUR",
        )

    def test_order_max_lenght(self):
        """To check the order fields max_lenght"""
        data = Order.objects.get(id=1)
        max_length = data._meta.get_field('marketplace').max_length
        self.assertEquals(max_length, 100)

    def test_order_verbose_name(self):
        """To check the order fields verbose names"""
        data = Order.objects.get(id=1)
        verbose_name = data._meta.get_field('currency').verbose_name
        self.assertEquals(verbose_name, "Devise")

    def test_order_max_digits(self):
        """To check the order amount max digits"""
        data = Order.objects.get(id=1)
        max_digits = data._meta.get_field('order_amount').max_digits
        self.assertEquals(max_digits, 5)

    def test_order_decimals(self):
        """To check the order amount decimals"""
        data = Order.objects.get(id=1)
        decimals = data._meta.get_field('order_amount').decimal_places
        self.assertEquals(decimals, 2)
