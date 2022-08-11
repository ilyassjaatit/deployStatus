from django.contrib import admin

from .models import Repository, Organization, PullRequest, GithubEvent


class RepositoryAdmin(admin.ModelAdmin):
    search_fields = ('name', 'description')


class PullRequestAdmin(admin.ModelAdmin):
    search_fields = ('number', 'number')
    list_filter = ('repository__organization', 'state')


admin.site.register(Repository, RepositoryAdmin)
admin.site.register(PullRequest, PullRequestAdmin)
admin.site.register(Organization)
admin.site.register(GithubEvent)
