from django.db import models
from django.contrib.auth.models import AbstractUser
from .manager import UserManager


class CustomUser(AbstractUser):
    phone_number = models.CharField(max_length=20,unique=True)
    bio = models.CharField(max_length=100)

    USERNAME_FIELD = 'phone_number'
    REQUIRED_FIELDS = []
    objects = UserManager()
# Create your models here.
