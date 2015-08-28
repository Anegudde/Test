# -*- coding: cp1252 -*-
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from HtmlTestRun import HTMLTestRunner
import unittest, time
'''
https://dhirendrajha.wordpress.com/2011/08/31/html-report-using-htmltestrunner/
'''

class main_script(unittest.TestCase):
    #     selenium = selenium("localhost", 4444, "*chrome","http://google.co.in")
    #     selenium.start()
    #     selenium.open("/")
    driver = webdriver.Chrome("D:\Work\Drivers\chromedriver.exe")
    driver.get("http://www.python.org")
    assert "Python" in driver.title
    elem = driver.find_element_by_name("q")
    elem.send_keys("pycon")
    elem.send_keys(Keys.RETURN)
    assert "No results found." not in driver.page_source
    driver.close()


def test01_script(self):
    browser=self.selenium
    print "Open the google page"
    browser.type("q", "selenium RC")
    print "Enter the search test Selenium RC"
    browser.click("btnG")
    print "Click on Google Search button"
    browser.stop()

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(main_script))
    dateTimeStamp = time.strftime('%Y%m%d_%H_%M_%S')
    buf = file("TestReport" + "_" + dateTimeStamp + ".html", 'wb')
    runner = HTMLTestRunner(stream=buf,title='Test the Report',description='Result of tests')
    runner.run(suite)
