import logging
from huey import crontab
from huey.contrib.djhuey import periodic_task
from newsfeed_portal.apps.news import services as services_news


logger = logging.getLogger(__name__)


@periodic_task(crontab(minute="*/10"))
def task_fetch_news_top_headlines():
    try:
        logger.info("[task_fetch_news_top_headlines] Executing ...")

        news_fetch_service = services_news.NewsFetchService()
        news_fetch_service.fetch_top_headlines()

        logger.info("[task_fetch_news_top_headlines] Executed - Successful")
    except Exception as e:
        logger.exception(e)
        logger.info("[task_fetch_news_top_headlines] Executed - Failed")
