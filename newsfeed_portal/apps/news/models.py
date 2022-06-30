from slugify import slugify
from django.db import models
from django.contrib.auth import get_user_model
from django.contrib.postgres.fields import ArrayField
from django.utils.translation import ugettext_lazy as _


User = get_user_model()


class NewsSource(models.Model):
    name = models.CharField(max_length=125)
    slug = models.SlugField(max_length=125, unique=True, null=True, blank=True)
    country = models.CharField(max_length=2, null=True, blank=True)

    class Meta:
        verbose_name = _("News Source")
        verbose_name_plural = _("News Sources")

    def __str__(self):
        return f"{self.name}"


class News(models.Model):
    source = models.ForeignKey(NewsSource, on_delete=models.CASCADE)
    headline = models.CharField(max_length=500)
    slug = models.SlugField(max_length=500, unique=True, null=True, blank=True)
    thumbnail_url = models.URLField(max_length=255)
    published_at = models.DateTimeField()
    news_url = models.URLField(max_length=255)

    class Meta:
        verbose_name = _("News")
        verbose_name_plural = _("News")

    def save(self, *args, **kwargs):
        if not self.slug:
            self.slug = slugify(self.headline, separator="-")

        super(News, self).save(*args, **kwargs)

    def __str__(self):
        return f"{self.headline}"


class NewsSettings(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    country = ArrayField(models.CharField(max_length=2))
    source = ArrayField(models.CharField(max_length=125))
    keywords = ArrayField(models.CharField(max_length=50))

    class Meta:
        verbose_name = _("News Settings")
        verbose_name_plural = _("News Settings")

    def __str__(self):
        return f"{self.id}"
