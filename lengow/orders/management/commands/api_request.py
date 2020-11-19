#! /usr/bin/env python3
# coding: utf-8

"""
Author: [Nastyflav](https://github.com/Nastyflav) 2020-18-11
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

"""

import xml.etree.ElementTree as ElmTree
from urllib.request import urlopen

from orders.models import Order


class APIRequest():
    """Get all the needed datas from the API"""
    def add_datas(self):
        """To parse the xml url and get the wanted datas"""
        with urlopen('http://test.lengow.io/orders-test.xml') as url:
            tree = ElmTree.parse(url)
            root = tree.getroot()
            for data in root[1].findall('order'):
                marketplace = data.find('marketplace').text
                order_purchase_date = data.find('order_purchase_date').text
                order_amount = data.find('order_amount').text
                currency = data.find('order_currency').text

                order = Order.objects.create(
                    marketplace=marketplace,
                    payment_date=order_purchase_date,
                    order_amount=order_amount,
                    currency=currency
                )