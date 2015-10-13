import org.sikuli.script.FindFailed;

 import org.sikuli.script.Screen;

public class DragAndDrop {

public static void main(String[] args) throws FindFailed, InterruptedException {

 // TODO Auto-generated method stub
 Screen s=new Screen();
 s.find("source.png");
 System.out.println("Source image found");
 s.find("target.png");
 System.out.println("target image found");
 s.dragDrop("source.png", "target.png");
 }
}
