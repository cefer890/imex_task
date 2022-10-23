from django.contrib.auth.models import AbstractUser, BaseUserManager, PermissionsMixin
from django.db import models


class MyUser(AbstractUser):
    address = models.CharField(default='', max_length=150)
    phonenumber = models.CharField(max_length=10)

    class Meta:
        verbose_name = 'MyUser'
        verbose_name_plural = 'MyUsers'
