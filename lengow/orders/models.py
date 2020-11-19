#! /usr/bin/env python3
# coding: utf-8

"""
Author: [Nastyflav](https://github.com/Nastyflav) 2020-18-11
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

"""

from django.db import models


class Order(models.Model):
    """Order model, restricted to a few fields"""
    marketplace = models.CharField(
        max_length=100, verbose_name='Marketplace', null=True
    )
    payment_date = models.DateField(
        verbose_name='Date du paiement', null=True
    )
    order_amount = models.DecimalField(
        max_digits=5, decimal_places=2,
        verbose_name='Montant en euros',
        null=True
    )
    currency = models.CharField(
        max_length=5, verbose_name='Devise', null=True
    )

    class Meta:
        verbose_name = 'Commande'
