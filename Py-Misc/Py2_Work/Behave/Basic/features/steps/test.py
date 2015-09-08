# file:features/steps/step_tutorial01.py
# ----------------------------------------------------------------------------
# STEPS:
# ----------------------------------------------------------------------------
from behave import given, when, then

@given('we have behave installed')
def step_1(context):
    pass

@when('we implement a test')
def step_2(context):
    assert True is not False

@then('behave will test it for us!')
def step_3(context):
    assert context.failed is False