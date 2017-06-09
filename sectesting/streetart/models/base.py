# -*- coding: utf-8 -*-
from __future__ import absolute_import

import uuid
from django.db import models


class BaseStreetArtModel(models.Model):
    """
    This is a base model for all models used by the Street Art project.
    """

    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ("created",)
        abstract = True

    def __repr__(self):
        return "<%s - %s>" % (self.__class__.__name__, self.uuid)
