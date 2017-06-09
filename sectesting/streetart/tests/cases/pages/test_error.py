# -*- coding: utf-8 -*-
from __future__ import absolute_import

import re

from ..base import BaseStreetArtTestCase


class ErrorDetailsXSSTestCase(BaseStreetArtTestCase):
    """
    This is a test case for testing for reflected cross-site scripting on the error details page.
    """

    ENCODE_REGEX = re.compile("\[SHOULDENCODE\](.*?)\[/SHOULDENCODE\]")
    XSS_ENCODE_CHARS = "<>'\"&"
    XSS_ENCODED_OUTPUT = "&lt;&gt;&#39;&quot;&amp;"

    def runTest(self):
        """
        Test to ensure that the error details page is not vulnerable to cross-site scripting via its
        error query string parameter.
        :return: None
        """
        data = {
            "error": "[SHOULDENCODE]%s[/SHOULDENCODE]" % (self.XSS_ENCODE_CHARS,),
        }
        response = self.client.get("/error-details/", data=data)
        encoded_data = self.ENCODE_REGEX.findall(response.content)[0]
        self.assertEqual(
            encoded_data,
            self.XSS_ENCODED_OUTPUT,
            "XSS encoding characters (%s) were not properly encoded in response (%s)."
            % (self.XSS_ENCODE_CHARS, encoded_data)
        )
