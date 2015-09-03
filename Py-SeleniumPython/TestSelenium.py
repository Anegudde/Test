# -*- coding: cp1252 -*-
from selenium import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from HtmlTestRun import HTMLTestRunner
import unittest, time, sys
from pyvirtualdisplay import Display
'''
https://dhirendrajha.wordpress.com/2011/08/31/html-report-using-htmltestrunner/
'''

class main_script(unittest.TestCase):    
    # for Firefox
    selenium = selenium("localhost", 5555, "*chrome","http://google.co.in")
    selenium.start()
    selenium.open("/")
    # end of Firefox
    # for IE 
    #driver = webdriver.Ie("C:\\Python34\\IEDriverServer.exe")
    #driver.close()
    # end of IE         
    # for Chrome
#     chromedriver = "D:\\Work\\Drivers\\chromedriver"
#     os.environ["webdriver.chrome.driver"] = chromedriver
#     driver = webdriver.Chrome(chromedriver)
#     driver.get("http://stackoverflow.com")
#     driver.quit()
#     selenium.start()
#     End for Chrome
#     selenium.open("/")              
    #display = Display(visible=0, size=(800, 600))
    #display.start()
    #driver = webdriver.Chrome("D:\Work\Drivers\chromedriver.exe")
    #driver.get("http://www.google.com")
    #print driver.page_source.encode('utf-8')
    pass
      
      
      
    

    def test01_script(self):
        pass
        browser=self.selenium
        print "Open the google page"
        browser.type("q", "selenium RC")
        print "Enter the search test Selenium RC"
        browser.click("btnG")
        print "Click on Google Search button"
        browser.stop()

    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    def test02_script(self):
        pass
        browser=self.selenium
        print "Open the google page"
        browser.type("q", "selenium RC")
        print "Enter the search test Selenium RC"
        browser.click("btnG")
        print "Click on Google Search button"
        browser.stop()
    
    @unittest.skipUnless(sys.platform.startswith("win"), "requires Windows")
    #@unittest.expectedFailure
    def test03_script(self):
        pass
        browser=self.selenium
        print "Open the google page"
        browser.type("q", "selenium RC")
        print "Enter the search test Selenium RC"
        browser.click("btnG")
        print "Click on Google Search button"
        browser.stop()
    
    def close_Chrome(self):
        self.driver.quit()
        #display.stop()
    

if __name__ == '__main__':
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(main_script))
    dateTimeStamp = time.strftime('%Y%m%d_%H_%M_%S')
    buf = file("TestSelenium" + "_" + dateTimeStamp + ".html", 'wb')
    runner = HTMLTestRunner(stream=buf,title='HTML Report',description='Result of tests')
    runner.run(suite)
