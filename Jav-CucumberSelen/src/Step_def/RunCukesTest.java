package Step_def;
import org.junit.runner.RunWith;
import cucumber.api.CucumberOptions;
import cucumber.api.junit.Cucumber;


@RunWith(Cucumber.class)
@CucumberOptions(
		features = "src",
		format = {"pretty", 
				  "html:target/cucumber-html-report",
				  "json:cucumber.json"},
		tags = {}
		)
public class RunCukesTest{
}