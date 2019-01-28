from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from tweetmood.watson import Watson
import unittest
from unittest import mock
from unittest.mock import patch


class APITest(LiveServerTestCase):

    def setUp(self):
        options = Options()
        options.add_argument('-headless')
        self.selenium = webdriver.Firefox(options=options)
        super(APITest, self).setUp()

    @patch('tweetmood.watson.Watson.send_for_analysis')
    @patch('tweetmood.tweeterpy.Tweeterpy.get_tweets')
    def test_submit_text_with_mock_api(self, mock_analysis, mock_tweets):
        mock_tweets.return_value = 'Test'
        mock_analysis.return_value = {'usage': {'text_units': 1, 'text_characters': 4177, 'features': 2}, 'language': 'en', 'keywords': [{'text': 'great events', 'relevance': 0.809691, 'emotion': {'sadness': 0.000692, 'joy': 0.4031, 'fear': 2.6e-05, 'disgust': 0.297596, 'anger': 0.421568}, 'count': 1}, {'text': 'theme amp', 'relevance': 0.740042, 'emotion': {'sadness': 0.000692, 'joy': 0.4031, 'fear': 2.6e-05, 'disgust': 0.297596, 'anger': 0.421568}, 'count': 4}], 'emotion': {'targets': [{'text': 'themes', 'emotion': {'sadness': 0.000704, 'joy': 0.404111, 'fear': 2.7e-05, 'disgust': 0.296487, 'anger': 0.421414}}], 'document': {'emotion': {'sadness': 0.000692, 'joy': 0.4031, 'fear': 2.6e-05, 'disgust': 0.297596, 'anger': 0.421568}}}}
        selenium = self.selenium
        selenium.get(self.live_server_url)
        text_field = selenium.find_element_by_name('text')
        text_field.send_keys('Test')
        selenium.find_element_by_name('analyse').click()
        body_text = selenium.find_element_by_tag_name('body').text
        print(body_text)
        assert 'Test' in body_text

    def tearDown(self):
        self.selenium.quit()
        super(APITest, self).tearDown()
