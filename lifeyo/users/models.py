from django.contrib.auth.models import AbstractUser, PermissionsMixin, UserManager
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.utils import timezone


class TestUser(AbstractUser):
    photo = models.ImageField(upload_to='users/photos/')


# class Profile(models.Model):
#     user = models.OneToOneField(User)
#     photo = models.ImageField(upload_to='profiles/photos/')