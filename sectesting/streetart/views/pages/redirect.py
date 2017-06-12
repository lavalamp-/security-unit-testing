# -*- coding: utf-8 -*-
from __future__ import absolute_import

from urlparse import urljoin

from django.shortcuts import redirect

from .base import BaseTemplateView
from ...tests import requested_by


@requested_by("streetart.tests.requestors.pages.RedirectViewRequestor")
class RedirectView(BaseTemplateView):
    """
    This is a view for redirecting users to various endpoints.
    """

    template_name = "pages/redirect.html"

    def get(self, request, *args, **kwargs):
        """
        Handle redirecting the user to the endpoint provided in the query string.
        :param request: The request to process.
        :param args: Positional arguments.
        :param kwargs: Keyword arguments.
        :return: The HTTP response.
        """
        if "redirect" in request.GET:
            host = request.get_host()
            redirect_target = request.GET["redirect"]
            target_url = urljoin(host, redirect_target)
            target_url = target_url.replace("://", "")
            return redirect(target_url)
        else:
            return super(RedirectView, self).get(request, *args, **kwargs)
