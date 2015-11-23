http://www.soapui.org/scripting---properties/working-with-properties.html

// Invoke Method
MethodWithThrowKeyword();

void MethodWithThrowKeyword() throws ArrayIndexOutOfBoundsException
{
    String[] countryNames = new String[5];
    countryNames[0] = 'India';
    countryNames[1] = 'Cyprus';
    countryNames[2] = 'Canada';
    countryNames[3] = 'Austria';
    countryNames[4] = 'Mauritius';
    for(int idx=0; idx<5; idx++)
    {
        log.info('Country Names: ' + countryNames[idx]);
    }
}


http://www.softwaretestinghelp.com/soapui-tutorial-11-exception-handling-in-soapui-groovy-scripts/

// initializing the variables
int a = 10;
int b = 0;
//int c=a/b
//log.info('Result:'+c)
// try, catch block
try
{
    // Dividing a number by zero
    int c = a/b;
    log.info('Result :' + c);
}
catch(Exception expObj)
{
  // Exception Handler
  log.info('You are trying to divide ' + a + ' by ' + b + '. This is not possible actually!');
}



String[] countryNames = new String[5];
// Try block
try    
{

    countryNames[0] = 'India';
    countryNames[1] = 'Cyprus';
    countryNames[2] = 'Canada';
    countryNames[3] = 'Austria';
    countryNames[4] = 'Mauritius';
 
    for(int idx=0; idx<5; idx++)
    {
        com.eviware.soapui.SoapUI.globalProperties.setPropertyValue( "CountryName", countryNames[idx]);
        //def testStep = testRunner.testCase.testSteps['GetCitiesByCountry'];
        //testStep.run(testRunner,context);
        log.info('Executed at ' + idx + ' times!');
    }
}
catch(Exception exp) // Catch the exception and displaying the message in the log
{
    log.info('You are trying to access invalid array index. Please check and try again!');
}



