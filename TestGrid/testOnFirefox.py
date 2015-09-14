from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

from selenium.webdriver.support.ui import WebDriverWait 
import time, unittest

class OnInternetExplorer (unittest.TestCase):
	def setUp(self)	:
		self.driver = webdriver.Remote(
		command_executor='http://10.137.235.57:4444/wd/hub',
		desired_capabilities=DesiredCapabilities.INTERNETEXPLORER)

	def test_Google_Search_FF(self):
		driver = self.driver()
		driver.get("http://www.google.com")
		inputElement = driver.find_element_by_name("q")	
		browser.save_screenshot('screenIE.png')
		inputElement.send_keys("Cheese!")
		inputElement.submit()
		WebDriverWait(driver, 20).until(lambda driver : driver.title.lower().startswith("cheese!"))
		self.assertEqual("cheese! - Google Search",driver.title)

	def tearDown(self):
		self.driver.quit()
		
if __name__ == "__main__":
	unittest.main()
