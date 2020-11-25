#! /usr/bin/env python3
# coding: utf-8

"""
Author: [Nastyflav](https://github.com/Nastyflav) 2020-18-11
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

"""

from rest_framework.serializers import HyperlinkedModelSerializer
from orders.models import Order


class OrderSerializer(HyperlinkedModelSerializer):
    """To serialize the Order model and get the datas"""
    class Meta:
        model = Order
        fields = ('marketplace', 'payment_date', 'order_amount', 'currency')
