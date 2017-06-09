# -*- coding: utf-8 -*-
from __future__ import absolute_import

from django.views.generic import ListView, DetailView, UpdateView, DeleteView
from django.views.generic.edit import FormView


class BaseListView(ListView):
    """
    This is a base class for all ListView pages used within the Street Art project.
    """


class BaseDetailView(DetailView):
    """
    This is a base class for all DetailView pages used within the Street Art project.
    """


class BaseFormView(FormView):
    """
    This is a base class for all FormView pages used within the Street Art project.
    """

    _created_object = None

    def _create_object(self, **create_kwargs):
        """
        Create an instance of the referenced model class and return it.
        :param create_kwargs: Keyword arguments to pass to the object create method.
        :return: The newly-created object.
        """
        self._created_object = self.form_class.Meta.model.objects.create(**create_kwargs)
        return self._created_object

    @property
    def created_object(self):
        """
        Get the model instance that was created by valid submission of the referenced form.
        :return: the model instance that was created by valid submission of the referenced form.
        """
        return self._created_object


class BaseUpdateView(UpdateView):
    """
    This is a base class for all UpdateView pages used within the Street Art project.
    """


class BaseDeleteView(DeleteView):
    """
    This is a base class for all DeleteView pages used within the Street Art project.
    """
