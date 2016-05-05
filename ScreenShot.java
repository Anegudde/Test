import java.io.IOException;

class Test1{
	public static void main(String args[]) {
		try {
			 //Process p = Runtime.getRuntime().exec("cmd /c adb shell screencap -p /sdcard/screencap.png && adb pull /sdcard/screencap.png");
			 String adb = "adb shell screencap -p /sdcard/screencap.png && adb pull /sdcard/screencap.png";
			 ProcessBuilder builder = new ProcessBuilder("cmd.exe", "/c", adb);
			 Process process = builder.start();
			 process.waitFor();
			 System.out.println("done");
		} catch (IOException e1) {
			 System.out.println("Exception Occured while capturing the screenshot");
			 e1.printStackTrace();
			}
		  catch (InterruptedException e1){
			  System.out.println("Exception Occured while capturing the screenshot");
			 e1.printStackTrace();			  
		  }
		System.out.println("ScreenshotCaptured");
		}
}

