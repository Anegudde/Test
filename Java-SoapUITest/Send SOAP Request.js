
source(findFile("scripts","soap.js"))
 
function main(){
 
    soap_req = squishinfo.testCase+"\\testdata\\SOAP_request.xml"
    soap_resp = squishinfo.testCase+"\\testdata\\SOAP_resp.xml";
 
    //Remove existing (old) response
    if (File.exists(soap_resp)) {
        test.log("Removed old SOAP response file: "+soap_resp)
        File.remove(soap_resp)
    }
 
    soap(soap_req,soap_resp)
 
    //Wait for SOAP response
    if (waitFor("File.exists(soap_resp)",30000))
        test.pass("SOAP response received")
    else
        test.fatal("Timeout waiting for SOAP response!")
 
}