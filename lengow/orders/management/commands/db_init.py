#! /usr/bin/env python3
# coding: utf-8

"""
Author: [Nastyflav](https://github.com/Nastyflav) 2020-18-11
Licence: `GNU GPL v3` GNU GPL v3: http://www.gnu.org/licenses/

"""

from django.core.management.base import BaseCommand

from .api_request import APIRequest


class Command(BaseCommand):
    """Command class for custom django commands"""
    help='Load datas from the xml API to our local database'

    def handle(self, *args, **options):
        self.db = APIRequest()
        self.db.add_datas()