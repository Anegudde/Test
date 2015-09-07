package ws.invoice.v3;

import java.net.URL;
import javax.xml.namespace.QName;
import javax.xml.ws.WebEndpoint;
import javax.xml.ws.WebServiceClient;
import javax.xml.ws.WebServiceFeature;
import javax.xml.ws.Service;

/**
 * This class was generated by Apache CXF 3.0.1
 * 2014-08-18T13:37:51.146+01:00
 * Generated source version: 3.0.1
 * 
 */
@WebServiceClient(name = "InvoiceServiceV3", 
                  wsdlLocation = "invoice_v3.wsdl",
                  targetNamespace = "http://soapui.cookbook.samples/contract/invoice") 
public class InvoiceServiceV3 extends Service {

    public final static URL WSDL_LOCATION;

    public final static QName SERVICE = new QName("http://soapui.cookbook.samples/contract/invoice", "InvoiceServiceV3");
    public final static QName InvoicePort = new QName("http://soapui.cookbook.samples/contract/invoice", "InvoicePort");
    static {
        URL url = InvoiceServiceV3.class.getResource("invoice_v3.wsdl");
        if (url == null) {
            url = InvoiceServiceV3.class.getClassLoader().getResource("invoice_v3.wsdl");
        } 
        if (url == null) {
            java.util.logging.Logger.getLogger(InvoiceServiceV3.class.getName())
                .log(java.util.logging.Level.INFO, 
                     "Can not initialize the default wsdl from {0}", "invoice_v3.wsdl");
        }       
        WSDL_LOCATION = url;
    }

    public InvoiceServiceV3(URL wsdlLocation) {
        super(wsdlLocation, SERVICE);
    }

    public InvoiceServiceV3(URL wsdlLocation, QName serviceName) {
        super(wsdlLocation, serviceName);
    }

    public InvoiceServiceV3() {
        super(WSDL_LOCATION, SERVICE);
    }
    
    //This constructor requires JAX-WS API 2.2. You will need to endorse the 2.2
    //API jar or re-run wsdl2java with "-frontend jaxws21" to generate JAX-WS 2.1
    //compliant code instead.
    public InvoiceServiceV3(WebServiceFeature ... features) {
        super(WSDL_LOCATION, SERVICE, features);
    }

    //This constructor requires JAX-WS API 2.2. You will need to endorse the 2.2
    //API jar or re-run wsdl2java with "-frontend jaxws21" to generate JAX-WS 2.1
    //compliant code instead.
    public InvoiceServiceV3(URL wsdlLocation, WebServiceFeature ... features) {
        super(wsdlLocation, SERVICE, features);
    }

    //This constructor requires JAX-WS API 2.2. You will need to endorse the 2.2
    //API jar or re-run wsdl2java with "-frontend jaxws21" to generate JAX-WS 2.1
    //compliant code instead.
    public InvoiceServiceV3(URL wsdlLocation, QName serviceName, WebServiceFeature ... features) {
        super(wsdlLocation, serviceName, features);
    }    

    /**
     *
     * @return
     *     returns InvoicePortType
     */
    @WebEndpoint(name = "InvoicePort")
    public InvoicePortType getInvoicePort() {
        return super.getPort(InvoicePort, InvoicePortType.class);
    }

    /**
     * 
     * @param features
     *     A list of {@link javax.xml.ws.WebServiceFeature} to configure on the proxy.  Supported features not in the <code>features</code> parameter will have their default values.
     * @return
     *     returns InvoicePortType
     */
    @WebEndpoint(name = "InvoicePort")
    public InvoicePortType getInvoicePort(WebServiceFeature... features) {
        return super.getPort(InvoicePort, InvoicePortType.class, features);
    }

}
