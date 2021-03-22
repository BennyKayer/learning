"""All of the project's models
"""
from django.contrib.auth.models import AbstractUser
from django.db import models


class User(AbstractUser):
    """Customized user"""

    pass


class Group(models.Model):
    """FB work group with country tags attached

    Args:
        models ([type]): [description]
    """

    name = models.CharField(max_length=255)
    link = models.URLField(max_length=255)
    job = models.CharField(max_length=255, blank=True)
    is_accepted = models.BooleanField(default=False)
    is_posted = models.BooleanField(default=False)
    country = models.ManyToManyField("Country")

    def __str__(self):
        return self.name


class Country(models.Model):
    """Country with name and code"""

    name = models.CharField(max_length=255)
    code = models.CharField(max_length=3)

    def __str__(self):
        """Country's name as its string representation"""
        return self.name
