from django.db import models
from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.utils.translation import gettext_lazy as _


# Create your models here.
class User(AbstractUser):
    pass
