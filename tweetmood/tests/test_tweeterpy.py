from django.test import TestCase
import unittest
from unittest import mock
from unittest.mock import patch, Mock, ANY, MagicMock
from ..tweeterpy import Tweeterpy
import tweepy

class TweeterpyUnitTests(TestCase):

    def iterable(self, text):
        class RandItem:
            def __init__(self, text):
                self.text = text
        item = RandItem(text)
        list = [item]
        return list

    def test_strips_hashtags(self):
        tweets = Tweeterpy()
        result_hashtag = tweets.strip_all_entities("#hello")
        assert result_hashtag == ""

    def test_strips_ats(self):
        tweets = Tweeterpy()
        result_at = tweets.strip_all_entities("@testing")
        assert result_at == ""

    def test_strips_urls(self):
        tweets = Tweeterpy()
        result_url = tweets.strip_links("https://www.test-this.com")
        assert result_url == ""

    def test_strips_rt(self):
        tweets = Tweeterpy()
        result_rt = tweets.strip_rt("RT")
        assert result_rt == ""

    def test_does_not_delete_words(self):
        tweets = Tweeterpy()
        result_word = tweets.format_output("RT #hi hello there Jeff! https://www.test-this.com @itworks")
        assert result_word == "hello there Jeff!"

    def test_send_for_tweets_and_get_result(self):
        mock_response_object = Mock()
        mock_response_object.items = Mock(return_value=self.iterable('Tweet'))
        tweepy.Cursor = Mock(return_value=mock_response_object)
        tweets = Tweeterpy()
        assert tweets.get_tweets('test') == "Tweet"
