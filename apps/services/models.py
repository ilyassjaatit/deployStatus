from django.db import models
from django.contrib.auth import get_user_model

from apps.repos.models import PullRequest, Repository

User = get_user_model()


class Service(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Server(models.Model):
    name = models.CharField(max_length=255)
    description = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    services = models.ManyToManyField(Service)


class Product(models.Model):
    name = models.CharField(max_length=255)
    service = models.ForeignKey(Service, on_delete=models.CASCADE)
    server = models.ForeignKey(Server, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)


class Deployment(models.Model):
    description = models.TextField(blank=True, null=True)
    github_id = models.BigIntegerField(null=True, blank=True)
    raw_data = models.JSONField(null=True, blank=True)
    is_processed = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE, blank=True, null=True)
    repository = models.ForeignKey(Repository, on_delete=models.CASCADE, blank=True, null=True)
    pull_request = models.ForeignKey(PullRequest, on_delete=models.CASCADE, blank=True, null=True)
    service = models.ForeignKey(Service, on_delete=models.CASCADE, blank=True, null=True)
    server = models.ForeignKey(Server, on_delete=models.CASCADE, blank=True, null=True)
    github_created = models.DateTimeField(blank=True, null=True, default=None)
    github_updated = models.DateTimeField(blank=True, null=True, default=None)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

