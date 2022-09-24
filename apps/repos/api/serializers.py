from rest_framework import serializers
from apps.repos.models import Organization, Repository, PullRequest, GithubEvent


class OrganizationSerializer(serializers.ModelSerializer):
    class Meta:
        model = Organization
        fields = '__all__'


# class RepositorySerializer(serializers.ModelSerializer):
#     class Meta:
#         model = Repository
#
#
# class PullRequestSerializer(serializers.ModelSerialize):
#     class Meta:
#         model = PullRequest
#
#
# class GithubEventSerializer(serializers.ModelSerialize):
#     class Meta:
#         model = GithubEvent
