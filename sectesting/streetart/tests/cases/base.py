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

    def _assert_response_has_header_key(self, response=None, header_key=None, message=None):
        """
        Assert that the given response contains a header corresponding to the given header key.
        :param response: The response to check.
        :param header_key: The header key to check.
        :param message: The message to print upon failure.
        :return: None
        """
        self.assertIn(
            header_key.lower(),
            [x.lower() for x in response._headers.keys()],
            msg=message,
        )

    def _assert_response_has_header_value(
            self,
            response=None,
            header_key=None,
            header_value=None,
            message=None,
    ):
        """
        Assert that the given response contains a header corresponding to the given key and value.
        :param response: The response to check.
        :param header_key: The header key.
        :param header_value: The header value.
        :param message: The message to print upon failure.
        :return: None
        """
        response_header_value = response._headers[header_key.lower()][1]
        self.assertEqual(response_header_value, header_value, msg=message)

    def _assert_response_not_has_header_key(self, response=None, header_key=None, message=None):
        """
        Assert that the given response does not contain a header corresponding to the given header
        key.
        :param response: The response to check.
        :param header_key: The header key to check.
        :param message: The message to print upon failure.
        :return: None
        """
        self.assertNotIn(
            header_key.lower(),
            [x.lower() for x in response._headers.keys()],
            msg=message,
        )

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


class BaseViewTestCase(BaseStreetArtTestCase):
    """
    This is a base class for all test cases that run tests on a view specified within the test
    case constructor.
    """

    def __init__(self, view=None, *args, **kwargs):
        self.view = view
        super(BaseViewTestCase, self).__init__(*args, **kwargs)


class BaseViewVerbTestCase(BaseViewTestCase):
    """
    This is a base class for all test cases that run tests on a view and a verb specified within the
    test case constructor.
    """

    def __init__(self, verb=None, *args, **kwargs):
        self.verb = verb
        super(BaseViewVerbTestCase, self).__init__(*args, **kwargs)

