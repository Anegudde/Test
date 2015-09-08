from selenium import webdriver  
  
def before_all(context):  
    context.browser = webdriver.Firefox()
    #context.browser = webdriver.Chrome("D:\Work\Drivers\chromedriver.exe")
    context.browser.implicitly_wait(20)
    context.browser.maximize_window()
  
def after_all(context):  
    context.browser.quit() 