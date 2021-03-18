"""Tests for all models in the project
"""
from django.contrib.auth import get_user_model
from django.test import TestCase

from core import models


def sample_user(
    username: str = "John1",
    email: str = "john@gmail.com",
    password: str = "p455WORDC",
):
    """Shortcut for creating sample users

    Args:
        username (str, optional): Username for User model. Defaults to "John1".
        password (str, optional): User's password. Defaults to "p455WORDC".
    """
    return get_user_model().objects.create_user(username, email, password)


def sample_group(
    name: str = "Polacy w Austrii",
    link: str = "https://www.facebook.com/groups/POLACYwAUSTRII.grupa/",
    job: str = "Zbrojarz betoniarz",
    country_tags: list = ["AT", "DE"],
):
    """Shortcut for creating sample groups

    Args:
        name (str, optional):
            Groups name. Defaults to "Polacy w Austrii".
        link (str, optional):
            Link to FB group. Defaults to
            "https://www.facebook.com/groups/POLACYwAUSTRII.grupa/".
        job (str, optional):
            Job title / titles or description.
            Defaults to "Zbrojarz betoniarz".
        country_tags (list, optional):
            Tags of countries in which the job takes place.
            Defaults to ["AT", "DE"].
    """
    return models.Group.objects.create(
        name=name, link=link, job=job, country_tags=country_tags
    )


class ModelTests(TestCase):
    """Tests for models"""

    def test_create_user_with_username_successful(self):
        """Test that creating user with username works"""
        username = "Johnson129"
        email = "johnson@gmail.com"
        password = "p455WORDCxd"
        user = sample_user(username, email, password)

        self.assertEqual(user.username, username)
        self.assertEqual(user.email, email)
        self.assertTrue(user.check_password(password))

    def test_create_group_successful(self):
        """Test that group is successfully created"""
        name = "Polacy w Austrii"
        link = "https://www.facebook.com/groups/POLACYwAUSTRII.grupa/"
        job = "Zbrojarz betoniarz"
        country_tags = ["AT", "DE"]
        group = sample_group(
            name=name, link=link, job=job, country_tags=country_tags
        )

        self.assertEqual(group.name, name)
        self.assertEqual(group.link, link)
        self.assertEqual(group.job, job)
        self.assertIn(group.country_tags, country_tags[0])
        self.assertIn(group.country_tags, country_tags[1])

    def test_group_string_representation(self):
        """Test that group's name is it's string representation"""
        group = sample_group()

        self.assertEqual(str(group), group.name)
