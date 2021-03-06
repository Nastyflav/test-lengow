#! /usr/bin/env python3
# coding: utf-8

"""
Author: [Nastyflav](https://github.com/Nastyflav) 2020-19-11
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

"""

from django.views.generic import DetailView, ListView, CreateView, UpdateView
from rest_framework. viewsets import ModelViewSet

from orders.models import Order
from orders.serializers import OrderSerializer


class IndexView(ListView):
    """To render the app index with the orders list"""
    template_name = 'orders/index.html'
    model = Order

    def query_set(self):
        return Order.objects.filter().order_by('id')


class OrderDetailsView(DetailView):
    """To render all the fields in every order"""
    model = Order
    template_name = "orders/order_details.html"


class OrderSearchView(ListView):
    """To render the results of the query"""
    model = Order
    template_name = 'orders/query_results.html'

    def get_queryset(self):
        """Get the orders matching with the query"""
        query = self.request.GET.get('query')
        query = str(query).casefold()

        orders = Order.objects.filter(
            marketplace__icontains=query).order_by('id') | \
            Order.objects.filter(
            payment_date__icontains=query).order_by('id') | \
            Order.objects.filter(
            order_amount__icontains=query).order_by('id') | \
            Order.objects.filter(
            currency__icontains=query).order_by('id')

        return orders


class OrderCreateView(CreateView):
    """To create a new order object"""
    model = Order
    fields = ['marketplace', 'payment_date', 'order_amount', 'currency']
    success_url = '/'


class OrderUpdateView(UpdateView):
    """To change any existing order"""
    model = Order
    template_name = 'orders/order_update.html'
    fields = ['marketplace', 'payment_date', 'order_amount', 'currency']
    success_url = '/'


class OrderViewSet(ModelViewSet):
    """To get all the orders and serialize its datas"""
    queryset = Order.objects.all()
    serializer_class = OrderSerializer
