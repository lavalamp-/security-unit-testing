# -*- coding: utf-8 -*-
from __future__ import absolute_import

from django import forms

from ..models import StreetArtPost


class NewStreetArtPostForm(forms.ModelForm):
    """
    This is a form for creating new street art posts.
    """

    image = forms.ImageField()

    class Meta:
        model = StreetArtPost
        fields = ["title", "description"]


class EditStreetArtPostForm(forms.ModelForm):
    """
    This is a form for editing a street art post.
    """

    class Meta:
        model = StreetArtPost
        fields = [
            "title",
            "description",
            "latitude",
            "longitude",
        ]
