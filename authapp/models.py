from django.db import models
from django.contrib.auth.base_user import AbstractBaseUser
from django.contrib.auth.models import UserManager, PermissionsMixin


class AbstractUserModel(AbstractBaseUser, PermissionsMixin):
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
    is_superuser = models.BooleanField(
        verbose_name="Superuser status",
        default=False
    )
    balance = models.FloatField(verbose_name="Balance", default=0.0)
    border_color = models.CharField(
        verbose_name="Border color", default="#FFFFFF", max_length=255)
    profile_background = models.CharField(
        verbose_name="Background profile", default="#FFFFFF", max_length=255)
    EMAIL_FIELD = "email"
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    class Meta:
        verbose_name = "User model"
        verbose_name_plural = "Users model"
