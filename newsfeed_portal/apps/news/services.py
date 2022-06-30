import pytz
import logging
from dateutil.parser import parse as dateutil_parse
from newsapi import NewsApiClient
from slugify import slugify
from django.conf import settings
from newsfeed_portal.apps.news import models as models_news


logger = logging.getLogger(__name__)


class NewsFetchService:
    def __init__(self):
        self.newsapi = NewsApiClient(api_key=settings.NEWSAPI_API_KEY)

    def _save_news(self, article_list):
        for article in article_list:
            news_source_name = article["source"]["name"]
            published_at = dateutil_parse(article["publishedAt"]).replace(tzinfo=pytz.UTC)
            headline_slug = slugify(article["title"], separator="-")

            try:
                if not models_news.News.objects.filter(slug=headline_slug).exists():
                    news_source = models_news.NewsSource.objects.filter(
                        name=news_source_name
                    ).first()
                    if not news_source:
                        news_source_slug = slugify(news_source_name, separator="-")
                        news_source = models_news.NewsSource.objects.create(
                            slug=news_source_slug,
                            name=news_source_name,
                            country=None,
                        )

                    models_news.News.objects.create(
                        source=news_source,
                        headline=article["title"],
                        thumbnail_url=article["urlToImage"],
                        news_url=article["url"],
                        published_at=published_at,
                    )
            except Exception as e:
                logger.exception(e)

    def _save_news_sources(self, source_list):
        for source in source_list:
            try:
                if not models_news.NewsSource.objects.filter(
                    name=source["name"]
                ).exists():
                    models_news.NewsSource.objects.create(
                        slug=source["id"],
                        name=source["name"],
                        country=source["country"],
                    )
            except Exception as e:
                logger.exception(e)

    def fetch_top_headlines(self):
        top_headlines = self.newsapi.get_top_headlines()
        if top_headlines["status"] == "ok":
            article_list = top_headlines["articles"]
            self._save_news(article_list)
        else:
            raise Exception(f"Response: {top_headlines['status']}")

    def fetch_news_sources(self):
        sources = self.newsapi.get_sources()

        if sources["status"] == "ok":
            source_list = sources["sources"]
            print(source_list)
            self._save_news_sources(source_list)
        else:
            raise Exception(f"Response: {sources['status']}")
