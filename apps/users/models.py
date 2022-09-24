from django.contrib.auth.models import AbstractUser
from django.db.models import BigIntegerField, CharField, DateTimeField, EmailField


class User(AbstractUser):
    """
        Default user
    """

    github_id = BigIntegerField(null=True, blank=True)
    github_username = CharField(max_length=255, null=True, blank=True)
    email = EmailField("email address", unique=True, null=True, blank=True)
    created_at = DateTimeField(auto_now_add=True)
    updated_at = DateTimeField(auto_now=True)
    USERNAME_FIELD = "username"
    REQUIRED_FIELDS = ["email"]

    def __str__(self):
        return self.username
