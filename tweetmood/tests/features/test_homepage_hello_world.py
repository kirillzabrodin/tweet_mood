from django.test import LiveServerTestCase
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class HelloWorldTest(LiveServerTestCase):

    def setUp(self):
        self.selenium = webdriver.Firefox()
        super(HelloWorldTest, self).setUp()

    def tearDown(self):
        self.selenium.quit()
        super(HelloWorldTest, self).tearDown()

    def test_register(self):
        selenium = self.selenium
        #Opening the link we want to test
        selenium.get(self.live_server_url)
        #find the form element
        body_text = selenium.find_element_by_tag_name('body').text
        #check the returned result
        assert 'Hello world' in body_text
