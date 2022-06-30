from django.contrib import admin
from .models import News, NewsSource, NewsSettings


admin.site.register(NewsSource)
admin.site.register(News)
admin.site.register(NewsSettings)
