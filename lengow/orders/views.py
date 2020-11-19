#! /usr/bin/env python3
# coding: utf-8

"""
Author: [Nastyflav](https://github.com/Nastyflav) 2020-19-11
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

"""

from django.shortcuts import render
from django.views.generic import DetailView, TemplateView, ListView


class IndexView(TemplateView):
    """To render the app index with the orders list"""
    template_name = 'orders/index.html'


class OrderDetailsView(DetailView):
    """To render all the fields in every order"""
    pass


class OrderSearchView(ListView):
    """To render the results of the query"""
    pass
