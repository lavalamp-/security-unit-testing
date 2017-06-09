# -*- coding: utf-8 -*-
from __future__ import absolute_import

from .base import BaseViewTestCase


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
        if "head" in allowed_verbs:
            allowed_verbs.remove("head")
        if "options" in allowed_verbs:
            allowed_verbs.remove("options")
        supported_verbs = [x.lower() for x in requestor.supported_verbs]
        self.assertTrue(
            all([x.lower() in supported_verbs for x in allowed_verbs]),
            "Unexpected verbs found for view %s. Expected %s, got %s."
            % (self.view, [x.upper() for x in supported_verbs], [x.upper() for x in allowed_verbs])
        )
