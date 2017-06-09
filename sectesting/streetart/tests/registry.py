# -*- coding: utf-8 -*-
from __future__ import absolute_import

from lib import Singleton
from .requestors import BaseRequestor


class InvalidRequestorException(Exception):
    """
    This is an exception for denoting that a given class is not of the expected type for
    requestor instances.
    """


class RequestorNotFoundException(Exception):
    """
    This is an exception for denoting that a requestor class cannot be found based on a
    class path.
    """


def requested_by(requestor_path):
    """
    This is a decorator for views that maps a requestor class to the view that it is configured to
    submit requests to.
    :param requestor_path: A string depicting the local file path to the requestor class for the given
    view.
    :return: A function that maps the view class to the requestor path and returns the called function
    or class.
    """

    def decorator(to_wrap):

        registry = TestRequestorRegistry.instance()
        registry.add_mapping(requestor_path=requestor_path, requested_view=to_wrap)
        return to_wrap

    return decorator


@Singleton
class TestRequestorRegistry(object):
    """
    This is a class that maintains mappings from views to test cases that are configured to
    send HTTP requests to the view in question.
    """

    # Class Members

    # Instantiation

    def __init__(self):
        self._registry = {}

    # Static Methods

    # Class Methods

    # Public Methods

    def add_mapping(self, requestor_path=None, requested_view=None):
        """
        Add a mapping from the view to the given requestor class specified by requestor_path.
        :param requestor_path: The path to the requestor class configured for the given view.
        :param requested_view: The view that the requestor is meant to send requests for.
        :return: None
        """
        try:
            requestor_class = self.__import_class(requestor_path)
        except (ImportError, AttributeError) as e:
            raise RequestorNotFoundException(
                "Unable to load requestor at %s: %s."
                % (requestor_path, e.message)
            )
        if not issubclass(requestor_class, BaseRequestor):
            raise InvalidRequestorException(
                "Class of %s is not a valid requestor class."
                % (requestor_class.__name__,)
            )
        self._registry[requested_view] = requestor_class

    def does_view_have_mapping(self, view):
        """
        Check to see if a mapping exists between the given view and a requestor class.
        :param view: The view to check a mapping for.
        :return: Whether or not a mapping exists for the given view.
        """
        return view in self.registry

    def get_requestor_for_view(self, view):
        """
        Get the requestor configured to send requests to the given view.
        :param view: The view to retrieve the requestor for.
        :return: The requestor configured to send requests to the given view.
        """
        return self.registry[view]

    # Protected Methods

    # Private Methods

    def __import_class(self, class_path):
        """
        Import the class at the given class path and return it.
        :param class_path: The class path to the class to load.
        :return: The loaded class.
        """
        components = class_path.split(".")
        mod = __import__(components[0])
        for component in components[1:]:
            mod = getattr(mod, component)
        return mod

    # Properties

    @property
    def registry(self):
        """
        Get the registry mapping functions and classes to the test classes that are configured to
        submit HTTP requests to them.
        :return: the registry mapping functions and classes to the test classes that are
        configured to submit HTTP requests to them.
        """
        return self._registry

    # Representation and Comparison
