from django.urls import path, include
from rest_framework.routers import DefaultRouter
from newsfeed_portal.apps.account.api import views as views_account


router = DefaultRouter(trailing_slash=True)
router.register(r"users", views_account.UserViewSet, basename="user")


urlpatterns = [path("", include(router.urls))]
