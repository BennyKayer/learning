"""All of the project's models
"""
from django.contrib.auth.models import AbstractUser
from django.db import models
from django.contrib.postgres.fields import ArrayField


class User(AbstractUser):
    """Customized user"""

    pass


class Group(models.Model):
    """FB work group with country tags attached

    Args:
        models ([type]): [description]
    """

    COUNTRY_CODES = (
        ("EU", "Europe"),
        ("AT", "Austria"),
        ("DE", "Germany"),
        ("NL", "Netherlands"),
        ("N", "Norway"),
        ("S", "Switzerland"),
        ("BE", "Belgium"),
    )

    name = models.CharField(max_length=255)
    link = models.URLField(max_length=255)
    job = models.CharField(max_length=255, blank=True)
    is_accepted = models.BooleanField(default=False)
    is_posted = models.BooleanField(default=False)
    country_codes = ArrayField(
        models.CharField(choices=COUNTRY_CODES, max_length=5)
    )

    def __str__(self):
        return self.name
