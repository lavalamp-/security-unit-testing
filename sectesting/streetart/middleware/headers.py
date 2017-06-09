# -*- coding: utf-8 -*-
from __future__ import absolute_import


class SecurityHeadersMiddleware(object):
    """
    This is a middleware class for handling the addition of HTTP security headers to all
    responses.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response["X-Frame-Options"] = "deny"
        response["X-Content-Type-Options"] = "nosniff"
        response["X-XSS-Protection"] = "1; mode=block"
        response["X-Permitted-Cross-Domain-Policies"] = "none"
        return response
