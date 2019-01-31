from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from tweetmood.watson import Watson
from tweetmood.holmes import Holmes
import unittest
from unittest import mock
from unittest.mock import patch
from selenium.webdriver.support.ui import WebDriverWait
from mock_watson_responses import MockWatsonResponses
from mock_holmes_responses import MockHolmesResponses


mock_watson_responses = MockWatsonResponses()
mock_holmes_responses = MockHolmesResponses()


class UserInteractionTests(LiveServerTestCase):

    def setUp(self):
        options = Options()
        options.add_argument('-headless')
        self.selenium = webdriver.Firefox(options=options)
        super(UserInteractionTests, self).setUp()

    @patch('tweetmood.watson.Watson.send_for_analysis')
    @patch('tweetmood.holmes.Holmes.holmes_classify')
    @patch('tweetmood.tweeterpy.Tweeterpy.get_tweets')
    def test_users_input_text_displayed_back(self, mock_tweets, mock_holmes, mock_analysis):
        mock_tweets.return_value = "Brexit tweets"
        mock_holmes.return_value = mock_holmes_responses.mock_ambivalent_response()
        mock_analysis.return_value = mock_watson_responses.mock_successful_response()
        selenium = self.selenium
        selenium.get(self.live_server_url)
        text_field = selenium.find_element_by_name('text')
        text_field.send_keys('Test')
        selenium.find_element_by_name('analyse').click()
        users_text = selenium.find_element_by_id('users-text').text
        assert 'Test' in users_text

    @patch('tweetmood.watson.Watson.send_for_analysis')
    @patch('tweetmood.tweeterpy.Tweeterpy.get_tweets')
    def test_twitter_no_results(self, mock_tweets, mock_analysis):
        mock_tweets.return_value = ""
        mock_analysis.return_value = mock_watson_responses.mock_successful_response()
        selenium = self.selenium
        selenium.get(self.live_server_url)
        text_field = selenium.find_element_by_name('text')
        text_field.send_keys('Test')
        selenium.find_element_by_name('analyse').click()
        users_text = selenium.find_element_by_id('users-text').text
        assert 'Hmm, nobody is talking about that, ask something else' in users_text

    @patch('tweetmood.watson.Watson.send_for_analysis')
    @patch('tweetmood.holmes.Holmes.holmes_classify')
    @patch('tweetmood.tweeterpy.Tweeterpy.get_tweets')
    def test_submit_text_with_watson_warning(self, mock_tweets, mock_holmes, mock_analysis):
        mock_tweets.return_value = "Brexit tweets"
        mock_holmes.return_value = mock_holmes_responses.mock_ambivalent_response()
        mock_analysis.return_value = mock_watson_responses.mock_warnings_response()
        selenium = self.selenium
        selenium.get(self.live_server_url)
        text_field = selenium.find_element_by_name('text')
        text_field.send_keys('Test')
        selenium.find_element_by_name('analyse').click()
        users_text = selenium.find_element_by_id('users-text').text
        assert "Hmm, Watson didn't like that, try rephrasing the question" in users_text

    def tearDown(self):
        self.selenium.quit()
        super(UserInteractionTests, self).tearDown()
