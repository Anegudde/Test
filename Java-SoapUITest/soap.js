function soap(soap_req,soap_resp){
    source(findFile("scripts","ws_params.js"))
    soap_vbs = findFile("scripts","MS_HTTPXML.vbs")
    cmd = soap_vbs+' '+soap_req+' '+soap_resp+' '+post+' '+soap_action+' '+ws_host
    var result = OS.system(cmd)
    if (result== -1)
        test.fatal("soap(): Fatal error")
}