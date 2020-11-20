#! /usr/bin/env python3
# coding: utf-8

"""
Author: [Nastyflav](https://github.com/Nastyflav) 2020-19-11
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

"""

from django.urls import path

from orders import views

app_name = 'orders'

urlpatterns = [
    path('', views.IndexView.as_view(), name='index'),
    path('order/<int:pk>', views.OrderDetailsView.as_view(), name='order'),
    path('results/', views.OrderSearchView.as_view(), name='results'),
    path('add/', views.OrderCreateView.as_view(), name='order-add')
]
