# -*- coding: utf-8 -*-
from __future__ import absolute_import

from .base import BaseStreetArtTestCase
from ..registry import TestRequestorRegistry


class RegularViewRequestIsSuccessfulTestCase(BaseStreetArtTestCase):
    """
    This is a test case for testing whether or not a view returns a HTTP response indicating
    that the request was successful for a regular user.
    """

    def __init__(self, view=None, verb=None, *args, **kwargs):
        self.view = view
        self.verb = verb
        super(RegularViewRequestIsSuccessfulTestCase, self).__init__(*args, **kwargs)

    def runTest(self):
        """
        Tests that the given view returns a successful HTTP response for the given verb.
        :return: None
        """
        requestor = self._get_requestor_for_view(self.view)
        response = requestor.send_request_by_verb(self.verb, user_string="user_1")
        self._assert_response_successful(
            response,
            "%s did not return a successful response for %s verb (%s status, regular user)"
            % (self.view, self.verb, response.status_code)
        )


class AdminViewRequestIsSuccessfulTestCase(BaseStreetArtTestCase):
    """
    This is a test case for testing whether or not a view returns a HTTP response indicating
    that the request was successful for an admin user.
    """

    def __init__(self, view=None, verb=None, *args, **kwargs):
        self.view = view
        self.verb = verb
        super(AdminViewRequestIsSuccessfulTestCase, self).__init__(*args, **kwargs)

    def runTest(self):
        """
        Tests that the given view returns a successful HTTP response for the given verb.
        :return: None
        """
        requestor = self._get_requestor_for_view(self.view)
        response = requestor.send_request_by_verb(self.verb, user_string="admin_1")
        self._assert_response_successful(
            response,
            "%s did not return a successful response for %s verb (%s status, admin user)"
            % (self.view, self.verb, response.status_code)
        )
