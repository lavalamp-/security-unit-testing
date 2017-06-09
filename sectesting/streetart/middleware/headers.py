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


class BadHeadersMiddleware(object):
    """
    This is a middleware class for adding some SUPER SENSITIVE stuff to HTTP response headers.
    """

    def __init__(self, get_response):
        self.get_response = get_response

    def __call__(self, request):
        response = self.get_response(request)
        response["X-Supah-Secret"] = "THIS IS TOTALLY MY PASSWORD"
        response["X-Supah-Dupah-Secret"] = "AND THIS IS A PRIVATE KEY LOLZ"
        return response
