#! /usr/bin/env python3
# coding: utf-8

"""
Author: [Nastyflav](https://github.com/Nastyflav) 2020-19-11
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

"""

from django.views.generic import DetailView, ListView

from orders.models import Order


class IndexView(ListView):
    """To render the app index with the orders list"""
    template_name = 'orders/index.html'
    model = Order

    def query_set(self):
        return Order.objects.filter().order_by("id")


class OrderDetailsView(DetailView):
    """To render all the fields in every order"""
    pass


class OrderSearchView(ListView):
    """To render the results of the query"""
    pass
