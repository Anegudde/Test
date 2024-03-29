/**
 * Copyright (C) 2010-2011 Diego Torres Milano
 */
package com.example.aatg.tc.test;

import java.lang.reflect.Constructor;
import java.lang.reflect.InvocationTargetException;
import java.lang.reflect.Method;
import java.util.HashMap;

import junit.framework.TestCase;

import com.example.aatg.tc.InvalidTemperatureException;
import com.example.aatg.tc.TemperatureConverter;

/**
 * @author diego
 *
 */
public class TemperatureConverterTests extends TestCase {
	
	private static final HashMap<Double, Double> conversionTableDouble =
	    new HashMap<Double, Double>();
	
	static {
	    // initialize (c, f) pairs
	    conversionTableDouble.put(0.0, 32.0);
	    conversionTableDouble.put(100.0, 212.0);
	    conversionTableDouble.put(-1.0, 30.20);
	    conversionTableDouble.put(-100.0, -148.0);
	    conversionTableDouble.put(32.0, 89.60);
	    conversionTableDouble.put(-40.0, -40.0);
	    conversionTableDouble.put(-273.0, -459.40);
	}

	/**
	 * @param name
	 */
	public TemperatureConverterTests(String name) {
		super(name);
	}

	/* (non-Javadoc)
	 * @see junit.framework.TestCase#setUp()
	 */
	protected void setUp() throws Exception {
		super.setUp();
	}

	/* (non-Javadoc)
	 * @see junit.framework.TestCase#tearDown()
	 */
	protected void tearDown() throws Exception {
		super.tearDown();
	}

	/**
	 * Test method for {@link com.example.aatg.tc.TemperatureConverter#fahrenheitToCelsius(double)}.
	 */
	public final void testFahrenheitToCelsius() {
		for (double c: conversionTableDouble.keySet()) {
			final double f = conversionTableDouble.get(c);
			final double ca = TemperatureConverter.fahrenheitToCelsius(f);
			final double delta = Math.abs(ca - c);
			final String msg = "" + f + "F -> " + c + "C but is " + ca + " (delta " + delta + ")";
			assertTrue(msg, delta < 0.0001);
		}
	}

	/**
	 * Test method for {@link com.example.aatg.tc.TemperatureConverter#celsiusToFahrenheit(double)}.
	 */
	public final void testCelsiusToFahrenheit() {
		for (double c: conversionTableDouble.keySet()) {
			final double f = conversionTableDouble.get(c);
			final double fa = TemperatureConverter.celsiusToFahrenheit(c);
			final double delta = Math.abs(fa - f);
			final String msg = "" + c + "C -> " + f + "F but is " + fa + " (delta " + delta + ")";
			assertTrue(msg, delta < 0.0001);
		}
	}
	
	public final void testExceptionForLessThanAbsoluteZeroF() {
		try {
			TemperatureConverter.fahrenheitToCelsius(TemperatureConverter.ABSOLUTE_ZERO_F-1);
			fail("Less than absolute zero F not detected");
		}
		catch (InvalidTemperatureException ex) {
			// do nothing
		}
	}
	
	public final void testExceptionForLessThanAbsoluteZeroC() {
		try {
			TemperatureConverter.celsiusToFahrenheit(TemperatureConverter.ABSOLUTE_ZERO_C-1);
			fail("Less than absolute zero C not detected");
		}
		catch (InvalidTemperatureException ex) {
			// do nothing
		}
	}
	
	public final void testPrivateConstructor() throws SecurityException, NoSuchMethodException, IllegalArgumentException, InstantiationException, IllegalAccessException, InvocationTargetException {
		Constructor<TemperatureConverter> ctor = TemperatureConverter.class.getDeclaredConstructor();
		ctor.setAccessible(true);
		TemperatureConverter tc = ctor.newInstance((Object[])null);
		assertNotNull(tc);
	}
	
	public final void testValueOfC2F() {
		assertEquals(TemperatureConverter.OP.C2F, TemperatureConverter.OP.valueOf("C2F"));
	}
	
	public final void testValueOfF2C() {
		assertEquals(TemperatureConverter.OP.F2C, TemperatureConverter.OP.valueOf("F2C"));
	}
}
