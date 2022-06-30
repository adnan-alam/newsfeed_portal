from rest_framework import viewsets
from rest_framework.permissions import IsAuthenticated
from newsfeed_portal.apps.core.api import permissions as permissions_core
from newsfeed_portal.apps.core.api.pagination import GlobalPagination
from newsfeed_portal.apps.news import models as models_news
from newsfeed_portal.apps.news.api import serializers as serializers_news


class NewsViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated & permissions_core.NotAdminUser]
    serializer_class = serializers_news.NewsSerializer
    queryset = models_news.News.all().order_by("-published_at")
    pagination_class = GlobalPagination
