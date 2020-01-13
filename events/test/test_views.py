from django.test import TestCase

from events.models import Post
from django.urls import reverse


class PostAPIViewTest(TestCase):

    @classmethod
    def setUpTestData(cls):
        number_of_posts = 13
        for post_num in range(number_of_posts):
            Post.objects.create(title='Title %s' %post_num,
                                body='body %s' %post_num,
                                url_image='URL - %s' %post_num,)

    def test_view_url_exists_at_desired_location(self):
        resp = self.client.get('/slack/endpoint')
        self.assertEqual(resp.status_code, 200)
