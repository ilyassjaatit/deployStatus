from django.db import models
from django.contrib.auth import get_user_model

User = get_user_model()


class Organization(models.Model):
    name = models.CharField(max_length=255)
    login = models.CharField(max_length=255)
    save_members = models.BooleanField(default=False)
    github_id = models.IntegerField(unique=True)
    save_repository = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class Repository(models.Model):
    name = models.CharField(max_length=255)
    url = models.CharField(max_length=510)
    description = models.CharField(max_length=510, null=True)
    github_id = models.IntegerField(unique=True)
    organization = models.ForeignKey(Organization, on_delete=models.CASCADE)
    save_pull_requests = models.BooleanField(default=False)
    event_tracking = models.BooleanField(default=False)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class PullRequest(models.Model):
    title = models.CharField(max_length=510)
    github_id = models.BigIntegerField(unique=True)
    url = models.CharField(max_length=510)
    state = models.CharField(max_length=15)
    body = models.TextField(default="", null=True)
    number = models.IntegerField(null=True, blank=True)
    num_events_scanned = models.IntegerField(default=0, help_text="Number of times the events have been scanned")
    raw_data = models.JSONField(null=True, blank=True)
    repository = models.ForeignKey(Repository, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title


class GithubEvent(models.Model):
    event_type = models.CharField(max_length=50)
    github_id = models.BigIntegerField(unique=True)
    raw_data = models.JSONField(null=True, blank=True)
    pull_request = models.ForeignKey(PullRequest, on_delete=models.CASCADE)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.event_type