source(findFile("scripts","soap.js"))
 
function main(){
 
    // Read template for SOAP Request
    var file = File.open(findFile("testdata","SOAP_request_template.xml"))
    var soap_template = file.read()
    file.close()
 
    var dataset = testData.dataset("data_1.tsv")
    var i=0
    for (var record in dataset) {
        i++
 
        // Prepare SOAP Request
        var countryname = testData.field(dataset[record], "CountryName");
        soap_req_content = soap_template.replace(/{CountryName}/g,countryname)
        soap_req = squishinfo.testCase+"\\testdata\\SOAP_request_"+i+".xml"
        var file2 = File.open(soap_req, "w")
        file2.write(soap_req_content)
        file2.close()
 
        // Send SOAP Request
        soap_resp = squishinfo.testCase+"\\testdata\\SOAP_resp_"+i+".xml"
 
        //Remove existing (old) response
        if (File.exists(soap_resp)) {
            test.log("Removed old SOAP response file: "+soap_resp)
            File.remove(soap_resp)
        }
 
        soap(soap_req,soap_resp)
 
        //WaitFor SOAP response
        if (!(waitFor("File.exists(soap_resp)",30000)))
                test.fatal("Timeout waiting for SOAP response!")
 
    }
 
}