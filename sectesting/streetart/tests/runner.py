# -*- coding: utf-8 -*-
from __future__ import absolute_import

from django.test.runner import DiscoverRunner
from django.conf import settings

from .registry import TestRequestorRegistry
from .helper import UrlPatternHelper
from .cases import ViewHasRequestorTestCase, RegularViewRequestIsSuccessfulTestCase, \
    AdminViewRequestIsSuccessfulTestCase, RegularUnknownMethodsTestCase
from .safaker import SaFaker


def get_view_from_callback(callback):
    """
    Get the view associated with the given callback.
    :param callback: The callback to get the view from.
    :return: The view associated with the given callback.
    """
    if hasattr(callback, "view_class"):
        return callback.view_class
    else:
        return callback


class StreetArtTestRunner(DiscoverRunner):
    """
    This is a custom discover runner for populating unit tests for the Street Art project.
    """

    # Class Members

    # Instantiation

    def __init__(self, *args, **kwargs):
        self._url_patterns = None
        super(StreetArtTestRunner, self).__init__(*args, **kwargs)

    # Static Methods

    # Class Methods

    # Public Methods

    def build_suite(self, test_labels=None, extra_tests=None, **kwargs):
        """
        Build the test suite to run for this discover runner.
        :param test_labels: A list of strings describing the tests to be run.
        :param extra_tests: A list of extra TestCase instances to add to the suite that is
        executed by the test runner.
        :param kwargs: Additional keyword arguments.
        :return: The test suite.
        """
        extra_tests = extra_tests if extra_tests is not None else []
        extra_tests.extend(self.__get_generated_test_cases())
        return super(StreetArtTestRunner, self).build_suite(
            test_labels=test_labels,
            extra_tests=extra_tests,
            **kwargs
        )

    def run_suite(self, suite, **kwargs):
        """
        Override the run_suite functionality to populate the database.
        :param suite: The suite to run.
        :param kwargs: Keyword arguments.
        :return: The rest suite result.
        """
        self.__populate_database()
        return super(StreetArtTestRunner, self).run_suite(suite, **kwargs)

    # Protected Methods

    # Private Methods

    def __get_dos_class_tests(self):
        """
        Get a list of test cases that will test to ensure that all of the configured URL routes
        return successful HTTP status codes.
        :return: A list of test cases that will test to ensure that all of the configured URL routes
        return successful HTTP status codes.
        """
        to_return = []
        registry = TestRequestorRegistry.instance()
        for _, _, callback in self.url_patterns:
            view = self.__get_view_from_callback(callback)
            requestor = registry.get_requestor_for_view(view)
            class AnonTestCase1(RegularViewRequestIsSuccessfulTestCase):
                pass
            class AnonTestCase2(AdminViewRequestIsSuccessfulTestCase):
                pass
            for supported_verb in requestor.supported_verbs:
                to_return.append(AnonTestCase1(view=view, verb=supported_verb))
                to_return.append(AnonTestCase2(view=view, verb=supported_verb))
        return to_return

    def __get_generated_test_cases(self):
        """
        Get a list containing the automatically generated test cases to add to the test suite
        this runner is configured to run.
        :return: A list containing the automatically generated test cases to add to the test suite
        this runner is configured to run.
        """

        # Ensure that all views are loaded
        import sectesting.urls

        to_return = []
        if settings.TEST_FOR_REQUESTOR_CLASSES:
            to_return.extend(self.__get_requestor_class_tests())
        if settings.TEST_FOR_DENIAL_OF_SERVICE:
            to_return.extend(self.__get_dos_class_tests())
        if settings.TEST_FOR_UNKNOWN_METHODS:
            to_return.extend(self.__get_unknown_methods_tests())
        return to_return

    def __get_requestor_class_tests(self):
        """
        Get a list of test cases that will test the views associated with the Street Art project to ensure
        that the view has a requestor class associated with it.
        :return: A list of test cases that will test the views associated with the Street Art project to ensure
        that the view has a requestor class associated with it.
        """
        to_return = []
        for _, _, callback in self.url_patterns:
            class AnonTestCase(ViewHasRequestorTestCase):
                pass
            to_return.append(AnonTestCase(self.__get_view_from_callback(callback)))
        return to_return

    def __get_unknown_methods_tests(self):
        """
        Get a list of test cases that will test whether or not views return the expected HTTP verbs
        through OPTIONS requests.
        :return: A list of test cases that will test whether or not views return the expected HTTP verbs
        through OPTIONS requests.
        """
        to_return = []
        for _, _, callback in self.url_patterns:
            view = self.__get_view_from_callback(callback)
            class AnonTestCase1(RegularUnknownMethodsTestCase):
                pass
            to_return.append(AnonTestCase1(view))
        return to_return

    def __get_view_from_callback(self, callback):
        """
        Get the view associated with the given callback.
        :param callback: The callback to get the view from.
        :return: The view associated with the given callback.
        """
        if hasattr(callback, "view_class"):
            return callback.view_class
        else:
            return callback

    def __populate_database(self):
        """
        Populate the database with dummy database models.
        :return: None
        """
        print("Now populating test database...")
        SaFaker.create_users()

    # Properties

    @property
    def url_patterns(self):
        """
        Get a list of tuples containing (1) the URL pattern regex, (2) the pattern name, and (3) the
        callback function for the views that this runner should generate automated tests for.
        :return: a list of tuples containing (1) the URL pattern regex, (2) the pattern name, and (3) the
        callback function for the views that this runner should generate automated tests for.
        """
        if self._url_patterns is None:
            self._url_patterns = UrlPatternHelper.get_all_streetart_views(
                include_admin_views=settings.INCLUDE_ADMIN_VIEWS_IN_TESTS,
                include_auth_views=settings.INCLUDE_AUTH_VIEWS_IN_TESTS,
                include_generic_views=settings.INCLUDE_GENERIC_VIEWS_IN_TESTS,
                include_contenttype_views=settings.INCLUDE_CONTENTTYPE_VIEWS_IN_TESTS,
            )
        return self._url_patterns

    # Representation and Comparison

    def __repr__(self):
        return "<%s>" % (self.__class__.__name__,)

