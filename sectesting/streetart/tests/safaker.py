# -*- coding: utf-8 -*-
from __future__ import absolute_import

from faker import Faker
from uuid import uuid4

from .data import StreetArtTestData
from ..models import StreetArtUser, StreetArtPost


class SaFaker(object):
    """
    This is a class for creating dummy database models for testing purposes.
    """

    # Class Members

    # Instantiation

    # Static Methods

    @staticmethod
    def create_posts_for_user(to_populate=None, count=20):
        """
        Create a number of StreetArtPost objects and associate them with the given
        user.
        :param to_populate: The user to populate.
        :param count: The number of posts to add to the user.
        :return: The newly-created posts.
        """
        new_posts = []
        faker = Faker()
        for i in range(count):
            new_posts.append(StreetArtPost.objects.create(
                latitude=float(faker.random_number()) * 0.01,
                longitude=float(faker.random_number()) * 0.01,
                title=faker.word(),
                description=faker.paragraph(),
                s3_bucket=faker.word(),
                s3_key=str(uuid4()),
                user=to_populate,
            ))
        return new_posts

    @staticmethod
    def create_users():
        """
        Create all of the test users for Street Art unit tests.
        :return: A list containing all of the users.
        """
        new_users = []
        for user_string in StreetArtTestData.USERS.keys():
            new_users.append(SaFaker.create_user(user_string))
        for new_user in new_users:
            SaFaker.populate_user(new_user)
        return new_users

    @staticmethod
    def create_user(user_string):
        """
        Create a user based on the given string.
        :param user_string: A string depicting which user to create.
        :return: The newly-created user.
        """
        user_data = StreetArtTestData.USERS[user_string]
        new_user = StreetArtUser.objects.create(**user_data)
        new_user.set_password(user_data["password"])
        new_user.save()
        return new_user

    @staticmethod
    def get_create_post_kwargs():
        """
        Get a dictionary of values to submit to the post creation endpoint.
        :return: A dictionary of values to submit to the post creation endpoint.
        """
        faker = Faker()
        f = open("streetart/tests/files/puppy.jpg", "r")
        return {
            "title": faker.word(),
            "description": faker.paragraph(),
            "image": f,
        }

    @staticmethod
    def get_create_user_kwargs():
        """
        Get a dictionary of values to submit to the user registration endpoint.
        :return: A dictionary of values to submit to the user registration endpoint.
        """
        faker = Faker()
        return {
            "email": faker.email(),
            "first_name": faker.first_name(),
            "last_name": faker.last_name(),
            "password": faker.password(),
        }

    @staticmethod
    def get_edit_post_kwargs():
        """
        Get a dictionary of values to submit to the edit post endpoint.
        :return: A dictionary of values to submit to the edit post endpoint.
        """
        faker = Faker()
        return {
            "title": faker.word(),
            "description": faker.paragraph(),
            "latitude": float(faker.pydecimal()),
            "longitude": float(faker.pydecimal()),
        }

    @staticmethod
    def get_post_for_user(user_string):
        """
        Get a StreetArtPost object owned by the given user.
        :param user_string: A string depicting the user to retrieve a post for.
        :return: A StreetArtPost corresponding to the given user.
        """
        user = SaFaker.get_user(user_string)
        return user.posts.first()

    @staticmethod
    def get_user(user_string):
        """
        Get the user object corresponding to the given string.
        :param user_string: A string depicting the user to retrieve.
        :return: The user corresponding to the given string.
        """
        user_data = StreetArtTestData.USERS[user_string]
        return StreetArtUser.objects.get(email=user_data["email"])

    @staticmethod
    def populate_user(to_populate):
        """
        Populate database data for the given user.
        :param to_populate: The user to populate.
        :return: None
        """
        SaFaker.create_posts_for_user(to_populate=to_populate)

    # Class Methods

    # Public Methods

    # Protected Methods

    # Private Methods

    # Properties

    # Representation and Comparison
