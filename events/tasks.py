import logging

from django.urls import reverse
from django.core.mail import send_mail
from django.contrib.auth import get_user_model
from djangoSlack.celery import app

from .models import User


@app.task
def send_email(email, title, body):
    user = User.objects.get(email=email)
    try:
        send_mail(
            'You send post',
            'Title: {0} ; Body: {1}'.format(title, body),
            'name@gmail.com',
            [user.email],
            fail_silently=False,
        )
    except Exception as e:
        print('Your error: {0}'.format(e))
        logging.warning("Tried to send email to non-existing user '%s'" % email)