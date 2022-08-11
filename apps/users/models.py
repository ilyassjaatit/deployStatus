from django.contrib.auth.models import AbstractUser
from django.db.models import BigIntegerField, CharField


class User(AbstractUser):
    github_id = BigIntegerField(null=True, blank=True)
    github_username = CharField(max_length=255, null=True, blank=True)
