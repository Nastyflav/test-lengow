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
        cls.query_url = reverse('orders:results')
        cls.order_add_url = reverse('orders:order-add')
        cls.order_update_url = reverse('orders:order-update', args=[1])
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

    def test_query_results_page_returns_200(self):
        """To test the status code and the OrderSearchView"""
        response = self.client.get(self.query_url + '?query=amazon')
        self.assertTemplateUsed(response, 'orders/query_results.html')
        self.assertEqual(response.status_code, 200)

    def test_query_is_valid(self):
        """To check if we've got an order if there's one"""
        response = self.client.get(self.query_url + '?query=amazon')
        self.assertEqual(response.context_data['object_list'].count(), 1)

    def test_order_add_page_returns_200(self):
        """To test the status code and the OrderCreateView"""
        response = self.client.get(self.order_add_url)
        self.assertTemplateUsed(response, 'orders/order_form.html')
        self.assertEqual(response.status_code, 200)

    def test_order_add_redirection_when_validation(self):
        """To check the redirection when a new order is created"""
        response = self.client.post(self.order_add_url, {
            'marketplace': 'Fnac',
            'payment_date': '2020-11-20',
            'order_amount': '56.28',
            'currency': 'EUR'
        })
        self.assertRedirects(
            response, '/', status_code=302, target_status_code=200
        )

    def test_order_update_page_returns_200(self):
        """To test the status code and the OrderUpdateView"""
        response = self.client.get(self.order_update_url)
        self.assertTemplateUsed(response, 'orders/order_update.html')
        self.assertEqual(response.status_code, 200)

    def test_order_update_redirection_when_validation(self):
        """To check the redirection when an order is modified"""
        response = self.client.post(self.order_update_url, {
            'marketplace': 'Amazon',
            'payment_date': '2020-11-19',
            'order_amount': '451.21',
            'currency': 'USD',
        })
        self.assertRedirects(
            response, '/', status_code=302, target_status_code=200
        )
