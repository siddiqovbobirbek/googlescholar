from django.contrib.auth.models import AbstractUser
from django.db import models
from .managers import CustomUserManager


class CustomUser(AbstractUser):
    address = models.CharField(max_length=200)
    number = models.CharField(max_length=200)
    email = models.EmailField(unique=True)
    age = models.PositiveIntegerField(null=True, blank=True)
    job = models.CharField(max_length=200)

    objects = CustomUserManager()

    REQUIRED_FIELDS = []
    USERNAME_FIELD = 'email'

    def __str__(self) -> str:
        return self.email
