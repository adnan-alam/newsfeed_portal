from rest_framework import serializers
from newsfeed_portal.apps.core.api.serializers import DynamicFieldsModelSerializer
from newsfeed_portal.apps.news import models as models_news


class NewsSerializer(DynamicFieldsModelSerializer):
    news_source = serializers.CharField(source="source.name", read_only=True)
    country = serializers.CharField(source="source.country", read_only=True)

    class Meta:
        model = models_news.News
        fields = ["id", "headline", "thumbnail_url", "news_source", "country", "news_url", "published_at"]
        read_only_fields = fields


class NewsSourceSerializer(DynamicFieldsModelSerializer):
    class Meta:
        model = models_news.NewsSource
        fields = ["id", "name", "slug", "country"]
        read_only_fields = fields


class NewsSettingsSerializer(DynamicFieldsModelSerializer):
    id = serializers.IntegerField(required=False)

    class Meta:
        model = models_news.NewsSettings
        fields = ["id", "user", "country", "source", "keywords"]
        read_only_fields = ["id", "user"]

    def update(self, instance, validated_data):
        models_news.NewsSettings.objects.filter(id=instance.id).update(**validated_data)
        instance.refresh_from_db()
        return instance
