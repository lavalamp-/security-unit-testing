# -*- coding: utf-8 -*-
from __future__ import absolute_import

from ..base import BaseStreetArtTestCase


class RedirectViewTestCase(BaseStreetArtTestCase):
    """
    This is a test case for testing for open redirects in the RedirectView view.
    """

    def runTest(self):
        """
        Tests to ensure that the RedirectView view is not vulnerable to open redirects.
        :return: None
        """
        target_url = "http://www.google.com"
        response = self.client.get("/redirect/?redirect=%s" % target_url)
        self.assertNotEqual(
            response["location"],
            target_url,
            msg="Redirect allowed for open redirect to target URL of %s."
            % (target_url,)
        )
