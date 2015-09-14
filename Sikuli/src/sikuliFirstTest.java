import org.junit.Test;
import org.sikuli.script.App;
import org.sikuli.script.FindFailed;
import org.sikuli.script.Pattern;
import org.sikuli.script.Screen;
public class sikuliFirstTest {
	
	@Test
	public void functionName() throws FindFailed {
	//Open FireFox application with google home page   
	App firefox = App.open("c:\\Program Files\\MozillaFirefox\\firefox.exe");
	//Create and initialize an instance of Screen object   
	Screen screen = new Screen();
	//Add image path  
	Pattern image = new Pattern("C:\\searchButton.png");
	   
	//Wait 10ms for image 
	screen.wait(image, 10);
	   
	//Click on the image
	//screen.click(image);
	//Close firefox  
	firefox.close();
	}
}