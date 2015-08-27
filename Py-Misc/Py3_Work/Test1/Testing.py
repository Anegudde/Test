import unittest
from selenium import webdriver

class Selenium2Example(unittest.TestCase):

    def setUp(self):
        desired_capabilities = webdriver.DesiredCapabilities.CHROME        
        desired_capabilities['version'] = '23.0'
        desired_capabilities['platform'] = 'WINDOWS'
        desired_capabilities['name'] = 'Testing Selenium 2 in Python'

        self.driver = webdriver.Remote(
            desired_capabilities=desired_capabilities,
            command_executor="http://key:secret@hub.testingbot.com/wd/hub"
        )
        self.driver.implicitly_wait(30)

    def test_google(self):
        self.driver.get('http://www.google.com')
        self.assertTrue("Google" in self.driver.title)

    def tearDown(self):
        print("Link to your test: https://testingbot.com/members/tests/%s" % self.driver.session_id)
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()
