"""Register models for django admin display
"""
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from core import models

admin.site.register(models.User, UserAdmin)
