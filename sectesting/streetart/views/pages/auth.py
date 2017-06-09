# -*- coding: utf-8 -*-
from __future__ import absolute_import

from .base import BaseFormView, BaseTemplateView
from ...forms import NewUserForm
from ...tests import requested_by


@requested_by("streetart.tests.requestors.pages.CreateUserViewRequestor")
class CreateUserView(BaseFormView):
    """
    This is a view for creating a new user.
    """

    template_name = "pages/register.html"
    form_class = NewUserForm
    success_url = "/register-success/"

    def form_valid(self, form):
        """
        Handle the processing of the form to create a new Street Art user.
        :param form: The form to process.
        :return: The HTTP redirect response from super.form_valid.
        """
        user = self._create_object(
            email=form.cleaned_data["email"],
            first_name=form.cleaned_data["first_name"],
            last_name=form.cleaned_data["last_name"],
            is_active=True,
            is_staff=False,
            is_superuser=False,
        )
        user.set_password(form.cleaned_data["password"])
        user.save()
        return super(CreateUserView, self).form_valid(form)


@requested_by("streetart.tests.requestors.pages.CreateUserSuccessRequestor")
class CreateUserSuccessView(BaseTemplateView):
    """
    This is a page for informing the user that their registration was successful.
    """

    template_name = "pages/register_success.html"
