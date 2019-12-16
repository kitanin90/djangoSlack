from slackeventsapi import SlackEventAdapter
from django.http import HttpResponse
from django.conf import settings
from slackclient import SlackClient

from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

SLACK_SIGNING_SECRET = getattr(settings, 'SLACK_SIGNING_SECRET', None)
# slack_event_adapter = SlackEventAdapter(SLACK_SIGNING_SECRET, '/slack/events')

# Create Slack Client
slack_bot_token = getattr(settings, 'SLACK_BOT_TOKEN', None)
slack_client = SlackClient(slack_bot_token)
slack_verification_token = getattr(settings, 'SLACK_VERIFICATION_TOKEN', None)


class Events(APIView):

    def post(self, request, *args, **kwargs):

        slack_message = request.data

        if slack_message.get('token') != slack_verification_token:
            return Response(status=status.HTTP_403_FORBIDDEN)

        # verification challenge
        if slack_message.get('type') == 'url_verification':
            return Response(data=slack_message,
                            status=status.HTTP_200_OK)

        if 'event' in slack_message:
            event_message = slack_message.get('event')

            # ignore bot's own message
            if event_message.get('subtype') == 'bot_message':
                return Response(status=status.HTTP_200_OK)

            # process user's message
            user = event_message.get('user')
            text = event_message.get('text')
            channel = event_message.get('channel')
            bot_text = 'Hi <@{}> :wave:'.format(user)
            print(text)

            if 'hi' in text.lower():
                slack_client.api_call(method='chat.postMessage',
                                      channel=channel,
                                      text=bot_text)
                return Response(status=status.HTTP_200_OK)

            if text.lower():
                slack_client.api_call(method='chat.postMessage',
                                      channel=channel,
                                      text='Your text: {0} '.format(text))

        return Response(status=status.HTTP_200_OK)
