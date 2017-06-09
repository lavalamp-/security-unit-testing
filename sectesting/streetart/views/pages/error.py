# -*- coding: utf-8 -*-
from __future__ import absolute_import

from .base import BaseTemplateView
from ...tests import requested_by


@requested_by("streetart.tests.requestors.pages.ErrorDetailsViewRequestor")
class ErrorDetailsView(BaseTemplateView):
    """
    This is a page for displaying error information to the user.
    """

    template_name = "pages/error_details.html"

    def get_context_data(self, **kwargs):
        to_return = super(ErrorDetailsView, self).get_context_data(**kwargs)
        to_return["error_text"] = self.request.GET.get("error", "No error details provided.")
        return to_return
