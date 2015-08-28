import unittest
from selenium import webdriver
from selenium.webdriver.remote.webelement import WebElement
from selenium.webdriver.firefox.webdriver import WebDriver as Chrome
#from selenium.webdriver.firefox.firefox_profile import FirefoxProfile
'''
http://richardtier.com/2014/02/20/customising-selenium-webdrivers/
https://github.com/appium/sample-code/tree/master/sample-code/examples/python
'''
class CustomWebDriver(Chrome):
    """
    web driver that returns CustomWebElement
    when get_element_by_*, etc are called.
    """ 
    def __init__(self):
        super(CustomWebDriver, self).__init__()
        self.find = ElementFinder(self)
 
    def create_web_element(self, element_id):
        return CustomWebElement(self, element_id)
 
 
class CustomWebElement(WebElement):
    """Attach ElementFinder instance to web elements."""
    def __init__(self, *args, **kwargs):
        self.find = ElementFinder(self)
        super(CustomWebElement, self).__init__(*args, **kwargs)
 
 
class ElementFinder(object):

#non-verbosely find elements. routes to find_element_by_id,
#find_element_by_class_name, etc.

    def __init__(self, element):
        self.element = element
 
    def __call__(self, many=False, *args, **kwargs):
    #
    #if many is True then find_elements_by_*, else find_element_by_*
    #note args will be concatenated to create the selector
    #
        selector = ''.join(map(str, args))
        prepend = 'find_element{0}_by_'.format('s' if many else '')
        # rough approximate check if selector is complex css selector, if not then
        # select element by id, class, or tag, and fall back to css_selector
        punctuation = """!"#$%&'()*+,./:;<=>?@[\]^`{|}~"""
        if sum(map(selector.count, punctuation)):
            append = 'css_selector'
        elif selector[0] == '^':
            append = 'id'
            selector = selector[1:]
        elif selector[0] == '.':
            append = 'class_name'
            selector = selector[1:]
        else:
            append = 'tag_name'
            selector = selector
 
        # now we know the method name to call, lets do it
        return getattr(self.element, prepend + append)(selector)

class TestOne(unittest.TestCase):
    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Chrome("D:\Work\Drivers\chromedriver.exe")
        cls.driver.set_window_size(1120, 550)
    
    @classmethod
    def test_url(cls):
        cls.driver.get("http://duckduckgo.com/")
        cls.driver.find('^search_form_input_homepage').send_keys("realpython")
        cls.driver.find("^search_button_homepage").click()
        cls.assertIn("https://duckduckgo.com/?q=realpython", cls.driver.current_url)        
        '''
        self.driver.find('#.contact-menu').find('.show-all').click()
        self.driver.find('#user-', user_id).click()
        self.driver.find('#write-mail-to-selected').click()
        self.driver.find('#user-info-', user_id).find('.edit').click()
        '''
    @classmethod
    def tearDown(cls):
        pass
        #self.driver.quit()

if __name__ == '__main__':
    unittest.main()