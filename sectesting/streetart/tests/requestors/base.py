# -*- coding: utf-8 -*-
from __future__ import absolute_import

from django.test import Client

from ..safaker import SaFaker


class BaseRequestor(object):
    """
    This is a base class for all requestor classes used by the Street Art project.
    """

    # Class Members

    requires_auth = False
    supported_verbs = []

    # Instantiation

    # Static Methods

    # Class Methods

    # Public Methods

    def get_delete_data(self, user="user_1"):
        """
        Get a dictionary containing data to submit in HTTP DELETE requests to the view.
        :param user: A string depicting the user to get DELETE data for.
        :return: A dictionary containing data to submit in HTTP DELETE requests to the view.
        """
        return None

    def get_get_data(self, user="user_1"):
        """
        Get a dictionary containing data to submit in HTTP GET requests to the view.
        :param user: A string depicting the user to get POST data for.
        :return: A dictionary containing data to submit in HTTP GET requests to the view.
        """
        return None

    def get_patch_data(self, user="user_1"):
        """
        Get a dictionary containing data to submit in HTTP PATCH requests to the view.
        :param user: A string depicting the user to get PATCH data for.
        :return: A dictionary containing data to submit in HTTP PATCH requests to the view.
        """
        return None

    def get_post_data(self, user="user_1"):
        """
        Get a dictionary containing data to submit in HTTP POST requests to the view.
        :param user: A string depicting the user to get POST data for.
        :return: A dictionary containing data to submit in HTTP POST requests to the view.
        """
        return None

    def get_put_data(self, user="user_1"):
        """
        Get a dictionary containing data to submit in HTTP PUT requests to the view.
        :param user: A string depicting the user to get PUT data for.
        :return: A dictionary containing data to submit in HTTP PUT requests to the view.
        """
        return None

    def get_trace_data(self, user="user_1"):
        """
        Get a dictionary containing data to submit in HTTP TRACE requests to the view.
        :param user: A string depicting the user to get TRACE data for.
        :return: A dictionary containing data to submit in HTTP TRACE requests to the view.
        """
        return None

    def get_url_path(self, user="user_1"):
        """
        Get the URL path to request through the methods found in this class.
        :param user: A string depicting the user that the requested URL should be generated off
        of.
        :return: A string depicting the URL path to request.
        """
        return None

    def send_delete(self, user_string="user_1", do_auth=True, *args, **kwargs):
        """
        Send a DELETE request to the configured URL endpoint on behalf of the given user.
        :param user_string: The user to send the request as.
        :param do_auth: Whether or not to log the user in if the view requires authentication.
        :param args: Positional arguments for client.delete.
        :param kwargs: Keyword arguments for client.delete.
        :return: The HTTP response.
        """
        client = Client()
        if self.requires_auth and do_auth:
            user = SaFaker.get_user(user_string)
            client.force_login(user)
        return client.delete(
            self.get_url_path(user=user_string),
            data=self.get_delete_data(user=user_string),
            *args,
            **kwargs
        )

    def send_get(self, user_string="user_1", do_auth=True, *args, **kwargs):
        """
        Send a GET request to the configured URL endpoint on behalf of the given user.
        :param user_string: The user to send the request as.
        :param do_auth: Whether or not to log the user in if the view requires authentication.
        :param args: Positional arguments for client.get.
        :param kwargs: Keyword arguments for client.get.
        :return: The HTTP response.
        """
        client = Client()
        if self.requires_auth and do_auth:
            user = SaFaker.get_user(user_string)
            client.force_login(user)
        return client.get(
            self.get_url_path(user=user_string),
            data=self.get_get_data(user=user_string),
            *args,
            **kwargs
        )

    def send_head(self, user_string="user_1", do_auth=True, *args, **kwargs):
        """
        Send a HEAD request to the configured URL endpoint on behalf of the given user.
        :param user_string: The user to send the request as.
        :param do_auth: Whether or not to log the user in if the view requires authentication.
        :param args: Positional arguments for client.head.
        :param kwargs: Keyword arguments for client.head.
        :return: The HTTP response.
        """
        client = Client()
        if self.requires_auth and do_auth:
            user = SaFaker.get_user(user_string)
            client.force_login(user)
        return client.head(
            self.get_url_path(user=user_string),
            *args,
            **kwargs
        )

    def send_options(self, user_string="user_1", do_auth=True, *args, **kwargs):
        """
        Send an OPTIONS request to the configured URL endpoint on behalf of the given user.
        :param user_string: The user to send the request as.
        :param do_auth: Whether or not to log the user in if the view requires authentication.
        :param args: Positional arguments for client.options.
        :param kwargs: Keyword arguments for client.options.
        :return: The HTTP response.
        """
        client = Client()
        if self.requires_auth and do_auth:
            user = SaFaker.get_user(user_string)
            client.force_login(user)
        return client.options(
            self.get_url_path(user=user_string),
            *args,
            **kwargs
        )

    def send_patch(self, user_string="user_1", do_auth=True, *args, **kwargs):
        """
        Send a PATCH request to the configured URL endpoint on behalf of the given user.
        :param user_string: The user to send the request as.
        :param do_auth: Whether or not to log the user in if the view requires authentication.
        :param args: Positional arguments for client.patch.
        :param kwargs: Keyword arguments for client.patch.
        :return: The HTTP response.
        """
        client = Client()
        if self.requires_auth and do_auth:
            user = SaFaker.get_user(user_string)
            client.force_login(user)
        return client.patch(
            self.get_url_path(user=user_string),
            data=self.get_patch_data(user=user_string),
            *args,
            **kwargs
        )

    def send_post(self, user_string="user_1", do_auth=True, *args, **kwargs):
        """
        Send a POST request to the configured URL endpoint on behalf of the given user.
        :param user_string: The user to send the request as.
        :param do_auth: Whether or not to log the user in if the view requires authentication.
        :param args: Positional arguments for client.post.
        :param kwargs: Keyword arguments for client.post.
        :return: The HTTP response.
        """
        client = Client()
        if self.requires_auth and do_auth:
            user = SaFaker.get_user(user_string)
            client.force_login(user)
        return client.post(
            self.get_url_path(user=user_string),
            data=self.get_post_data(user=user_string),
            *args,
            **kwargs
        )

    def send_put(self, user_string="user_1", do_auth=True, *args, **kwargs):
        """
        Send a PUT request to the configured URL endpoint on behalf of the given user.
        :param user_string: The user to send the request as.
        :param do_auth: Whether or not to log the user in if the view requires authentication.
        :param args: Positional arguments for client.put.
        :param kwargs: Keyword arguments for client.put.
        :return: The HTTP response.
        """
        client = Client()
        if self.requires_auth and do_auth:
            user = SaFaker.get_user(user_string)
            client.force_login(user)
        return client.put(
            self.get_url_path(user=user_string),
            data=self.get_put_data(user=user_string),
            *args,
            **kwargs
        )

    def send_request_by_verb(self, verb, *args, **kwargs):
        """
        Send a request to the configured view based on the given verb.
        :param verb: The verb to send the request as.
        :param args: Positional arguments for the send method.
        :param kwargs: Keyword arguments for the send method.
        :return: The HTTP response.
        """
        verb = verb.lower()
        if verb == "get":
            return self.send_get(*args, **kwargs)
        elif verb == "post":
            return self.send_post(*args, **kwargs)
        elif verb == "options":
            return self.send_options(*args, **kwargs)
        elif verb == "delete":
            return self.send_delete(*args, **kwargs)
        elif verb == "put":
            return self.send_put(*args, **kwargs)
        elif verb == "head":
            return self.send_head(*args, **kwargs)
        elif verb == "patch":
            return self.send_patch(*args, **kwargs)
        elif verb == "trace":
            return self.send_trace(*args, **kwargs)
        else:
            raise ValueError(
                "Unsure of how to handle HTTP verb of %s."
                % (verb.upper(),)
            )

    def send_trace(self, user_string="user_1", do_auth=True, *args, **kwargs):
        """
        Send a TRACE request to the configured URL endpoint on behalf of the given user.
        :param user_string: The user to send the request as.
        :param do_auth: Whether or not to log the user in if the view requires authentication.
        :param args: Positional arguments for client.trace.
        :param kwargs: Keyword arguments for client.trace.
        :return: The HTTP response.
        """
        client = Client()
        if self.requires_auth and do_auth:
            user = SaFaker.get_user(user_string)
            client.force_login(user)
        return client.trace(
            self.get_url_path(user=user_string),
            data=self.get_trace_data(user=user_string),
            *args,
            **kwargs
        )

    # Protected Methods

    # Private Methods

    # Properties

    # Representation and Comparison

    def __repr__(self):
        return "<%s - %s>" % (self.__class__.__name__, self.get_url_path())
