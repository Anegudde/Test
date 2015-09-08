// Read SOAP request file
var file = File.open(soap_resp)
var soap_xml = file.read()
file.close()
 
// Parse SOAP XML
var documentNode = XML.parse(soap_xml)
var soap_body = documentNode.firstChild.nextSibling.firstChild
test.compare(soap_body.nodeName,"soap:Body")
var data_set = soap_body.firstChild.firstChild.firstChild
test.compare(data_set.nodeName,"NewDataSet")
 
// answ = <Table>
var answ = data_set.firstChild
test.compare(answ.isNull,false,"<Table> element exists.")
 
test.compare(answ.firstChild.nextSibling.textContent,"Gdansk-Rebiechowo","First is Gdansk?")
answ = answ.nextSibling;
test.compare(answ.firstChild.nextSibling.textContent,"Krakow","Second is Krakow?")