import squishtest
 
def before_scenario(context, scenario):
    squishtest.setTestResult( "xml2", "results.xml" )
    squishtest.testSettings.setWrappersForApplication( "AddressBook.class", "Java" )
    squishtest.objectMap.load(“/suites/suite_java_addressbook/objects.map")
    squishtest.startApplication( "AddressBook.class" )
