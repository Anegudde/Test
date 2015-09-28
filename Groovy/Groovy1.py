http://www.softwaretestinghelp.com/soapui-tutorial-11-exception-handling-in-soapui-groovy-scripts/

// initializing the variables
int a = 10;
int b = 0;
int c=a/b
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

