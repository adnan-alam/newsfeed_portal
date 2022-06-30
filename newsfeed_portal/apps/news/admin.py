from django.contrib import admin
from .models import News, NewsSource


admin.site.register(NewsSource)
admin.site.register(News)
