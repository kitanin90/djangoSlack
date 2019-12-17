from django.conf import settings
from django.http import JsonResponse
from django.shortcuts import render
from django.views.generic import TemplateView
from rest_framework.renderers import TemplateHTMLRenderer
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


def Slack_Send(request, work, hello_message):
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

    if '{0}'.format(work) in text.lower():
        slack_client.api_call(method='chat.postMessage',
                              channel=channel,
                              attachments='{0}'.format(hello_message))

    return Response(status=status.HTTP_200_OK)


class EventsAPIView(APIView):

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

        hello_message = [
            {
                'text': 'Hello'
            }
        ]

        work = 'hi'

        Slack_Send(request, work, hello_message)
        return Response(status=status.HTTP_200_OK)


class EndpointAPIView(TemplateView):
    template_name = 'post_list.html'

    def post(self, request):
        title = request.POST.get('title')
        body = request.POST.get('body')
        url_image = request.POST.get('url_image')

        print(title, body, url_image)

        send_block = [
            {
                "blocks": [
                    {
                        "type": "section",
                        "text": {
                            "type": "mrkdwn",
                            "text": "{0}".format(title)
                        }
                    },
                    {
                        "type": "section",
                        "block_id": "section567",
                        "text": {
                            "type": "mrkdwn",
                            "text": "{0}".format(body)
                        },
                        "accessory": {
                            "type": "image",
                            "image_url": "{0}".format(url_image),
                            "alt_text": "Haunted hotel image"
                        }
                    }
                ]
            }
        ]

        slack_client.api_call(method='chat.postMessage',
                              channel='CR9LJQM7D',
                              attachments='{0}'.format(send_block))

        return render(request, 'post_list.html')
