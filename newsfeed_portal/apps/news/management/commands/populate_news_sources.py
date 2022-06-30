from django.core.management.base import BaseCommand
from django.utils.translation import ugettext_lazy as _
from newsfeed_portal.apps.news import services as services_news


class Command(BaseCommand):
    help = "Populate News Sources"

    def handle(self, *args, **options):
        try:
            news_fetch_service = services_news.NewsFetchService()
            news_fetch_service.fetch_news_sources()

            self.stdout.write(
                self.style.SUCCESS("Populated News Sources from NewsAPI successfully")
            )
        except Exception as e:
            self.stdout.write((self.style.ERROR(e)))
