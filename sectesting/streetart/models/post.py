# -*- coding: utf-8 -*-
from __future__ import absolute_import

from django.db import models
from django.conf import settings

from lib import S3Helper
from .base import BaseStreetArtModel


class StreetArtPost(BaseStreetArtModel):
    """
    This is a model for containing all of the relevant data for a post referencing street art.
    """

    # Columns

    latitude = models.FloatField(null=True)
    longitude = models.FloatField(null=True)
    title = models.CharField(max_length=32, null=True)
    description = models.CharField(max_length=256, null=True)
    s3_bucket = models.CharField(max_length=32, null=True)
    s3_key = models.CharField(max_length=64, null=True)
    current_vote = models.IntegerField(default=0)

    # Foreign Keys

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="posts",
        on_delete=models.CASCADE,
        null=True,
    )

    # Methods

    def get_absolute_url(self):
        """
        Get the absolute URL to view the contents of this post at.
        :return: The absolute URL to view the contents of this post at.
        """
        return "/view-post/%s/" % (self.uuid,)

    # Properties

    @property
    def coordinates_string(self):
        """
        Get a string representing the coordinates where this photograph was taken.
        :return: a string representing the coordinates where this photograph was taken.
        """
        return "%s, %s" % (self.latitude, self.longitude)

    @property
    def has_coordinates(self):
        """
        Get whether or not this post has coordinates associated with it.
        :return: whether or not this post has coordinates associated with it.
        """
        return self.latitude is not None and self.longitude is not None

    @property
    def s3_url(self):
        """
        Get a signed URL to retrieve the referenced image from Amazon S3.
        :return: a signed URL to retrieve the referenced image from Amazon S3.
        """
        s3_helper = S3Helper.instance()
        return s3_helper.get_signed_url_for_key(key=str(self.uuid), bucket=settings.AWS_S3_BUCKET)


class StreetArtPostVote(BaseStreetArtModel):
    """
    This is a model for containing all of the relevant data for a vote cast by a user for a given
    street art post.
    """

    # Columns

    vote_direction = models.BooleanField(null=False)

    # Foreign Keys

    user = models.ForeignKey(
        settings.AUTH_USER_MODEL,
        related_name="votes",
        on_delete=models.CASCADE,
    )

    post = models.ForeignKey(
        "streetart.StreetArtPost",
        related_name="votes",
        on_delete=models.CASCADE,
    )

    # Class Meta

    class Meta:
        unique_together = (
            ("user", "post")
        )
