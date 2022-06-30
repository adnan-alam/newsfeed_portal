import operator as python_operator
from functools import reduce
from rest_framework import viewsets, mixins
from rest_framework.permissions import IsAuthenticated
from django.db.models import Q
from newsfeed_portal.apps.core.api import permissions as permissions_core
from newsfeed_portal.apps.core.api.pagination import GlobalPagination
from newsfeed_portal.apps.news import models as models_news
from newsfeed_portal.apps.news.api import serializers as serializers_news


class NewsViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated & permissions_core.NotAdminUser]
    serializer_class = serializers_news.NewsSerializer
    queryset = models_news.News.all().order_by("-published_at")
    pagination_class = GlobalPagination

    def get_queryset(self):
        user_newsettings = self.request.user.newssettings
        source_list = user_newsettings.source
        country_list = user_newsettings.country
        keyword_list = user_newsettings.keywords

        if keyword_list:
            conditions = []
            for keyword in keyword_list:
                queries = Q(**{"headline__icontains": keyword})
                conditions.append(reduce(python_operator.or_, queries))

            qs = self.queryset.filter(
                reduce(python_operator.and_, conditions),
                source__slug__in=source_list,
                source__country__in=country_list,
            )
        else:
            qs = self.queryset.filter(
                source__slug__in=source_list,
                source__country__in=country_list,
            )

        return qs


class NewsSourceViewSet(viewsets.ReadOnlyModelViewSet):
    permission_classes = [IsAuthenticated & permissions_core.NotAdminUser]
    serializer_class = serializers_news.NewsSourceSerializer
    queryset = models_news.NewsSource.all().order_by("slug")


class NewsSettingsViewSet(
    viewsets.GenericViewSet, mixins.UpdateModelMixin, mixins.RetrieveModelMixin
):
    permission_classes = [IsAuthenticated & permissions_core.NotAdminUser]
    serializer_class = serializers_news.NewsSettingsSerializer
    queryset = models_news.NewsSettings.all()

    def get_queryset(self):
        qs = self.queryset.filter(user=self.request.user)
        return qs
