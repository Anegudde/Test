package se.waymark.rentit.soap;

import se.waymark.rentit.model.dao.CarDAO;
import se.waymark.rentit.model.dao.InMemoryCarDAO;
import se.waymark.rentit.model.entiy.Car;

import javax.jws.WebService;

@WebService(endpointInterface = "se.waymark.rentit.soap.RentCar",
        serviceName = "RentCarService")
public class SoapRentCar implements RentCar {
    private static CarDAO carDAO = new InMemoryCarDAO();

    @Override
    public void createCars(Integer numberOfCars) {
        for (int i = 0; i < numberOfCars; i++) {
            Car car = new Car();
            carDAO.add(car);
        }
    }

    @Override
    public void rentCar() {
        Car car = carDAO.findAvailableCar();
        car.rent();
    }

    @Override
    public Integer getAvailableCars() {
        return carDAO.getNumberOfAvailableCars();
    }
}