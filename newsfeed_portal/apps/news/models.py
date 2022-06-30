from django.db import models
from django.contrib.postgres.fields import ArrayField


class NewsSource(models.Model):
    name = models.CharField(max_length=125)
    slug = models.SlugField(max_length=125, unique=True)
    country = models.CharField(max_length=2)

    def __str__(self):
        return f"{self.name}"


class News(models.Model):
    source = models.ForeignKey(NewsSource, on_delete=models.CASCADE)
    headline = models.CharField(max_length=255)
    slug = models.SlugField(max_length=255, unique=True, null=True, blank=True)
    thumbnail_url = models.URLField(max_length=255)
    thumbnail = models.ImageField(upload_to="news_thumbnails/")
    published_at = models.DateTimeField()
    news_url = models.URLField(max_length=255)

    def __str__(self):
        return f"{self.headline}"


class NewsSettings(models.Model):
    country = ArrayField(models.CharField(max_length=2))
    source = ArrayField(models.CharField(max_length=125))
    keywords = ArrayField(models.CharField(max_length=50))

    def __str__(self):
        return f"{self.id}"
