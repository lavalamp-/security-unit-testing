# -*- coding: utf-8 -*-
from __future__ import absolute_import

import re

from ..base import BaseStreetArtTestCase
from ....models import StreetArtPost
from ...safaker import SaFaker


class PersistentXSSPostViewTestCase(BaseStreetArtTestCase):
    """
    This is a test case for testing for persistent cross-site scripting on the view post
    page.
    """

    ENCODE_REGEX = re.compile("\[SHOULDENCODE\](.*?)\[/SHOULDENCODE\]")
    XSS_ENCODE_CHARS = "<>'\"&"
    XSS_ENCODED_OUTPUT = "&lt;&gt;&#39;&quot;&amp;"
    XSS_PAYLOAD = "[SHOULDENCODE]%s[/SHOULDENCODE]" % XSS_ENCODE_CHARS

    def runTest(self):
        """
        Tests to ensure that the persistent XSS vulnerability in the "view post" page is not
        present.
        :return: None
        """
        post_data = SaFaker.get_edit_post_kwargs()
        post_data["title"] = "TITLE %s" % self.XSS_PAYLOAD
        post_data["description"] = "DESCRIPTION %s" % self.XSS_PAYLOAD
        new_post = StreetArtPost.objects.create(**post_data)
        url = "/view-post/%s/" % new_post.uuid
        response = self.client.get(url)
        encoded_data = self.ENCODE_REGEX.findall(response.content)
        self.assertFalse(
            any([self.XSS_ENCODE_CHARS in x for x in encoded_data]),
            "Persistent XSS test failed for PostView. Extracted encoded data was %s."
            % (encoded_data,)
        )
