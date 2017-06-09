# -*- coding: utf-8 -*-
from __future__ import absolute_import

from .base import BaseViewVerbTestCase


class HeaderKeyExistsTestCase(BaseViewVerbTestCase):
    """
    This is a test case for testing whether or not a header key is contained within all of the HTTP
    responses returned by the Street Art project.
    """

    def __init__(self, header_key=None, *args, **kwargs):
        self.header_key = header_key
        super(HeaderKeyExistsTestCase, self).__init__(*args, **kwargs)

    def runTest(self):
        """
        Tests that the HTTP response received from the view contains a header corresponding to
        self.header_key.
        :return: None
        """
        requestor = self._get_requestor_for_view(self.view)
        response = requestor.send_request_by_verb(self.verb, user_string="user_1")
        self._assert_response_has_header_key(
            response=response,
            header_key=self.header_key,
            message="Response from view %s with verb %s did not contain header key of %s. Keys were %s."
            % (self.view, self.verb, self.header_key, response._headers.keys())
        )


class HeaderValueAccurateTestCase(BaseViewVerbTestCase):
    """
    This is a test case for testing whether or not a response header has the expected value.
    """

    def __init__(self, header_key=None, header_value=None, *args, **kwargs):
        self.header_key = header_key
        self.header_value = header_value
        super(HeaderValueAccurateTestCase, self).__init__(*args, **kwargs)

    def runTest(self):
        """
        Tests that the HTTP response received from the view contains a header key and value corresponding
        to self.header_key and self.header_value.
        :return: None
        """
        requestor = self._get_requestor_for_view(self.view)
        response = requestor.send_request_by_verb(self.verb, user_string="user_1")
        self._assert_response_has_header_value(
            response=response,
            header_key=self.header_key,
            header_value=self.header_value,
            message="Response from view %s with verb %s did not contain expected header value of %s: %s. "
                    "Headers were %s."
            % (self.view, self.verb, self.header_key, self.header_value, response._headers)
        )
