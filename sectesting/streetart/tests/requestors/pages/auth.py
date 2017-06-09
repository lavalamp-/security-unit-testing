# -*- coding: utf-8 -*-
from __future__ import absolute_import

from ..base import BaseRequestor
from ...safaker import SaFaker


class CreateUserViewRequestor(BaseRequestor):
    """
    This is a requestor class for sending requests to the CreateUserView view.
    """

    supported_verbs = ["GET", "POST", "PUT"]

    def get_post_data(self, user="user_1"):
        return SaFaker.get_create_user_kwargs()

    def get_put_data(self, user="user_1"):
        return SaFaker.get_create_user_kwargs()

    def get_url_path(self, user="user_1"):
        return "/register/"


class CreateUserSuccessRequestor(BaseRequestor):
    """
    This is a requestor class for sending requests to the create_user_success view.
    """

    supported_verbs = ["GET"]

    def get_url_path(self, user="user_1"):
        return "/register-success/"
