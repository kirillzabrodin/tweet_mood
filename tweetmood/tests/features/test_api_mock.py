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

    def tearDown(self):
        self.selenium.quit()
        super(APITest, self).tearDown()

    @patch('tweetmood.watson.Watson.send_for_analysis')
    def test_submit_text_with_mock_api(self, mock_analysis):
        mock_analysis.return_value = {'emotion': {'targets': [{'text': 'death', 'emotion': {'sadness': 0.372566, 'joy': 0.116822, 'fear': 0.084264, 'disgust': 0.540895, 'anger': 0.16676}}]}}
        selenium = self.selenium
        selenium.get(self.live_server_url)
        text_field = selenium.find_element_by_name('text')
        text_field.send_keys('Test')
        selenium.find_element_by_name('analyse').click()
        body_text = selenium.find_element_by_tag_name('body').text
        assert 'Test' in body_text
