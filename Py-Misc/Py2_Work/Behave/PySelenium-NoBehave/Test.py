from selenium import webdriver
import unittest
import sys

class ExampleTestCase(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Remote(desired_capabilities=
        {
            "browserName": "firefox",
            "platform": "MAC",
        }
        )

    def test_example(self):
        self.driver.get("http://www.google.com")
        self.assertEqual(self.driver.title, "Google")

    def tearDown(self):
        self.driver.quit()

if __name__ == "__main__":
    ExampleTestCase.capabilities = {
        "browserName": sys.argv[1],
        "platform": sys.argv[2],
    }
    unittest.main()