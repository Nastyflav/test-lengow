#! /usr/bin/env python3
# coding: utf-8

"""
Author: [Nastyflav](https://github.com/Nastyflav) 2020-27-11
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

"""

from django.test import TransactionTestCase
from django.core.management import call_command

from orders.models import Order


class TestDbInit(TransactionTestCase):
    """To test if the command populates the database"""
    def test_insert_orders(self):
        """To check the orders numbers"""
        call_command('db_init')
        self.assertEqual(Order.objects.all().count(), 5)