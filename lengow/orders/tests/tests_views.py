#! /usr/bin/env python3
# coding: utf-8

"""
Author: [Nastyflav](https://github.com/Nastyflav) 2020-18-11
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

"""

from django.test import TestCase, Client
from django.urls import reverse

from orders.models import Order


def db_init():
    """To create temp orders to perform tests"""
    order_1 = Order.objects.create(
        marketplace='Amazon',
        payment_date='2020-11-19',
        order_amount='451.21',
        currency='EUR',
    )
    order_1.save()
    order_2 = Order.objects.create(
        marketplace='CDiscount',
        payment_date='2020-11-05',
        order_amount='330',
        currency='EUR',
    )
    order_2.save()
    order_3 = Order.objects.create(
        marketplace='Instagram',
        payment_date='2020-09-25',
        order_amount='14.90',
        currency='EUR',
    )
    order_3.save()


class TestViews(TestCase):
    """To test the orders app views"""
    @classmethod
    def setUpTestData(cls):
        cls.client = Client()
        cls.index_url = reverse('orders:index')
        cls.order_url = reverse('orders:order', args=[3])
        db_init()

    def test_index_page_returns_200(self):
        """To test the status code and the index view"""
        response = self.client.get(self.index_url)
        self.assertTemplateUsed(response, 'orders/index.html')
        self.assertEqual(response.status_code, 200)

    def test_index_page_query_set(self):
        """To check if the index view returns the right objects number"""
        response = self.client.get(self.index_url)
        self.assertEqual(response.context_data['object_list'].count(), 3)

    def test_order_details_page_returns_200(self):
        """To test the status code and the OrderDetailView"""
        response = self.client.get(self.order_url)
        self.assertTemplateUsed(response, 'orders/order_details.html')
        self.assertEqual(response.status_code, 200)

    def test_order_details_page_returns_404_if_missing_order(self):
        """To check the invalid response when there's no order"""
        response = self.client.get('/order/14')
        self.assertEqual(response.status_code, 404)