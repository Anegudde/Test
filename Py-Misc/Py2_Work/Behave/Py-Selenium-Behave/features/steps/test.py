from behave import *
from hamcrest import assert_that, equal_to
from selenium import webdriver 


@given('I open seleniumframework website')
def step_1(context):
   context.browser.get("http://www.seleniumframework.com")

@then('I print the title')
def step_2(context):
   title = context.browser.title
   assert "Selenium" in title