# -*- coding: utf-8 -*-
from __future__ import absolute_import

from ..base import BaseRequestor


class RedirectViewRequestor(BaseRequestor):
    """
    This is a requestor class for sending requests to the RedirectView view.
    """

    supported_verbs = ["GET", "OPTIONS", "HEAD"]

    def get_url_path(self, user="user_1"):
        return "/redirect/"
