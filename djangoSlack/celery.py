from __future__ import absolute_import, unicode_literals
from django.conf import settings
from celery.schedules import crontab


import os

from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'djangoSlack.settings')

app = Celery('djangoSlack')

app.config_from_object('django.conf:settings')

app.autodiscover_tasks(packages=settings.INSTALLED_APPS)

app.conf.beat_schedule = {
    'send-report-every-single-minute': {
        'task': 'publisher.tasks.send_view_count_report',
        'schedule': crontab(),  # change to `crontab(minute=0, hour=0)` if you want it to run daily at midnight
    },
}

