from django.urls import path, include
from rest_framework.routers import DefaultRouter
from newsfeed_portal.apps.news.api import views as views_news


router = DefaultRouter(trailing_slash=True)
router.register(r"news", views_news.NewsViewSet, basename="news")


urlpatterns = [path("", include(router.urls))]
