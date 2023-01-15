#User_app/models.py

from django.db import models
from django.contrib.auth.models import AbstractUser
from django.utils.translation import gettext_lazy as _

class User(AbstractUser):
	primeiro_nome = models.CharField(_(""), max_length=32, blank=False, null=True)
	sobrenome = models.CharField(_(""), max_length=128, blank=False, null=True)