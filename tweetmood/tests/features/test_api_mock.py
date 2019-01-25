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

    def test_submit_button_is_show(self):
        selenium = self.selenium
        selenium.get(self.live_server_url)
        text_field = selenium.find_element_by_name('text')
        text_field.send_keys('Test')
        selenium.find_element_by_name('analyse').click()
        body_text = selenium.find_element_by_tag_name('body').text
        assert 'Test' in body_text
