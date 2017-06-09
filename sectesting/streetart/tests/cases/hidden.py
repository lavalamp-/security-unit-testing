# -*- coding: utf-8 -*-
from __future__ import absolute_import

from .base import BaseViewTestCase, BaseViewVerbTestCase


class RegularUnknownMethodsTestCase(BaseViewTestCase):
    """
    This is a test case for testing whether or not a view returns the expected HTTP verbs through
    an OPTIONS request from a regular user.
    """

    def runTest(self):
        """
        Tests that the HTTP verbs returned by an OPTIONS request match the expected values.
        :return: None
        """
        requestor = self._get_requestor_for_view(self.view)
        response = requestor.send_options(user_string="user_1")
        allowed_verbs = response._headers.get("allow", None)
        if not allowed_verbs:
            raise ValueError("No allow header returned by view %s." % self.view)
        allowed_verbs = [x.strip().lower() for x in allowed_verbs[1].split(",")]
        supported_verbs = [x.lower() for x in requestor.supported_verbs]
        self.assertTrue(
            all([x.lower() in supported_verbs for x in allowed_verbs]),
            "Unexpected verbs found for view %s. Expected %s, got %s."
            % (self.view, [x.upper() for x in supported_verbs], [x.upper() for x in allowed_verbs])
        )


class AdminUnknownMethodsTestCase(BaseViewTestCase):
    """
    This is a test case for testing whether or not a view returns the expected HTTP verbs through
    an OPTIONS request from an admin user.
    """

    def runTest(self):
        """
        Tests that the HTTP verbs returned by an OPTIONS request match the expected values.
        :return: None
        """
        requestor = self._get_requestor_for_view(self.view)
        response = requestor.send_options(user_string="admin_1")
        allowed_verbs = response._headers.get("allow", None)
        if not allowed_verbs:
            raise ValueError("No allow header returned by view %s." % self.view)
        allowed_verbs = [x.strip().lower() for x in allowed_verbs[1].split(",")]
        supported_verbs = [x.lower() for x in requestor.supported_verbs]
        self.assertTrue(
            all([x.lower() in supported_verbs for x in allowed_verbs]),
            "Unexpected verbs found for view %s. Expected %s, got %s."
            % (self.view, [x.upper() for x in supported_verbs], [x.upper() for x in allowed_verbs])
        )


class RegularVerbNotSupportedTestCase(BaseViewVerbTestCase):
    """
    This is a test case for testing whether or not a given HTTP verb is denied when submitted against
    a view by a regular user.
    """

    def runTest(self):
        """
        Tests that self.verb does not work against self.view.
        :return: None
        """
        requestor = self._get_requestor_for_view(self.view)
        response = requestor.send_request_by_verb(self.verb, user_string="user_1")
        self._assert_response_not_allowed(
            response,
            "HTTP verb %s returned %s status code when it should have been 405 (regular user)."
            % (self.verb, response.status_code)
        )


class AdminVerbNotSupportedTestCase(BaseViewVerbTestCase):
    """
    This is a test case for testing whether or not a given HTTP verb is denied when submitted against
    a view by an admin user.
    """

    def runTest(self):
        """
        Tests that self.verb does not work against self.view.
        :return: None
        """
        requestor = self._get_requestor_for_view(self.view)
        response = requestor.send_request_by_verb(self.verb, user_string="admin_1")
        self._assert_response_not_allowed(
            response,
            "HTTP verb %s returned %s status code when it should have been 405 (admin user)."
            % (self.verb, response.status_code)
        )
