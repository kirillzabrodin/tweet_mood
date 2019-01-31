from django.test import TestCase
import unittest
from unittest import mock
from unittest.mock import patch, Mock, ANY, MagicMock
from ..tweeterpy import Tweeterpy, strip_all_entities, strip_links, strip_rt, format_output
import tweepy

class TweeterpyUnitTests(TestCase):

    def iterable(self, text):
        class RandItem:
            def __init__(self, text):
                self.text = text
        item = RandItem(text)
        list = [item]
        return list

    def test_strips_entities(self):
        result_hashtag = strip_all_entities("#hello @testing")
        assert result_hashtag == ""

    def test_strips_urls(self):
        result_url = strip_links("https://www.test-this.com")
        assert result_url == ""

    def test_strips_rt(self):
        result_rt = strip_rt("RT")
        assert result_rt == ""

    def test_does_not_delete_words(self):
        result_word = format_output("RT #hi hello there Jeff! https://www.test-this.com @itworks")
        assert result_word == "hello there Jeff!"

    def test_send_for_tweets_and_get_result(self):
        mock_response_object = Mock()
        mock_response_object.items = Mock(return_value=self.iterable('Tweet'))
        tweepy.Cursor = Mock(return_value=mock_response_object)
        tweets = Tweeterpy()
        assert tweets.get_tweets('test') == "Tweet"
