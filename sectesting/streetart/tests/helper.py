# -*- coding: utf-8 -*-
from __future__ import absolute_import

from django.urls import RegexURLPattern, RegexURLResolver


class UrlPatternHelper(object):
    """
    This is a class that contains helper methods for extracting URL patterns and their
    related views from the URL configuration of a Django application.
    """

    # Class Members

    # Instantiation

    # Static Methods

    @staticmethod
    def get_all_streetart_views(
            include_admin_views=False,
            include_auth_views=False,
            include_generic_views=False,
            include_contenttype_views=False,
    ):
        """
        Get a list of tuples containing (1) the URL pattern regex, (2) the pattern name, and (3) the
        callback function for all of the registered URLs in the Street Art project.
        :param include_admin_views: Whether or not to include administrative views.
        :param include_auth_views: Whether or not to include default Django authentication views.
        :param include_generic_views: Whether or not to include default Django generic views.
        :param include_contenttype_views: Whether or not to include default Django contenttype views.
        :return: A list of tuples containing (1) the URL pattern regex, (2) the pattern name, and (3) the
        callback function for all of the registered URLs in the Street Art project.
        """
        from sectesting.urls import urlpatterns as streetart_urlpatterns
        to_return = UrlPatternHelper.get_all_views_from_patterns(streetart_urlpatterns)
        if not include_admin_views:
            to_return = filter(lambda x: not x[2].__module__.startswith("django.contrib.admin"), to_return)
        if not include_auth_views:
            to_return = filter(lambda x: not x[2].__module__.startswith("django.contrib.auth"), to_return)
        if not include_generic_views:
            to_return = filter(lambda x: not x[2].__module__.startswith("django.views.generic"), to_return)
        if not include_contenttype_views:
            to_return = filter(lambda x: not x[2].__module__.startswith("django.contrib.contenttypes"), to_return)
        return to_return

    @staticmethod
    def get_all_views_from_patterns(url_patterns):
        """
        Get a list of tuples containing (1) the URL pattern regex, (2) the pattern name, and (3) the
        callback function for all of the registered URLs in the given list of URL patterns.
        :param url_patterns: A list of URL patterns to process.
        :return: A list of tuples containing (1) the URL pattern regex, (2) the pattern name, and (3) the
        callback function for all of the registered URLs in the given list of URL patterns.
        """
        to_return = []
        for pattern in url_patterns:
            if isinstance(pattern, RegexURLResolver):
                to_return.extend(UrlPatternHelper.get_all_views_from_patterns(pattern.url_patterns))
            elif isinstance(pattern, RegexURLPattern):
                to_return.append((pattern.regex, pattern.name, pattern.callback))
        return to_return

    # Class Methods

    # Public Methods

    # Protected Methods

    # Private Methods

    # Properties

    # Representation and Comparison

    def __repr__(self):
        return "<%s>" % (self.__class__.__name__,)

