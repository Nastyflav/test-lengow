#! /usr/bin/env python3
# coding: utf-8

"""
Author: [Nastyflav](https://github.com/Nastyflav) 2020-18-11
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

"""

from django.test import TestCase
from django.urls import reverse


class TestUrls(TestCase):
    """To test the orders app urls"""
    @classmethod
    def setUpTestData(cls):
        cls.index_url = reverse('orders:index')
        cls.order_url = reverse('orders:order', args=[1])
        cls.result_url = reverse('orders:results')

    def test_index_page_url(self):
        """To check the index url when requested"""
        self.assertEqual(self.index_url, '/')

    def test_order_details_page_url(self):
        """To check an order details url when requested"""
        self.assertEqual(self.order_url, '/order/1')

    def test_query_results_page_url(self):
        """To check the query results url when requested"""
        self.assertEqual(self.result_url, '/results/')