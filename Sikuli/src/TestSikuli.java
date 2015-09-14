import org.sikuli.script.*;
import org.sikuli.script.FindFailed;

public class TestSikuli {

        public static void main(String[] args) {
                Screen s = new Screen();
                try{
                        //s.click("imgs/spotlight.png");
                        //s.wait("imgs/spotlight-input.png");
                        //s.click();
                        s.write("hello world#ENTER.");
                }
                catch(FindFailed e){
                        e.printStackTrace();
                }
        }

}