from behave import *
import squishtest
 
@given('no prior existing addressbook')
def step_impl(context):
    pass
     
@when('I create a new addressbook')
def step_impl(context):
    squishtest.activateItem(squishtest.waitForObjectItem(":Address Book_JMenuBar", "File"))
    squishtest.activateItem(squishtest.waitForObjectItem(":File_JMenu", "New..."))
 
@then('"{number}" entries should be present')   
def step_impl(context,number):
    assert squishtest.findObject(":Address Book*_JTable").rowcount is int(number)
     
@given('a newly created addressbook')
def step_impl(context):
    squishtest.activateItem(squishtest.waitForObjectItem(":Address Book_JMenuBar", "File"))
    squishtest.activateItem(squishtest.waitForObjectItem(":File_JMenu", "New..."))
 
@when('adding persons to addressbook')
def step_impl(context):
    for row in context.table:
        squishtest.activateItem(squishtest.waitForObjectItem(":Address Book_JMenuBar", "Edit"))
        squishtest.activateItem(squishtest.waitForObjectItem(":Edit_JMenu", "Add..."))
        squishtest.type(squishtest.waitForObject(":Address Book - Add.Forename:_JTextField"), row['firstname'])
        squishtest.type(squishtest.waitForObject(":Address Book - Add.Surname:_JTextField"), row['lastname'])
        squishtest.type(squishtest.waitForObject(":Address Book - Add.Email:_JTextField"), row['email'])
        squishtest.type(squishtest.waitForObject(":Address Book - Add.Phone:_JTextField"), row['phone'])
        squishtest.clickButton(squishtest.waitForObject(":Address Book - Add.OK_JButton"))