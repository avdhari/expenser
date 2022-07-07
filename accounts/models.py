from django.db import models
from django.contrib.auth.models import AbstractUser
from django.db.models.deletion import PROTECT
from django.utils.translation import gettext_lazy as _


class User(AbstractUser):
    first_name = models.CharField(max_length=255)
    last_name = models.CharField(max_length=255)
    email = models.EmailField(max_length=200)
    phone = models.CharField(max_length=10, blank=True)

    def __str__(self):
        return self.first_name + str(' ') + self.last_name