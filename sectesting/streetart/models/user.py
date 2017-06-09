# -*- coding: utf-8 -*-
from __future__ import absolute_import

from django.contrib.auth.models import AbstractBaseUser
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.contrib.auth.models import PermissionsMixin
from django.core.mail import send_mail
from django.contrib.auth.base_user import BaseUserManager

from .base import BaseStreetArtModel


class StreetArtUserManager(BaseUserManager):
    """
    This is the manager class for managing the creation of users for the Street Art project.
    """

    use_in_migrations = True

    def _create_user(self, email, password, **extra_fields):
        """
        Create and save a user with the given email address and password.
        :param email: The email to assign the user.
        :param password: The password to assign the user.
        :param extra_fields: Extra fields to attribute to the user.
        :return: The created user object.
        """
        if not email:
            raise ValueError("The given email must be set.")
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_user(self, email, password=None, **extra_fields):
        """
        Create and save a regular user based on the given email and password.
        :param email: The email to assign the user.
        :param password: The password to assign the user.
        :param extra_fields: Extra fields to attribute to the user.
        :return: The created user object.
        """
        extra_fields.setdefault("is_superuser", False)
        return self._create_user(email, password, **extra_fields)

    def create_superuser(self, email, password, **extra_fields):
        """
        Create and save a super user based on the given email and password.
        :param email: The email to assign the user.
        :param password: The password to assign the user.
        :param extra_fields: Extra fields to attribute to the user.
        :return: The created user object.
        """
        extra_fields.setdefault("is_superuser", True)
        extra_fields.setdefault("is_staff", True)
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser must have is_superuser=True.")
        return self._create_user(email, password, **extra_fields)


class StreetArtUser(AbstractBaseUser, PermissionsMixin, BaseStreetArtModel):
    """
    This is a custom user class for users of the Street Art project.
    """

    # Columns

    email = models.EmailField(_('email address'), unique=True)
    first_name = models.CharField(_('first name'), max_length=30, blank=True)
    last_name = models.CharField(_('last name'), max_length=30, blank=True)
    date_joined = models.DateTimeField(_('date joined'), auto_now_add=True)
    is_active = models.BooleanField(_('active'), default=True)
    is_staff = models.BooleanField(default=False)

    USERNAME_FIELD = "email"
    REQUIRED_FIELDS = []

    objects = StreetArtUserManager()

    # Class Meta

    class Meta:
        verbose_name = _('user')
        verbose_name_plural = _('users')

    # Methods

    def get_full_name(self):
        """
        Get a string representing the user's full name.
        :return: A string representing the user's full name.
        """
        to_return = "%s %s" % (self.first_name, self.last_name)
        return to_return.strip()

    def get_short_name(self):
        """
        Get a string representing the user's short name.
        :return: A string representing the user's short name.
        """
        return self.first_name

    def send_email(self, subject, message, from_email=None, **kwargs):
        """
        Send an email to this user.
        :param subject: The subject for the email.
        :param message: The message to include in the email.
        :param from_email: The email address where the email should originate from.
        :param kwargs: Keyword arguments for send_mail.
        :return: None
        """
        send_mail(subject, message, from_email, [self.email], **kwargs)
