from django.db import models
from django.contrib.auth.models import AbstractUser
from Accounts.manager import CustomUserManager


# Custom User Model
class User(AbstractUser):
    is_school = models.BooleanField(default=False)
    is_parent = models.BooleanField(default=False)

    email = models.EmailField(
        ("email Address"),
        blank=True,
        max_length=200,
        error_messages={
            "unique": "A User with that email already exists.",
        },
    )
    username = models.CharField(
        max_length=150,
        unique=True,
        help_text="Required. 150 characters or fewer. Letters, digits and @/./+/-/_ only.",
        validators=[],
        error_messages={
            "unique": "A user with that username already exists.",
        },
    )

    objects = CustomUserManager()

    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    def save(self, *args, **kwargs):
        if not self.username:
            self.username = self.email
        return super().save(*args, **kwargs)

    def __str__(self):
        return str(self.username)
