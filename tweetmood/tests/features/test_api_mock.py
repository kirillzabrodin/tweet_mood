from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from tweetmood.watson import Watson
import unittest
from unittest import mock
from unittest.mock import patch
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

class APITest(LiveServerTestCase):

    def setUp(self):
        options = Options()
        options.add_argument('-headless')
        self.selenium = webdriver.Firefox(options=options)
        super(APITest, self).setUp()

    @patch('tweetmood.watson.Watson.send_for_analysis')
    @patch('tweetmood.tweeterpy.Tweeterpy.get_tweets')
    def test_submit_text_with_mock_api(self, mock_tweets, mock_analysis):
        mock_tweets.return_value = "Brexit tweets"
        mock_analysis.return_value = {'usage': {'text_units': 1, 'text_characters': 8531, 'features': 2}, 'language': 'en', 'keywords': [{'text': 'video Brexit Crisis', 'relevance': 0.808171, 'emotion': {'sadness': 0.123281, 'joy': 0.2856, 'fear': 0.00047, 'disgust': 0.363526, 'anger': 0.466701}, 'count': 1}, {'text': 'deal Brexit warnings', 'relevance': 0.736128, 'emotion': {'sadness': 0.123281, 'joy': 0.2856, 'fear': 0.00047, 'disgust': 0.363526, 'anger': 0.466701}, 'count': 1}], 'emotion': {'targets': [{'text': 'brexit', 'emotion': {'sadness': 0.594142, 'joy': 0.536118, 'fear': 0.132222, 'disgust': 0.25296, 'anger': 0.50368}}], 'document': {'emotion': {'sadness': 0.123281, 'joy': 0.2856, 'fear': 0.00047, 'disgust': 0.363526, 'anger': 0.466701}}}}
        selenium = self.selenium
        selenium.get(self.live_server_url)
        text_field = selenium.find_element_by_name('text')
        text_field.send_keys('Test')
        selenium.find_element_by_name('analyse').click()
        users_text = selenium.find_element_by_id('users-text').text
        assert 'Test' in users_text

    @patch('tweetmood.tweeterpy.Tweeterpy.get_tweets')
    def test_no_response_from_twitter(self, mock_tweets):
        mock_tweets.return_value = ""
        selenium = self.selenium
        selenium.get(self.live_server_url)
        text_field = selenium.find_element_by_name('text')
        text_field.send_keys('Test')
        selenium.find_element_by_name('analyse').click()
        body_text = selenium.find_element_by_tag_name('body').text
        assert 'Hmm, nobody is talking about that, ask something else' in body_text

    @patch('tweetmood.watson.Watson.send_for_analysis')
    @patch('tweetmood.tweeterpy.Tweeterpy.get_tweets')
    def test_submit_text_with_api_warning(self, mock_tweets, mock_analysis):
        mock_tweets.return_value = "Brexit tweets"
        mock_analysis.return_value = {'warnings': {'text_units': 1, 'text_characters': 8531, 'features': 2}, 'language': 'en', 'keywords': [{'text': 'video Brexit Crisis', 'relevance': 0.808171, 'emotion': {'sadness': 0.123281, 'joy': 0.2856, 'fear': 0.00047, 'disgust': 0.363526, 'anger': 0.466701}, 'count': 1}, {'text': 'deal Brexit warnings', 'relevance': 0.736128, 'emotion': {'sadness': 0.123281, 'joy': 0.2856, 'fear': 0.00047, 'disgust': 0.363526, 'anger': 0.466701}, 'count': 1}], 'emotion': {'targets': [{'text': 'brexit', 'emotion': {'sadness': 0.594142, 'joy': 0.536118, 'fear': 0.132222, 'disgust': 0.25296, 'anger': 0.50368}}], 'document': {'emotion': {'sadness': 0.123281, 'joy': 0.2856, 'fear': 0.00047, 'disgust': 0.363526, 'anger': 0.466701}}}}
        selenium = self.selenium
        selenium.get(self.live_server_url)
        text_field = selenium.find_element_by_name('text')
        text_field.send_keys('Test')
        selenium.find_element_by_name('analyse').click()
        body_text = selenium.find_element_by_tag_name('body').text
        assert "Hmm, Watson didn't like that, try rephrasing the question" in body_text

    def tearDown(self):
        self.selenium.quit()
        super(APITest, self).tearDown()
