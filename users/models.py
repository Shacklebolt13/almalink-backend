from django.db import models
from django_use_email_as_username.models import BaseUser, BaseUserManager


class User(BaseUser):
    skill = models.CharField(max_length=100, blank=True, null=True)
    objects = BaseUserManager()

    username = models.CharField(max_length=100, blank=True, null=True)
