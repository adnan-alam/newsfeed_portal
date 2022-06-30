from django.urls import path, include
from rest_framework.routers import DefaultRouter
from newsfeed_portal.apps.news.api import views as views_news


router = DefaultRouter(trailing_slash=True)
router.register(r"news", views_news.NewsViewSet, basename="news")
router.register(r"news-sources", views_news.NewsSourceViewSet, basename="news-sources")
router.register(
    r"news-settings", views_news.NewsSettingsViewSet, basename="news-settings"
)

urlpatterns = [path("", include(router.urls))]
