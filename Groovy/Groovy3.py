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
    for(int idx=0; idx<=5; idx++)
    {
        log.info('Country Names: ' + countryNames[idx]);
    }
}
