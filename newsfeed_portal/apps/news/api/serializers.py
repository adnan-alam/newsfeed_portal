from rest_framework import serializers
from newsfeed_portal.apps.core.api.serializers import DynamicFieldsModelSerializer
from newsfeed_portal.apps.news import models as models_news


class NewsSerializer(DynamicFieldsModelSerializer):
    news_source = serializers.CharField(source="source.name", read_only=True)
    country = serializers.CharField(source="source.country", read_only=True)

    class Meta:
        model = models_news.News
        fields = ["id", "headline", "thumbnail", "news_source", "country", "news_url"]
        read_only_fields = fields
