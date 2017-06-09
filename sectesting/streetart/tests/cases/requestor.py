# -*- coding: utf-8 -*-
from __future__ import absolute_import

from .base import BaseViewTestCase
from ..registry import TestRequestorRegistry


class ViewHasRequestorTestCase(BaseViewTestCase):
    """
    This is a test case for testing whether or not a view has a corresponding requestor
    mapped to it.
    """

    def runTest(self):
        """
        Tests that the given view has a requestor mapped to it.
        :return: None
        """
        registry = TestRequestorRegistry.instance()
        self.assertTrue(
            registry.does_view_have_mapping(self.view),
            "No requestor found for view %s." % self.view,
        )
