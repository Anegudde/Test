import unittest, time
from HtmlTestRun import HTMLTestRunner
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

class PythonOrgSearch(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome("D:\Work\Drivers\chromedriver.exe")
        cls.driver.implicitly_wait(20)

    def test_search_in_python_org(self):
        driver = self.driver
        driver.get("http://www.python.org")

    def test_url(self):
        self.assertIn("Python", self.driver.title)
        self.elem = self.driver.find_element_by_name("q")
        
    def test_details(self):
        self.elem.send_keys("pycon")
        self.elem.send_keys(Keys.RETURN)
        assert "No results found." not in self.driver.page_source

    @classmethod
    def tearDown(cls):
        cls.driver.close()

if __name__ == "__main__":
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(PythonOrgSearch))
    dateTimeStamp = time.strftime('%Y%m%d_%H_%M_%S')
    buf = file("TestReport" + "_" + dateTimeStamp + ".html", 'wb')
    runner = HTMLTestRunner(stream=buf,title='Test the Report',description='Result of tests')
    runner.run(suite)