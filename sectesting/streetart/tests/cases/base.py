# -*- coding: utf-8 -*-
from __future__ import absolute_import

from django.test import TestCase

from ..registry import TestRequestorRegistry


class BaseStreetArtTestCase(TestCase):
    """
    This is a base class for all test cases used by the Street Art project.
    """

    # Class Members

    # Instantiation

    # Static Methods

    # Class Methods

    # Public Methods

    # Protected Methods

    def _assert_response_permission_denied(self, response, message):
        """
        Assert that the contents of the given response indicate that the request did
        not have sufficient permissions.
        :param response: The response to check.
        :param message: The message to print upon failure.
        :return: None
        """
        self.assertEqual(response.status_code, 403, msg=message)

    def _assert_response_successful(self, response, message):
        """
        Assert that the contents of the given response indicate a successful response.
        :param response: The response to check.
        :param message: The message to print upon failure.
        :return: None
        """
        self.assertIn(
            response.status_code,
            [200, 201, 202, 301, 302],
            msg=message,
        )

    def _get_requestor_for_view(self, view):
        """
        Get the requestor class to use to send requests to the given view.
        :param view: The view to retrieve the requestor class for.
        :return: The requestor class to use to send requests to the given view.
        """
        registry = TestRequestorRegistry.instance()
        return registry.get_requestor_for_view(view)()

    # Private Methods

    # Properties

    # Representation and Comparison

    def __repr__(self):
        return "<%s>" % (self.__class__.__name__,)

