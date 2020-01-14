from django.db import models
from django.utils import timezone


class Post(models.Model):
    title = models.CharField(max_length=100)
    body = models.TextField()
    url_image = models.TextField()
    created_date = models.DateTimeField(default=timezone.now)
    fullname = models.ForeignKey('Profile', null=True, on_delete=models.PROTECT,
                                 verbose_name='Profile')

    def __str__(self):
        return self.title

    def get_title(self):
        return 'Title: ' + self.title

    class Meta:
        ordering = ["-created_date"]


class Profile(models.Model):
    fullname = models.CharField(max_length=100, verbose_name='Profile')
    number_message = models.IntegerField(default=0)

    class Meta:
        verbose_name_plural = 'Profiles'
        verbose_name = 'Profile'
        ordering = ['fullname']

    def __str__(self):
        return self.fullname
