package se.waymark.rentit.soap;

import javax.jws.WebParam;
import javax.jws.WebService;

@WebService
public interface RentCar {
    void createCars(@WebParam(name = "initialNumberOfCars") Integer initialNumberOfCars);

    void rentCar();

    Integer getAvailableCars();
