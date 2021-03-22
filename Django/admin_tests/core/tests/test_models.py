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
    """
    return models.Group.objects.create(name=name, link=link, job=job)


def sample_country(name: str = "Austria", code: str = "AT"):
    """Shortcut for creating sample countries

    Args:
        name (str, optional): Full country's name. Defaults to "Austria".
        code (str, optional): Country's code. Defaults to "AT".
    """
    return models.Country.objects.create(name=name, code=code)


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
        group = sample_group(name=name, link=link, job=job)

        self.assertEqual(group.name, name)
        self.assertEqual(group.link, link)
        self.assertEqual(group.job, job)

    def test_group_string_representation(self):
        """Test that group's name is it's string representation"""
        group = sample_group()

        self.assertEqual(str(group), group.name)

    def test_country_str_representation(self):
        """Test that country tag's string representation is it's name"""
        name = "European Union"
        code = "EU"
        country = sample_country(name=name, code=code)

        self.assertEqual(str(country), country.name)
