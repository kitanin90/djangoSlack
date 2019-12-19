from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=120)
    body = models.TextField()
    url_image = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)

    def __str__(self):
        return self.title

    class Meta:
        ordering = ["-created_date"]