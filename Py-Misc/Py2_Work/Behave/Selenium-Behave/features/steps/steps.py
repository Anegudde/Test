from hamcrest import assert_that, equal_to
from blender  import Blender

@when('we visit "{browser_page:w}"')  
def step_1(context, browser_page): 
   #context.browser.get("https://crash-stats.mozilla.com/")  
   context.blender = Blender()
   #context.blender.add(browser_page)
   context.browser.get(browser_page)    
    
@when("we visit https://crash-stats.mozilla.com/ for URL") #we visit <browser_page> for URL
def step_2(context):
    #raise NotImplementedError("STEP: When we visit https://crash-stats.mozilla.com/")
    pass

@then('it should have a title "Crash Data for Firefox" in the Page')
def step_3(context):
    #raise NotImplementedError('STEP: Then it should have a title "Crash Data for Firefox" in the Page')
    pass

@then('it should have a title "{browser_title:w}" in the Page')  #"Crash Data for Firefox"
def step_4(context, browser_title):  
    #assert context.browser.title == "Google Page in Chrome"
    #assert context.browser.title == "Google"
    print context.browser.title()
    assert_that(context.browser.title, equal_to(browser_title))

@when("we visit http://google.com/ for URL")  #we visit <browser_page> for URL
def step_5(context):
    #raise NotImplementedError('STEP: When we visit http://google.com/')
    pass

