from selenium import webdriver  

from distutils.util import strtobool as _bool
import os

BEHAVE_DEBUG_ON_ERROR = _bool(os.environ.get("BEHAVE_DEBUG_ON_ERROR", "no"))

def after_step(context, step):
    if BEHAVE_DEBUG_ON_ERROR and step.status == "failed":
        # -- ENTER DEBUGGER: Zoom in on failure location.
        # NOTE: Use IPython debugger, same for pdb (basic python debugger).
        #import ipdb
        #ipdb.post_mortem(step.exc_traceback)
        pass
        
def before_all(context):
    print("Executing before all")

def before_feature(context, feature):
    print("Before feature\n")

#Scenario level objects are popped off context when scenario exits
def before_scenario(context,scenario):
    #context.browser = webdriver.Chrome("D:\Work\Drivers\chromedriver.exe")
    context.browser = webdriver.Firefox
    print("Before scenario\n")

def after_scenario(context,scenario):
    #context.browser.quit()
    print("After scenario\n")

def after_feature(context,feature):
    print("\nAfter feature")

def after_all(context):
    print("Executing after all")

