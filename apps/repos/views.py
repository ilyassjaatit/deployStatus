from django.views import generic

from .models import Repository, PullRequest


class RepositoryDetailView(generic.DetailView):
    model = Repository

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['pullRequest'] = PullRequest.objects.filter(repository__id=context['object'].pk)[:5]
        return context


class RepositoryListView(generic.ListView):
    model = Repository
    paginate_by = 6


class PullrequestListView(generic.ListView):
    model = PullRequest
    paginate_by = 15

    def get_queryset(self):
        repository_pk = self.kwargs['pk']
        return PullRequest.objects.filter(repository__pk=repository_pk)


class PullrequestDetailView(generic.DetailView):
    model = PullRequest
    pk_url_kwarg = 'pullrequest_pk'
