

// Initializing array with 5 elements
String[] countryNames = new String[5];
// Assigning values to the array
countryNames[0] = 'India';
countryNames[1] = 'Cyprus';
countryNames[2] = 'Canada';
countryNames[3] = 'Austria';
countryNames[4] = 'Mauritius';


// Iterate the array elements and assign value to the global property
for(int idx=0; idx<=5; idx++)
{
 com.eviware.soapui.SoapUI.globalProperties.setPropertyValue( "CountryName", countryNames[idx]);
	def testStep = testRunner.testCase.testSteps['GetCitiesByCountry'];

	testStep.run(testRunner,context);

	log.info('Executed at ' + idx + ' times!');

}
