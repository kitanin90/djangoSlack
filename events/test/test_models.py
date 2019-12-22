from django.test import TestCase
from events.models import Post


class PostTestCase(TestCase):

    def setUp(self):
        Post.objects.create(
            title='Первый заголовок', body='Первое описание', url_image='Ссылка')
        Post.objects.create(
            title='Второй заголовок', body='Второе описание', url_image='Вторая Ссылка')

    def test_post(self):
        first_post = Post.objects.get(title='Первый заголовок')
        second_post = Post.objects.get(title='Второй заголовок')
        self.assertEqual(
            first_post.get_title(), 'Заголовок: Первый заголовок')
        self.assertEqual(
            second_post.get_title(), 'Заголовок: Второй заголовок')
