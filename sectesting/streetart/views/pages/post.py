# -*- coding: utf-8 -*-
from __future__ import absolute_import

from django.contrib.auth.mixins import LoginRequiredMixin
from django.core.exceptions import ValidationError
from uuid import uuid4
from django.conf import settings
from django.urls import reverse_lazy
from django.utils.decorators import method_decorator
from django.views.decorators.csrf import csrf_exempt

from ...models import StreetArtPost
from ...forms import NewStreetArtPostForm, EditStreetArtPostForm
from .base import BaseListView, BaseDetailView, BaseFormView, BaseUpdateView, BaseDeleteView
from lib import ImageProcessingHelper, InvalidImageFileException, S3Helper
from streetart.tests import requested_by


@requested_by("streetart.tests.requestors.pages.PostListViewRequestor")
class PostListView(BaseListView):
    """
    This is the main landing view that presents the user with all of the street art posts
    contained within the Street Art project database.
    """

    template_name = "pages/streetart_post_list.html"
    model = StreetArtPost
    paginate_by = 2


@requested_by("streetart.tests.requestors.pages.MyPostsListViewRequestor")
class MyPostsListView(LoginRequiredMixin, BaseListView):
    """
    This is a page for displaying all of the posts associated with the logged-in user.
    """

    template_name = "pages/streetart_post_list.html"
    model = StreetArtPost
    paginate_by = 2

    def get_queryset(self):
        """
        Get all of the posts that are associated with the requesting user.
        :return: All of the posts that are associated with the requesting user.
        """
        return self.request.user.posts.all()


@method_decorator(csrf_exempt, name="dispatch")
@requested_by("streetart.tests.requestors.pages.CreatePostViewRequestor")
class CreatePostView(BaseFormView):
    """
    This is a view for creating new street art posts.
    """

    template_name = "pages/new_streetart_post.html"
    form_class = NewStreetArtPostForm

    def form_valid(self, form):
        """
        Handle the processing of the uploaded image to S3 and add the expected fields to the saved
        StreetArtPost object.
        :param form: The form that was submitted.
        :return: The HTTP redirect response from super.form_valid.
        """
        try:
            image_processor = ImageProcessingHelper.from_in_memory_uploaded_file(form.files["image"])
        except InvalidImageFileException as e:
            raise ValidationError(e.message)
        latitude, longitude = image_processor.coordinates
        post_uuid = str(uuid4())
        s3_helper = S3Helper.instance()
        response = s3_helper.upload_file_to_bucket(
            local_file_path=form.files["image"].temporary_file_path(),
            key=post_uuid,
            bucket=settings.AWS_S3_BUCKET,
        )
        if response["ResponseMetadata"]["HTTPStatusCode"] != 200:
            raise ValueError("Unable to upload image file to Amazon S3.")
        user = self.request.user if self.request.user.is_authenticated else None
        self._create_object(
            latitude=latitude,
            longitude=longitude,
            title=form.cleaned_data["title"],
            description=form.cleaned_data["description"],
            s3_bucket=settings.AWS_S3_BUCKET,
            s3_key=post_uuid,
            uuid=post_uuid,
            user=user,
        )
        return super(CreatePostView, self).form_valid(form)

    def get_success_url(self):
        """
        Get the URL to redirect users to after a successful post creation.
        :return: The URL to redirect users to after a successful post creation.
        """
        return "/post-successful/%s/" % (self.created_object.uuid,)


@requested_by("streetart.tests.requestors.pages.SuccessfulPostDetailViewRequestor")
class SuccessfulPostDetailView(BaseDetailView):
    """
    This is the page for providing the user with details regarding the post that they uploaded.
    """

    template_name = "pages/streetart_post_successful.html"
    model = StreetArtPost


@requested_by("streetart.tests.requestors.pages.PostDetailViewRequestor")
class PostDetailView(BaseDetailView):
    """
    This is the page for providing the user with details regarding a single post.
    """

    template_name = "pages/streetart_post.html"
    model = StreetArtPost


@method_decorator(csrf_exempt, name="dispatch")
@requested_by("streetart.tests.requestors.pages.EditPostViewRequestor")
class EditPostView(LoginRequiredMixin, BaseUpdateView):
    """
    This is the page for editing the contents of a street art post object.
    """

    template_name = "pages/edit_streetart_post.html"
    form_class = EditStreetArtPostForm
    model = StreetArtPost


@method_decorator(csrf_exempt, name="dispatch")
@requested_by("streetart.tests.requestors.pages.DeletePostViewRequestor")
class DeletePostView(LoginRequiredMixin, BaseDeleteView):
    """
    This is the page for deleting the contents of a street art post object.
    """

    template_name = "pages/streetart_post_confirm_delete.html"
    model = StreetArtPost
    success_url = reverse_lazy("post-list")
