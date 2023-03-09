from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager, PermissionsMixin

class AbstractUserModel(AbstractBaseUser):
    objects = UserManager()
    username = models.CharField(
        verbose_name="Username", 
        unique=True,
        max_length=255
    )
    email = models.EmailField(verbose_name="Email", unique=True)
    is_staff = models.BooleanField(
        verbose_name="Staff status",
        default=False
    )
    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]
