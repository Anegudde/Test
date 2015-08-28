from HtmlTestRun import HTMLTestRunner
import unittest, os, time
from selenium import webdriver


class TestOne(unittest.TestCase):
    @classmethod
    def setUp(self):
        self.driver = webdriver.Chrome("D:\Work\Drivers\chromedriver.exe")
        self.driver.set_window_size(1120, 550)

    def test_url(self):
        self.driver.get("http://duckduckgo.com/")
        self.driver.find_element_by_id('search_form_input_homepage').send_keys("realpython")
        self.driver.find_element_by_id("search_button_homepage").click()
        self.assertIn("https://duckduckgo.com/?q=realpython", self.driver.current_url)

    @classmethod
    def tearDown(self):
        self.driver.quit()

def main():
    test_classes_to_run = [TestOne]
    loader = unittest.TestLoader()
    suites_list = []
    for test_class in test_classes_to_run:
        suite = loader.loadTestsFromTestCase(test_class)
        suites_list.append(suite)
    FullSuite = unittest.TestSuite(suites_list)
    dir = os.getcwd()
    outfile = open(dir + "\TestChromeSelenium.html", "w")
    runner = HTMLTestRunner(stream = outfile,title = 'Selenium',description = 'SeleniumTest')
    results = runner.run(FullSuite) 


if __name__ == '__main__':
    main(verbosity=2)
    #unittest.main()
    
    