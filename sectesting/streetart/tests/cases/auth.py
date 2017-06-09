# -*- coding: utf-8 -*-
from __future__ import absolute_import

from .base import BaseStreetArtTestCase


class AuthenticationEnforcementTestCase(BaseStreetArtTestCase):
    """
    This is a test case for testing whether or not authentication is properly enforced on a
    view.
    """

    def __init__(self, view=None, verb=None, *args, **kwargs):
        self.view = view
        self.verb = verb
        super(AuthenticationEnforcementTestCase, self).__init__(*args, **kwargs)

    def runTest(self):
        """
        Tests that the given view returns the expected HTTP response value when an unauthenticated
        request is submitted to it.
        :return: None
        """
        requestor = self._get_requestor_for_view(self.view)
        response = requestor.send_request_by_verb(self.verb, do_auth=False)
        self._assert_response_permission_denied(
            response,
            "Response from unauthenticated request to view %s was %s. Expected %s."
            % (self.view, response.status_code, 403)
        )
