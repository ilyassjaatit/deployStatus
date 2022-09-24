from github import Github
from celery.utils.log import get_task_logger
from django.contrib.auth import get_user_model
from django.utils.dateparse import parse_datetime
import time
from apps.repos.models import Repository, Organization, PullRequest, GithubEvent
from apps.services.models import Deployment

from config.celery import app

User = get_user_model()
GITHUB_TOKING = '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'
STATE_PULLREQUEST_OPEN = 'open'
STATE_PULLREQUEST_CLOSE = 'close'
GITHUB_API_PAGINATION_LEN = 50
logger = get_task_logger(__name__)


@app.task()
def get_users_github():
    g = Github(GITHUB_TOKING, per_page=GITHUB_API_PAGINATION_LEN)
    organizations = Organization.objects.all()
    for organization in organizations:
        if organization.save_members:
            members = g.get_organization(organization.login).get_members()
            for member in members:
                User.objects.update_or_create(username=member.login,
                                              github_id=member.id,
                                              github_username=member.login,
                                              )
        continue


@app.task()
def get_deploys():
    g = Github(GITHUB_TOKING, per_page=GITHUB_API_PAGINATION_LEN)
    repositories = Repository.objects.filter(save_pull_requests=True)
    for report in repositories:
        github_report_count = g.get_repo(report.name).get_deployments().totalCount
        num_of_pages = int(github_report_count / GITHUB_API_PAGINATION_LEN) + 1
        for num_page in range(0, num_of_pages):
            for deployment in g.get_repo(report.name).get_deployments().get_page(num_page):
                try:
                    created_user = User.objects.filter(github_id=deployment.creator.id,
                                                       github_username=deployment.creator.login,
                                                       username=deployment.creator.login
                                                       )
                    if created_user:
                        Deployment.objects.update_or_create(github_id=deployment.id,
                                                            github_updated=deployment.created_at,
                                                            github_created=deployment.created_at,
                                                            repository=report,
                                                            raw_data=deployment.raw_data,
                                                            user=created_user.first()
                                                            )
                    else:
                        Deployment.objects.update_or_create(github_id=deployment.id,
                                                            repository=report.id,
                                                            raw_data=deployment.raw_data
                                                            )
                    logger.info("Saved Deployment")
                except:
                    pass


def parser_deploys():
    deployments = Deployment.objects.filter(is_processed=False)
    g = Github(GITHUB_TOKING, per_page=GITHUB_API_PAGINATION_LEN)
    for deployment in deployments:
        print(deployment.github_id)
        pass


@app.task()
def get_pull_request(state='close'):
    repositories = Repository.objects.filter(save_pull_requests=True)
    g = Github(GITHUB_TOKING, per_page=GITHUB_API_PAGINATION_LEN)
    for report in repositories:
        pull_request_count = g.get_repo(report.name).get_pulls(state=state).totalCount
        num_of_pages = int(pull_request_count / GITHUB_API_PAGINATION_LEN) + 1
        for num_page in range(169, num_of_pages):
            pulls_requests = g.get_repo(report.name).get_pulls(state=state).get_page(num_page)
            for pull_request in pulls_requests:
                time.sleep(2)
                print(num_page)
                data_pull = {
                    "title": pull_request.title,
                    "url": pull_request.html_url,
                    "body": pull_request.body,
                    "state": pull_request.state,
                    "raw_data": pull_request.raw_data,
                    "number": pull_request.number,
                    "repository": report
                }
                exists_pull_request = PullRequest.objects.filter(github_id=pull_request.id)
                if exists_pull_request:
                    print("Update get_pull_request")
                    PullRequest.objects.filter(github_id=pull_request.id).update(**data_pull)
                else:
                    data_pull.update({"github_id": pull_request.id})
                    print("Created get_pull_request")
                    PullRequest.objects.create(**data_pull)


@app.task()
def get_events():
    repositories = Repository.objects.filter(event_tracking=True)
    g = Github(GITHUB_TOKING, per_page=GITHUB_API_PAGINATION_LEN)
    for report in repositories:
        pull_requests = PullRequest.objects.filter(repository_id=report.pk, num_events_scanned=0)
        for pull_request in pull_requests:

            events = g.get_repo(report.name).get_pull(pull_request.number).get_issue_events()
            print(events.totalCount)
            print(pull_request.number)
            for event in events:
                try:
                    user_actor = User.objects.get(username=event.actor.login,
                                                  github_id=event.actor.id,
                                                  github_username=event.actor.login)
                except:
                    user_actor = None

                GithubEvent.objects.update_or_create(
                    pull_request=pull_request,
                    user=user_actor,
                    raw_data=event.raw_data,
                    event_type=event.event,
                    github_id=event.id,
                )
                update_num_events_scanned = pull_request.num_events_scanned + 1
                PullRequest.objects.filter(pk=pull_request.pk)\
                    .update(num_events_scanned=update_num_events_scanned)


@app.task()
def get_orgs():
    g = Github(GITHUB_TOKING)
    for item in g.get_user().get_orgs():
        Organization.objects.update_or_create(name=item.name, github_id=item.id, login=item.login)


@app.task()
def get_repos():
    g = Github(GITHUB_TOKING)
    for repo in g.get_user().get_repos():
        org_pk = Organization.objects.filter(github_id=repo.organization.id, save_repository=True).first()
        if org_pk and org_pk.pk == 1:
            Repository.objects.update_or_create(name=repo.full_name,
                                                description=repo.description,
                                                github_id=repo.id,
                                                url=repo.url,
                                                organization=org_pk)
