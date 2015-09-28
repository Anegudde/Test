String[] countryNames = new String[5];
// Try block
try    
{

    countryNames[0] = 'India';
    countryNames[1] = 'Cyprus';
    countryNames[2] = 'Canada';
    countryNames[3] = 'Austria';
    countryNames[4] = 'Mauritius';
 
    for(int idx=0; idx<=5; idx++)
    {
        com.eviware.soapui.SoapUI.globalProperties.setPropertyValue( "CountryName", countryNames[idx]);
        def testStep = testRunner.testCase.testSteps['GetCitiesByCountry'];
        testStep.run(testRunner,context);
        log.info('Executed at ' + idx + ' times!');
    }
}
catch(Exception exp) // Catch the exception and displaying the message in the log
{
    log.info('You are trying to access invalid array index. Please check and try again!');
}
