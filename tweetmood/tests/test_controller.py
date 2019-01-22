from django.test import TestCase
from django.urls import resolve
from tweetmood.views import index

class Webpage(TestCase):

    def test_root_irl_resolves_to_main_page(self):
        root = resolve('/')
        # self.assertEqual(found.func, index)
        self.assertEquals(author.get_absolute_url(), '/')
