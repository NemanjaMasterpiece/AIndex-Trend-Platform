from django.db import models
from django.utils import timezone

class TrendArticle(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    published_date = models.DateTimeField(default=timezone.now)
    importance = models.IntegerField(default=0)
    link = models.URLField(default='https://example.com')