from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.firefox.options import Options
from unittest.mock import patch
import time


class HomepageTest(LiveServerTestCase):

    def setUp(self):
        options = Options()
        options.add_argument('-headless')
        self.selenium = webdriver.Firefox(options=options)
        super(HomepageTest, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(HomepageTest, self).tearDown()

    def test_how_does_london_feel(self):
        selenium = self.selenium
        selenium.get(self.live_server_url)
        form_text = selenium.find_element_by_tag_name('form').text
        assert 'How does London feel about right now?' in form_text

    def test_button_text(self):
        selenium = self.selenium
        selenium.get(self.live_server_url)
        button_text = selenium.find_element_by_tag_name('button').text
        assert 'Ask Holmes & Watson...' in button_text

    @patch('tweetmood.views.analysis')
    def test_loading_button_text(self, mock_view_response):
        selenium = self.selenium
        selenium.get(self.live_server_url)
        time.sleep(2)
        text_field = selenium.find_element_by_name('text')
        text_field.send_keys('Test')
        selenium.find_element_by_name('analyse').click()
        button_text = selenium.find_element_by_tag_name('button').text
        assert 'Hmmm...a 3 patch problem...' in button_text
