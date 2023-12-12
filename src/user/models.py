from typing import List

from django.contrib.auth.models import AbstractUser, BaseUserManager
from django.db import models


class CustomUserManager(BaseUserManager):
    def create_user(self, email: str, password: str, **extra_fields):
        email = self.normalize_email(email)
        user = self.model(
            email=email,
            **extra_fields
        )

        user.set_password(password)
        user.save()

    def create_superuser(self, email: str, password: str, **extra_fields):
        extra_fields.setdefault("is_staff", True)
        extra_fields.setdefault("is_superuser", True)

        if extra_fields.get("is_staff") is not True:
            raise ValueError("Superuser has to have is_staff being True")
        
        if extra_fields.get("is_superuser") is not True:
            raise ValueError("Superuser has to have is_superuser being True")
        
        return self.create_user(email=email, password=password, **extra_fields)

class MAUser(AbstractUser):
    email = models.EmailField(('email address'), max_length=255, unique=True)
    username = models.CharField(max_length=50, unique=True)
    is_lawyer = models.BooleanField(default=True)

    objects = CustomUserManager()
    USERNAME_FIELD: str = "email"
    REQUIRED_FIELDS: List[str] = ["username"]
    

    def __str__(self):
        return self.username