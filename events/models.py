from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    url_image = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    fullname = models.ForeignKey('User', null=True, on_delete=models.PROTECT,
                                 verbose_name='Profile')

    def __str__(self):
        return self.title

    def get_title(self):
        return 'Title: ' + self.title

    class Meta:
        ordering = ["-created_date"]


class User(models.Model):
    fullname = models.CharField(max_length=100, verbose_name='User')
    number_message = models.IntegerField(default=0)
    email = models.CharField(max_length=100)

    class Meta:
        verbose_name_plural = 'Users'
        verbose_name = 'User'
        ordering = ['fullname']

    def __str__(self):
        return self.fullname
