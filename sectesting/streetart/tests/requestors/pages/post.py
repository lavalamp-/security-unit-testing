# -*- coding: utf-8 -*-
from __future__ import absolute_import

from ..base import BaseRequestor
from ...safaker import SaFaker


class PostListViewRequestor(BaseRequestor):
    """
    This is a requestor class for sending requests to the PostListView view.
    """

    supported_verbs = ["HEAD", "OPTIONS", "GET"]

    def get_url_path(self, user="user_1"):
        return "/"


class MyPostsListViewRequestor(BaseRequestor):
    """
    This is a requestor class for sending requests to the MyPostsList view.
    """

    supported_verbs = ["HEAD", "OPTIONS", "GET"]
    requires_auth = True

    def get_url_path(self, user="user_1"):
        return "/my-posts/"


class CreatePostViewRequestor(BaseRequestor):
    """
    This is a requestor class for sending requests to the CreatePostView view.
    """

    supported_verbs = ["HEAD", "OPTIONS", "GET", "POST", "PUT"]

    def get_post_data(self, user="user_1"):
        return SaFaker.get_create_post_kwargs()

    def get_put_data(self, user="user_1"):
        return SaFaker.get_create_post_kwargs()

    def get_url_path(self, user="user_1"):
        return "/new-post/"


class NewCreatePostViewRequestor(BaseRequestor):
    """
    This is a requestor class for sending requests to the NewCreatePostView view.
    """

    supported_verbs = ["HEAD", "OPTIONS", "GET", "POST", "PUT"]
    requires_auth = True

    def get_post_data(self, user="user_1"):
        return SaFaker.get_create_post_kwargs()

    def get_put_data(self, user="user_1"):
        return SaFaker.get_create_post_kwargs()

    def get_url_path(self, user="user_1"):
        return "/new-post-2/"


class SuccessfulPostDetailViewRequestor(BaseRequestor):
    """
    This is a requestor class for sending requests to the SuccessfulPostDetailView view.
    """

    supported_verbs = ["HEAD", "OPTIONS", "GET"]

    def get_url_path(self, user="user_1"):
        post = SaFaker.get_post_for_user(user)
        return "/post-successful/%s/" % (post.uuid,)


class PostDetailViewRequestor(BaseRequestor):
    """
    This is a requestor class for sending requests to the PostDetailView view.
    """

    supported_verbs = ["HEAD", "OPTIONS", "GET"]

    def get_url_path(self, user="user_1"):
        post = SaFaker.get_post_for_user(user)
        return "/view-post/%s/" % (post.uuid,)


class EditPostViewRequestor(BaseRequestor):
    """
    This is a requestor class for sending requests to the EditPostView view.
    """

    supported_verbs = ["HEAD", "OPTIONS", "GET", "POST", "PUT"]
    requires_auth = True

    def get_post_data(self, user="user_1"):
        return SaFaker.get_edit_post_kwargs()

    def get_put_data(self, user="user_1"):
        return SaFaker.get_edit_post_kwargs()

    def get_url_path(self, user="user_1"):
        post = SaFaker.get_post_for_user(user)
        return "/edit-post/%s/" % (post.uuid,)


class DeletePostViewRequestor(BaseRequestor):
    """
    This is a requestor class for sending requests to the DeletePostView view.
    """

    supported_verbs = ["HEAD", "OPTIONS", "GET", "POST", "DELETE"]
    requires_auth = True

    def get_url_path(self, user="user_1"):
        post = SaFaker.get_post_for_user(user)
        return "/delete-post/%s/" % (post.uuid,)
