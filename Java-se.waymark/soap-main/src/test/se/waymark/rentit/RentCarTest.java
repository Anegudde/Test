package se.waymark.rentit;

import org.junit.Test;
import se.waymark.rentit.soap.RentCar;
import se.waymark.rentit.soap.SoapRentCar;

import static org.hamcrest.core.Is.is;
import static org.junit.Assert.assertThat;

public class RentCarTest {

    @Test
    public void shouldRentACar() {
        int initialNumberOfCars = 43;

        RentCar rentCar = new SoapRentCar();
        rentCar.createCars(initialNumberOfCars);

        rentCar.rentCar();

        int oneRentedCar = 1;
        Integer expected = initialNumberOfCars - oneRentedCar;

        Integer actual = rentCar.getAvailableCars();

        assertThat(actual, is(expected));
    }

}