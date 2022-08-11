"""deployStatus URL Configuration
"""
from django.contrib import admin
from django.urls import path, include
from apps.repos.views import *

urlpatterns = [
    path('repository/', RepositoryListView.as_view(), name="repository-list"),
    path('repository/<pk>/', RepositoryDetailView.as_view(), name="repository-detail"),
    path('repository/<pk>/pull-request/', PullrequestListView.as_view(), name="repository-detail-pull-request-list"),
    path('repository/<pk>/pull-request/<int:pullrequest_pk>/', PullrequestDetailView.as_view(),
         name="repository-detail-pull-request-detail"),
    path('admin/', admin.site.urls),
    # Debug
    path('__debug__/', include('debug_toolbar.urls')),
]
