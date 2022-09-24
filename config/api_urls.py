from django.conf import settings

from rest_framework.routers import DefaultRouter, SimpleRouter
from apps.users.views import UserViewSet

from apps.repos.api.views import OrganizationViewSet

if settings.DEBUG:
    router = DefaultRouter()
else:
    router = SimpleRouter()

router.register("users", UserViewSet)
router.register("organizations", OrganizationViewSet)

app_name = "api"
urlpatterns = router.urls