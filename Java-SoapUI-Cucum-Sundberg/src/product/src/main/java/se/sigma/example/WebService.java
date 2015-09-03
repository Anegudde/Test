package product.src.main.java.se.sigma.example;

import javax.xml.ws.Endpoint;

public class WebService {
    public static void main(String[] args) {
        Endpoint.publish("http://127.0.0.1:8090/car", new Car());
    }
}