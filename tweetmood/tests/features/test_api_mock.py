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

    def tearDown(self):
        self.selenium.quit()
        super(APITest, self).tearDown()

    @patch('tweetmood.watson.Watson.send_for_analysis')
    def test_submit_text_with_mock_api(self, mock_analysis):
        response = {'document_tone': {'tones': [{'score': 0.135076, 'tone_id': 'joy', 'tone_name': 'Joy'}, {'score': 0.262356, 'tone_id': 'analytical', 'tone_name': 'Analytical'}]}}
        mock_analysis.return_value = response
        selenium = self.selenium
        selenium.get(self.live_server_url)
        text_field = selenium.find_element_by_name('text')
        text_field.send_keys('Test')
        selenium.find_element_by_name('analyse').click()
        users_text = selenium.find_element_by_id('users-text').text
        assert 'Test' in users_text
