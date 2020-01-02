from django.test import TestCase
from events.models import Post


class PostTestCase(TestCase):

    def setUp(self):
        Post.objects.create(
            title='First title', body='First description', url_image='First URL')
        Post.objects.create(
            title='Second title', body='Second description', url_image='Second URL')

    def test_post(self):
        first_post = Post.objects.get(title='First title')
        second_post = Post.objects.get(title='Second title')
        self.assertEqual(
            first_post.get_title(), 'Title: First title')
        self.assertEqual(
            second_post.get_title(), 'Title: Second title')
