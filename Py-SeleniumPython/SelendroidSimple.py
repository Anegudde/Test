import os
from time import sleep
import unittest
from appium import webdriver
PLATFORM_VERSION = '4.4'
# Returns abs path relative to this file and not cwd
PATH = lambda p: os.path.abspath( os.path.join(os.path.dirname(__file__), p))

# think times can be useful e.g. when testing with an emulator
THINK_TIME = 5.

class SimpleSalendroidTests(unittest.TestCase):
    @classmethod
    def setUp(cls):
        desired_caps = {}
        desired_caps['platformName'] = 'Android'
        desired_caps['platformVersion'] = '4.1'
        desired_caps['deviceName'] = 'Android Emulator'        
        desired_caps['app'] = PATH('D:\Work\Drivers\selendroid-test-app-0.16.0.apk' )
        if (PLATFORM_VERSION != '4.4'):
            desired_caps['automationName'] = 'selendroid'
            cls.driver = webdriver.Remote('http://localhost:4444/wd/hub', desired_caps)

    @classmethod
    def test_selendroid(cls):
        el = cls.driver.page_source()()
        # assert el.text == "Animation"
        cls.assertEqual('Animation', el.text)
        if(0):
            el = cls.driver.find_element_by_class_name("android.widget.TextView")
            # assert el.text == "Accessibility"
            cls.assertEqual('Accessibility', el.text)
            el = cls.driver.find_element_by_name("App")
            el.click()
            sleep(THINK_TIME)
            els = cls.driver.find_elements_by_class_name("android.widget.TextView")
            # Selendroid gets all the elements, not just the visible ones
            cls.assertLessEqual(30, len(els))
            cls.driver.find_element_by_name('Action Bar')
            cls.driver.back()
            sleep(THINK_TIME)
            el = cls.driver.find_element_by_name("Animation")
            cls.assertEqual('Animation', el.text)
            
    @classmethod
    def tearDown(cls):
        # end the session
        pass
        cls.driver.quit()

if __name__ == '__main__':
    suite = unittest.TestLoader().loadTestsFromTestCase(SimpleSalendroidTests)
    unittest.TextTestRunner(verbosity=2).run(suite)