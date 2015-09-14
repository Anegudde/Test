import org.junit.Test;
import org.openqa.selenium.WebDriver;
import org.openqa.selenium.firefox.FirefoxDriver;
import org.sikuli.script.App;
import org.sikuli.script.FindFailed;
import org.sikuli.script.Pattern;
import org.sikuli.script.Screen;
import org.sikuli.script.Region;
public class Test3 {
@Test
public void functionName() throws FindFailed {
  
	// Create a new instance of the Firefox driver
	WebDriver driver = new FirefoxDriver();
	// And now use this to visit Google
	driver.get("http://www.google.com");
	//Create and initialize an instance of Screen object   
	Screen screen = new Screen();
	//Add image path  
	Pattern image = new Pattern("C:\\searchButton.png");
	//Wait 10ms for image 
	screen.wait(image, 10);
	   
	//Click on the image
	//screen.showClick(image);
    }
}