package test.java.se.thinkcode;

import cucumber.api.CucumberOptions;
import cucumber.api.junit.Cucumber;
import org.junit.runner.RunWith;

@RunWith(Cucumber.class)
@CucumberOptions
	(	
			features = {"src/resources/se/thinkcode"},
			format ={"pretty"}
	)
public class RunCukesTest {
	
	
}