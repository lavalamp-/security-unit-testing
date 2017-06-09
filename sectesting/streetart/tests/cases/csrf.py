# -*- coding: utf-8 -*-
from __future__ import absolute_import

from .base import BaseViewVerbTestCase


class CsrfEnforcementTestCase(BaseViewVerbTestCase):
    """
    This is a test case for testing that a CSRF token is properly enforced on a view with
    a given verb via a request that is submitted by a regular user.
    """

    def runTest(self):
        """
        Test to ensure that that the CSRF token is properly enforced on the referenced view.
        :return: None
        """
        requestor = self._get_requestor_for_view(self.view)
        response = requestor.send_request_by_verb(
            self.verb,
            user_string="user_1",
            enforce_csrf_checks=True,
        )
        self._assert_response_permission_denied(
            response,
            "Response from %s indicated that CSRF protection was not enabled (verb was %s, status %s)."
            % (self.view, self.verb, response.status_code)
        )
