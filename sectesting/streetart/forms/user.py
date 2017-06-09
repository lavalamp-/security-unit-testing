# -*- coding: utf-8 -*-
from __future__ import absolute_import

from django import forms

from ..models import StreetArtUser


class NewUserForm(forms.ModelForm):
    """
    This is a form for handling the registration of a new user.
    """

    class Meta:
        model = StreetArtUser
        fields = [
            "email",
            "first_name",
            "last_name",
            "password",
        ]
