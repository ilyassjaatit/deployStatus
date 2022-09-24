"""deployStatus URL Configuration
"""
from django.contrib import admin
from django.urls import path, include


from apps.repos.views import *
from rest_framework.authtoken.views import obtain_auth_token

urlpatterns = [
    path('repository/', RepositoryListView.as_view(), name="repository-list"),
    path('repository/<pk>/', RepositoryDetailView.as_view(), name="repository-detail"),
    path('repository/<pk>/pull-request/', PullrequestListView.as_view(), name="repository-detail-pull-request-list"),
    path('repository/<pk>/pull-request/<int:pullrequest_pk>/', PullrequestDetailView.as_view(),
         name="repository-detail-pull-request-detail"),
    path('admin/', admin.site.urls),
    # Debug
    path('__debug__/', include('debug_toolbar.urls')),
    path("api/", include("config.api_urls")),
]


# API URLS
urlpatterns += [
    path("auth-token/", obtain_auth_token),
]