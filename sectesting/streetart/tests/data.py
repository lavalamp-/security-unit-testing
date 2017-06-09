# -*- coding: utf-8 -*-
from __future__ import absolute_import

from datetime import datetime


class StreetArtTestData(object):
    """
    This class contains test data for use in unit testing the Street Art project.
    """

    USERS = {
        "user_1": {
            "email": "test1@streetart.com",
            "first_name": "Barry",
            "last_name": "Bonds",
            "date_joined": datetime.now(),
            "is_active": True,
            "is_staff": False,
            "is_superuser": False,
            "password": "Password123",
        },
        "user_2": {
            "email": "test2@streetart.com",
            "first_name": "Billy",
            "last_name": "Bonds",
            "date_joined": datetime.now(),
            "is_active": True,
            "is_staff": False,
            "is_superuser": False,
            "password": "Password123",
        },
        "admin_1": {
            "email": "test3@streetart.com",
            "first_name": "Bondy",
            "last_name": "Bonds",
            "date_joined": datetime.now(),
            "is_active": True,
            "is_staff": False,
            "is_superuser": True,
            "password": "Password123",
        }
    }
