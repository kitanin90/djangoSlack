from django.conf import settings
from django.shortcuts import render
from django.views.generic import TemplateView
from slackclient import SlackClient
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status

from .models import Post
from .serializers import PostSerializer


SLACK_SIGNING_SECRET = getattr(settings, 'SLACK_SIGNING_SECRET', None)
slack_bot_token = getattr(settings, 'SLACK_BOT_TOKEN', None)
slack_client = SlackClient(slack_bot_token)
slack_verification_token = getattr(settings, 'SLACK_VERIFICATION_TOKEN', None)


class EventsAPIView(APIView):

    def get(self, request):
        posts = Post.objects.all()
        serializer = PostSerializer(posts, many=True)
        return Response({'posts': serializer.data})

    def post(self, request, *args, **kwargs):
        slack_message = request.data

        if slack_message.get('token') != slack_verification_token:
            return Response(status=status.HTTP_403_FORBIDDEN)

        if slack_message.get('type') == 'url_verification':
            return Response(data=slack_message,
                            status=status.HTTP_200_OK)

        if 'event' in slack_message:
            event_message = slack_message.get('event')

            if event_message.get('subtype') == 'bot_message':
                return Response(status=status.HTTP_200_OK)
            user = event_message.get('user')
            text = event_message.get('text')
            channel = event_message.get('channel')
            bot_text = 'Hi <@{}> :wave:'.format(user)

            if 'hi' in text.lower():
                slack_client.api_call(method='chat.postMessage',
                                      channel=channel,
                                      text=bot_text)

                return Response(status=status.HTTP_200_OK)

            elif text.lower():
                slack_client.api_call(method='chat.postMessage',
                                      channel=channel,
                                      text='Your text: {0} '.format(text))

        return Response(status=status.HTTP_200_OK)


class EndpointAPIView(TemplateView):
    template_name = 'post_list.html'

    def post(self, request):
        title = request.POST.get('title')
        body = request.POST.get('body')
        url_image = request.POST.get('url_image')

        Post.objects.create(title=title,
                            body=body,
                            url_image=url_image)

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
                        }
                    },
                    {
                        "type": "image",
                        "title": {
                            "type": "plain_text",
                            "text": "image1"
                        },
                        "image_url": "{0}".format(url_image),
                        "alt_text": "image1"
                    },
                    {
                        "type": "context",
                        "elements": [
                            {
                                "type": "mrkdwn",
                                "text": "Author: V.O. Kitanin"
                            }
                        ]
                    }
                ]
            }
        ]

        slack_client.api_call(method='chat.postMessage',
                              channel='CR9LJQM7D',
                              attachments='{0}'.format(send_block))

        return render(request, 'post_list.html')
