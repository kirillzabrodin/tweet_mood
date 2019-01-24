from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

class HelloWorldTest(LiveServerTestCase):

    def setUp(self):
        options = Options()
        options.add_argument('-headless')
        self.selenium = webdriver.Firefox(options=options)
        super(HelloWorldTest, self).setUp()


    def tearDown(self):
        self.selenium.quit()
        super(HelloWorldTest, self).tearDown()


    def test_register(self):
        selenium = self.selenium
        selenium.get(self.live_server_url)
        body_text = selenium.find_element_by_tag_name('body').text
        assert 'how are you feeling?' in body_text


    def test_button(self):
        selenium = self.selenium
        selenium.get(self.live_server_url)
        text_field = selenium.find_element_by_name('text')
        text_field.send_keys('Test')
        selenium.find_element_by_name('analyse').click()
        body_text = selenium.find_element_by_tag_name('body').text
        assert 'Test' in body_text


    def test_no_analysis_shortcut(self):
        selenium = self.selenium
        selenium.get(self.live_server_url + '/analysis')
        body_text = selenium.find_element_by_tag_name('body').text
        assert 'You did not submit to analysis' in body_text


    def test_no_result_shortcut(self):
        selenium = self.selenium
        selenium.get(self.live_server_url + '/result')
        body_text = selenium.find_element_by_tag_name('body').text
        assert 'You did not submit to analysis' in body_text
